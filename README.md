# test-1 — Agentic CI/CD Copilot Testbed

A multi-language repository that serves as the live-test target for the
**Agentic CI/CD Copilot** — a system that watches GitHub Actions failures
and automatically opens fix PRs.

## Repository layout

```
.
├── .github/workflows/
│   ├── python-ci.yml      # ruff lint + pytest
│   ├── go-ci.yml          # go vet + go test
│   └── config-ci.yml      # validate config/settings.json
├── pyapp/                 # Python utility library
│   ├── mathutils.py
│   ├── strutils.py
│   └── tests/
│       ├── test_mathutils.py
│       └── test_strutils.py
├── goapp/                 # Go module
│   ├── go.mod
│   └── strutil/
│       ├── strutil.go
│       └── strutil_test.go
├── config/
│   └── settings.json      # Required config validated by config-ci
├── requirements.txt       # Pinned Python deps
└── pyproject.toml         # ruff + pytest config
```

## CI branch triggers

All workflows fire on pushes/PRs to:
- `main`
- `smoke/**`
- `cicd-copilot/**` ← where the copilot opens fix PRs
- `eval/**`

## Running locally

**Python**
```bash
pip install -r requirements.txt
ruff check .
pytest -q
```

**Go**
```bash
cd goapp
go vet ./...
go test ./...
```

**Config**
```bash
python -c "import json; json.load(open('config/settings.json')); print('OK')"
```

---

## How to test the copilot

Each recipe below introduces a **real** CI failure on a branch (not `main`).
The copilot should detect the failure and open a fix PR targeting that branch.

### Tier 1 — Dependency failure

Remove a used package from `requirements.txt` so `pip install` succeeds but
`import` fails at runtime:

```bash
git checkout -b smoke/dep-failure
# Remove "pytest==..." line from requirements.txt
sed -i '/^pytest==/d' requirements.txt
git commit -am "break: remove pytest from requirements"
git push origin smoke/dep-failure
```

**Expected failure:** `python-ci / Install dependencies` or `pytest` step —
`ModuleNotFoundError: No module named 'pytest'`.  
**Expected fix:** copilot re-adds `pytest==8.3.4` to `requirements.txt`.

---

### Tier 2 — Lint failure

Add an unused import to a Python source file so `ruff` fails:

```bash
git checkout -b smoke/lint-failure
# Prepend an unused import to strutils.py
sed -i '1s/^/import os\n/' pyapp/strutils.py
git commit -am "break: add unused import"
git push origin smoke/lint-failure
```

**Expected failure:** `python-ci / Lint with ruff` — `F401 'os' imported but unused`.  
**Expected fix:** copilot removes the `import os` line.

---

### Tier 3a — Python test failure

Flip an operator in `mathutils.py` so a test assertion fails:

```bash
git checkout -b smoke/py-test-failure
# Change `a + b` to `a - b` in add()
sed -i 's/return a + b/return a - b/' pyapp/mathutils.py
git commit -am "break: flip operator in add()"
git push origin smoke/py-test-failure
```

**Expected failure:** `python-ci / Run tests` — `AssertionError` in `test_add`.  
**Expected fix:** copilot restores `return a + b` in `mathutils.py` (not the test).

---

### Tier 3b — Go test failure

Flip an operator in `strutil.go` so a table-driven test fails:

```bash
git checkout -b smoke/go-test-failure
# Change `i < j` to `i > j` in the Reverse loop guard
sed -i 's/i < j/i > j/' goapp/strutil/strutil.go
git commit -am "break: flip loop condition in Reverse()"
git push origin smoke/go-test-failure
```

**Expected failure:** `go-ci / Test` — `TestReverse` fails.  
**Expected fix:** copilot restores `i < j` in `strutil.go`.

---

### Missing-file failure

Delete the required config file so `config-ci` fails:

```bash
git checkout -b smoke/missing-config
git rm config/settings.json
git commit -m "break: delete config/settings.json"
git push origin smoke/missing-config
```

**Expected failure:** `config-ci / Validate config/settings.json` —
`FileNotFoundError: [Errno 2] No such file or directory: 'config/settings.json'`.  
**Expected fix:** copilot re-creates `config/settings.json` with valid JSON content.

<!-- retest: go subdir-path fix verification -->
<!-- behavioral-gate verify -->
