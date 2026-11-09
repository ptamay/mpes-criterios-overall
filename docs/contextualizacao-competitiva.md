# Contextualização de atributos entre competições — protocolo v1.9

**Estado:** princípio aprovado pela liga; conversão numérica **ainda NÃO calibrada**. **Liga de referência:** Brasileirão Série A. Preserve os pesos gerais T45/D35/C15/H5 em `config/criteria.v1.json`.

## Registro de força da liga — China / Brasil (v1.9, 08/11/2026)

- **Referência histórica pública:** levantamento da Opta Power Rankings relatado em 04/11/2025 (dados divulgados em 03/11): **Chinese Super League 62,8** (102ª colocação) e **Brasileirão 77,9** (8º), **mesmo snapshot** e diferença de **15,1**. Fonte **secundária**, não feed direto da Opta: <https://biz.chosun.com/en/en-sports/2025/11/04/XTVX4JYVHZDM5OLTSB6XJMUVVY/?outputType=amp>.
- **C62,8:** somente proxy histórica na ausência de rating chinês contemporâneo de 2026 ou força dos adversários reais ponderada por minutos. **C60:** cenário conservador escolhido para análise de sensibilidade, NÃO número oficial da Opta. Ver `config/competition-snapshots.v1.json`.
- **Proibição de mistura de recortes:** o Brasileirão aparece como **83,3 em julho/2026** em outra edição da Opta; não comparar 83,3 (2026) com 62,8 (2025) como se fossem simultâneos.
- **Atributos:** percentil/eficiência de dribles, passe, finalização, defesa e jogo aéreo na China precisam de dificuldade ajustada por adversário; sem coeficiente calibrado, avaliar com faixas, justificativas e cautela. Não aplicar automaticamente −N pontos fixos por liga, sobretudo a atributos físicos mensuráveis.
- **Auditoria de dupla contagem:** D = produção/regularidade **observada** na liga; T = capacidade de execução **potencialmente transferível** em oposição de nível comparável; C = exposição ao nível competitivo (**proxy histórica**); H = histórico. Não dizer que D prediz diretamente gols/assistências no Brasil. C deve ser reavaliado se uma normalização explícita já for aplicada a T e D.
- **Cryzan refeito:** T78 D82 C62,8 H77 → **77,07**, Overall-alvo 77; C60 → **76,65**, Overall-alvo 77. Atributos reavaliados sem conversão causal comprovada: drible 80, finalização 78, contato físico 80, cabeceio 73, velocidade 78/aceleração 77 Nível C. Ver `examples/cryzan.json`.

## Princípio

**O mesmo percentual de sucesso em uma ação não implica a mesma habilidade transferível entre ligas.** Ex.: 62,5% de dribles certos na Superliga Chinesa não é automaticamente equivalente a 62,5% no Brasileirão; qualidade da oposição, pressão, espaços e papel tático variam. Não reduzir cada atributo por um número fixo com base apenas no nome da liga.

A avaliação da ação precisa considerar: tentativas e sucessos **por 90 minutos**, taxa de sucesso, dificuldade das tentativas, nível dos marcadores, posição/função, força e estilo das equipes, tamanho da amostra e recortes por temporada/competição. Quando disponível, usar força do **adversário enfrentado por minuto** (Opta Power Rankings), preferencialmente acompanhada de métricas de pressão e contexto. Ranking Opta de clube/competição **não mede habilidade de drible individual**.

## Mapa de sensibilidade dos 25 atributos

| Contexto de oposição | Atributos | Abordagem |
| --- | --- | --- |
| **Alto** | Drible; condução firme; talento ofensivo; finalização; cabeceio; talento defensivo; desarme | Corrigir a **interpretação das ações** pelo nível e situação do adversário, não transformar % em nota PES diretamente. |
| **Médio/alto** | Passe rasteiro; passe alto | Considerar dificuldade, pressão e direção dos passes; separar lançamento de cruzamento. |
| **Médio** | Controle de bola; equilíbrio; contato físico | Combinar ações sob pressão e análise técnica; medir força/mobilidade se houver dados específicos. |
| **Sem redução automática por liga** | Velocidade; aceleração; impulsão; força do chute; resistência; curva; chute colocado | Preferir dados físicos ou observação técnica relevante. Não reduzir km/h por estar em liga inferior. |

A ordem e a intensidade acima são hipóteses de **dependência de contexto**, não coeficientes numéricos validados. Ações sob pressão contra melhores defensores têm maior exigência; isso não significa que toda ação na China seja fácil ou toda ação no Brasil seja difícil.

## Protocolo de aplicação

1. Identificar atleta, posição PES, data de corte e temporadas. Consultar Opta e Sofascore; quando indisponível, identificar fontes substitutas.
2. Separar jogadores comparáveis por função e **medir tentativas, sucessos e eficiência por 90**. Não usar só gols/assistências, rating ou percentil dentro da liga de origem.
3. Para cada ação, levantar qualidade dos oponentes e, quando possível, intensidade de pressão, localização e dificuldade. Preferir rating de cada equipe enfrentada ao da liga inteira.
4. Aplicar **suavização amostral** antes de comparar taxas. Uma taxa de sucesso de 60% em 5 tentativas é muito menos confiável que 60% em 100.
5. Calibrar **equivalência entre ligas e por atributo** com jogadores transferidos que atuaram nas duas ligas; controlar idade, minutagem, posição e papel. Comparar desempenho antes/depois. Não inventar fator exato.
6. Se ainda não houver fator empírico válido, marcar cada atributo como `ESTIMATIVA_EDITORIAL_CONTEXTUALIZADA`, com faixa e confiança, e tornar explícita a hipótese de força da liga.
7. Executar teste de sensibilidade e evitar **dupla penalização**: quando D já incorpora correção integral pela liga de destino, não descontar D novamente pela mesma razão. O componente C continua com peso 15%, mas testar sua redundância; enquanto não calibrado, tratar T/D/C como estimativas editoriais separadas.
8. Preservar atributos físicos medidos (velocidade máxima, aceleração, salto) quando a liga muda. Confirmar no PES o OVR realmente exibido; não ajustar atributos para perseguir OVR-alvo.

## Exemplo — Cryzan (revisão experimental)

Estatísticas brutas da Superliga Chinesa (recorte histórico de 23 jogos, antes da partida de 08/11/2026): 85 dribles certos, 62,5% de sucesso, 19 gols, 9 assistências. Essas são evidências de **produção observada**, não garantia de produção equivalente no Brasileirão. O ajuste experimental atualizado de `dribbling` 84→80, `finishing` 81→78, `attacking_prowess` 82→78 e `low_pass` 76→74 expressa cautela de transferibilidade; **esses deltas não foram calculados a partir de um fator validado** e devem ser recalibrados. `speed` 78, `acceleration` 77, `jump` 78 e `kicking_power` 83 permanecem **estimativas físicas não medidas**, sem desconto por país.

Revisão atual v1.9: T78, D82, C62,8 (proxy histórica Opta relatada em fonte secundária), H77 → índice 77,07, **OVR-alvo provisório 77**. O 62,8 NÃO é rating contemporâneo de 2026. As alterações em T/D/C representam hipóteses editoriais distintas (capacidade transferível, produção/regularidade observada, exposição competitiva); não declarar ausência de dupla contagem até validação empírica. Cenário conservador C60 → 76,65 (OVR77). Testar sensibilidade também para T e D. `overall_game_verified` continua nulo.

## Fontes e limites

- [Opta Power Rankings: funcionamento e escala de equipes](https://theanalyst.com/articles/power-rankings-your-club-ranked)
- [Opta: comparabilidade de ligas](https://theanalyst.com/articles/strongest-football-leagues-in-the-world-opta-power-rankings)
- [Estudo de transferência de desempenho entre ligas (2026)](https://doi.org/10.1177/22150218261481583)
- [CIES/SkillCorner: desempenho sob pressão](https://football-observatory.com/IMG/sites/mr/mr93/en/)
- [Estudo sobre dinâmica de dribles](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624867/)

A literatura sustenta a necessidade de contextualização, **não** valida os valores de atributos específicos desta ficha. O exemplo é uma hipótese para testes em uma liga personalizada, não modelo pronto para predição profissional.
