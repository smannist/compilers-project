#!/bin/bash
set -euo pipefail
cd "$(dirname "${0}")"
poetry run mypy . --explicit-package-bases --exclude tests --exclude __main__
rm -Rf test_programs/workdir
poetry run pytest -vv tests/
