# Metodologia — fórmula-base v1.0 (documentação MPES v1.10.2)

**Política de uso desde 11/11/2026:** o MPES fornece a metodologia para **avaliações sob demanda**. O repositório não precisa receber uma ficha por jogador analisado; `examples/` permanece como acervo histórico. Novas fichas só são publicadas por solicitação explícita do responsável. O que deve ser sincronizado continuamente são as regras e os protocolos, não cada recomendação individual.

**Exceções não recalibram outros jogadores:** Montoro teve uma votação com participação dos membros da liga; foram adotados **77 OVR e 83 de drible**, diferentes do índice editorial anterior **78,295 → 78**. A votação não altera pesos, escalas, estimativas de outros atletas ou a exigência de evidências. Em condições normais, o Overall-alvo calculado permanece a recomendação. Se um registro excepcional for solicitado, usar `league_assignment` separado de `overall_target` e `overall_game_verified`, que depende de comprovação no jogo.

**Fonte canônica:** [ptamay/mpes-criterios-overall](https://github.com/ptamay/mpes-criterios-overall) · [guia de atualização](publicacao-github.md). Este documento explica a fórmula aprovada; a versão de documentação 1.10.2 não significa revisão dos pesos. Datas de 07/11/2026 abaixo identificam recortes históricos e não instruem a reutilizá-los em avaliações futuras.

## 1. Finalidade e escopo

A liga PES 2021 adota escala comparável ao **Brasileirão Série A**; seus Overalls são internos e não precisam coincidir com patches ou PESDB. **Messi 86** (âncora máxima atual) e **Estêvão 82** (âncora extraclasse) são referências fornecidas pela liga, não pontos já auditados. No momento, a fórmula gera **Overall-alvo editorial**, não o Overall matemático do motor PES.

## 2. Fórmula ponderada — aprovada

```text
I = 0.45*T + 0.35*D + 0.15*C + 0.05*H
Overall-alvo = arredondamento half-up(I)
```

Todos os componentes T/D/C/H vão de 0 a 100. Os exemplos atuais usam **julgamentos editoriais informados por evidências**. Não existe ainda uma função calibrada que mapeie automaticamente estatísticas em T/D/C/H; seria incorreto apresentar as notas dos componentes como resultados de um algoritmo objetivo.

### T — Técnica e físico atual, 45%

Capacidade de execução na posição, não potencial futuro. Considerar vídeos/scouting, atributos observáveis, drible, progressão, passes, finalização, posicionamento, força, movimentação. Variáveis diferentes por função. Ponta e centroavante exigem distribuições distintas; evitar dupla contagem com D.

### D — Desempenho e regularidade, 35%

Proposta para o futuro: 60% indicadores específicos por posição (por 90 minutos e eficiência), 25% percentil de Nota Sofascore relativo à posição e nível comparável, 15% regularidade. **Ainda NÃO aplicado numericamente**: faltam população de referência, definição das métricas, normalizações e tratamento de minutos. Média Sofascore não é Overall e não deve ser simplesmente multiplicada por 10.

Indicadores úteis: ponta — drible certo, taxa de acerto, progressões, passes decisivos, xA, xG sem pênalti, perdas; centroavante — xG sem pênalti, gols, finalizações, chance desperdiçada, duelos, jogo aéreo e apoio à construção. Não selecionar apenas G+A.

### C — Exigência competitiva, 15%

Se houver rating confiável de cada adversário: `C = sum(minutos_contra_adversário * força_adversário) / sum(minutos)` na mesma escala do rating. Sem isso, usar média datada da liga, **rotulada como proxy**. Não conceder pontos por nome de clube. Para jogador com mudanças de liga, competição ou pouca minutagem, um C misto sem pesos reproduzíveis é **estimativa editorial**, não média exata. Os índices da Opta servem como referência externa, não como medição infalível da qualidade individual.

Foto histórica das ligas (27/07/2026, Opta): Premier League 92,0; Bundesliga 85,9; LaLiga 85,7; Serie A Itália 85,0; Ligue 1 84,8; Brasileirão 83,3; Portugal 81,3; Turquia 79,0. Atualizar antes de avaliações futuras.

### Contextualização dos atributos técnicos entre ligas — regra adicional aprovada

**China (registro 08/11/2026):** referência histórica Opta via fonte secundária em 03/11/2025: CSL 62,8, Brasileirão 77,9 (mesma data); usar CSL C62,8 apenas como proxy datada e C60 como cenário conservador editorial. **Não comparar com Brasileirão 83,3 de julho/2026 como se fosse mesmo snapshot.** Evidências em `config/competition-snapshots.v1.json`.

Antes de propor drible, passe, finalização, talento ofensivo e ações defensivas, consultar [`contextualizacao-competitiva.md`](contextualizacao-competitiva.md). Estatísticas idênticas não representam a mesma habilidade quando a oposição é diferente. A tradução técnica exige avaliação de dificuldade, pressão, amostra e força do adversário; sem fatores calibrados, usar intervalos e estimativas explícitas. **Não aplicar descontos automáticos a velocidade, aceleração ou impulsão** pela liga. Evitar dupla penalização entre técnica, desempenho e o peso competitivo C.

### H — Histórico/reputação comprovada, 5%

Evidências de 2–3 temporadas, desempenho em grandes competições, continuidade e capacidade sustentada. Sem bônus por fama ou valor de mercado. O peso de 5% já limita a contribuição; calibrar mais tarde uma política mais explícita de diferencial vs. histórico neutro. Jogador lesionado ou veterano não merece OVR alto só pelo auge, mas também não deve zerar capacidade técnica pela falta de minutos.

## 3. Corte e amostras

**Gate obrigatório de pesquisa histórica:** seguir [`coleta-historica.md`](coleta-historica.md), consultando **Opta (Career History)** e **Sofascore (Temporada / Partidas)** antes de atribuir qualquer score. Coletar as mesmas temporadas e competições, registrar fontes e lacunas. Ter URL do perfil **não significa** ter verificado a média da nota histórica do Sofascore. A falta de uma das fontes deve ser informada e pode reduzir confiança.


Na avaliação de 07/11/2026, **2025/26 é a temporada prioritária encerrada**, e 2026/27 é complemento. Para amostras fracas, buscar 2024/25 e sinalizar defasagem. Proposta de confiança por minutos da amostra-base: alta ≥1800, moderada 900–1799, baixa <900. O parecer final pode baixar pela lesão e falta de continuidade.

Proposta de suavização NÃO aplicada aos exemplos:

`D_estimado = m/(m+900)*D_recente + 900/(m+900)*D_anterior`

Só aplicar quando D_recente e D_anterior já tiverem a mesma escala validada. Não misturar estatísticas de copas e ligas sem identificar o escopo e minutos de cada competição.

## 4. Faixas e classificação

Ver `config/criteria.v1.json` (fonte única). 86 referência máxima atual; 83–85 elite mundial; 80–82 extraclasse; 78–79 craque; 76–77 muito bom; 74–75 bom; 72–73 regular; 70–71 rotação; <70 abaixo do padrão. Acima de 86: revisão necessária, sem truncar silenciosamente.

## 5. Processo de edição

1. Registrar identidade, posição PES, clube e data de corte.
2. **Executar dupla consulta histórica Opta/Sofascore** por temporada e competição conforme `docs/coleta-historica.md`. Levantar jogos, minutos, gol/assistência, média Sofascore daquela temporada e outras métricas por posição apenas quando visíveis, com URL, data e escopo; registrar o que faltar.
3. Atribuir T/D/C/H **com justificativa e marcadores de incerteza**.
4. Calcular índice e Overall-alvo; devolver faixa quando a base for fraca.
5. Sugerir separadamente **25 atributos PES**, pé fraco (uso e precisão), forma, resistência a lesão, inspiração, habilidades especiais (catálogo de 41) e estilo de jogo. Não confundir com os 7 estilos COM.
6. Observar ou calcular com ferramenta especializada o Overall real do PES; registrar `overall_game_verified` apenas com evidência concreta.
7. Se o jogo divergir, investigar ponderação da posição e atributos, **sem inflar nota artificialmente**.
8. Avaliar vários jogadores e posições para calibrar os escores e prevenir viés de liga/reputação.

## 6. Restrições de honestidade

Não é fórmula oficial da Konami. O projeto [`gvoze32/pes21-player-rating`](https://github.com/gvoze32/pes21-player-rating) propõe engenharia reversa de OVR do motor; avaliar independentemente sua aplicabilidade ao patch antes de integrar. Não afirmar que a escala editorial *calcula* atributos a partir do desempenho: isso permanece aberto.
