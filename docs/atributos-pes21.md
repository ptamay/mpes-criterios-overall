# Dicionário de atributos PES 2021

Transcrição/paráfrase operacional das definições da captura apresentada pelo administrador da liga em 07/11/2026. **É a referência adotada pela liga**; este repositório não constitui documentação oficial publicada pela Konami. Os nomes em inglês são chaves de dados internas. Todos os **25 atributos principais** são numéricos na escala comum do editor do PES; os limites específicos para cada um devem ser confirmados conforme patch/editor.

| Chave JSON | Atributo | Interpretação operacional |
| --- | --- | --- |
| `attacking_prowess` | Talento ofensivo | Habilidade ao atacar, movimentação e aproveitamento de espaço |
| `ball_control` | Controle de bola | Domínio e controle geral, incluindo recepção e fintas |
| `dribbling` | Drible | Controle de bola ao progredir/contornar adversário em velocidade |
| `tight_possession` | Condução firme | Capacidade de mudar a direção do drible em baixa velocidade |
| `low_pass` | Passe rasteiro | Precisão de passes pelo chão |
| `lofted_pass` | Passe alto | Precisão de passes aéreos |
| `finishing` | Finalização | Precisão do chute ao gol |
| `heading` | Cabeceio | Precisão do cabeceio, **não capacidade de salto** |
| `set_piece_taking` | Chute colocado | Precisão em bolas paradas, incluindo faltas |
| `curl` | Curva | Quantidade de efeito imprimível à bola |
| `speed` | Velocidade | Agilidade/velocidade sem bola |
| `acceleration` | Aceleração | Rapidez para alcançar velocidade máxima |
| `kicking_power` | Força do chute | Potência gerada ao chutar |
| `jump` | Impulsão | Capacidade de saltar |
| `physical_contact` | Contato físico | Afastar adversários e manter equilíbrio sob pressão física |
| `balance` | Equilíbrio | Evitar desarmes e se manter de pé sob contato |
| `stamina` | Resistência | Preparo e menor desgaste durante a partida |
| `defensive_awareness` | Talento defensivo | Habilidade e posicionamento ao defender |
| `ball_winning` | Desarme | Proficiência para ganhar posse em desarmes |
| `aggression` | Agressividade | Intensidade/frequência de tentativa de desarme |
| `gk_awareness` | Talento de GO | Atributo específico do goleiro (definição detalhada não veio na captura) |
| `gk_catching` | Firmeza de GO | Atributo específico do goleiro (não detalhado na captura) |
| `gk_clearing` | Afast. de bola de GO | Atributo específico do goleiro (não detalhado na captura) |
| `gk_reflexes` | Reflexos de GO | Atributo específico do goleiro (não detalhado na captura) |
| `gk_reach` | Alcance de GO | Atributo específico do goleiro (não detalhado na captura) |

## Escalas especiais

| Campo | Faixa | Interpretação |
| --- | --- | --- |
| `weak_foot_usage` | 1–4 | Frequência de uso do pior pé |
| `weak_foot_accuracy` | 1–4 | Precisão de ações com o pior pé |
| `form` | 1–8 | Capacidade de permanecer em boa forma ao longo do tempo |
| `injury_resistance` | 1–3 | Resistência a lesões; **não** igual ao total de minutos disponíveis |

## Campos separados dos 25 atributos

- `inspiration`: estrelas no contexto de **carregando, passe rasteiro e passe alto**; os exemplos usam 0–2 conforme a interface da liga.
- `special_skills_proposed`: lista editorial de habilidades especiais, **não confirmada** em partidas atuais ou base de dados do PES.
- `playing_style`: tipo de movimentação no PES; `null` quando não foi escolhido/validado.
- `position_pes`, `preferred_foot`: posição principal e pé dominante.

**Atenção:** a fórmula de OVR in-game pode considerar alguns campos de forma diferente segundo a posição; não assumir que as escalas especiais, inspiração e habilidades especiais entram diretamente no índice 45/35/15/5.

## Habilidades de jogador e estilos COM

Consulte o catálogo de **41 habilidades de jogador** e **7 estilos COM** em [`../config/pes21-skills.json`](../config/pes21-skills.json), e a visualização integral no [`../README.md`](../README.md). Os nomes EN são identificadores estáveis; traduções PT-BR explicativas. Resistência a lesões, forma e pé fraco são parâmetros especiais, não habilidades.
