# MPES — Critérios de Overall para PES 2021

**Metodologia aberta e auditável de avaliação de jogadores do PES 2021**, pensada para uma liga personalizada cujo nível de comparação é o Brasileirão Série A. Inclui regras, definições dos 25 atributos e nove exemplos editoriais (Garnacho, Lukaku, Álvaro Montoro, Gabriel Bontempo, Kevin De Bruyne, Luciano Acosta, Cryzan, Messi e Neymar, até 09/11/2026).

> **Documentação publicada: v1.10 (09/11/2026). Fórmula-base: v1.0.** Os pesos gerais foram adotados pela liga, mas as conversões de estatísticas para notas ainda **não foram calibradas**. Valores de atributos são propostas editoriais. Não confundir o índice da metodologia com o Overall gerado pelo motor do PES.

## Comece aqui

**Repositório oficial:** [ptamay/mpes-criterios-overall](https://github.com/ptamay/mpes-criterios-overall), branch `main`. Este repositório é a fonte canônica das regras e fichas; arquivos ZIP anteriores são registros históricos. Consulte o [guia de manutenção e publicação](docs/publicacao-github.md) antes de atualizar. **v1.10** é a versão do pacote documental/de exemplos; `config/criteria.v1.json` continua identificando a **fórmula v1.0**, cujo peso 45/35/15/5 não mudou.

**Validação local** (Python 3.11+, na raiz do repositório): `python -m src.pes21_method validate` e `python -m unittest discover -s tests -v`. A verificação estrutural não substitui teste do Overall no motor do PES.


- **Para IAs:** [`AGENTS.md`](AGENTS.md) → [`docs/contrato-ia.md`](docs/contrato-ia.md).
- **Regras computáveis:** [`config/criteria.v1.json`](config/criteria.v1.json).
- **Explicação dos critérios:** [`docs/metodologia.md`](docs/metodologia.md).
- **Todos os atributos e escalas:** [`docs/atributos-pes21.md`](docs/atributos-pes21.md).
- **Todas as 41 habilidades PES e 7 estilos COM:** [`docs/habilidades-pes21.md`](docs/habilidades-pes21.md) e tabela integral neste README.
- **Pesquisa histórica obrigatória:** [`docs/coleta-historica.md`](docs/coleta-historica.md).
- **Nove exemplos completos:** [`examples/garnacho.json`](examples/garnacho.json), [`examples/lukaku.json`](examples/lukaku.json) , [`examples/alvaro-montoro.json`](examples/alvaro-montoro.json) e [`examples/gabriel-bontempo.json`](examples/gabriel-bontempo.json) e [`examples/kevin-de-bruyne.json`](examples/kevin-de-bruyne.json) e [`examples/luciano-acosta.json`](examples/luciano-acosta.json) e [`examples/cryzan.json`](examples/cryzan.json), além de [`examples/lionel-messi.json`](examples/lionel-messi.json) e [`examples/neymar.json`](examples/neymar.json).
- **Calibração do drible pelo momento atual (v1.10):** [`docs/recalibracao-drible-2026.md`](docs/recalibracao-drible-2026.md). Messi 90 (não 93 automático), Neymar 88 (não 93 do auge). Propostas editoriais, dados 2026 Sofascore e C datado comparável.
- **Contextualização de atributos por liga (v1.9):** [`docs/contextualizacao-competitiva.md`](docs/contextualizacao-competitiva.md). Drible, passe, finalização e ações defensivas exigem interpretação segundo força dos adversários; não descontar automaticamente atributos físicos. Não confundir taxas de sucesso entre competições.
- **Velocidade e aceleração:** [`docs/avaliacao-fisica.md`](docs/avaliacao-fisica.md); verificar **primeiro** no Sofascore a seção **Desempenho de corrida** (velocidade máxima em km/h, sprints/90, distância/90) e outros dados rastreados. A velocidade máxima é dado físico direto, elegível ao Nível A quando rastreável; sprints/90 **não** são aceleração. Sem medição de arranque, aceleração permanece estimativa Nível C. **Ainda não existe conversão calibrada km/h → nota PES.**
- **Schema JSON para integrações:** [`schema/assessment.schema.json`](schema/assessment.schema.json).
- **Limitações e próximos passos:** [`docs/calibracao.md`](docs/calibracao.md).

## Reavaliação Messi × Neymar — 09/11/2026

| Jogador | Sofascore liga 2026 | G+A | Sofascore | Dribles certos/jogo | Sucesso | Índice | OVR-alvo | Drible PES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Messi (Inter Miami real, Fluminense no patch) | 30j / 2.574 min | 26+13 | 8,39 | 2,0 | 51,3% | 86,025 | **86** | **90** |
| Neymar (Santos real, Botafogo no patch) | 14j / 1.178 min | 8+3 | 7,62 | 1,4 | 33,3% | 82,185 | **82** | **88** |

**As estatísticas são do Sofascore na temporada e liga especificadas, com recortes diferentes dos dados mais recentes do FotMob (Messi 31j/2.664 min e Neymar 15j/1.223 min).** Neymar marcou 4 de 8 gols de pênalti no recorte FotMob. Nenhuma nota PES se considera medida pelas fontes. Confrontos de ligas usam snapshot Opta secundário **2025-11-03**, Brasil 77,9 e MLS 76,5, não a referência Brasil julho 2026. A fórmula segue T45/D35/C15/H5 e não é o OVR do jogo.

Ver: [`docs/recalibracao-drible-2026.md`](docs/recalibracao-drible-2026.md).

## Pesquisa histórica obrigatória para IAs (Sofascore + Opta)

> **Antes de avaliar um jogador, consulte as DUAS fontes e temporadas anteriores.** Uma URL listada, um perfil de clube ou uma nota dos últimos 12 meses **não significa** que o histórico foi examinado. Instruções detalhadas: [`docs/coleta-historica.md`](docs/coleta-historica.md).

| Ordem | Onde consultar | O que registrar | Regra |
| --- | --- | --- | --- |
| **1. Opta** | [Opta Analyst — Career History](https://theanalyst.com/players/4179/alejandro-garnacho/career) (localize o perfil do atleta) | Última temporada completa + atual + anterior; clube, liga/copa, jogos, minutos, gols, assistências | Separar **League**, **Domestic Cups**, **Continental Cups**; não misturar recortes |
| **2. Sofascore** | Perfil → **Temporada** → escolher **ano e competição**, depois **Partidas** | Nota média daquela temporada/competição e estatísticas disponíveis por posição (xG/xA, passes, dribles, duelos etc.) | Não confundir gráfico dos 12 meses nem nota de uma partida com média da temporada |
| **3. Cruzamento** | Mesmo atleta, ano, clube e competição | Divergências, minutagem, escopo e disponibilidade dos campos | Não inventar campo ausente; registrar fonte por métrica |
| **4. Corte amostral** | Comparar 2026/27 ↔ 2025/26 ↔ 2024/25 (no corte 07/11/2026) | Temporada principal, confiança e motivo da escolha | Abaixo de 900 min na temporada encerrada, recorrer à última amostra robusta |
| **5. Método da liga** | `criteria.v1.json` + definições PES | T/D/C/H, justificativas, índice, OVR-alvo e ficha completa | Os escores e atributos ainda são **estimativas editoriais**, não extração automática dos sites |

**Exemplos de atalhos:** [Garnacho — Sofascore](https://www.sofascore.com/pt/football/player/alejandro-garnacho/1135873) · [Garnacho — Opta](https://theanalyst.com/players/4179/alejandro-garnacho/career) · [Lukaku — Sofascore](https://www.sofascore.com/pt/football/player/romelu-lukaku/78893) · [Lukaku — Opta](https://theanalyst.com/players/4855/romelu-lukaku/career).

Se uma fonte não puder ser consultada, **não declarar a pesquisa completa**: informar a ausência e reduzir a confiança. A disponibilidade de detalhes varia entre competições e anos. Salvar URLs, data da consulta e escopo; preservar evidências e não inventar percentis.

## Cálculo do índice editorial

`I = 0,45 × Técnica + 0,35 × Desempenho + 0,15 × Competição + 0,05 × Histórico`

Cada componente é uma **nota editorial padronizada de 0 a 100**; não inserir diretamente nota Sofascore (0–10), percentil (0–100), xG ou minutos sem metodologia de conversão. Arredondamento `ROUND_HALF_UP`.

| Componente | Peso | O que representa |
| --- | ---: | --- |
| Técnica/físico atual | 45% | Capacidade na posição, execução e condição atual |
| Desempenho | 35% | Produção por posição, nota relativa e regularidade |
| Força da competição | 15% | Preferencialmente força dos adversários ponderada por minutos |
| Histórico | 5% | Nível sustentado e comprovado, não fama |

## Resultados de exemplo (07/11/2026)

| | Garnacho | Lukaku |
| --- | ---: | ---: |
| Posição | PTE | CA |
| T · técnica | 77 | 79 |
| D · desempenho | 73 | 76 |
| C · competição | 92 | 84 |
| H · histórico | 77 | 89 |
| Índice exato | **77,85** | **79,20** |
| Overall-alvo arredondado | **78** | **79** |
| Categoria | Craque | Craque |
| Confiança | Moderada | Moderada-baixa |
| Overall verificado dentro do PES? | **Não** | **Não** |

**Por quê?** Garnacho teve 1.268 min, 1 gol e 4 assistências pela Premier League 2025/26; sua explosão e drible são diferenciais, mas finalização e regularidade exigem cautela. Lukaku teve apenas 39 minutos em 2025/26 após lesão; o último período robusto foi 2024/25 (2.871 minutos, 14 gols, 10 assistências), justificando mais peso histórico e menor confiança na condição atual. Fontes e escopos nos JSONs.

## Terceiro caso — Álvaro Montoro, Botafogo (08/11/2026)

**Resultado provisório: MAT, Overall-alvo 78 (Craque).** Índice: **78,295** → **78**, em quatro dimensões ainda editoriais: técnica 79 (45%), desempenho 76 (35%), competição 83,3 (15%; média de liga histórica) e histórico 73 (5%). **Overall in-game não confirmado.**

| Evidência | Montoro | Proveniência |
| --- | ---: | --- |
| Brasileirão 2026 | 28 jogos, 1.867 minutos, 1 gol, 5 assistências | [FotMob](https://www.fotmob.com/players/1607035/alvaro-montoro) / [Driblou](https://www.driblou.com.br/data/jogador/alvaro-montoro-1650770) |
| Nota Sofascore compilada 2026 | 6,89 | Driblou Data, não extração direta da aba interativa |
| Dribles certos / 90 | 2,46 (P96 entre meias) | Driblou Data |
| Chances criadas / xA | 34 / 3,03 | FotMob |
| Bolas longas certas | 39 / 49,4% | FotMob |
| Cruzamentos certos | 7 / 22,6% | FotMob |
| Brasileirão 2025 | 16 jogos, 940 minutos, 3 gols, 3 assistências | [Opta Career](https://theanalyst.com/players/11189/alvaro-montoro/career) |

**Perfil:** forte no drible e na criação; precisão geral dos passes apenas 79,9% (P13), com baixa taxa comparativa de desarmes; finalização e ações defensivas limitadas. Velocidade **77** e aceleração **81** são **Nível C (estimadas)**, NÃO medidas de rastreamento. Consulte [`docs/avaliacao-fisica.md`](docs/avaliacao-fisica.md).

### Atributos integrais — Montoro (estimativa para edição)

| Atributo PES 2021 | Proposta |
| --- | ---: |
| Talento ofensivo | 77 |
| Controle de bola | 82 |
| Drible | 85 |
| Condução firme | 82 |
| Passe rasteiro | 74 |
| Passe alto | 72 |
| Finalização | 68 |
| Cabeceio | 53 |
| Chute colocado | 65 |
| Curva | 73 |
| Velocidade | 77 |
| Aceleração | 81 |
| Força do chute | 72 |
| Impulsão | 62 |
| Contato físico | 60 |
| Equilíbrio | 83 |
| Resistência | 77 |
| Talento defensivo | 52 |
| Desarme | 52 |
| Agressividade | 57 |
| Talento de GO | 40 |
| Firmeza de GO | 40 |
| Afast. de bola de GO | 40 |
| Reflexos de GO | 40 |
| Alcance de GO | 40 |

**Ficha integral:** [`examples/alvaro-montoro.json`](examples/alvaro-montoro.json) (25 atributos, 4 parâmetros especiais, 3 inspiradores e habilidades candidatas). Resumo dos parâmetros especiais: pé fraco uso 2/4; precisão 2/4; forma 5/8; lesões 2/3; inspiração carregar 2/2, rasteiro 1/2, alto 0/2. Histórico de lesão não equivale a suscetibilidade crônica.


## Comparação auditada — Montoro × Bontempo (08/11/2026)

**Atenção:** ambos do Brasileirão 2026, mas o Driblou/Sofascore tem recortes próprios; os totais da tabela abaixo são exclusivamente FotMob. Percentis da fonte Driblou são usados somente para contexto técnico, nunca convertidos diretamente em números PES.

| Métrica / ficha | Montoro (MAT) | Bontempo (MLG) |
| --- | ---: | ---: |
| Jogos da Série A | 28 | 30 |
| Minutos, fonte FotMob | 1.867 | 2.090 |
| Gols + assistências | 1 + 5 | 1 + 3 |
| Chances criadas | 34 | 45 |
| xA | 3,03 | 3,36 |
| Dribles certos | 51 (58,0%) | 28 (56,0%) |
| Precisão geral de passes | 79,9% | 87,1% |
| Passes longos certos | 39 (49,4%) | 16 (47,1%) |
| Cruzamentos certos | 7 (22,6%) | 9 (21,4%) |
| Desarmes | 18 | 40 |
| Técnica T / Desempenho D | 79 / 76 | 76 / 74 |
| Competição C / Histórico H | 83,3 / 73 | 83,3 / 71 |
| Índice editorial | 78,295 | 76,145 |
| **Overall-alvo editorial** | **78** | **76** |
| **Velocidade / Aceleração** | **77 / 81 (Nível C)** | **74 / 77 (Nível C)** |
| Overalls testados no motor PES | Não | Não |

**Justificativa:** Montoro dribla mais e progride de modo individual; Bontempo troca passes com mais segurança e contribui mais nos desarmes. O fato de Montoro ter 5 assistências não comprova passe rasteiro superior. Em ambos, dribles são indicadores técnicos *indiretos* para a avaliação física, não cronometrias. O pé fraco de Bontempo (uso 3/4) é hipótese apoiada por sua distribuição de chutes entre pernas, não medida de precisão.

**Fontes:** [Montoro — Sofascore](https://www.sofascore.com/pt/football/player/alvaro-montoro/1650770), [Driblou](https://www.driblou.com.br/data/jogador/alvaro-montoro-1650770), [FotMob](https://www.fotmob.com/pt-BR/players/1607035/alvaro-montoro); [Bontempo — Sofascore](https://www.sofascore.com/pt/football/player/gabriel-bontempo/1656036), [Driblou](https://www.driblou.com.br/data/jogador/gabriel-bontempo-1656036), [FotMob](https://www.fotmob.com/pt-BR/players/1712138). Fichas JSON completas: [`alvaro-montoro`](examples/alvaro-montoro.json) e [`gabriel-bontempo`](examples/gabriel-bontempo.json).


## Cryzan — Shandong Taishan (refeito v1.9; 08/11/2026)

**Overall-alvo editorial: 77 (Muito bom)**; faixa 76–78; **NÃO validado no motor PES**. **T78 D82 C62,8 H77 → 77,07 → 77**; cenário conservador C60 → 76,65 → 77. O 62,8 é **rating histórico da liga na Opta, divulgado por fonte secundária em novembro/2025**, não medição de 2026. No mesmo snapshot, o Brasileirão tinha 77,9. **Não misturar** com o rating Brasil 83,3 (julho/2026). Ver [`config/competition-snapshots.v1.json`](config/competition-snapshots.v1.json) e [`docs/contextualizacao-competitiva.md`](docs/contextualizacao-competitiva.md).

- **FotMob pós-jogo de 08/11/2026:** 24 jogos, ~1.931 min, 20 gols (4 de pênalti), 9 assistências, 90 dribles certos (~62,1%) e 58 chances criadas. **Atenção à cache:** página detalhada / FBref ainda podem trazer 23 jogos, 19 gols, ~1.839–1.841 min, 85 dribles/62,5%, 57 chances. Não misturar linhas de snapshots diferentes. [FotMob](https://www.fotmob.com/players/637316) · [FBref histórico](https://fbref.com/en/players/70acbadc/Cryzan) · [Sofascore](https://www.sofascore.com/pt/football/player/cryzan/794884).
- **Atributos contextuais PES:** talento ofensivo 78, controle 79, drible **80**, condução firme 77, passe rasteiro 74, passe alto 72, finalização **78**, cabeceio **73**, contato físico **80**; demais 25 atributos, parâmetros e fontes em [`examples/cryzan.json`](examples/cryzan.json).
- **Físico sem punição automática por liga:** velocidade 78, aceleração 77 (ambas Nível C, sem tracking), impulsão 78, potência do chute 83. Contato físico (80) reflete análise individual de duelos, não desconto fixo por atuar na China.
- D82 representa produção **observada dentro da China**, C62,8 contexto competitivo e T78 transferibilidade técnica estimada; **fatores quantitativos China→Brasil não calibrados**. A fórmula é um índice editorial, não conversão estatística nem cálculo oficial da Konami.


<!-- BEGIN FULL_PES21_FICHA: generated by scripts/render_readme.py -->
## Ficha PES 2021 completa — Garnacho × Lukaku

**Todos os 25 atributos** (escala do editor de referência: 40–99). As notas abaixo são **propostas de edição**, não medidas extraídas do Sofascore/Opta e **não foram testadas no motor PES**.

| Grupo | Atributo | O que representa | Garnacho | Lukaku |
| --- | --- | --- | ---: | ---: |
| Ataque/técnica | Talento ofensivo | Habilidade ao atacar, movimentação e aproveitamento de espaço | **78** | **84** |
| Ataque/técnica | Controle de bola | Domínio e controle geral, incluindo recepção e fintas | **81** | **77** |
| Ataque/técnica | Drible | Controle de bola ao progredir/contornar adversário em velocidade | **83** | **72** |
| Ataque/técnica | Condução firme | Capacidade de mudar a direção do drible em baixa velocidade | **80** | **72** |
| Ataque/técnica | Passe rasteiro | Precisão de passes pelo chão | **75** | **76** |
| Ataque/técnica | Passe alto | Precisão de passes aéreos | **72** | **69** |
| Ataque/técnica | Finalização | Precisão do chute ao gol | **76** | **84** |
| Ataque/técnica | Cabeceio | Precisão do cabeceio, **não capacidade de salto** | **58** | **81** |
| Ataque/técnica | Chute colocado | Precisão em bolas paradas, incluindo faltas | **64** | **63** |
| Ataque/técnica | Curva | Quantidade de efeito imprimível à bola | **77** | **70** |
| Físico/movimento | Velocidade | Agilidade/velocidade sem bola | **86** | **74** |
| Físico/movimento | Aceleração | Rapidez para alcançar velocidade máxima | **85** | **68** |
| Físico/movimento | Força do chute | Potência gerada ao chutar | **79** | **86** |
| Físico/movimento | Impulsão | Capacidade de saltar | **70** | **79** |
| Físico/movimento | Contato físico | Afastar adversários e manter equilíbrio sob pressão física | **67** | **88** |
| Físico/movimento | Equilíbrio | Evitar desarmes e se manter de pé sob contato | **79** | **70** |
| Físico/movimento | Resistência | Preparo e menor desgaste durante a partida | **79** | **70** |
| Defesa | Talento defensivo | Habilidade e posicionamento ao defender | **48** | **48** |
| Defesa | Desarme | Proficiência para ganhar posse em desarmes | **49** | **48** |
| Defesa | Agressividade | Intensidade/frequência de tentativa de desarme | **60** | **62** |
| Goleiro | Talento de GO | Atributo específico do goleiro (definição detalhada não veio na captura) | **40** | **40** |
| Goleiro | Firmeza de GO | Atributo específico do goleiro (não detalhado na captura) | **40** | **40** |
| Goleiro | Afast. de bola de GO | Atributo específico do goleiro (não detalhado na captura) | **40** | **40** |
| Goleiro | Reflexos de GO | Atributo específico do goleiro (não detalhado na captura) | **40** | **40** |
| Goleiro | Alcance de GO | Atributo específico do goleiro (não detalhado na captura) | **40** | **40** |

### Parâmetros especiais — todos os 4 campos

| Parâmetro | Escala | Significado | Garnacho | Lukaku |
| --- | --- | --- | ---: | ---: |
| Pé fraco — uso | 1–4 | Frequência de uso do pior pé | **2** | **2** |
| Pé fraco — precisão | 1–4 | Precisão de ações com o pior pé | **2** | **3** |
| Forma física | 1–8 | Capacidade de permanecer em boa forma ao longo do tempo | **5** | **5** |
| Resistência a lesões | 1–3 | Resistência a lesões; **não** igual ao total de minutos disponíveis | **2** | **2** |

**Resistência (stamina)** = desgaste durante o jogo. **Resistência a lesões** = propensão/susceptibilidade a se lesionar (escala 1–3). **Forma física** = estabilidade da condição ao longo do tempo (1–8). São campos diferentes.

### Inspirador — 3 categorias (0–2 estrelas)

| Inspirador | Garnacho | Lukaku |
| --- | ---: | ---: |
| Carregando / drible | 1/2 | 0/2 |
| Passe rasteiro | 0/2 | 0/2 |
| Passe alto | 0/2 | 0/2 |

### Habilidades especiais sugeridas para os dois jogadores

Esta tabela indica **quais habilidades do catálogo foram propostas**; não comprova que o atleta possua a habilidade no PES atual ou no patch da liga.

| Habilidade (inglês do catálogo) | PT-BR explicativo | Garnacho | Lukaku |
| --- | --- | :---: | :---: |
| `Double Touch` | Toque duplo | Proposta | — |
| `Acrobatic Finishing` | Finalização acrobática | Proposta | — |
| `Long Range Shooting` | Chute de longa distância | Proposta | — |
| `Heading` | Cabeceio | — | Proposta |
| `First-time Shot` | Chute de primeira | — | Proposta |
| `Penalty Specialist` | Especialista em pênaltis | — | Proposta |
| `Fighting Spirit` | Espírito combativo | — | Proposta |
| `Captaincy` | Capitania | — | Proposta |

**Pendência de nomenclatura:** Controle de domínio: nomenclatura/mapeamento de habilidade ainda não confirmados no editor. Não converter essa descrição automaticamente em habilidade do PES.

**Estilo de jogo principal:** ainda não definido/validado para os dois exemplos. Não é o mesmo que habilidades especiais ou estilos COM.

## Catálogo de habilidades disponíveis no PES 2021

### As 41 habilidades de jogador (lista de referência)

Os nomes em inglês funcionam como identificadores. As traduções são **explicativas**, podendo variar de acordo com o idioma/patch. Fonte comunitária: [PES Master — PES 2021](https://www.pesmaster.com/pes-2021/search/).

| Grupo | Habilidade (ID do PES) | PT-BR explicativo | Efeito resumido |
| --- | --- | --- | --- |
| Fintas e domínio | `Scissors Feint` | Finta tesoura | Finta com movimentação rápida das pernas. |
| Fintas e domínio | `Double Touch` | Toque duplo | Troca rápida de direção com dois toques. |
| Fintas e domínio | `Flip Flap` | Elástico | Finta de elástico com o pé. |
| Fintas e domínio | `Marseille Turn` | Roleta | Giro para proteger e conduzir a bola. |
| Fintas e domínio | `Sombrero` | Chapéu | Levanta a bola para superar o marcador. |
| Fintas e domínio | `Cross Over Turn` | Giro de mudança de direção | Finta de troca de direção. |
| Fintas e domínio | `Cut Behind & Turn` | Corte por trás e giro | Corte e giro para escapar da marcação. |
| Fintas e domínio | `Scotch Move` | Scotch Move | Movimento técnico de desvio e mudança de direção. |
| Fintas e domínio | `Step On Skill Control` | Domínio com a sola | Controle de bola usando a sola do pé. |
| Finalização | `Heading` | Cabeceio | Melhora a execução de cabeceios. |
| Finalização | `Long Range Drive` | Chute de longe com curva | Facilita finalizações de longe com efeito. |
| Finalização | `Chip Shot Control` | Cavadinha controlada | Melhora bolas encobertas na finalização. |
| Finalização | `Long Range Shooting` | Chute de longa distância | Melhora a execução de chutes de longe. |
| Finalização | `Knuckle Shot` | Chute sem giro | Permite chute potente com trajetória oscilante. |
| Finalização | `Dipping Shot` | Chute que cai | Permite finalização de trajetória descendente. |
| Finalização | `Rising Shots` | Chute ascendente | Permite chute que sobe na trajetória. |
| Finalização | `Acrobatic Finishing` | Finalização acrobática | Melhora finalizações em posições difíceis. |
| Finalização | `Heel Trick` | Toque de calcanhar | Ajuda em passes e chutes de calcanhar. |
| Finalização | `First-time Shot` | Chute de primeira | Melhora a execução de chutes sem dominar. |
| Passe e criação | `One-touch Pass` | Passe de primeira | Melhora passes executados em um toque. |
| Passe e criação | `Through Passing` | Passe em profundidade | Melhora a precisão dos passes que rompem linhas. |
| Passe e criação | `Weighted Pass` | Passe calibrado | Melhora ajuste do peso em certos passes. |
| Passe e criação | `Pinpoint Crossing` | Cruzamento preciso | Melhora cruzamentos com precisão e efeito. |
| Passe e criação | `Outside Curler` | Trivela | Permite executar passes e chutes com a parte externa. |
| Passe e criação | `Rabona` | Rabona | Permite passes e chutes em rabona. |
| Passe e criação | `No Look Pass` | Passe sem olhar | Permite passe com dissimulação da direção. |
| Passe e criação | `Low Lofted Pass` | Passe alto rasteiro | Permite passe aéreo longo e de trajetória baixa. |
| Goleiro | `GK Low Punt` | Reposição baixa de goleiro | Permite reposição de goleiro longa e baixa. |
| Goleiro | `GK High Punt` | Reposição alta de goleiro | Permite reposição de goleiro longa e alta. |
| Passe e criação | `Long Throw` | Arremesso lateral longo | Aumenta o alcance do lateral. |
| Goleiro | `GK Long Throw` | Lançamento longo do goleiro | Aumenta o alcance de lançamentos com as mãos. |
| Finalização | `Penalty Specialist` | Especialista em pênaltis | Melhora cobranças de pênalti. |
| Goleiro | `GK Penalty Saver` | Defensor de pênaltis | Melhora a reação do goleiro aos pênaltis. |
| Mental e defesa | `Gamesmanship` | Cavar faltas | Facilita obter faltas ao conduzir a bola. |
| Mental e defesa | `Man Marking` | Marcação individual | Melhora a perseguição e marcação do adversário. |
| Mental e defesa | `Track Back` | Retorno defensivo | Estimula pressão e retorno de jogadores ofensivos. |
| Mental e defesa | `Interception` | Interceptação | Melhora a capacidade de interceptar passes. |
| Mental e defesa | `Acrobatic Clear` | Corte acrobático | Permite afastamentos difíceis com os pés. |
| Mental e defesa | `Captaincy` | Capitania | Efeito de liderança sobre companheiros. |
| Mental e defesa | `Super-sub` | Super-reserva | Favorece jogador que entra no segundo tempo. |
| Mental e defesa | `Fighting Spirit` | Espírito combativo | Ajuda desempenho sob pressão e fadiga. |

### Os 7 estilos de jogo COM — não são habilidades de jogador

| Estilo COM (inglês) | PT-BR explicativo | Comportamento típico da IA |
| --- | --- | --- |
| `Trickster` | Habilidoso | Tende a realizar fintas com frequência. |
| `Mazing Run` | Condução sinuosa | Tende a carregar a bola superando marcadores. |
| `Speeding Bullet` | Velocista | Tende a explorar corrida e velocidade. |
| `Incisive Run` | Infiltração | Tende a atacar espaços em condução. |
| `Long Ball Expert` | Especialista em bolas longas | Tende a procurar lançamentos longos. |
| `Early Cross` | Cruzamento antecipado | Tende a cruzar cedo nas jogadas. |
| `Long Ranger` | Finalizador de longe | Tende a arriscar chutes distantes. |

**Diferenciação:** os 25 atributos, quatro parâmetros especiais, três inspiradores, 41 habilidades de jogador, sete estilos COM e estilo de jogo principal são categorias distintas. Ver [`docs/habilidades-pes21.md`](docs/habilidades-pes21.md) e [`docs/atributos-pes21.md`](docs/atributos-pes21.md).
<!-- END FULL_PES21_FICHA -->

## Faixas da liga

| Overall | Perfil |
| --- | --- |
| 86 | Referência máxima atual (âncora Messi) |
| 83–85 | Elite mundial |
| 80–82 | Extraclasse (âncora Estêvão 82) |
| 78–79 | Craque |
| 76–77 | Muito bom |
| 74–75 | Bom |
| 72–73 | Regular |
| 70–71 | Rotação |
| Abaixo de 70 | Abaixo do padrão |

Acima de 86: classificação ainda não calibrada; não impor teto oculto. Âncoras são notas **existentes na liga**, não validações independentes.

## Usar o cálculo localmente

Requer Python 3.10+ (apenas biblioteca padrão):

```bash
python -m src.pes21_method validate
python -m src.pes21_method evaluate examples/garnacho.json
python -m src.pes21_method evaluate examples/lukaku.json --json
python -m unittest discover -s tests -v
python scripts/render_readme.py  # regenera tabelas quando exemplos mudarem
```

O script **valida e calcula os quatro componentes informados**, mas **não estima** atributos a partir de estatísticas e **não implementa a fórmula interna do PES**.

## Fontes e princípios

É **obrigatório** realizar a dupla consulta histórica Sofascore/Opta antes de nova avaliação. Sofascore não equivale ao Overall; os dados de cada torneio devem ser comparados por posição, minutagem e nível dos adversários. No corte de 07/11/2026, 2025/26 é preferível e 2024/25 torna-se a base quando a amostra mais recente é insuficiente. Procedimento: [`docs/coleta-historica.md`](docs/coleta-historica.md). Referências: [`docs/fontes.md`](docs/fontes.md).

Projeto independente e não afiliado à Konami, Sofascore ou Opta. Não redistribui bancos de dados proprietários.

**Licença:** MIT para documentação, exemplos e código autoral deste repositório.


## Quinto caso — Kevin De Bruyne (Napoli, 08/11/2026)

**Proposta experimental: MAT, Overall-alvo 82 (Extraclasse)**. Índice 82,40 = 45% técnica 83 + 35% desempenho 79 + 15% competição 85 + 5% histórico 93. Não é Overall medido no PES.

| Temporada de liga | Jogos | Minutos | Gols | Assistências |
|---|---:|---:|---:|---:|
| Premier League 2024/25 | 28 | 1.706 | 4 | 7 |
| Serie A 2025/26 | 18 | 1.169 | 5 (3 pênaltis) | 2 |
| Serie A 2026/27 | 11 | 624 | 4 (1 pênalti) | 1 |

Opta: [histórico por temporada](https://theanalyst.com/players/4141/kevin-de-bruyne/career). Sofascore: [perfil](https://www.sofascore.com/pt/football/player/kevin-de-bruyne/70996). FotMob 2026/27: [23 chances, 2,31 xA e 17 cruzamentos certos em 623 minutos](https://www.fotmob.com/pt-BR/players/169200/kevin-de-bruyne). **Média Sofascore da temporada inteira 2025/26 não verificada diretamente**; nota de recorte parcial não equivale à média final.

**Dados físicos específicos:** [UEFA UCL 2026/27](https://www.uefa.com/uefachampionsleague/clubs/players/250008901--kevin-de-bruyne/statistics/) registra velocidade máxima **31,22 km/h** em 4 partidas / 360 minutos. É medição pública, mas abaixo das cinco partidas exigidas internamente para certificação Nível A; conversão para PES **não calibrada**. Velocidade 70 e aceleração 68 seguem estimadas, sendo a aceleração sem medição direta.

Ficha integral e limitações: [`examples/kevin-de-bruyne.json`](examples/kevin-de-bruyne.json). As oito habilidades propostas são candidatas, não validações atuais, e há histórico documentado de lesão muscular pelo [Napoli](https://sscnapoli.it/en/bollettino-medico-le-condizioni-di-de-bruyne/).


## Sexto caso — Luciano Acosta (Fluminense, 08/11/2026)

**Proposta experimental: MAT, Overall-alvo 79 (Craque).** Índice **79,195** = T78 (45%), D78 (35%), C83,3 (15%), H86 (5%). **Não** foi verificado no motor PES.

| Recorte | Jogos | Minutos | Gols | Assistências | Fonte |
| --- | ---: | ---: | ---: | ---: | --- |
| MLS 2025, Dallas | 21 | 1.696 | 5 | 1 | [Opta](https://theanalyst.com/players/11152/lucho-acosta/career) |
| Brasileirão 2025, Fluminense | 16 | 1.214 | 3 | 2 | [Opta](https://theanalyst.com/players/11152/lucho-acosta/career) |
| Brasileirão 2026, Fluminense | 29 | 1.623 | 6 | 5 | [FotMob](https://www.fotmob.com/players/521338/lucho-acosta) |

2026 FotMob registra 55 chances, 35 dribles certos (60,3%), 33 lançamentos certos (66,0%) e 9 cruzamentos certos (28,1%), **sem equiparar estes percentuais ao atributo passe alto**. O [Sofascore](https://www.sofascore.com/pt/football/player/luciano-acosta/548030) foi consultado; **média final sazonal não foi extraída** do seletor interativo.

Histórico: [MVP oficial da MLS em 2023](https://www.mlssoccer.com/news/fc-cincinnati-s-luciano-lucho-acosta-named-2023-landon-donovan-mls-most-valuable) com 17 gols e 14 assistências da temporada regular; Opta exibe totais diferentes em 2023 por recorte, não os misturar.

**Velocidade 73 e aceleração 79:** Nível C estimado, sem medição de sprint ou tempo de arrancada. Ficha dos 25 atributos, parâmetros, limitações e fontes: [`examples/luciano-acosta.json`](examples/luciano-acosta.json) e [`examples/cryzan.json`](examples/cryzan.json), além de [`examples/lionel-messi.json`](examples/lionel-messi.json) e [`examples/neymar.json`](examples/neymar.json).
