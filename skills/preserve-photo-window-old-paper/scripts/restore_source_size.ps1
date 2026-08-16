[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $true)]
    [string]$SourcePath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path
$resolvedSource = (Resolve-Path -LiteralPath $SourcePath).Path
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputPath)

if ([System.IO.Path]::GetExtension($resolvedOutput).ToLowerInvariant() -ne '.png') {
    throw 'OutputPath must use the .png extension.'
}

if ((Test-Path -LiteralPath $resolvedOutput) -and -not $Force) {
    throw "Output already exists: $resolvedOutput. Choose a new path or pass -Force."
}

$outputDirectory = [System.IO.Path]::GetDirectoryName($resolvedOutput)
if ([string]::IsNullOrWhiteSpace($outputDirectory)) {
    throw 'OutputPath must include a directory.'
}
[System.IO.Directory]::CreateDirectory($outputDirectory) | Out-Null

try {
    Add-Type -AssemblyName System.Drawing.Common -ErrorAction Stop
}
catch {
    Add-Type -AssemblyName System.Drawing -ErrorAction Stop
}

$sourceImage = $null
$inputImage = $null
$bitmap = $null
$graphics = $null

try {
    $sourceImage = [System.Drawing.Image]::FromFile($resolvedSource)
    $inputImage = [System.Drawing.Image]::FromFile($resolvedInput)

    $targetWidth = $sourceImage.Width
    $targetHeight = $sourceImage.Height

    $bitmap = New-Object System.Drawing.Bitmap($targetWidth, $targetHeight, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
    $bitmap.SetResolution(96, 96)

    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.Clear([System.Drawing.Color]::White)
    $graphics.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceCopy
    $graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $graphics.DrawImage($inputImage, 0, 0, $targetWidth, $targetHeight)

    $bitmap.Save($resolvedOutput, [System.Drawing.Imaging.ImageFormat]::Png)
}
finally {
    if ($null -ne $graphics) { $graphics.Dispose() }
    if ($null -ne $bitmap) { $bitmap.Dispose() }
    if ($null -ne $inputImage) { $inputImage.Dispose() }
    if ($null -ne $sourceImage) { $sourceImage.Dispose() }
}

$verificationImage = $null
try {
    $verificationImage = [System.Drawing.Image]::FromFile($resolvedOutput)
    Write-Output "Output: $resolvedOutput"
    Write-Output "Dimensions: $($verificationImage.Width)x$($verificationImage.Height)"
}
finally {
    if ($null -ne $verificationImage) { $verificationImage.Dispose() }
}
