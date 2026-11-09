#!/usr/bin/env bash
# Publica commits locais já revisados. Não cria repositório ou commit; sem force-push.
set -euo pipefail
command -v git >/dev/null || { echo 'Instale Git'; exit 1; }
command -v python3 >/dev/null || { echo 'Instale Python 3.11+'; exit 1; }
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo 'Clone o repositório oficial.'; exit 1; }
[[ "$(git branch --show-current)" == main ]] || { echo 'Use a branch main.'; exit 1; }
origin="$(git remote get-url origin)"
case "$origin" in
  https://github.com/ptamay/mpes-criterios-overall|https://github.com/ptamay/mpes-criterios-overall.git|git@github.com:ptamay/mpes-criterios-overall|git@github.com:ptamay/mpes-criterios-overall.git) ;;
  *) echo "Origin diferente do repositório oficial: $origin"; exit 1 ;;
esac
python3 -m src.pes21_method validate
python3 -m unittest discover -s tests -v
[[ -z "$(git status --porcelain)" ]] || { echo 'Revise e faça commit das alterações antes de publicar.'; exit 1; }
git fetch origin main
git merge-base --is-ancestor origin/main HEAD || { echo 'Branch divergiu/está atrás do remoto; sincronize via fast-forward antes de publicar.'; exit 1; }
git push origin main
echo 'Publicado em: https://github.com/ptamay/mpes-criterios-overall'
