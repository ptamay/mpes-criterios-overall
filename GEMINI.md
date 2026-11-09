# Gemini CLI — entrada do projeto MPES

@./AGENTS.md

**Fonte canônica:** `AGENTS.md` → `docs/contrato-ia.md` →
`config/criteria.v1.json`. Este arquivo não redefine a metodologia.

## Procedimento

- Para avaliações, leia os documentos aplicáveis de `docs/` e a ficha de referência
  em `examples/`; não conclua que um arquivo foi lido sem efetivamente acessá-lo.
- Pesquise Opta + Sofascore com temporada, competição, data e status de acesso.
  Identifique ausência de dados e fontes alternativas.
- Cuidado com estatísticas de drible, finalização e passe de ligas com forças diferentes.
  Não desconte velocidade e aceleração automaticamente pela liga.
- Diferencie índice editorial/OVR-alvo do Overall efetivamente exibido no PES.
- Para alterar arquivos, valide com `python -m src.pes21_method validate` e
  `python -m unittest discover -s tests -v`; revise o diff antes de publicar.
- Repositório oficial: `ptamay/mpes-criterios-overall` (`main`).

**Gemini CLI:** `GEMINI.md` é contexto de projeto; confira com `/memory show`
e recarregue alterações com `/memory reload`.

**Gemini no navegador:** importar o repositório por **Adicionar arquivos →
Mais uploads → Importar código**. Importação é um snapshot, não sincronização.
O chat web não deve ser considerado como carregando automaticamente `GEMINI.md`
como instrução ativa: peça explicitamente para ler `AGENTS.md`,
`docs/contrato-ia.md` e a configuração. Tutorial: `docs/uso-gemini.md`.
