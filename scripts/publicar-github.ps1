# Publica commits locais JA revisados para o repositório MPES existente.
# Execute na raiz de um clone de https://github.com/ptamay/mpes-criterios-overall
# Não cria repositório, não faz git add/commit e nunca faz force-push.
$ErrorActionPreference = 'Stop'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Instale Git: https://git-scm.com/' }
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw 'Instale Python 3.11+.' }
& git rev-parse --is-inside-work-tree | Out-Null
if ($LASTEXITCODE -ne 0) { throw 'Clone o repositório oficial antes de publicar.' }
$branch = (& git branch --show-current).Trim()
if ($branch -ne 'main') { throw 'Execute a publicação na branch main (atual: ' + $branch + ').' }
$origin = (& git remote get-url origin).Trim()
if ($LASTEXITCODE -ne 0 -or $origin -notmatch '^(https://github\.com/ptamay/mpes-criterios-overall(\.git)?|git@github\.com:ptamay/mpes-criterios-overall(\.git)?)$') {
  throw ('Origin diferente do repositório oficial: ' + $origin)
}
& python -m src.pes21_method validate
if ($LASTEXITCODE -ne 0) { throw 'Validação do projeto falhou.' }
& python -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw 'Testes do projeto falharam.' }
if (& git status --porcelain) { throw 'Há mudanças não commitadas. Revise, faça git add + git commit e execute de novo.' }
& git fetch origin main
if ($LASTEXITCODE -ne 0) { throw 'Falha ao consultar origin/main.' }
& git merge-base --is-ancestor origin/main HEAD
if ($LASTEXITCODE -ne 0) { throw 'Branch divergiu/está atrás da main remota: faça git pull --ff-only origin main e revise antes de enviar.' }
& git push origin main
if ($LASTEXITCODE -ne 0) { throw 'Push falhou. Nenhum force-push foi tentado.' }
Write-Host 'Publicado em: https://github.com/ptamay/mpes-criterios-overall'
