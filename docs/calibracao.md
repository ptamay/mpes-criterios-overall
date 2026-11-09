# Lacunas conhecidas e agenda de calibração

## O que já está fixado

- Quatro pesos: 45% técnica, 35% desempenho, 15% competição, 5% histórico.
- Escala de Overall da liga; referência Messi 86, Estêvão 82.
- Período-base 2025/26 no corte 07/11/2026, recuo justificado quando houver amostra pequena.
- Regras qualitativas para liga, histórico, amostras e 25 atributos.
- Duas fichas editoriais coerentes, completas e com fontes/limitações.

## O que AINDA NÃO está validado

1. **Calibração de T/D/C/H:** percentis por posição, conversão de rendimento para 0–100, comparação padronizada de funções. Os subscores dos exemplos foram atribuídos editorialmente.
2. **Distribuição de 60/25/15 dentro de D:** os pesos são uma proposta, mas não implementável com integridade sem métricas confiáveis e baseline posicional.
3. **Competição por oponente:** faltam notas individuais e minutos por confronto; C=84 de Lukaku é aproximação editorial, C=92 de Garnacho usa força média da liga, não média efetiva de rivais.
4. **Overall do PES:** não foi validado que a ficha proposta produz 78/79; nenhuma função do jogo é incorporada aqui.
5. **Atributos físicos de Lukaku:** possível queda após lesão, sem medição objetiva de velocidade/impulsão atual. Os valores permanecem hipóteses.
6. **Inspiração, estilo e habilidades especiais:** precisam ser conferidos no patch e em lances.
7. **Viés posicional e variação de nível:** calibrar em amostra significativa de várias posições, ligas e jogadores, inclusive Messi 86 e Estêvão 82.
8. **Escalas do jogo:** confirmar mínimos e tetos aceitos pelo editor/patch para os 25 atributos.

## Experimento futuro sugerido

Criar conjunto ouro com 10–20 jogadores por função (PTE/PTD, MAT, CA, MC, VOL, ZAG, laterais, goleiros), registrar dados 2025/26, comparar blind reviews, testar concordância entre avaliadores e impacto de alterar cada peso; depois integrar cálculo de OVR do motor verificado no patch, sem contaminar a atribuição técnica. Só declarar versão 'calibrada' quando os testes sustentarem os limites.
