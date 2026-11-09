# Claude Code — entrada do projeto MPES

@AGENTS.md

Este arquivo importa as instruções canônicas acima. Não copie nem reformule os pesos,
atributos ou procedimentos aqui: a fonte normativa continua em `AGENTS.md`,
`docs/contrato-ia.md` e `config/criteria.v1.json`.

## Fluxo no Claude Code

- Antes de avaliar jogador ou editar ficha, consulte `docs/contrato-ia.md`,
  `docs/coleta-historica.md`, `docs/contextualizacao-competitiva.md`
  e `docs/avaliacao-fisica.md` conforme a tarefa.
- Consulte o estado atual de `main` antes de editar; não use um ZIP histórico como fonte da verdade.
- Não publique modificações sem validação e autorização para a ação.
- Validações: `python -m src.pes21_method validate` e
  `python -m unittest discover -s tests -v`.
- Relate fontes realmente consultadas, limitações, OVR-alvo editorial e se o PES foi testado.
- Confira o contexto carregado com `/context all` (Claude Code). Em caso de
  mudança de documentação, reinicie a sessão ou atualize o contexto.

**Uso:** Claude Code (CLI/Desktop). No chat web Claude, disponibilize o repositório
ou os arquivos do projeto pela integração ou anexos: não há garantia de
carregamento automático deste arquivo apenas por digitar uma URL.
