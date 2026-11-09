# Habilidades e estilos de jogo do PES 2021

As **41 habilidades de jogador** e os **7 estilos COM** são conjuntos diferentes. O catálogo estruturado está em [`../config/pes21-skills.json`](../config/pes21-skills.json). A tabela integral, com nomes em inglês, descrição resumida e os exemplos de Garnacho/Lukaku, aparece diretamente no [`README.md`](../README.md).

Fonte comunitária de nomenclatura do PES 2021: https://www.pesmaster.com/pes-2021/search/ . Os nomes em português no repositório são **traduções explicativas** e podem não coincidir com o idioma exato do patch utilizado pela liga. O projeto não se apresenta como manual oficial da Konami.

**Não confundir:**

- **Atributos numéricos (25):** notas 40–99 no editor de referência, que formam as capacidades do jogador e se relacionam ao Overall calculado pelo jogo.
- **Parâmetros especiais (4):** uso de pé fraco, precisão do pé fraco, forma física, resistência a lesões. Não são habilidades ativáveis.
- **Inspiração (3):** carregando, passe rasteiro, passe alto, de zero a duas estrelas.
- **Habilidades de jogador (41 possibilidades):** recursos como Double Touch, First-time Shot e Captaincy; cada jogador possui um subconjunto. A lista de habilidades **propostas** nos exemplos não está validada no editor.
- **Estilos COM (7 possibilidades):** tendências de ações da IA quando controla o jogador, não são as 41 habilidades de jogador.
- **Estilo de jogo principal:** papel/movimentação (por exemplo, pontas, centroavantes, organizadores). Campo distinto, ainda não definido nos exemplos.

## Política de nomenclatura

Em arquivos JSON use o identificador em **inglês** do catálogo. Na resposta em PT-BR, use rótulo traduzido e opcionalmente apresente o inglês. Termos sem correspondência inequívoca ficam em `skills_pending_mapping` em vez de criar uma habilidade inexistente.

Exemplo de decisão editorial: a proposta antiga de Garnacho mencionou **"Controle de domínio"**; essa expressão não foi vinculada de forma segura a um item específico do catálogo de 41. Foi mantida como pendência, **não** como uma habilidade PES confirmada. Demais sugestões foram normalizadas ao catálogo, mas sua atribuição ao atleta ainda é provisória.

O significado de cada habilidade pode ser consultado em https://pesmyclubguide.com/player-skills/ , que é também uma fonte comunitária, não uma confirmação da versão ou edição específica da liga.
