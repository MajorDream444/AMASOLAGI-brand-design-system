# Repository import / recovery
Current target: MajorDream444/AMASOLAGI-brand-design-system, main. Use a review branch; never overwrite existing rows or approved files.
If importing this review ZIP manually:
1. Clone the target repo and fetch main.
2. Create branch review/ama-brand-package-v0.1.0.
3. Unzip outside the checkout; copy the contents of AMA-Solutions-Brand-v0.1.0/ into the checkout. Preserve any newer foundation changes and reconcile CSV rows by asset_id/path.
4. Run `python logos/working/verify_package.py`. Inspect comparison PDF/PNG and application HTML.
5. Commit, push the review branch and open a draft PR against main. Do not merge as identity approval.
This ZIP deliberately includes review artifacts and is not an approved production release. Obtain explicit founder decisions and rights before preparing a separate approved-only release.
