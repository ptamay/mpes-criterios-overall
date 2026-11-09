# Histórico de alterações — MPES

## Integração multi-IA — 09/11/2026 (documentação, sem revisão de notas)

- Entradas leves `CLAUDE.md` e `GEMINI.md`, ambas incorporando `AGENTS.md` por importação nativa, sem duplicar pesos ou políticas.
- Novo `docs/uso-gemini.md` com importação de GitHub no Gemini web, limitação de snapshots e procedimento via Gemini CLI.
- README, AGENTS, guia de manutenção e testes de documentação atualizados. Fórmula-base v1.0, fichas e Overalls **inalterados**; pacote documental permanece v1.10.

## Documentação e publicação — 09/11/2026 (repositório oficial)

- Repositório canônico confirmado: [`ptamay/mpes-criterios-overall`](https://github.com/ptamay/mpes-criterios-overall), branch `main`. A versão **v1.10** foi publicada inicialmente no commit [`571f12f`](https://github.com/ptamay/mpes-criterios-overall/commit/571f12f4378e1fcd3ee2e39998a9574e491d3638), com 47 arquivos.
- README atualizado para distinguir versão do pacote **v1.10** da fórmula-base **v1.0**; adicionadas instruções de validação e guia de manutenção do repositório.
- Scripts de publicação corrigidos para o repositório existente. Não criam repositório, não fazem force push e exigem commit local já revisado, checkout `main`, origin correto e avanço fast-forward.
- Exemplos indexados; testes de consistência do nome canônico e do procedimento de publicação adicionados. **Nenhuma alteração em pesos, atributos ou Overall-alvo.**

> **Nota histórica:** as entradas abaixo descrevem os estados na data em que foram produzidas. Menções a “GitHub não publicado” e ao nome de repositório anterior são registros históricos, não o estado atual. **O estado atual é o repositório oficial acima.**

## v1.10 — 09/11/2026 (reavaliação Messi × Neymar; pacote local, GitHub não publicado)

- Novas fichas completas em `examples/lionel-messi.json` e `examples/neymar.json` com 25 atributos, 4 parâmetros, 3 inspiradores, candidatas do catálogo PES, posição MAT e clubes REAIS distintos dos clubes da liga personalizada.
- Pesquisa do Sofascore 2026: Messi 30j/2574min, 26g/13a, 8,39, 2,0 dribles/jogo 51,3%; Neymar 14j/1178min, 8g/3a, 7,62, 1,4 dribles/jogo 33,3%. FotMob com recortes mais recentes em separado, inclusive Neymar 4 gols de pênalti.
- Reavaliação **sem assumir** antigos OVR/atributos: Messi índice 86,025 => OVR-alvo 86, Drible 90; Neymar 82,185 => OVR-alvo 82, Drible 88; ambos experimentais e não validados no jogo.
- Força da competição no **mesmo snapshot histórico** de 03/11/2025 (notícia secundária): MLS C76,5 e Brasil C77,9. Nada de comparar MLS 2025 com Brasil julho 2026.
- Novo `docs/recalibracao-drible-2026.md`: drible atual != auge, produção bruta != habilidade, não penalizar fisicamente pelo país, auditar dupla contagem T/D/C.
- O registro em pacote local NÃO equivale a commit no GitHub. Nenhum repositório remoto criado.


## v1.9 — 08/11/2026 (pacote local, SEM PUBLICAÇÃO REMOTA)

- **Força da CSL documentada:** snapshot Opta 03/11/2025 conforme fonte secundária publicada 04/11/2025: China 62,8 (102ª), Brasil 77,9 (8ª). **Mesmo snapshot**, diferença 15,1; **C60 é cenário editorial**, não medida Opta. Proibido misturar China 2025 com Brasil 83,3 de julho 2026. Fontes em `config/competition-snapshots.v1.json`.
- **Cryzan refeito:** T78, D82, C62,8 histórica, H77 → índice 77,07, **OVR-alvo 77** (Muito bom); C60 → 76,65 → OVR77. Atributos: talento ofensivo 78, drible 80, cabeceio 73, contato 80, demais preservados. 25 atributos + especiais. FotMob atualizado em 08/11 registra 20g/9a em 24j/1931min, 90 dribles e 58 chances; ressalva de cache mais antigo 19g/9a em 23j. Sem fator de conversão China→Brasil calibrado.
- Mantidos pesos 45/35/15/5 e regras de não descontar automaticamente velocidade, aceleração, impulsão ou potência. Advertência de possível redundância T/D/C preservada. Novo teste do cenário histórico e sensibilidade.
- GitHub `ptamay/pes21-criterios-overall`: não localizado; NÃO HOUVE COMMIT/PUSH. Pacote ZIP local é a entrega disponível.

## 1.8.0 — 2026-11-08

- Novo protocolo de **contextualização dos atributos por adversário/competição**, em `docs/contextualizacao-competitiva.md` e `config/competition-adjustment.v1.json`.
- Dribles, finalização, passes e ações defensivas são sensíveis à dificuldade da oposição; drible 62,5% na China **não** equivale automaticamente ao Brasileirão. Sem fatores empíricos por atributo, marcar **estimativa contextualizada**.
- **Cryzan corrigido:** T79 D82 C65 (C é cenário NÃO Opta) H77 → índice 77,85 → **OVR-alvo 78**; drible 84→81, finalização 81→78 e demais ajustes técnicos detalhados na ficha. Dados brutos de 2026 preservados. Velocidade/aceleração/impulsão/potência **sem desconto automático** por liga.
- Pesos T45/D35/C15/H5 permanecem. Risco de dupla penalização explicitado; nenhuma conversão matemática de liga→atributo é alegada. OVR do jogo ainda não verificado. Somente pacote local; **sem publicação GitHub**.

## 1.7.0 — 2026-11-08

- Cryzan adicionado como exemplo, 25 atributos, quatro especiais, inspiração e habilidades candidatas; OVR-alvo 80 (índice 79,75).
- Recortes 2024–2026 em FBref, temporada 2026 em FotMob e identificação Sofascore. Informada diferença de atualização em 2026.
- Rating de força da liga chinesa **NÃO verificado**: C=70 é cenário; análise de sensibilidade C=65..75; faixa OVR 79..81.
- Opta Career individual e média Sofascore sazonal não extraídos. Velocidade/aceleração Nível C. PES motor não validado.
- Pacote local somente, sem publicação remota.

## 1.6.0 — 2026-11-08

- Exemplo Luciano Acosta (Fluminense) adicionado com evidências Opta/FotMob/Sofascore, distinção de recortes históricos e 25 atributos.
- Nenhuma mudança nos pesos da metodologia; desempenho de corrida permanece não medido e Nível C físico.
- A ficha não foi validada dentro do PES. Sem publicação remota no GitHub.


## v1.5 — 08/11/2026 (Kevin De Bruyne; pacote local; GitHub ainda não publicado)

- Novo exemplo `examples/kevin-de-bruyne.json` com 25 atributos, 4 parâmetros, inspirações, habilidades candidatas e todas as fontes, OVR editorial 82 (índice 82,40).
- Opta histórico 2023/24–2026/27 separado por liga; esclarecidos os pênaltis. FotMob 2026/27 confirma 23 chances e 2,31 xA em 623 min. Média Sofascore FINAL de 2025/26 não auditada.
- Velocidade medida pela UEFA UCL: 31,22 km/h em 4 partidas; sem completar regra interna de 5 jogos e sem calibração para atributo PES. Aceleração permanece não medida.
- Sem alteração na fórmula, nos outros jogadores ou na regra de certificação. Nenhum commit remoto realizado.

## v1.4 — 08/11/2026 (correção do protocolo de dados físicos; pacote local; sem publicação GitHub)

- Reconhecidas e documentadas as métricas físicas publicadas pelo Sofascore em **Desempenho de corrida**: velocidade máxima (pico km/h), sprints/90 e distância/90. A verificação do painel passa a ser etapa obrigatória antes do fallback de estatísticas técnicas.
- Separados Nível A de velocidade e Nível A de aceleração: velocidade máxima é medida diretamente; sprints/90 **não** medem aceleração. Exigir fonte, atleta, campeonato, período e amostra para certificação Nível A. Sem fórmula calibrada km/h → pontos PES.
- Captura 9,4 km/90 · 7,8 sprints/90 · 34,8 km/h registrada como **exemplo sem identificação do atleta**; nenhuma ficha ou Overall anterior alterado automaticamente.
- AGENTS, README, coleta histórica, contrato de IA e fontes sincronizados; publicação remota pendente.

## v1.3 — 08/11/2026 (revisão Montoro × Bontempo; pacote local; sem publicação GitHub)

- Reanalisada a ficha de Montoro por comparação direta de percentis e contexto posicional: técnica 80→79, desempenho 75→76, drible 84→85, condução firme 83→82, passe rasteiro 76→74, passe alto 71→72, talento defensivo 51→52; índice 78,395→78,295, OVR-alvo 78 inalterado.
- Novo exemplo `examples/gabriel-bontempo.json`, 25 atributos e parâmetros completos; índice 76,145 (OVR 76), passe rasteiro 79, velocidade 74/aceleração 77 Nível C. Uso de pé fraco 3/4 provisório conforme finalizações registradas.
- Recortes e proveniências explícitas: FotMob 28/1.867 para Montoro, 30/2.090 para Bontempo; compilações Sofascore/Driblou com recorte diferente em Bontempo; nenhuma medição física nem validação in-game.
- Protocolo de comparação e README atualizados, método/pesos 45/35/15/5 preservados.
- GitHub remoto não atualizado (repositório ainda inexistente na conta conectada).

## v1.2 — 08/11/2026 (pacote local, AINDA NÃO PUBLICADO NO GITHUB)

- Novo exemplo completo e auditável: Álvaro Montoro (Botafogo), `examples/alvaro-montoro.json`; 25 atributos + quatro especiais + três inspiradores + skills candidatas. Overall-alvo 78, índice editorial 78,395, OVR no motor PES não validado.
- Protocolo obrigatório de velocidade/aceleração em `docs/avaliacao-fisica.md`: rastreamento nível A prioritário, estimativa Sofascore nível C quando não houver rastreamento; não confundir dribles com velocidade sem a bola.
- Documentadas as pendências de Victor Hugo (passe alto 70, velocidade 76/aceleração 78 provisórias) e Gabriel Bontempo (velocidade 74/aceleração 77 provisórias), sem publicar fichas completas não auditadas.
- Atualizados README, contrato de IA, AGENTS e testes. Fórmula editorial 45/35/15/5 **não alterada**.
- Status GitHub: **NÃO PUBLICADO**; não existe ainda `ptamay/pes21-criterios-overall` entre os repositórios conectados na verificação de 08/11/2026.

## v1.1 — 07/11/2026 (pacote documental; fórmula v1.0 preservada)

- README com **tabela integral dos 25 atributos PES 2021**, valores comparados de Garnacho e Lukaku e interpretações.
- Inclusão de **todos os 4 parâmetros especiais** (pé fraco uso/precisão, forma física e resistência a lesões), **3 inspiradores** e **41 habilidades de jogador** mais **7 estilos COM** sem confundi-los.
- Catálogo estruturado de habilidades (`config/pes21-skills.json`); identificadores EN; tradução PT-BR explicativa.
- Exemplos com habilidades normalizadas ao catálogo. A sugestão "Controle de domínio" permanece pendente de mapeamento, não é silenciosamente convertida em habilidade.
- Pesquisa histórica **obrigatória** pelo Sofascore (aba Temporada/Partidas) **e pela Opta** (Career History/competição), documentada em `docs/coleta-historica.md`, `AGENTS.md`, `README.md`, `docs/contrato-ia.md` e `docs/metodologia.md`.
- Geração de tabelas do README a partir dos JSONs/catálogo e testes para evitar divergências.
- **Sem alteração na fórmula, nos quatro subscores, nos Overall-alvo ou nos 25 atributos propostos.**
- Não há alegação de consulta das médias históricas Sofascore para os exemplos: URLs de perfil não equivalem a coleta sazonal.
