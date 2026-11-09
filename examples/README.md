# Exemplos editoriais — v1.10

- **[Garnacho](garnacho.json):** PTE, 78, confiança moderada; Premier League 2025/26 como temporada principal.
- **[Lukaku](lukaku.json):** CA, 79, confiança moderada-baixa; última amostra robusta em 2024/25, lesão e baixa minutagem depois.

Garnacho e Lukaku contêm: identidade, evidências por temporada, quatro notas com justificativas, cálculo reproduzível, os **25 atributos** e parâmetros especiais, fontes e riscos. Não são avaliações oficialmente verificadas no PES; `overall_game_verified` permanece `null`.

**Pesquisa histórica para futuras avaliações:** [`../docs/coleta-historica.md`](../docs/coleta-historica.md). Consultar Opta e Sofascore em temporadas equivalentes; os JSONs atuais incluem URLs, mas **não** uma média Sofascore histórica validada. Habilidades propostas foram normalizadas ao catálogo de 41; sugestões sem mapeamento inequívoco ficam em `skills_pending_mapping`.

- [`alvaro-montoro.json`](alvaro-montoro.json): Botafogo, 2026, 28 jogos/1.867 minutos de Série A; **liga adotou Overall 77 e Drible 83** (09/11/2026). Índice histórico MPES 78,295 → alvo editorial 78, mantido para auditoria. Aceleração/velocidade Nível C; ainda sem confirmação in-game.

- [`gabriel-bontempo.json`](gabriel-bontempo.json): Santos, 2026, 30 jogos/2.090 min Série A (FotMob); 1 gol/3 assistências, 45 chances criadas, 40 desarmes, Overall-alvo 76; Nível C físico. Contraste com Montoro em [`../README.md`](../README.md).

- [`kevin-de-bruyne.json`](kevin-de-bruyne.json): Napoli, MAT, Overall-alvo 82; estatísticas por Opta, criação no FotMob, velocidade máxima UEFA 31,22 km/h (4 jogos; certificação nível A incompleta); aceleração não medida.

- [`luciano-acosta.json`](luciano-acosta.json): Fluminense, MAT, índice 79,195 → Overall-alvo 79. Série A 2026: 29j/1.623min/6g/5a, 55 chances, drible e criação fortes; velocidade/aceleração estimadas Nível C.

- [`cryzan.json`](cryzan.json): **revisado v1.9**, índice 77,07 → OVR-alvo 77; atributos técnicos contextualizados à liga chinesa com estimativas editoriais, sem coeficiente validado; atributos físicos não penalizados pela competição. Ler [`../docs/contextualizacao-competitiva.md`](../docs/contextualizacao-competitiva.md).

- [`lionel-messi.json`](lionel-messi.json): Inter Miami (clube real), MAT no patch, MLS 2026; Overall-alvo **86**, Drible **90**, produção e minutagem auditadas por recorte, sem validação in-game.
- [`neymar.json`](neymar.json): Santos (clube real), MAT no patch, Brasileirão 2026; Overall-alvo **82**, Drible **88**, recorte Sofascore distinto do FotMob, sem validação in-game.

**Como avaliar ou atualizar:** [`../docs/contrato-ia.md`](../docs/contrato-ia.md) · [`../docs/recalibracao-drible-2026.md`](../docs/recalibracao-drible-2026.md) · [`../docs/publicacao-github.md`](../docs/publicacao-github.md). Os nove JSONs são fichas **editoriais**, nunca Overalls medidos dentro do PES.
