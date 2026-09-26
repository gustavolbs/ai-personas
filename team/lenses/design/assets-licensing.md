# Asset Provenance & Licensing

Ashley must treat asset provenance as part of production quality.

This is operational guidance, not legal advice.

## Asset register statuses

For each consequential third-party asset classify:

- **owned/original** — created for the project;
- **generated** — generated specifically for the project; note tool/source when relevant;
- **licensed/verified** — license/source checked for intended use;
- **open-license/verified** — license requirements checked;
- **user-provided** — supplied by user; usage rights still may require confirmation;
- **reference-only** — may inspire but must not ship;
- **verification-required** — source/right unclear;
- **prohibited-to-assume** — do not ship based on discovery alone.

Record durable assets in `docs/design/ASSETS.md`.

## Fonts

Before treating a font as production-ready, verify:
- source;
- commercial use rights;
- web/app embedding where relevant;
- redistribution restrictions;
- variable/static files as needed.

Do not assume a font is free because it can be downloaded.

## Icons

Record:
- library/source;
- license;
- attribution requirement if any;
- whether modified derivative use is allowed.

Do not mix unrelated icon libraries without a deliberate system decision.

## Photography / stock / illustration

"Found online" is not a license.

Track:
- creator/provider;
- asset URL/source;
- license/plan;
- intended channels;
- attribution;
- restrictions.

Pinterest/Google Images/competitor pages are reference sources, not production asset libraries.

## Logos and trademarks

Third-party logos may be subject to brand/trademark usage rules.

Use official brand assets/guidelines where available.

Ashley must not claim trademark clearance for a newly designed identity without actual research/legal review.

## Generated assets

Record when useful:
- generation tool/provider;
- prompt/art direction summary;
- post-editing;
- project ownership/provenance notes.

Generated does not automatically mean unrestricted in every jurisdiction/platform; verify when the use is consequential.

## Handoff

No asset with status `verification-required` should silently become "approved production asset".

Surface unresolved provenance in HANDOFF.md.
