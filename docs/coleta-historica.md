# Protocolo obrigatório de pesquisa histórica — Sofascore + Opta

**Finalidade:** antes de propor um novo Overall ou atualizar um existente, consultar temporadas anteriores do jogador **em duas fontes complementares**. A página inicial do perfil, o gráfico "últimos 12 meses", o nome do clube e o histórico de transferências **não substituem** as estatísticas por temporada e competição.

**Fontes prioritárias:**
- **Sofascore:** perfil do jogador → aba **Temporada** → escolher ano **e competição**; consultar a seção de estatísticas/avaliações e a aba de partidas. Comparação sazonal: https://www.sofascore.com/pt/football/player/compare (permite, quando disponível, comparar o mesmo jogador entre temporadas ou equipes).
- **Opta / Opta Analyst:** perfil do jogador → **Career History** → selecionar **League**, **Domestic Cups** ou **Continental Cups**. Usar os registros por ano, clube e torneio; seção **Stats** e Opta Player Radars se a ferramenta pública cobrir o atleta/época: https://theanalyst.com/articles/opta-player-radars-comparison-tool.

**Acesso:** navegar normalmente por páginas públicas e ferramentas autorizadas. Não pressupor acesso a dados premium ou APIs internas. Se um campo exigir login, não carregar, estiver ausente ou não existir naquela competição, registrar `NÃO DISPONÍVEL`; não preencher a partir de memória, inferência ou um valor de outro torneio.

## Passo a passo — execução mínima exigida para cada atleta

1. **Identificar** nome, perfil inequívoco (URL/ID), posição PES, clube(s), data de corte e histórico de transferências. Conferir que não há homônimo.
2. **Abrir a Opta — Career History.** Listar a temporada corrente, a **última temporada completa** e **pelo menos mais uma anterior**; buscar a terceira anterior quando lesão, poucos minutos ou transferência distorcerem a amostra. Para cada clube/torneio, registrar jogos, minutos, gols, assistências e escopo. Se necessário, repetir nas opções de copas domésticas/continentais. Não somar uma linha agregada de clube à linha da mesma liga: são recortes sobrepostos.
3. **Abrir o Sofascore — aba Temporada.** Selecionar a **mesma temporada e competição** da linha Opta. Registrar a **média de nota Sofascore da temporada**, minutos/partidas e métricas da posição que estiverem disponíveis: xG, xA, finalizações, dribles, passes decisivos, duelos, perdas de posse e frequência de bons/maus jogos. **Inspecionar também "Desempenho de corrida", se disponível**: velocidade máxima (km/h, pico), número de sprints/90 e distância/90, junto com a amostra/escopo. Consultar [`avaliacao-fisica.md`](avaliacao-fisica.md) para certificação Nível A e fallback físico; sprint count não é aceleração. Verificar a aba **Partidas** e, se útil, a comparação entre anos. Não usar uma nota de jogo isolado ou gráfico de meses como se fosse média anual.
4. **Confrontar por escopo.** A comparação só é direta quando temporada, clube, competição e natureza da estatística coincidem. Anotar discrepâncias; escolher uma fonte prioritária por **campo**, sem harmonização silenciosa. Gols de copa não entram na conta de liga. Utilizar valores por 90 minutos **somente** com denominador de minutos compatível.
5. **Escolher a amostra.** Como regra inicial, a última temporada completa é a base. A temporada em andamento é contexto. Quando a completa tiver menos de **900 minutos**, recuperar a última temporada robusta (normalmente 2024/25, no corte de 07/11/2026) e **reduzir a confiança**. Entre 900–1.799 min = confiança amostral moderada; >=1.800 = alta. Lesão ou grande mudança de função pode reduzir a confiança final independentemente dos minutos.
6. **Avaliar por posição.** Para ponta, priorizar dribles certos/taxa, progressão, criação, xG/xA e eficiência. Para centroavante, priorizar xG sem pênalti, gols, chances, finalização, presença de área, duelos e jogo aéreo. Para outras funções, construir conjunto equivalente. Média Sofascore é indício, não OVR nem atributo PES automático.
7. **Força competitiva.** Priorizar nível de cada adversário enfrentado ponderado pelos minutos; se inviável, usar média datada da liga (Opta Power Rankings) rotulada **proxy**, sem premiar automaticamente o clube ou duplicar o efeito da liga já considerado nos dados.
8. **Emitir registro de auditoria.** Informar links consultados, data da consulta, temporadas, escopo, quais métricas estavam disponíveis, contradições e dados ausentes. Separar `DADO_VERIFICADO`, `ESTIMATIVA_EDITORIAL`, `PROPOSTA_PES` e `NÃO_VERIFICADO`.
9. **Só então calcular T/D/C/H** com os pesos da liga e propor a ficha PES. Os quatro subscores ainda são **editoriais** — não existe conversão estatística calibrada. Indicar o intervalo de incerteza e deixar `overall_game_verified=null` até confirmar no editor do PES.

## Campos mínimos de uma coleta por temporada

| Campo | Tipo/nota |
| --- | --- |
| Jogador e ID | nome e URL persistente do perfil |
| `as_of` e `retrieved_at` | data de corte esportiva e data da consulta; não são a mesma coisa |
| Temporada | `2025/26`, `2024/25`, etc. |
| Clube e torneio | nomes explícitos, considerando transferências |
| Escopo | liga, copa doméstica, continental ou *todas as competições* |
| Minutos, jogos, G, A | incluir URL da linha ou tabela Opta; registrar ausência |
| Sofascore temporada | média apenas do ano/torneio selecionado, com URL da tela ou perfil e seleção anotada |
| Métricas de função | métricas avançadas disponíveis e denominador correto |
| Nível dos oponentes | rating/força e data, ou `proxy` explicita |
| Disponibilidade e histórico clínico | somente quando fontes confiáveis permitirem, sem deduzir atributo de lesão de um único evento |
| Conflitos entre provedores | valores lado a lado e decisão explicada |

**Importante:** Sofascore explica que as notas dependem das ações registradas e da posição: https://sofascore.helpscoutdocs.com/article/50-sofascore-statistical-ratings-explained. A própria plataforma alerta que determinadas ligas podem ter dados tardios ou ausentes: https://sofascore.helpscoutdocs.com/article/176-player-stats-and-ratings-availability?lng=pt-BR.

## Links prontos para os exemplos — não substituem a navegação por temporadas

| Jogador | Sofascore | Opta — Career History |
| --- | --- | --- |
| Alejandro Garnacho | https://www.sofascore.com/pt/football/player/alejandro-garnacho/1135873 | https://theanalyst.com/players/4179/alejandro-garnacho/career |
| Romelu Lukaku | https://www.sofascore.com/pt/football/player/romelu-lukaku/78893 | https://theanalyst.com/players/4855/romelu-lukaku/career |

### Exemplo de trilha documental para 07/11/2026

- **Garnacho:** Opta 2025/26, Chelsea, Premier League: 24 jogos, 1.268 min, 1 G e 4 A; verificar separadamente seu desempenho por competição no Sofascore. A amostra de 2026/27 ainda é pequena. A ficha JSON preserva o recorte da Opta; **não foi registrada média histórica Sofascore por temporada**, portanto não inventar.
- **Lukaku:** Opta 2025/26, Napoli, Serie A: 39 min (não é amostra suficiente). Recuar para 2024/25 (2.871 min, 14 G, 10 A), consultar a temporada correspondente no Sofascore e sinalizar possível defasagem física/lesão. **Não há nota Sofascore histórica validada armazenada** nos exemplos.

**Controle de qualidade:** se a IA não conseguiu acessar uma das duas fontes, não deve declarar que concluiu uma dupla consulta. Pode apresentar resultado parcial, descrever a lacuna e reduzir a confiança. Nenhum link por si só prova que a aba da temporada foi consultada.
