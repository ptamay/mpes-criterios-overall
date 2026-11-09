# Contrato de resposta para agentes e IAs

## Valores comunicados pela liga

Uma ficha pode conter `league_assignment` com a decisão do responsável sobre atributos e Overall. É um **registro de edição da liga**, não um resultado calculado automaticamente e não uma validação independente da exibição no PES. Se houver divergência, exiba primeiro o **Overall adotado pela liga** e depois o `overall_target` editorial, preservando o índice e os quatro subscores originais. `overall_game_verified` continua `null` sem evidência. Exemplo em 09/11/2026: Montoro **77 OVR / 83 drible na liga**; índice MPES **78,295**, alvo editorial anterior **78**. Jamais reescrever T/D/C/H para obter o número escolhido.

## Resposta humana: regra de visualização

**Padrão: ficha curta e auditável**, não um dump de 25 atributos, **mas nunca sem a dupla consulta histórica à Opta e ao Sofascore**. Procedimento obrigatório: [`coleta-historica.md`](coleta-historica.md). Estrutura recomendada:

```text
NOME — POSIÇÃO | CLUBE | DATA DE CORTE
OVR-alvo: 78 (Craque) | Índice: 77,85 | Confiança: moderada
Base: temporada 2025/26, Premier League, 1.268 min (1G, 4A)
T 77 (45%) · D 73 (35%) · C 92 (15%) · H 77 (5%)
Destaques: aceleração 85; velocidade 86; drible 83
Limites: estatísticas sem percentis calibrados; OVR do jogo não validado
Pesquisa histórica: Opta [consultado/não acessível] | Sofascore [consultado/não acessível]
Fontes: [URLs e temporadas específicas] | Status: ESTIMATIVA EDITORIAL
```

**Quando solicitado a editar**, acrescentar grupos de atributos: ataque/técnica (10), físico (7), defesa (3), goleiro (5), parâmetros especiais (4), inspiração e habilidades. Usar catálogo de **41 skills/7 estilos COM** em `config/pes21-skills.json`; nenhuma habilidade fora do catálogo entra como confirmada. O README contém todas as tabelas. Nunca deixar atributo essencial implícito numa ficha 'completa'.

## Objeto JSON mínimo de saída

```json
{
  "player": "Alejandro Garnacho",
  "as_of": "2026-11-07",
  "main_season": "2025/26",
  "main_position": "PTE",
  "league": "Premier League",
  "sample_minutes": 1268,
  "dimension_scores": {"technical":77,"performance":73,"competition":92,"history":77},
  "index":77.85,
  "overall_target":78,
  "tier":"Craque",
  "overall_game_verified":null,
  "confidence":"moderate",
  "data_quality":"expert_estimate_not_calibrated",
  "positive_reasons":["...","..."],
  "uncertainties":["...","..."],
  "sources":["https://..."],
  "method_version":"1.0.0-experimental"
}
```

Este bloco é **um modelo**, não é permissão para inventar os campos ausentes. Cite fontes e separe fatos (`season_evidence`) de julgamentos (`dimensions`, `attributes`, `skills`). Use chaves do JSON mesmo quando responder em linguagem natural.

## Tipos de evidência

| Etiqueta | Significado |
| --- | --- |
| `verified_source` | Extraído de fonte externa citada, com data e escopo |
| `expert_estimate` | Avaliação editorial, sem fórmula treinada e validada |
| `editorial_proposal_not_measured_not_in_game_validated` | Valores sugeridos para o editor PES |
| `pending_validation` | Falta verificação técnica/estatística |

Os exemplos existentes têm `overall_game_verified: null`. O script local verifica **só a soma dos quatro scores** e a integridade de campos — não simula o motor PES.

## Consulta nova: procedimento obrigatório

1. Posição PES, jogador inequívoco, corte e clubes; **não pular a pesquisa histórica**.
2. Abrir Opta `Career History`, separar liga/copas e consultar as temporadas corrente, encerrada e anterior (e anteriores adicionais se necessário).
3. Abrir Sofascore, selecionar **Temporada + competição equivalente**, conferir média histórica da nota e métricas de posição; conferir partidas. Ausência é `NÃO_VERIFICADO`.
4. Registrar **duas URLs**, data da coleta, ano, torneio e resultado de acesso de cada fonte; harmonizar somente escopos iguais. Um link não prova que uma aba interativa foi consultada.
5. Análise por função; se faltarem percentis, sinalizar `expert_estimate` nas quatro notas.
6. Calcular índice com `config/criteria.v1.json` e indicar OVR-alvo, classificação, confiança, motivos e limites.
7. Em edição, entregar 25 atributos, quatro especiais, três inspiradores, habilidades do catálogo e status do estilo de jogo.
8. **Nunca** chamar os valores de OVR do jogo até conferência em editor; `overall_game_verified=null` enquanto pendente.

### Status de consulta a relatar

| Status | Quando usar |
| --- | --- |
| `CONSULTADO` | A página/dado da temporada foi efetivamente inspecionado na análise corrente |
| `PARCIAL` | Fonte acessada, mas período ou métrica crítica indisponível |
| `NÃO_ACESSÍVEL` | Fonte não acessada, bloqueada ou dependente de acesso não disponível |
| `HISTÓRICO_ARQUIVADO` | Dado oriundo de registro anterior com URL, sem consulta nova; informar data original |

Os exemplos de 07/11/2026 trazem dados de temporada Opta com URLs e **não documentam média histórica Sofascore por competição**. Não preencher esse campo por inferência.


## Velocidade e aceleração: contrato novo (08/11/2026)

Antes de propor velocidade/aceleração, ler [`avaliacao-fisica.md`](avaliacao-fisica.md). Verificar **primeiro o painel "Desempenho de corrida" do Sofascore**, além de outros dados de rastreamento: reportar `top_speed_kmh` (pico, não por 90), `sprints_per90`, `distance_km_per90`, fonte, temporada, competição, amostra e confiabilidade. Um dado físico rastreável pode apoiar **Velocidade Nível A**, sem conversão calibrada automática para nota PES. Para **Aceleração Nível A**, exigir medição de tempo de arrancada — sprints/90 não bastam. Na ausência, indicar estimativa Nível C com faixa e evidências técnicas indiretas ou `NÃO_VERIFICADO`. Não vincular captura anônima a nenhum atleta.

## Consulta de força da competição ao atribuir atributos (v1.8)

O agente DEVE ler [`contextualizacao-competitiva.md`](contextualizacao-competitiva.md) antes de usar dribles, chutes ou passes para gerar notas PES. Taxas e percentis da liga chinesa, MLS ou outras ligas não podem ser tratados como capacidades equivalentes no Brasileirão sem correção/ressalva. Informar `liga_origem`, `liga_referencia`, `status_coeficiente_transferencia` e `grau_de_confianca` por atributo crucial. Sem fatores validados: **estimativa editorial**, nunca valor medido/calculado. Não reduzir atributos físicos automaticamente nem aplicar dois descontos completos para a mesma diferença competitiva.
