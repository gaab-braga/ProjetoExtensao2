# RESUMO PARA TRELLO — Projeto Acessibilidade Digital
## Guia da Gerente de Projetos — Todas as tarefas, responsaveis e estrutura final

> **Projeto:** Acessibilidade Digital em Plataformas Educacionais  
> **PO:** Gabriel (gaab-braga) | **Orientador:** Prof. Guilherme Bueno  
> **Equipe:** 6 pessoas (Gabriel + 2 Secretariado + 2 Dados + 1 ADS)  
> **Entregas:** Toda quarta-feira as 20h  
> **Documento de referencia:** BACKLOG_PROJETO.md + GUIA_TAREFAS_EQUIPE.md

---
---

# PARTE 1 — LISTA COMPLETA DE TAREFAS PARA O TRELLO

## Como organizar no Trello

**Listas (colunas) sugeridas:**
```
| Backlog | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 | Em Andamento | Concluido |
```

**Etiquetas de cor por equipe:**
- AZUL = Equipe de Dados (2 pessoas)
- ROXO = Equipe ADS (1 pessoa)
- VERDE = Secretariado (2 pessoas)
- AMARELO = Gabriel (PO)
- VERMELHO = Todos (entrega coletiva)

**Etiquetas de prioridade:**
- MUST HAVE = Obrigatorio para aprovacao
- SHOULD HAVE = Importante mas nao bloqueante
- COULD HAVE = Enriquece se houver tempo

---

## SPRINT 1 — Fundacao (Semana 1)

### CARD 1 — Download e exploracao dos microdados
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Baixar CSV do TIC Educacao 2024 (Modulo Escolas/Gestores) em cetic.br. Abrir em Jupyter Notebook, verificar separador, encoding, nomes das colunas. Enviar ao Gabriel: quantidade de linhas, separador, encoding e se colunas batem com o dicionario.
- **Checklist:**
  - [ ] CSV baixado e salvo em dados/raw/
  - [ ] Jupyter Notebook criado (01_limpeza.ipynb)
  - [ ] Relatorio enviado ao Gabriel (linhas, colunas, encoding)
- **Prazo:** Dia 1-2 da Sprint 1
- **Conexao backlog:** Pre-requisito de TUDO

### CARD 2 — Limpeza e tratamento do CSV
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Tratar valores 97 (Nao sabe) e 98 (Nao respondeu) como NaN. Manter 99 (Nao se aplica) com tratamento caso a caso. Criar colunas derivadas: TEM_ACESSIBILIDADE, EXCLUSAO_ATIVA, EXCLUSAO_PCD. Exportar CSV limpo em dados/processed/.
- **Checklist:**
  - [ ] Valores 97 e 98 convertidos para NaN
  - [ ] Coluna TEM_ACESSIBILIDADE criada (1 se P32_A/B/C/D = 1)
  - [ ] Coluna EXCLUSAO_ATIVA criada (plataforma SIM + acessibilidade NAO)
  - [ ] Coluna EXCLUSAO_PCD criada (PcD + plataforma + sem acessibilidade)
  - [ ] Contagens de verificacao enviadas ao Gabriel
  - [ ] CSV limpo salvo em dados/processed/
- **Prazo:** Dia 2-4 da Sprint 1
- **Conexao backlog:** Secao 1 (Regras de ETL)

### CARD 3 — Fichamento da Lei Brasileira de Inclusao (LBI)
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | MUST HAVE
- **Descricao:** Ler e fichar os Art. 28 (incisos V, XI, XIV), Art. 63 e Art. 67 da Lei 13.146/2015. Para cada artigo: texto original, resumo com proprias palavras, e como usaremos no projeto. Formato: Word ou Google Docs.
- **Checklist:**
  - [ ] Art. 28, V fichado (recursos de TI acessiveis)
  - [ ] Art. 28, XI fichado (formacao de professores)
  - [ ] Art. 28, XIV fichado (oferta de TI assistiva)
  - [ ] Art. 63 fichado (acessibilidade em sites)
  - [ ] Art. 67 fichado (acessibilidade em comunicacoes)
- **Prazo:** Quarta-feira da Semana 1
- **Conexao backlog:** Alimenta TODOS os Epicos

### CARD 4 — Fichamento do Decreto 5.296/2004
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | MUST HAVE
- **Descricao:** Ler e fichar o Art. 47 (acessibilidade em portais e sitios eletronicos). Mesmo formato do fichamento da LBI.
- **Checklist:**
  - [ ] Art. 47 fichado
  - [ ] Documento salvo em docs/fichamento_leis.docx
- **Prazo:** Quarta-feira da Semana 1
- **Conexao backlog:** US-4.1 (Funil de Digitalizacao)

### CARD 5 — Fichamento da Portaria MEC 3.284/2003
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | SHOULD HAVE
- **Descricao:** Pesquisar e fichar os requisitos de acessibilidade para credenciamento de instituicoes de ensino. Mesmo formato.
- **Checklist:**
  - [ ] Portaria localizada e fichada
  - [ ] Documento atualizado em docs/fichamento_leis.docx
- **Prazo:** Quarta-feira da Semana 1
- **Conexao backlog:** Legislacao complementar

### CARD 6 — Fichamento do e-MAG
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | SHOULD HAVE
- **Descricao:** Acessar gov.br/governodigital e ler recomendacoes de acessibilidade. Anotar quais sao aplicaveis a plataformas educacionais (Google Classroom, Moodle, etc.).
- **Checklist:**
  - [ ] e-MAG lido
  - [ ] Recomendacoes aplicaveis listadas
  - [ ] Documento atualizado
- **Prazo:** Quarta-feira da Semana 1
- **Conexao backlog:** Referencia para todos os Epicos

### CARD 7 — Validacao da limpeza (PO)
- **Responsavel:** Gabriel
- **Etiqueta:** AMARELO | MUST HAVE
- **Descricao:** Receber os numeros da equipe de dados (total escolas, escolas com internet, com plataforma, com acessibilidade, exclusao ativa, escolas com PcD, exclusao PcD). Validar se estao coerentes com o esperado. Dar GO para Sprint 2.
- **Checklist:**
  - [ ] Numeros recebidos e conferidos
  - [ ] GO comunicado no grupo
- **Prazo:** Fim da Semana 1
- **Conexao backlog:** Gate de qualidade

---

## SPRINT 2 — Analises Principais (Semana 2)

### CARD 8 — US-1.1: Grafico Plataformas vs. Acessibilidade
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Calcular % ponderado de escolas com plataformas (P42_2_AGREG=1) vs. % com acessibilidade (TEM_ACESSIBILIDADE=1). Gerar grafico de barras comparativo. USAR PESO. Mostrar n bruto.
- **Entrega:** grafico_US1_1.png
- **Notebook:** 02_epico1_ilusao.ipynb
- **Conexao backlog:** US-1.1 — Epico 1

### CARD 9 — US-1.2: KPI Exclusao Ativa (Donut)
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Filtrar escolas com plataformas. Calcular % SEM nenhum recurso assistivo (ponderado). Gerar grafico donut. ESTE E O NUMERO MAIS IMPORTANTE DO PROJETO.
- **Entrega:** grafico_US1_2_KPI.png
- **Notebook:** 02_epico1_ilusao.ipynb
- **Conexao backlog:** US-1.2 — Epico 1

### CARD 10 — US-1.5: Escolas com PcD + Plataforma sem Acessibilidade
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Filtrar escolas com P31=1 (tem PcD) E P42_2_AGREG=1 (usa plataforma). Calcular % sem nenhum recurso assistivo. PERCENTUAL DE MAIOR IMPACTO ACADEMICO. Enviar resultado imediatamente ao Secretariado para confrontar com Art. 28 da LBI.
- **Entrega:** Percentual + print do calculo
- **Notebook:** 02_epico1_ilusao.ipynb
- **Conexao backlog:** US-1.5 — Epico 1

### CARD 11 — US-1.3: Detalhamento por tipo de recurso assistivo
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Descricao:** Calcular taxa de adocao de CADA recurso individualmente (P32_A hardware, P32_B software, P32_C aulas, P32_D materiais) entre escolas com plataformas. Grafico de barras horizontais.
- **Entrega:** grafico_US1_3.png
- **Notebook:** 02_epico1_ilusao.ipynb
- **Conexao backlog:** US-1.3 — Epico 1

### CARD 12 — US-2.1: Acessibilidade por Dependencia Administrativa
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Calcular % com acessibilidade segmentado por COD_DEPENDENCIA (Federal, Estadual, Municipal, Particular). Grafico de barras agrupadas. Ponderado por PESO.
- **Entrega:** grafico_US2_1.png
- **Notebook:** 03_epico2_abismo.ipynb
- **Conexao backlog:** US-2.1 — Epico 2

### CARD 13 — US-2.2: Centro-Oeste vs. Media Nacional
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Calcular % com acessibilidade por COD_REGIAO, com destaque para Centro-Oeste (COD_REGIAO=5). Grafico de barras com linha de referencia na media nacional.
- **Entrega:** grafico_US2_2.png
- **Notebook:** 03_epico2_abismo.ipynb
- **Conexao backlog:** US-2.2 — Epico 2

### CARD 14 — US-2.4: Urbana vs. Rural
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Descricao:** Calcular diferenca percentual de acessibilidade entre COD_ZONA=1 (urbana) e COD_ZONA=2 (rural). Grafico comparativo com 2 barras por recurso.
- **Entrega:** grafico_US2_4.png
- **Notebook:** 03_epico2_abismo.ipynb
- **Conexao backlog:** US-2.4 — Epico 2

### CARD 15 — US-2.7: Funil da Sala de Recursos Multifuncionais
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Descricao:** Funil de 3 estagios: Tem Sala (P24_G=1) -> Tem Internet na sala (P25_G=1) -> Aluno acessa Internet (P26_G=1). Excelente para storytelling visual. Enviar ao Secretariado para vincular com Art. 67 da LBI.
- **Entrega:** grafico_US2_7_funil.png
- **Notebook:** 03_epico2_abismo.ipynb
- **Conexao backlog:** US-2.7 — Epico 2

### CARD 16 — US-4.1: Funil de Digitalizacao Inclusiva (Nacional)
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Funil de 5 estagios: Internet -> +Computador -> +Plataforma -> +Acessibilidade -> +Sala AEE com Internet. MELHOR VISUALIZACAO DO PROJETO. Ponderado por PESO.
- **Entrega:** grafico_US4_1_funil_completo.png
- **Notebook:** 04_epico4_funil.ipynb
- **Conexao backlog:** US-4.1 — Epico 4

### CARD 17 — Tabela "Dado -> Argumento Juridico"
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | MUST HAVE
- **Descricao:** Receber graficos e percentuais da Equipe de Dados. Criar tabela com 3 colunas: Dado estatistico | Argumento juridico | Lei citada. Minimo 6 linhas (uma por analise MUST HAVE).
- **Checklist:**
  - [ ] Receber todos os graficos MUST HAVE
  - [ ] Escrever argumento para US-1.1 (Art. 63 LBI)
  - [ ] Escrever argumento para US-1.2 (Art. 63 LBI)
  - [ ] Escrever argumento para US-1.5 (Art. 28 V e XIV LBI)
  - [ ] Escrever argumento para US-2.1 (Art. 28 LBI)
  - [ ] Escrever argumento para US-2.2 (Art. 28 LBI)
  - [ ] Escrever argumento para US-4.1 (Art. 63 LBI + Decreto 5.296)
- **Prazo:** Uma semana apos receber graficos
- **Conexao backlog:** Epicos 1, 2 e 4

### CARD 18 — Preparar base para modelagem
- **Responsavel:** ADS
- **Etiqueta:** ROXO | SHOULD HAVE
- **Descricao:** Receber DataFrame limpo da Equipe de Dados. Criar variavel Y_SEM_ACESSIBILIDADE (binaria). Selecionar 10 preditores (COD_ZONA, PORTE, COD_DEPENDENCIA, COD_REGIAO, COD_TIPO_CIDADE, NIVEL_ENSINO, P8, P10_AGREG, P59_P73_AGREG, P42_2_AGREG). Fazer one-hot encoding das categoricas. Registrar % de linhas validas.
- **Checklist:**
  - [ ] DataFrame recebido da equipe de dados
  - [ ] Y criado corretamente
  - [ ] Preditores selecionados
  - [ ] One-hot encoding feito
  - [ ] Base exportada sem NaN nos preditores
- **Notebook:** 05_regressao_logistica.ipynb
- **Conexao backlog:** US-3.1 — Epico 3

---

## SPRINT 3 — Modelos e Complementos (Semana 3)

### CARD 19 — US-3.1: Regressao Logistica
- **Responsavel:** ADS
- **Etiqueta:** ROXO | SHOULD HAVE
- **Descricao:** Treinar regressao logistica (sklearn ou statsmodels) com sample_weight=PESO. Split 70/30 estratificado. Gerar: classification_report, AUC-ROC, tabela de Odds Ratio, grafico de importancia das features. Se AUC < 0.55, reportar ao Gabriel (isso tambem e um achado valido).
- **Entrega:** grafico_US3_1_odds_ratio.png + metricas
- **Notebook:** 05_regressao_logistica.ipynb
- **Conexao backlog:** US-3.1 — Epico 3

### CARD 20 — US-3.3: Arvore de Decisao
- **Responsavel:** ADS
- **Etiqueta:** ROXO | COULD HAVE
- **Descricao:** Treinar DecisionTreeClassifier (max_depth=4, min_samples_leaf=30). Visualizar com plot_tree. A arvore mostra uma "receita" visual: ex. "Se municipal + rural + sem internet = 95% sem acessibilidade". Muito poderoso na apresentacao.
- **Entrega:** grafico_US3_3_arvore.png
- **Notebook:** 06_arvore_decisao.ipynb
- **Conexao backlog:** US-3.3 — Epico 3

### CARD 21 — US-3.2: Perfil da Escola Excluida
- **Responsavel:** ADS + Equipe de Dados
- **Etiqueta:** ROXO + AZUL | COULD HAVE
- **Descricao:** Filtrar escolas com EXCLUSAO_ATIVA=1. Comparar perfil (% rural, % municipal, % NE, etc.) com escolas incluidas. Tabela de frequencias — Retrato da exclusao.
- **Entrega:** Tabela comparativa
- **Notebook:** 06_arvore_decisao.ipynb
- **Conexao backlog:** US-3.2 — Epico 3

### CARD 22 — US-4.3: Formacao do Gestor como Fator
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Descricao:** Comparar taxa de acessibilidade entre escolas com gestor com formacao TIC (P59_P73_AGREG=1) vs. sem. Grafico comparativo. Insight para recomendacao de politica publica.
- **Entrega:** grafico_US4_3.png
- **Notebook:** 04_epico4_funil.ipynb
- **Conexao backlog:** US-4.3 — Epico 4

### CARD 23 — US-4.2: Velocidade de Internet e Acessibilidade
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | COULD HAVE
- **Descricao:** Verificar se escolas com maior velocidade (P76) tendem a ter mais recursos assistivos. Barras por faixa de velocidade.
- **Entrega:** grafico_US4_2.png
- **Conexao backlog:** US-4.2 — Epico 4

### CARD 24 — US-1.4: Plataforma especifica vs. Acessibilidade
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | COULD HAVE
- **Descricao:** Cruzar cada plataforma (Teams, Zoom, Classroom, Moodle, Meet, AVAMEC) com % de acessibilidade. Heatmap ou tabela cruzada. Atencao: n amostral por plataforma pode ser pequeno.
- **Entrega:** tabela_US1_4.png
- **Conexao backlog:** US-1.4 — Epico 1

### CARD 25 — US-2.3: Dupla segmentacao Regiao x Dependencia
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | COULD HAVE
- **Descricao:** Tabela pivot 5 regioes x 2 categorias (Publica/Privada). Destaque para Centro-Oeste. Atencao: subgrupos podem ficar pequenos.
- **Entrega:** tabela_US2_3.png
- **Conexao backlog:** US-2.3 — Epico 2

### CARD 26 — US-2.5: Capital vs. Interior
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | COULD HAVE
- **Descricao:** Comparar COD_TIPO_CIDADE=1 (Capital) vs. 2 (Interior) em acessibilidade. Cruzar com dependencia administrativa. Tabela cruzada.
- **Entrega:** tabela_US2_5.png
- **Conexao backlog:** US-2.5 — Epico 2

### CARD 27 — US-2.6: Acessibilidade por Porte
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | COULD HAVE
- **Descricao:** Barras empilhadas com % de acessibilidade por 6 faixas de porte (PORTE).
- **Entrega:** grafico_US2_6.png
- **Conexao backlog:** US-2.6 — Epico 2

### CARD 28 — Redacao parcial (Metodologia + Resultados)
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | MUST HAVE
- **Descricao:** Comecar a redigir o capitulo de Metodologia (Gabriel fornece texto tecnico sobre a base TIC Educacao) e o capitulo de Resultados (cada grafico + interpretacao juridica da Tabela Dado->Lei).
- **Prazo:** Semana 3
- **Conexao backlog:** Sprint 4 (Consolidacao)

---

## SPRINT 4 — Consolidacao e Entrega Final (Semana 4)

### CARD 29 — Dashboard Power BI
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Descricao:** Compilar os graficos principais em um dashboard interativo no Power BI. Incluir: KPI de exclusao, funil de digitalizacao, comparativos por regiao e dependencia. Exportar como powerbi/dashboard.pbix.
- **Checklist:**
  - [ ] KPI central (exclusao ativa %) em destaque
  - [ ] Funil de 5 estagios
  - [ ] Filtros por regiao e dependencia
  - [ ] Todos percentuais ponderados por PESO
- **Conexao backlog:** Todos os Epicos

### CARD 30 — Texto final ABNT + Slides
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | MUST HAVE
- **Descricao:** Finalizar o artigo completo em ABNT: Introducao, Referencial Teorico, Metodologia, Resultados, Conclusao. Montar slides da apresentacao (PowerPoint ou Google Slides). Incluir todos os graficos e a argumentacao juridica.
- **Checklist:**
  - [ ] Introducao escrita
  - [ ] Referencial Teorico (fichamentos integrados)
  - [ ] Metodologia (base + tratamento + limitacoes)
  - [ ] Resultados (graficos + interpretacao juridica)
  - [ ] Conclusao + Recomendacoes
  - [ ] Formatacao ABNT (fonte, margens, citacoes, referencias)
  - [ ] Slides prontos
- **Entrega:** docs/artigo_final.docx + slides
- **Conexao backlog:** Consolidacao final

### CARD 31 — Revisao final e ensaio da apresentacao
- **Responsavel:** TODOS
- **Etiqueta:** VERMELHO | MUST HAVE
- **Descricao:** Revisao coletiva do artigo + slides. Ensaio da apresentacao oral. Verificar se todos os numeros estao corretos e se o storytelling faz sentido.
- **Checklist:**
  - [ ] Revisao cruzada: Dados confere numeros, Secretariado confere texto
  - [ ] Ensaio cronometrado
  - [ ] Versao final commitada no GitHub
- **Conexao backlog:** Entrega final

---

## TAREFAS CONTINUAS (sem sprint fixo)

### CARD 32 — Controle de cronograma semanal
- **Responsavel:** Secretariado
- **Etiqueta:** VERDE | MUST HAVE
- **Descricao:** Manter planilha com status de cada equipe. Enviar print ao Gabriel toda quarta antes das 18h.
- **Frequencia:** Semanal continuo

### CARD 33 — Validacao de resultados intermediarios
- **Responsavel:** Gabriel
- **Etiqueta:** AMARELO | MUST HAVE
- **Descricao:** Receber e validar cada entrega antes de prosseguir. Dar GO/NO-GO para proxima etapa.
- **Frequencia:** A cada entrega de sprint

---
---

# PARTE 2 — ESTRUTURA DO ARQUIVO FINAL (Data Storytelling)

## A Logica da Narrativa

O arquivo final (artigo + apresentacao) precisa contar uma HISTORIA com os dados.
A ordem abaixo segue o raciocinio:

```
CONTEXTO -> PROBLEMA -> METODO -> DESCOBERTAS -> LEIS -> PREVISAO -> CONCLUSAO
   "O que     "Do que     "Como     "O que os     "O que    "E no       "O que
    esta     estamos    fizemos?"   dados        a lei     futuro?"    devemos
  acontecendo?"  falando?"            dizem?"     diz?"                 fazer?"
```

---

## Ordem dos Capitulos com Mapeamento ao Backlog

### CAPITULO 1 — INTRODUCAO (Contextualizacao)
**Pergunta narrativa:** "O Brasil digitalizou suas escolas. Mas digitalizou para todos?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Contexto da digitalizacao acelerada pos-pandemia | Secretariado | Pesquisa bibliografica |
| Apresentacao da pesquisa TIC Educacao 2024 | Gabriel | Cetic.br |
| A pergunta central: plataformas digitais vieram acompanhadas de acessibilidade? | Secretariado | BACKLOG (hipotese geral) |
| Justificativa: Educacao Inclusiva como tema obrigatorio do projeto de extensao | Secretariado | Regulamento da disciplina |

**Impacto narrativo:** O leitor entende POR QUE estamos fazendo essa pesquisa.

---

### CAPITULO 2 — REFERENCIAL TEORICO (Base Legal)
**Pergunta narrativa:** "O que a legislacao brasileira OBRIGA em termos de acessibilidade digital na educacao?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Lei Brasileira de Inclusao (13.146/2015) — Art. 28, 63, 67 | Secretariado | Fichamento (Card 3) |
| Decreto 5.296/2004 — Art. 47 | Secretariado | Fichamento (Card 4) |
| Portaria MEC 3.284/2003 | Secretariado | Fichamento (Card 5) |
| Modelo e-MAG | Secretariado | Fichamento (Card 6) |
| Conceitos: Tecnologia assistiva, Desenho Universal, Inclusao digital | Secretariado | Pesquisa bibliografica |

**Impacto narrativo:** O leitor agora sabe que NAO e opcional — a lei OBRIGA acessibilidade. Isso cria expectativa: "Sera que as escolas estao cumprindo?"

---

### CAPITULO 3 — METODOLOGIA
**Pergunta narrativa:** "Como investigamos essa questao?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Descricao da base TIC Educacao 2024 (Cetic.br, modulo Gestores, amostra nacional) | Gabriel | Documentacao Cetic.br |
| Variaveis utilizadas (tabela com as 4 categorias do inventario) | Gabriel | Backlog Secao 0 |
| Regras de tratamento: 97/98->NaN, 99 contextual, PESO obrigatorio | Equipe de Dados | Backlog Secao 1 |
| Colunas derivadas: TEM_ACESSIBILIDADE, EXCLUSAO_ATIVA, EXCLUSAO_PCD | Equipe de Dados | Backlog Secao 1 |
| Tecnicas: Analise descritiva ponderada + Regressao Logistica + Arvore de Decisao | ADS | Backlog Secao 4 (Epico 3) |
| Limitacoes: Sem dados de percepcao do aluno, sem tipo de deficiencia, sem teste e-MAG | Gabriel | Backlog Secao 6 (Alertas) |

**Impacto narrativo:** Credibilidade. O leitor confia no metodo e sabe dos limites.

---

### CAPITULO 4 — RESULTADOS

Aqui esta o coracao da historia. A ordem dos resultados segue um FUNIL de impacto crescente:

#### 4.1 — O Panorama: "As escolas se digitalizaram" (Setup)
**Pergunta:** As escolas brasileiras usam plataformas digitais? Em que proporcao?

| Grafico/Tabela | User Story | Responsavel | Arquivo |
|---|---|---|---|
| Barras: % com plataformas vs. % com acessibilidade | US-1.1 | Dados | grafico_US1_1.png |

**Transicao narrativa:** "Sim, as escolas digitalizaram. MAS..."

---

#### 4.2 — A Revelacao: "A Ilusao da Digitalizacao" (Ponto de virada)
**Pergunta:** Dentre essas escolas digitalizadas, quantas esqueceram da acessibilidade?

| Grafico/Tabela | User Story | Responsavel | Arquivo |
|---|---|---|---|
| Donut: % SEM acessibilidade entre as que usam plataformas | US-1.2 | Dados | grafico_US1_2_KPI.png |
| Barras horizontais: taxa de cada recurso assistivo | US-1.3 | Dados | grafico_US1_3.png |

**Transicao narrativa:** "E a situacao e ainda mais grave quando olhamos escolas que TEM alunos com deficiencia..."

---

#### 4.3 — O Dado mais Critico: "Exclusao com PcD presente" (Climax)
**Pergunta:** Entre escolas que TEM alunos PcD E usam plataformas, quantas NAO possuem NENHUM recurso?

| Grafico/Tabela | User Story | Responsavel | Arquivo |
|---|---|---|---|
| Percentual-chave (destaque visual no texto e no slide) | US-1.5 | Dados | Numero no texto |

**Confronto legal:** Secretariado vincula com Art. 28, incisos V e XIV da LBI + Portaria MEC 3.284/2003

**Transicao narrativa:** "Esse problema e uniforme pelo Brasil? Ou ha regioes e tipos de escola mais afetados?"

---

#### 4.4 — As Desigualdades: "O Abismo Administrativo e Geografico" (Aprofundamento)
**Pergunta:** Onde a exclusao e pior? Publico vs. privado? Urbano vs. rural? Centro-Oeste vs. pais?

| Grafico/Tabela | User Story | Responsavel | Arquivo |
|---|---|---|---|
| Barras por dependencia (Federal/Estadual/Municipal/Particular) | US-2.1 | Dados | grafico_US2_1.png |
| Barras por regiao com destaque Centro-Oeste | US-2.2 | Dados | grafico_US2_2.png |
| Comparativo Urbana vs. Rural | US-2.4 | Dados | grafico_US2_4.png |
| Tabela dupla segmentacao Regiao x Dependencia | US-2.3 | Dados | tabela_US2_3.png |
| Comparativo Capital vs. Interior | US-2.5 | Dados | tabela_US2_5.png |
| Barras por Porte da escola | US-2.6 | Dados | grafico_US2_6.png |

**Transicao narrativa:** "Mas antes de ter acessibilidade, a escola precisa ter infraestrutura. Quanta infraestrutura existe de fato?"

---

#### 4.5 — A Barreira Previa: "Infraestrutura como Pre-condicao" (Contexto estrutural)
**Pergunta:** Quantas escolas sequer tem Internet + computador + plataforma ANTES de falar em acessibilidade?

| Grafico/Tabela | User Story | Responsavel | Arquivo |
|---|---|---|---|
| Funil de 5 estagios (Internet->PC->Plataforma->Acessibilidade->Sala AEE) | US-4.1 | Dados | grafico_US4_1_funil_completo.png |
| Funil da Sala de Recursos (Tem->Internet->Aluno acessa) | US-2.7 | Dados | grafico_US2_7_funil.png |
| Velocidade de Internet vs. Acessibilidade | US-4.2 | Dados | grafico_US4_2.png |
| Formacao do Gestor vs. Acessibilidade | US-4.3 | Dados | grafico_US4_3.png |

**Confronto legal:** Art. 63 LBI + Decreto 5.296/2004 + Art. 67 LBI

**Transicao narrativa:** "Com tantas variaveis influenciando, e possivel PREVER quais escolas serao excluidas?"

---

#### 4.6 — A Previsao: "Previsibilidade de Exclusao" (Modelagem)
**Pergunta:** Quais caracteristicas preveem a ausencia de acessibilidade? E possivel tracar um perfil?

| Grafico/Tabela | User Story | Responsavel | Arquivo |
|---|---|---|---|
| Tabela de Odds Ratio + Grafico de importancia | US-3.1 | ADS | grafico_US3_1_odds_ratio.png |
| Arvore de Decisao visual (max_depth=4) | US-3.3 | ADS | grafico_US3_3_arvore.png |
| Tabela: Perfil da escola excluida vs. incluida | US-3.2 | ADS + Dados | Tabela no texto |

**Impacto narrativo:** "Se sabemos QUAIS escolas estao em risco, podemos agir ANTES."

---

### CAPITULO 5 — DISCUSSAO
**Pergunta narrativa:** "O que tudo isso significa? O que a lei diz vs. o que os dados mostram?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Tabela Dado->Argumento Juridico (6+ linhas) | Secretariado | Card 17 |
| Confronto sistematico: cada resultado vs. artigo de lei | Secretariado | Fichamentos + graficos |
| Comparacao com estudos anteriores (se houver) | Secretariado | Pesquisa bibliografica |
| Analise critica: correlacao vs. causalidade (Alerta 4 do backlog) | Gabriel | Backlog Secao 6 |

**Impacto narrativo:** Aqui o numero vira ARGUMENTO. O leitor ve que a exclusao nao e acidente — e falha sistemica.

---

### CAPITULO 6 — CONCLUSAO E RECOMENDACOES
**Pergunta narrativa:** "O que devemos fazer a partir desses achados?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Resumo dos principais achados (3-5 pontos) | Secretariado | Resultados |
| Recomendacoes de politica publica: (1) Formacao de gestores em TIC inclusiva, (2) Investimento em infraestrutura basica antes de digitalizar, (3) Auditoria de acessibilidade em plataformas adotadas, (4) Regulamentacao do uso de plataformas educacionais com criterios e-MAG | Secretariado + Gabriel | Resultados + Legislacao |
| Sugestoes para pesquisas futuras (o que esta base NAO responde) | Gabriel | Backlog Secao 6 (Alerta 5) |

**Impacto narrativo:** O leitor sai com acoes concretas. O projeto entrega VALOR.

---

## Resumo Visual da Narrativa (para os slides)

```
SLIDE 1:  "O Brasil digitalizou suas escolas" .............. (Contexto)
SLIDE 2:  "Mas a acessibilidade ficou para tras" .......... (US-1.1)
SLIDE 3:  "X% das escolas com plataforma NAO tem recurso".. (US-1.2 KPI)
SLIDE 4:  "Ate com alunos PcD presentes, Y% sem recurso".. (US-1.5 CLIMAX)
SLIDE 5:  "A escola publica sofre mais" ................... (US-2.1)
SLIDE 6:  "O Centro-Oeste no mapa da exclusao" ............ (US-2.2)
SLIDE 7:  "Rural vs. Urbano: o abismo" .................... (US-2.4)
SLIDE 8:  "O funil que afunila: quem sobrevive?" .......... (US-4.1 FUNIL)
SLIDE 9:  "Sem Internet nao ha plataforma ativa" .......... (US-2.7 + US-4.2)
SLIDE 10: "Gestor capacitado = escola mais acessivel" ..... (US-4.3)
SLIDE 11: "O modelo previu: perfil da escola excluida" .... (US-3.1 + US-3.3)
SLIDE 12: "O que a lei diz vs. o que os dados mostram" .... (Discussao)
SLIDE 13: "Recomendacoes: 4 acoes concretas" .............. (Conclusao)
SLIDE 14: "Obrigado — Perguntas?" ......................... (Encerramento)
```

---

## Mapa Completo: Card Trello -> Capitulo Final -> User Story

| Card Trello | Capitulo | Secao | User Story | Prioridade |
|---|---|---|---|---|
| Card 3-6 | Cap 2 (Referencial) | Legislacao | — | MUST |
| Card 1-2 | Cap 3 (Metodologia) | Base e tratamento | — | MUST |
| Card 8 | Cap 4.1 | Panorama | US-1.1 | MUST |
| Card 9 | Cap 4.2 | Ilusao | US-1.2 | MUST |
| Card 11 | Cap 4.2 | Ilusao | US-1.3 | SHOULD |
| Card 10 | Cap 4.3 | Climax | US-1.5 | MUST |
| Card 12 | Cap 4.4 | Desigualdades | US-2.1 | MUST |
| Card 13 | Cap 4.4 | Desigualdades | US-2.2 | MUST |
| Card 14 | Cap 4.4 | Desigualdades | US-2.4 | SHOULD |
| Card 25 | Cap 4.4 | Desigualdades | US-2.3 | COULD |
| Card 26 | Cap 4.4 | Desigualdades | US-2.5 | COULD |
| Card 27 | Cap 4.4 | Desigualdades | US-2.6 | COULD |
| Card 16 | Cap 4.5 | Infraestrutura | US-4.1 | MUST |
| Card 15 | Cap 4.5 | Infraestrutura | US-2.7 | SHOULD |
| Card 23 | Cap 4.5 | Infraestrutura | US-4.2 | COULD |
| Card 22 | Cap 4.5 | Infraestrutura | US-4.3 | SHOULD |
| Card 19 | Cap 4.6 | Previsao | US-3.1 | SHOULD |
| Card 20 | Cap 4.6 | Previsao | US-3.3 | COULD |
| Card 21 | Cap 4.6 | Previsao | US-3.2 | COULD |
| Card 17 | Cap 5 | Discussao | — | MUST |
| Card 28-30 | Cap 1-6 | Todos | — | MUST |
| Card 29 | Apresentacao | Dashboard | Todos | MUST |

---

## Cronograma Resumido para o Trello

```
SEMANA 1 (Sprint 1)          SEMANA 2 (Sprint 2)
========================      ========================
DADOS: Download + Limpeza     DADOS: Graficos Epico 1+2
  Cards 1, 2                    Cards 8-16
SECRET: Fichamento leis       SECRET: Tabela Dado->Lei
  Cards 3, 4, 5, 6             Card 17
ADS: Aguarda df limpo         ADS: Prepara base modelo
  (sem card ativo)              Card 18
GABRIEL: Valida limpeza       GABRIEL: Valida graficos
  Card 7                        Card 33

SEMANA 3 (Sprint 3)          SEMANA 4 (Sprint 4)
========================      ========================
DADOS: Graficos Epico 4       DADOS: Dashboard Power BI
  Cards 22, 23                  Card 29
SECRET: Redacao parcial       SECRET: Texto ABNT + Slides
  Card 28                       Card 30
ADS: Regressao + Arvore       ADS: Revisao
  Cards 19, 20, 21              Card 31
GABRIEL: Valida modelos       GABRIEL: Revisao final
  Card 33                       Card 31
```

---

## Regras de Movimentacao no Trello

| Situacao | Acao no Trello |
|---|---|
| Tarefa comecou | Mover card para "Em Andamento" |
| Tarefa precisa de input de outra equipe | Adicionar comentario no card: "@equipe preciso de X" |
| Tarefa travada | Adicionar etiqueta VERMELHA "BLOQUEADO" + comentar motivo |
| Tarefa concluida | Mover para "Concluido" + marcar checklist |
| Entrega validada pelo Gabriel | Adicionar etiqueta DOURADA "APROVADO" |
| Quarta-feira semanal | Secretariado atualiza planilha + verifica status de todos os cards |
