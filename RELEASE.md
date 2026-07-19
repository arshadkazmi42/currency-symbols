# Release

Releases are published through the [Publish to PyPI](.github/workflows/publish.yml)
GitHub Actions workflow. It is triggered manually and pauses for admin
approval before anything is uploaded. No PyPI tokens are stored in the
repository — authentication uses [PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/) (OIDC).

## Publishing a release

1. Bump the package version on `master` (merge a version-bump PR).
2. Go to **Actions → Publish to PyPI → Run workflow** and run it on `master`.
3. The `build` job builds the sdist + wheel, validates metadata with
   `twine check`, and fails fast if the version already exists on PyPI.
4. The `publish` job waits for approval from the required reviewers of the
   `release` environment. Approve it to publish.
5. After a successful upload, the workflow creates the `v<version>` git tag
   and a GitHub release with auto-generated notes.

## One-time setup (already required before first run)

### 1. PyPI trusted publisher

On PyPI: **currency-symbols → Manage → Publishing → Add a new publisher**

| Field | Value |
| --- | --- |
| Owner | `arshadkazmi42` |
| Repository | `currency-symbols` |
| Workflow name | `publish.yml` |
| Environment | `release` |

### 2. GitHub `release` environment

On GitHub: **Settings → Environments → New environment** named `release`.
Enable **Required reviewers** and add the admin(s) who may approve
releases. This is what enforces the manual approval gate.

## Manual publishing (fallback)

If the workflow is unavailable:

```
python3 -m pip install --upgrade build twine
python3 -m build
python3 -m twine upload dist/*
```
