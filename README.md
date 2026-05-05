# testable-demo-python (DEV branch)

Dev branch: contains intentional failures across every metric category for whitebox tool validation.

This project is intentionally broken in many specific, well-cataloged ways so the
Testable platform's whitebox analyzer pipeline can be validated end-to-end. Do
NOT use this code as a reference for anything real.

## Injected failure types

1. **pylint** lint violations: unused imports, unused variables, single-letter
   names, ALL_CAPS non-constants, bare `except:`, mutable default arguments,
   redefined builtins, lines > 120 chars, missing return-type annotations.
2. **radon / lizard / cognitive-ast** high cyclomatic & cognitive complexity:
   `complex_router` in `calculator.py` and `process_records` in `legacy.py`.
3. **jscpd-py** duplicated code: identical 8+ line slug block in
   `calculator.slugify_loose` and `strings.slugify_loose_dup`.
4. **bandit + semgrep** SAST issues populating all 7 categories: see
   `security.py` (eval/exec, shell=True, os.system, pickle.loads, yaml.load,
   verify=False, hardcoded secrets, md5/sha1, Jinja2 autoescape=False, SQL
   f-string, Flask debug=True / 0.0.0.0, tempfile.mktemp, XXE-prone XML parse,
   `assert` for auth).
5. **pip-audit** known-vulnerable pinned dependencies: `requests==2.19.1`,
   `urllib3==1.24.1`, `pyyaml==5.1`, `jinja2==2.10`, `flask==1.0`.
6. **coverage.py** large untested surface: `data_flow.py` and `http_client.py`
   have no tests at all; many functions in other modules are untested.
7. **failing tests**: `test_calculator.test_subtract_wrong` and
   `test_legacy.test_process_records` assert wrong values on purpose.
8. **cosmic-ray** weak assertions: `test_strings` only asserts `is not None`.
9. **py-all-defs-uses** dead variables: `data_flow.stats` defines several
   locals that are never read.
10. **git-churn**: handled downstream when the repo is initialized with
    multiple commits — no action required at the file-creation stage.
