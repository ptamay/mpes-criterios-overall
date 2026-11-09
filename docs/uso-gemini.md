# Tutorial — MPES no Gemini (navegador e CLI)

Repositório oficial: https://github.com/ptamay/mpes-criterios-overall

## Gemini no navegador — forma recomendada para avaliar jogadores

Em **computador**, acesse https://gemini.google.com/ e faça login. Na caixa
de mensagem, selecione **Adicionar arquivos** → **Mais uploads** →
**Importar código**. Cole a URL acima, clique em **Importar** e prossiga
com as instruções de autorização, se aparecerem. Em seguida, envie um prompt
de leitura e só depois peça a avaliação do jogador.

Exemplo de prompt de preparação:

> Use o repositório importado `ptamay/mpes-criterios-overall` como fonte canônica.
> Leia `AGENTS.md`, `docs/contrato-ia.md`, `config/criteria.v1.json`,
> `docs/metodologia.md`, `docs/contextualizacao-competitiva.md`
> e `docs/avaliacao-fisica.md`. Confirme quais arquivos realmente conseguiu
> ler e informe a versão da documentação, os pesos T/D/C/H e as limitações
> do método. Não avalie um jogador ainda e não invente dados ausentes.

Depois, solicite: `Avalie [jogador] na posição PES [posição], com data de
corte [AAAA-MM-DD]. Pesquise Sofascore/Opta, entregue índice, Overall-alvo,
25 atributos, parâmetros especiais, evidências, faixa e confiança. Não
presuma que o Overall foi validado dentro do PES.`

### Limitações da integração web

- **Não basta colar a URL como mensagem**: é necessário usar a opção
  **Importar código** para que o conteúdo entre na conversa.
- A importação é uma **captura estática**. Se novos commits forem publicados,
  **importe o repositório novamente** para obter a versão atualizada.
- O conector do Gemini web **não escreve alterações no GitHub** e não
  recupera histórico de commits ou PRs. Para registrar fichas, traga o
  resultado para revisão e publicação pelo fluxo do projeto.
- Atualmente a ajuda do Google informa **1 repositório por conversa**,
  limite de **5.000 arquivos** e **100 MB**; a funcionalidade de importação
  é disponibilizada no **web app em computador**, não diretamente no
  aplicativo móvel. O uso exige idade mínima de 18 anos, login e
  **Manter atividade** ativado. Contas de trabalho/escola podem exigir
  edição e autorização administrativa elegíveis.

Ajuda oficial:
https://support.google.com/gemini/answer/16176929?hl=pt-419

## Gemini CLI — uso alternativo para automação e edição

Na máquina com Git, Python e Gemini CLI configurados:

```bash
git clone https://github.com/ptamay/mpes-criterios-overall.git
cd mpes-criterios-overall
gemini
```

O Gemini CLI carrega `GEMINI.md` como contexto do projeto; este arquivo
importa `AGENTS.md`. Digite `/memory show` para verificar e
`/memory reload` depois de atualizações nos arquivos.
Antes de qualquer publicação, execute:

```bash
python -m src.pes21_method validate
python -m unittest discover -s tests -v
```

Ajuda oficial Gemini CLI:
https://geminicli.com/docs/cli/gemini-md/

## Controle de qualidade

O repositório fornece **regras e propostas editoriais**, não resultados
automáticos de Sofascore ou do PES. Um assistente não deve alegar ter
consultado as abas interativas do Sofascore ou Opta sem tê-las acessado.
As fichas do repositório têm validade restrita à data do snapshot.
