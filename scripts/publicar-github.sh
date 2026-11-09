#!/usr/bin/env bash
set -euo pipefail
command -v gh >/dev/null || { echo 'Instale gh: https://cli.github.com/'; exit 1; }
command -v git >/dev/null || { echo 'Instale Git'; exit 1; }
gh auth status
python3 -m src.pes21_method validate
if [ ! -d .git ]; then git init -b main; fi
git add .
git commit -m 'docs: publish PES 2021 overall methodology v1'
gh repo create ptamay/pes21-criterios-overall --public --source . --remote origin --push --description 'Critérios auditáveis e exemplos para avaliar jogadores no PES 2021'
echo 'Publicado: https://github.com/ptamay/pes21-criterios-overall'
