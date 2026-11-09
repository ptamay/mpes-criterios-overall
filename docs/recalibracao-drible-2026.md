# Calibração do atributo Drible — recorte 2026 (v1.10)

## Regra de evidência

- A classificação "drible" do PES deve representar **capacidade atual de superar adversários em condução**, separada de **controle de bola** (recepção/domínio) e **condução firme** (retenção em espaços curtos).
- Não transformar automaticamente percentil ou aproveitamento de drible dentro de uma liga em ponto PES. Observar dribles certos e tentados/90, amostra, zona, nível de marcador, qualidade e tipo da ação, posição e vídeo.
- Dar peso à continuidade da capacidade técnica observada, sem tomar a versão histórica/auge como atributo atual. Histórico e reputação NÃO são ancoragem obrigatória.
- Evitar atribuir `93–94` a um jogador apenas por seu auge ou nome; os números devem ser sustentados por evidência de execução e nível atual dos oponentes. Isso não cria teto definitivo para toda a liga.
- Separar: velocidade = velocidade de corrida sem bola, aceleração = arrancada, drible = execução técnica com a bola. O número de dribles certos não determina diretamente velocidade/aceleração.
- Contextualizar dificuldade competitiva nas notas técnicas e manter C como proxy de exposição competitiva residual, auditando possível dupla penalização.

## Exemplo documentado — 09/11/2026

| Jogador | Liga | Sofascore jogos/minutos | Média | Dribles certos/jogo | Acerto | Drible PES editorial | OVR-alvo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Messi | MLS 2026 | 30 / 2.574 | 8,39 | 2,0 | 51,3% | 90 | 86 |
| Neymar | Brasileirão 2026 | 14 / 1.178 | 7,62 | 1,4 | 33,3% | 88 | 82 |

- Fonte comparativa: [Messi Sofascore](https://www.sofascore.com/pt/football/player/compare?ids=12994), [Neymar Sofascore](https://www.sofascore.com/pt/football/player/compare?ids=124712).
- Snapshot de força de liga de **03/11/2025**, publicado em 04/11/2025 por fonte secundária referindo Opta: MLS 76,5 e Brasil 77,9. Não misturar 83,3 (Brasil 27/07/2026) ao mesmo cálculo.
- Dúvida: a diferença técnica de 2 pontos não deriva de uma fórmula estatística calibrada; ela é uma **proposta editorial orientada pelos dados de 2026**.
- A evidência física rastreada de pico de velocidade ou tempo de aceleração por jogador não foi certificada nessa coleta. Não inventar km/h.
- Ambas as fichas preservam posição **MAT** para comparação com a liga personalizada; clubes reais em 2026: Inter Miami e Santos.
- Fichas: [`lionel-messi.json`](../examples/lionel-messi.json), [`neymar.json`](../examples/neymar.json).
