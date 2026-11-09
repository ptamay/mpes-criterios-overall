# Execute no PowerShell 5.1 ou superior, dentro da pasta do projeto.
# Requer: Git + GitHub CLI (gh) autenticado via "gh auth login".
$ErrorActionPreference = 'Stop'
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'Instale o GitHub CLI: https://cli.github.com/' }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Instale o Git: https://git-scm.com/' }
& gh auth status
if ($LASTEXITCODE -ne 0) { throw 'Autentique: gh auth login' }
& python -m src.pes21_method validate
if ($LASTEXITCODE -ne 0) { throw 'Validação falhou' }
if (-not (Test-Path '.git')) {
  & git init -b main
  if ($LASTEXITCODE -ne 0) { throw 'git init falhou' }
}
& git add .
if ($LASTEXITCODE -ne 0) { throw 'git add falhou' }
& git commit -m 'docs: publish PES 2021 overall methodology v1'
if ($LASTEXITCODE -ne 0) { throw 'git commit falhou; configure nome/email no Git ou revise alterações' }
& gh repo create ptamay/pes21-criterios-overall --public --source . --remote origin --push --description 'Critérios auditáveis e exemplos para avaliar jogadores no PES 2021'
if ($LASTEXITCODE -ne 0) { throw 'Publicação falhou; confirme se o repositório já existe ou se há permissão' }
Write-Host 'Publicado: https://github.com/ptamay/pes21-criterios-overall'
