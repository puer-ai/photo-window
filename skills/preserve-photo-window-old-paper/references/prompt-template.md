# Prompt Templates

Use the automatic branch by default. Replace bracketed fields with observations from the target photograph.

## Automatic Core Selection

```text
Edit type: precise mixed-media photographic compositing with autonomous visual-core selection.

Image roles:
- Image 1 is the clean source photograph and fidelity authority.
- Image 2, when present, is style reference only. Borrow its paper material, palette, and mark-making without copying its wording, layout, logo, date, watermark, or subject arrangement.

First analyze Image 1 using semantic salience, compositional dominance, sharpness, light, contrast, leading lines, and narrative necessity. The visual core is [one-sentence core hypothesis]. Preserve one coherent photographic region containing [primary subject] and [essential contextual elements]. Route its organic boundary through [quiet sky / peripheral branches / soft foreground / low-detail terrain / other low-salience areas], clear of every defining subject contour.

Keep the photographic core at the same scale, coordinates, silhouette, perspective, lighting, texture detail, and color relationships as Image 1. Preserve sufficient context for scale, atmosphere, pose, gaze, or interaction. This is a photographic island, not a tight object cutout.

Coverage contract: [insert the old-paper coverage range and target from SKILL.md]. Reserve the complementary area for the photographic core. Judge coverage by visible area rather than opacity. Place the illustrated treatment across [name broad connected regions of the frame] so it reads as a major part of the composition rather than a thin border or vignette.

Transform only the periphery into an editorial old-paper illustration. Use warm ivory aged paper, visible fibers, small dust flecks, subtle scan grain, charcoal and ink contours, dry-brush hatching, faded blue-gray washes, and restrained translucent sepia accents. Redraw the source's peripheral objects in their original positions so lines, terrain, shadows, and depth connect naturally to the preserved photographic region.

Use a narrow irregular torn-paper or rubbed-pigment transition. Retain the source composition and aspect ratio. Add no text, logo, date, watermark, frame label, unrelated object, mask line, or decorative guide mark.
```

## User-Named Core Override

Use this branch only when the user names the subject to preserve:

```text
The user-selected visual core is [named subject]. Infer its complete photographic region directly from Image 1, including [essential context]. Preserve it at its original scale and position, route an organic boundary through surrounding low-salience areas, and apply the same old-paper illustration treatment only to the periphery. No drawn mask is required.
```

## Targeted Retry

Append a concrete correction after a failed first pass:

```text
Correction pass: re-evaluate Image 1 itself. The true visual core is [revised core hypothesis], including [missing defining details and necessary context]. Restore that complete region to the source scale, coordinates, silhouette, lighting, color, and photographic texture. Move the organic transition outward through [specific low-salience areas] and stylize every remaining peripheral area. Make no other compositional changes.
```

## Coverage Retry

Append this correction only when the visual-area estimate misses the Coverage Contract or the treatment reads as a narrow frame:

```text
Coverage correction pass: keep the complete visual core intact, then move the organic boundary through [specific low-salience areas] so old-paper ink-and-watercolor occupies [target from the Coverage Contract] of the visible canvas. Extend the illustrated treatment across [broad connected regions], not just the outer edge. Preserve source-aligned objects, depth, and transitions everywhere else.
```

## Core Examples

- Snow mountain landscape: preserve the dominant illuminated peak, connected central ridges and valley atmosphere; illustrate edge forests, foreground branches, and quieter sky.
- Portrait in foliage: preserve the complete face, hair silhouette, shoulders, gaze direction, and immediately interacting leaves; illustrate distant foliage and empty background.
- Product on a table: preserve the entire product, contact shadow, and a small area of supporting surface; illustrate peripheral props and room context.

## Final QA

- The photographic region contains the scene's strongest narrative anchor and all identity-defining details.
- The core retains source position, scale, silhouette, light, color, and recognizable texture.
- The region includes essential context and does not read as a minimal cutout.
- The illustrated area visually meets the Coverage Contract and occupies broad connected regions rather than a thin frame.
- The periphery is consistently illustrated while retaining source alignment.
- The boundary is organic, visually quiet, and clear of critical contours.
- No guide-like mark, copied text, invented text, logo, watermark, date, or unrelated object appears.
- The final file matches the clean source's exact pixel dimensions.
