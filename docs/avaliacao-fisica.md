# Protocolo de velocidade e aceleração — pesquisa física, Sofascore e fallback

**Estado:** protocolo atualizado em 08/11/2026; a conversão numérica ao PES ainda **não está calibrada**. Nenhuma ficha anterior foi alterada automaticamente nesta revisão.

## Ordem obrigatória — procurar dados físicos antes das estatísticas técnicas

1. **Abrir o Sofascore do jogador**, escolher temporada e competição e procurar o painel **Desempenho de corrida / Running Performance**, quando houver. Registrar: **velocidade máxima (km/h)**, **número de sprints por 90**, **distância percorrida por 90 (km)**, URL do atleta, temporada/competição, data de consulta, quantidade de partidas/minutos cobertos e qualquer definição de cobertura ou medição publicada. A disponibilidade depende da competição e do período; **não presumir** que a seção esteja presente em todos os campeonatos. A Sofascore confirmou publicamente as três métricas em 2025: https://www.sofascore.com/news/running-performance-sofascore-brings-you-one-of-the-most-requested-features e https://www.sofascore.com/pt/news/estatisticas-de-corrida-da-premier-league-principais-corredores-da-primeira-rodada .
2. **Buscar dados físicos independentes**, quando disponíveis: Opta Vision, SkillCorner, órgão oficial de liga ou rastreamento validado. Para velocidade preferir métricas de pico robusto / distribuição de picos por jogo; para aceleração, **tempos de arrancada, Time to Sprint, Time to HSR, 0–10 m** ou equivalente medido. Registrar se as métricas são equivalentes, sem combinar limiares de sprint de provedores diferentes sem metadados.
3. **Separar claramente as três medidas Sofascore**:
   - `top_speed_kmh`: medida física de **velocidade de pico** (evidência direta de **Velocidade**); **NÃO** é um número "por 90" nem velocidade média da partida, ainda que esteja dentro de um painel rotulado "por 90". O pico depende das oportunidades de correr e do período monitorado.
   - `sprints_per90`: **frequência** de sprints, não valor de aceleração ou velocidade máxima. Sem definição pública do limiar de sprint, não comparar diretamente entre fontes. Pode fornecer contexto de intensidade e uso da velocidade.
   - `distance_km_per90`: **volume de deslocamento**, evidência complementar para **Resistência**, mas não prova capacidade de manter rendimento sob fadiga nem velocidade.
4. **Nível A — VELOCIDADE**: elegível quando o dado físico de pico for atribuível inequivocamente ao atleta, com fonte rastreável, temporada/competição, período, amostra e unidade; preferir consistência em várias partidas e a referência operacional proposta de **5 partidas**. Sem período/identificação/amostra, o número do screenshot pode ser reportado como **medição apresentada**, mas **não é certificação A da ficha**. Além disso, ainda exige **calibração de km/h para a escala PES 40–99** usando atletas de referência: nunca deduzir uma nota exata por regra de três.
5. **Nível A — ACELERAÇÃO**: exige medição direta de arrancada/tempo para velocidade de referência; **velocidade máxima, sprints por 90, km por 90, dribles e faltas sofridas não medem aceleração**. Se ausente, pode-se estimar conservadoramente em **Nível C** com esses indicadores indiretos do Sofascore, registrando faixa e incerteza; ou **Nível B** com observação estruturada de vídeo efetivamente realizada.
6. **Sem métricas de corrida**: utilizar o fallback anterior pelo Sofascore (dribles certos/tentados por 90, taxa, faltas sofridas, transições e progressões quando disponíveis). Não inventar km/h, velocidades, tempos de sprint nem percentis físicos. Se for impossível estimar, devolver `NÃO_VERIFICADO`.
7. **Manter independência:** a força da liga, reputação, altura, idade e gols **não acrescentam pontos automaticamente** a Velocidade ou Aceleração. Manter `overall_target` separado de `overall_game_verified`; não mexer em avaliações históricas automaticamente só porque uma nova fonte está disponível.

## Exemplo de leitura do painel (captura sem identificação do atleta)

A imagem apresentada pelo gestor da liga contém `distance_km_per90=9.4`, `sprints_per90=7.8` e `top_speed_kmh=34.8`. **Não associar esses valores a Montoro, Bontempo ou qualquer outro atleta sem confirmação da origem do painel**, temporada e amostra. O último indicador é uma velocidade de pico elevada, mas **não determina por si só um atributo PES**; o dado de aceleração permanece ausente.

## Exemplos de aplicação anteriores (não recalculados)

- **Álvaro Montoro (08/11/2026):** velocidade 77 e aceleração 81, ambas nível **C**, com base em evidências técnicas indiretas; **verificar agora também o painel de corrida da competição/temporada antes de revalidar**. Fontes anteriores: https://www.driblou.com.br/data/jogador/alvaro-montoro-1650770 ; https://www.fotmob.com/players/1607035/alvaro-montoro .
- **Gabriel Bontempo:** velocidade 74 e aceleração 77, estimativas nível **C**, igualmente pendentes de nova verificação do painel físico.
- **Victor Hugo:** velocidade 76 e aceleração 78, estimativas não certificadas; passe alto discutido anteriormente de 67 para 70, sem ficha incorporada.

## Campos para a coleta por atleta

- `level_speed` e `level_acceleration`: `A_TRACKED`, `B_VIDEO`, `C_SOFA_INDIRECT`, `UNVERIFIED` — **independentes**.
- `player_id`, `source_url`, `retrieved_at`, `season`, `competition`, `match_count`, `minutes`, `measurement_scope` (`single_match`, `season_aggregation`, `unknown`).
- `top_speed_kmh`, `sprints_per90`, `distance_km_per90`, `sprint_threshold_kmh` (pode ser `null`), `time_to_speed_seconds` (pode ser `null`), `tracking_provider` (se conhecido), `source_methodology` (se publicada).
- `pes_speed_estimate`, `pes_acceleration_estimate`, `plausible_range`, `rationale`, `limitations`, `calibration_status`, `pes_game_verified`.
- **Se apenas o pico de velocidade for verificado**, `level_speed` pode diferir de `level_acceleration`; não atribuir os dois Nível A por analogia.
