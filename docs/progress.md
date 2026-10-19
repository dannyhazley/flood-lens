# Progress

## 2026-10-19 — C0 setup evidence for initial commit

- **Repository:** `/Users/dannyhazley/Documents/GitHub/flood-lens`; branch `main`; remote `origin` =
  `https://github.com/dannyhazley/flood-lens.git` (fetch/push configured; remote execution and branch enforcement not
  verified).
- **Revision:** `73ff6e98802d783ab83bb58eb02035c1dd258894` (`Initial commit`, authored 2026-10-16). This is the
  checked-out commit, but the current working tree has numerous staged, modified and untracked setup files; these checks
  therefore describe the current working tree, not only that commit.
- **Environment:** macOS 26.6.2, arm64; Python 3.13.9 (Anaconda build); uv 0.12.3; project runtime declaration
  `.python-version` = 3.13. Locked development tools: pytest 9.1.1 and Ruff 0.17.1. `uv sync --locked --all-groups`
  succeeded using `UV_CACHE_DIR=/tmp/floodlens-uv-cache` after the default cache path was denied by the sandbox.
- **Verified installed-wheel command:** isolated wheel install from `/tmp`, then
  `python -c 'from importlib.metadata import version; print(version("flood-lens"))'` printed `0.1.0`;
  `/tmp/floodlens-wheel-venv/bin/flood-lens --help` exited 0 and printed `Hello from flood-lens!`.
- **README run command added and verified:** `uv sync --locked --all-groups` followed by `uv run --locked flood-lens`
  exited successfully and printed `Hello from flood-lens!` (sandbox verification used
  `UV_CACHE_DIR=/tmp/floodlens-uv-cache`). README says this only checks the package entry point; it does not perform
  flood mapping.
- **Local checks on current working tree:** `uv run --locked ruff check .` — passed (`All checks passed!`);
  `uv run --locked ruff format --check .` — passed (49 files already formatted);
  `uv run --locked pytest --junitxml=/tmp/floodlens-pytest.xml` — passed (5 tests); `uv build` — passed (sdist and wheel
  built); isolated wheel install/import/entry-point check — passed as above. These are local results only.
- **CI status:** `.github/workflows/ci.yml` now runs `uv build` before installing `dist/*.whl`, matching the local
  build-and-install sequence. GitHub Actions execution and merge/branch enforcement remain unverified.
- **Hardware:** no accelerator/capacity benchmark performed. `system-info.txt` records 30 GB physical memory (at
  capture, with 889 MB unused) and 93 GiB available disk; no GPU/accelerator capability is established.
- **Human hours:** 5 total (recorded earlier; category breakdown was not supplied).
- **Learning evidence:** maintainer confirmed the C0 learning check is done; explanation/repetition details were not
  recorded.
- **Supported status/claim:** repository and a small Python package are present in the working tree. No dataset has been
  accepted and no water-mapping model, result or operational application is established.
- **C0 gate:** not yet passed. See [`docs/checkpoints/C0.md`](checkpoints/C0.md) for requirements, observed evidence and
  open items.
- **Next single action:** finish the C0 definition-of-done review, including ignored local data/artifact paths and the
  human-hour category breakdown, without inferring missing hours.
