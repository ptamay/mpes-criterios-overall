# Repositório oficial, manutenção e publicação

## Estado canônico em 09/11/2026

- **Nome exato:** [`ptamay/mpes-criterios-overall`](https://github.com/ptamay/mpes-criterios-overall).
- **Branch principal:** `main`; repositório público. O nome antigo `pes21-criterios-overall` era uma proposta local, **não** o destino remoto.
- **Publicação inicial v1.10:** commit [`571f12f`](https://github.com/ptamay/mpes-criterios-overall/commit/571f12f4378e1fcd3ee2e39998a9574e491d3638).
- **Versão documental:** v1.10.2 (política de avaliações sob demanda; exemplos antigos preservados); **versão da fórmula-base:** v1.0 (`config/criteria.v1.json`). Não atualizar pesos só para alinhar numericamente os dois identificadores.

O GitHub é a fonte da verdade. Pacotes ZIP anteriores são capturas históricas que **não** substituem os arquivos da `main`. Para novas análises por IAs, carregar primeiro `AGENTS.md`, `docs/contrato-ia.md`, `config/criteria.v1.json` e os arquivos de evidência pertinentes.

## Uso em outras IAs

- **Claude Code:** `CLAUDE.md` importa o `AGENTS.md` canônico; confira o contexto por `/context all`.
- **Gemini CLI:** `GEMINI.md` importa o `AGENTS.md` canônico; confira por `/memory show`.
- **Gemini no navegador:** importe a URL do GitHub pela opção **Importar código**, então peça explicitamente a leitura das regras. O conteúdo não é atualizado automaticamente após novos commits. Guia: [`uso-gemini.md`](uso-gemini.md).
- **Política:** entradas específicas por ferramenta só orientam o carregamento e o fluxo; não duplicar nem redefinir `config/criteria.v1.json`.

## Política de sincronização da metodologia (11/11/2026)

- **Repositório como fonte da metodologia:** manter critérios, referências, coleta histórica, contexto competitivo, escala, documentação para Claude/Gemini e testes.
- **Jogadores não precisam ser salvos:** avaliações feitas por ChatGPT, Gemini e Claude são respostas sob demanda. **Não criar/atualizar** `examples/*.json` ou listas de atletas após cada análise, exceto quando o responsável pedir expressamente.
- **Exemplos existentes permanecem arquivados:** não apagá-los nem tratá-los como fonte de verdade para toda avaliação futura. Suas datas e limitações continuam valendo.
- **Regra geral:** respeitar o resultado do cálculo MPES; **não alterar a nota de outros jogadores** por causa de um voto excepcional.
- **Exceção Montoro:** votação dos participantes da liga fixou OVR **77** e Drible **83**, enquanto o índice original **78,295** arredonda para **78**. Não presumir unanimidade, nem transformar essa decisão em calibração da fórmula.
- **Se solicitada a gravação de um jogador:** documentar proveniência e data, preservar `overall_target` e `overall_game_verified=null` se não houver comprovação in-game.

## Arquivos e responsabilidades

| Caminho | Responsabilidade |
| --- | --- |
| `README.md` | Apresentação, índice das regras e exemplos, ressalvas |
| `CLAUDE.md` / `GEMINI.md` | Pontos de entrada específicos, com importação de `AGENTS.md` |
| `docs/uso-gemini.md` | Tutorial Gemini web e Gemini CLI, limitações de sincronização |
| `AGENTS.md` e `docs/contrato-ia.md` | Instruções e requisitos de evidência para IAs |
| `config/criteria.v1.json` | Pesos e classificação (não alterar por atualização documental) |
| `docs/metodologia.md` | Definições e cálculo do índice editorial |
| `docs/contextualizacao-competitiva.md` | Ajustes pela força dos adversários; evitar dupla penalização |
| `docs/avaliacao-fisica.md` | Níveis de evidência de velocidade e aceleração |
| `docs/recalibracao-drible-2026.md` | Reavaliação contextual do drible Messi × Neymar |
| `examples/*.json` | Propostas editoriais individuais e fontes datadas |
| `CHANGELOG.md` | Histórico de mudanças; registros antigos não representam o estado remoto atual |
| `tests/` e `.github/workflows/validate.yml` | Validação estrutural, cálculos e verificações automatizadas |

## Procedimento para atualizar

1. Abra a [`main` atual](https://github.com/ptamay/mpes-criterios-overall/tree/main), leia as regras e **verifique se houve alterações desde seu último acesso**. Não reutilize ZIPs ou hashes antigos como se fossem o HEAD.
2. Para avaliar um jogador no chat, pesquise fontes e recortes, entregue o resultado solicitado e suas limitações **sem escrever arquivos**. Apenas mediante pedido explícito de publicação, prepare uma ficha completa e valide a persistência.
3. Para mudança metodológica: documente hipótese, exemplos de casos afetados, risco de dupla contagem entre T/D/C e necessidade de calibração por adversário. Não converta percentil Sofascore, nota 0–10 ou ranking Opta diretamente em atributo PES.
4. Atualize `README.md` e documentos pertinentes, `AGENTS.md` se a regra de IA mudar e `CHANGELOG.md`. **Não alterar `examples/` por padrão.** A seção gerada do README pertence a `scripts/render_readme.py`: não a edite manualmente.
5. Execute os comandos abaixo na raiz do clone. Só depois faça commit; não afirme publicação até confirmar o SHA remoto.

```bash
git clone https://github.com/ptamay/mpes-criterios-overall.git
cd mpes-criterios-overall
git switch main
git pull --ff-only origin main
python -m src.pes21_method validate
python -m unittest discover -s tests -v
# Caso tenha alterado fontes das tabelas geradas:
python scripts/render_readme.py
# Revise o diff ANTES de adicionar ou publicar:
git diff --check
git diff
git add README.md AGENTS.md CHANGELOG.md docs examples scripts tests
git commit -m "docs: atualizar documentação MPES"
bash scripts/publicar-github.sh
```

No Windows, o último comando é `powershell -ExecutionPolicy Bypass -File scripts/publicar-github.ps1` em vez de `bash`. Os scripts validam origin, branch e testes e **apenas enviam commits já criados**; não criam repositórios, não sobrescrevem o histórico e não utilizam `--force`. Se o remoto avançou, sincronize e revise antes de repetir.

## Publicação pela integração GitHub

É possível atualizar por meio de um assistente com acesso autorizado à integração GitHub, usando o repositório **exato** `ptamay/mpes-criterios-overall`. Antes de modificar, leia os arquivos atuais, preserve o estado da `main`, use SHA/lease para evitar sobrescrever alterações simultâneas e execute as validações disponíveis. Relate sempre os caminhos alterados, o commit e o status dos testes/CI.

## Limitações explícitas

- **Índice editorial ≠ Overall do motor PES 2021**. As fichas publicadas não foram validadas no editor do jogo.
- **Sofascore, Opta, FotMob e avaliações próprias têm escopos distintos**. Registre competição, período, método, amostra e fonte, distinguindo fatos de estimativas.
- A média de competição em determinada data não é fixa nem deve ser misturada à média de outro ano sem ressalva. Exemplo: China 62,8 (levantamento histórico divulgado em 2025) e cenário editorial China 60 não são a mesma evidência.
- Testes do projeto garantem sobretudo integridade estrutural e aritmética; não certificam todas as notas de atributos nem convertem estatísticas de drible em rating PES.
