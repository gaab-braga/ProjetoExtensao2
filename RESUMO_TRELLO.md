# RESUMO PARA TRELLO — Projeto Acessibilidade Digital
## Todas as tarefas, responsaveis e estrutura final
### v3 — Equipe de 4 pessoas · Foco nas Perguntas

> **Projeto:** Acessibilidade Digital em Plataformas Educacionais  
> **PO:** Gabriel (gaab-braga) | **Orientador:** Prof. Guilherme Bueno  
> **Equipe:** 4 pessoas (Gabriel PO + 2 Dados + 1 ADS)  
> **Entregas:** Toda quarta-feira as 20h  
> **Documento de referencia:** BACKLOG_PROJETO.md + GUIA_TAREFAS_EQUIPE.md

> ⚠️ **ATENCAO:** Este projeto trabalha com **Tabelas de Indicadores Agregados** do Cetic.br (arquivos XLSX com 69 abas cada), NAO com microdados CSV. Nao existem colunas derivadas, nao existe ML, nao existe cruzamento entre variaveis de abas diferentes.

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
- ROXO = Equipe ADS (1 pessoa — Power BI / Visualizacao)
- AMARELO = Gabriel (PO — redacao, validacao, leis)
- VERMELHO = Todos (entrega coletiva)

**Etiquetas de prioridade:**
- MUST HAVE = Obrigatorio para aprovacao
- SHOULD HAVE = Importante mas nao bloqueante
- COULD HAVE = Enriquece se houver tempo

---

## SPRINT 1 — Extracao e Fundacao (Semana 1)

### CARD 1 — Extracao e exploracao dos XLSX
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta que responde:** Pre-requisito de TODAS as perguntas
- **Descricao:** Abrir os 3 arquivos Excel (tabela_proporcao, tabela_total, dicionario) em Jupyter Notebook usando openpyxl/pandas. Listar todas as 69 abas. Verificar a estrutura padrao: ~29 linhas de segmentos por aba. Enviar ao Gabriel: lista de abas, confirmacao da estrutura, e os valores nacionais das abas-chave (D1A, D2, D3B, D4, D5, G4A, A1, B1).
- **Checklist:**
  - [ ] 3 arquivos XLSX confirmados e acessiveis
  - [ ] Notebook criado (01_extracao.ipynb)
  - [ ] Lista completa de 69 abas documentada
  - [ ] Estrutura padrao confirmada (~29 linhas × segmentos)
  - [ ] Valores nacionais das abas-chave extraidos e enviados ao Gabriel
- **Prazo:** Dia 1-2 da Sprint 1

### CARD 2 — Script de extracao padronizada das abas
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta que responde:** Pre-requisito de TODAS as perguntas
- **Descricao:** Criar funcao `extrair_aba(arquivo, nome_aba)` que leia qualquer aba do XLSX e retorne um DataFrame padronizado com colunas nomeadas (Segmento, Sim, Nao, NS, NR, NSA, N). Extrair todas as abas relevantes (D1A, D2, D3A, D3B, D4, D5, G4, G4A, A1, A3_1, B1, B2, C1, K1_1). Exportar cada uma como CSV em dados/processed/.
- **Checklist:**
  - [ ] Funcao extrair_aba() criada e testada
  - [ ] Abas do modulo D extraidas (D1A, D2, D3A, D3B, D4, D5)
  - [ ] Abas dos modulos G, A, B, C, K extraidas
  - [ ] CSVs salvos em dados/processed/
  - [ ] Validacao: percentuais extraidos conferem com os do XLSX original
  - [ ] README criado em dados/ documentando cada CSV
- **Prazo:** Dia 2-4 da Sprint 1

### CARD 3 — Validacao da extracao (PO)
- **Responsavel:** Gabriel
- **Etiqueta:** AMARELO | MUST HAVE
- **Descricao:** Receber os valores nacionais extraidos pela equipe de dados e conferir com os valores de referencia do backlog:
  - G4A = 73,8% (plataformas)
  - D2 Hardware = 19,6% · Software = 15,9% · Aulas = 12,0% · Materiais = 34,0%
  - D1A = 81,4% (escolas com PcD)
  - D3B = 43,5% · D4 = 41,2% · D5 = 35,1% (funil sala de recursos)
  - A1 = 95,9% (Internet) · B1 = 88,7% (computador)
  Validar se estao coerentes. Dar GO para Sprint 2.
- **Checklist:**
  - [ ] Valores nacionais conferidos
  - [ ] CSVs processados verificados (amostra)
  - [ ] GO comunicado no grupo
- **Prazo:** Fim da Semana 1

### CARD 4 — Pesquisa bibliografica: legislacao (PO)
- **Responsavel:** Gabriel
- **Etiqueta:** AMARELO | MUST HAVE
- **Descricao:** Pesquisar e documentar os artigos de lei que serao citados no artigo final. NAO e fichamento extenso — e coleta direta dos artigos para citacao na redacao. Leis: LBI 13.146/2015 (Art. 28, 63, 67), Decreto 5.296/2004 (Art. 47), Portaria MEC 3.284/2003, Modelo e-MAG.
- **Checklist:**
  - [ ] Art. 28 LBI localizado (incisos V, XI, XIV)
  - [ ] Art. 63 LBI localizado
  - [ ] Art. 67 LBI localizado
  - [ ] Art. 47 Decreto 5.296 localizado
  - [ ] e-MAG consultado
  - [ ] Anotacoes salvas para uso na redacao
- **Prazo:** Semana 1
- **Conexao backlog:** Alimenta a Discussao (Cap. 5) e Referencial Teorico (Cap. 2)

---

## SPRINT 2 — Analises MUST HAVE (Semana 2)

### CARD 5 — P1 (US-1.1): Panorama Nacional — Digitalizacao vs. Acessibilidade
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta:** "Qual o gap entre digitalizacao e acessibilidade no nivel nacional?"
- **Descricao:** Grafico de barras com 5 barras: G4A = 73,8% (plataformas) ao lado de D2 Hardware = 19,6%, Software = 15,9%, Aulas = 12,0%, Materiais = 34,0%. Incluir nota metodologica: "Indicadores de abas diferentes — comparacao contextual, nao cruzamento".
- **Entrega:** graficos/US1_1_panorama.png
- **Notebook:** 02_epico1_retrato.ipynb
- **Resposta esperada:** "73,8% das escolas usam plataformas, mas o recurso assistivo mais presente (materiais) atinge apenas 34%. Aulas assistivas: 12%."

### CARD 6 — P2 (US-1.2): Heatmap Completo D2 — 4 Recursos × Todos os Segmentos
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta:** "Qual a adocao de acessibilidade por segmento? Onde estao os piores gaps?"
- **Descricao:** Extrair TODAS as 29 linhas da aba D2 (proporcao), coluna "Sim" de cada recurso. Gerar heatmap com seaborn: eixo Y = segmentos, eixo X = 4 recursos. ANALISE MAIS RICA DO PROJETO. Destacar: Porte ate 50 = 0,3% aulas (gap 83x vs. 1000+); Rural = 2,6x a 4,1x menor.
- **Entrega:** graficos/US1_2_heatmap_D2.png + tabela CSV
- **Notebook:** 02_epico1_retrato.ipynb
- **Resposta esperada:** "Centro-Oeste lidera tudo. Gaps brutais: Rural 3,2x menos hardware; Porte ate 50 tem 0,3% aulas (83x menos que 1000+)."

### CARD 7 — P3 (US-1.3): Escolas com Alunos PcD — Panorama (D1A)
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta:** "Quantas escolas atendem alunos com deficiencia?"
- **Descricao:** Extrair aba D1A (proporcao), gerar grafico de barras por segmento. Nacional = 81,4%. Destacar: Rural 65% vs Urbana 90,6%; Porte ate 50 = 39,6% vs 1000+ = 99%.
- **Entrega:** graficos/US1_3_D1A_pcd.png
- **Notebook:** 02_epico1_retrato.ipynb
- **Resposta esperada:** "81,4% das escolas tem alunos PcD. Rural: 65%, Porte ate 50: 39,6%. Contextualiza 'Nao se aplica' de D2."

### CARD 8 — P4 (US-2.2): Acessibilidade por Regiao — Centro-Oeste em Destaque
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta:** "Centro-Oeste realmente lidera? Quem sao os excluidos regionais?"
- **Descricao:** Da aba D2 (proporcao), extrair linhas de REGIAO. Barras agrupadas (5 regioes × 4 recursos) com linha de media nacional. Centro-Oeste LIDERA TODOS os recursos. Norte e Nordeste excluidos.
- **Entrega:** graficos/US2_2_regioes.png
- **Notebook:** 03_epico2_abismo.ipynb
- **Resposta esperada:** "Centro-Oeste lidera: Hardware 31,8%, Materiais 53,5%. Nordeste mais excluido (Hardware 11,1%, Aulas 4,7%)."

### CARD 9 — P5 (US-2.3): O Abismo Urbano-Rural
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta:** "Qual a desigualdade entre escolas urbanas e rurais?"
- **Descricao:** Da aba D2, extrair linhas AREA (Urbana/Rural). Grafico comparativo com 2 barras por recurso. Gaps: Hardware 3,2x · Software 3,6x · Aulas 4,1x · Materiais 2,6x.
- **Entrega:** graficos/US2_3_urbano_rural.png
- **Notebook:** 03_epico2_abismo.ipynb
- **Resposta esperada:** "Gaps de 2,6x (materiais) a 4,1x (aulas). Rural: aulas assistivas em apenas 4%."

### CARD 10 — P6 (US-3.1): Funil da Sala de Recursos (D3B → D4 → D5)
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | MUST HAVE
- **Pergunta:** "O funil da Sala de Recursos — quanta perda entre ter a sala e o aluno acessar?"
- **Descricao:** Extrair abas D3B (43,5%), D4 (41,2%), D5 (35,1%) — todas com mesma base amostral (escolas com Internet). Gerar FUNNEL CHART de 3 estagios: Tem Sala → Internet na Sala → Aluno Acessa. UNICO FUNIL LEGITIMO DO PROJETO.
- **Entrega:** graficos/US3_1_funil_sala.png
- **Notebook:** 04_epico3_funil.ipynb
- **Resposta esperada:** "43,5% tem Sala → 41,2% com Internet na Sala → 35,1% onde aluno acessa. Perda de 8,4 pp. ~20% perdem o aluno entre ter e acessar."

### CARD 11 — ADS: Estrutura inicial do Power BI
- **Responsavel:** ADS
- **Etiqueta:** ROXO | SHOULD HAVE
- **Descricao:** Receber os CSVs processados da equipe de dados. Importar no Power BI Desktop. Criar modelo de dados com tabelas separadas por aba. Configurar relacionamentos (coluna "Segmento" como chave). Criar pagina inicial com KPIs nacionais (G4A, D2 × 4 recursos, D1A).
- **Checklist:**
  - [ ] CSVs importados no Power BI
  - [ ] Modelo de dados configurado
  - [ ] Pagina de KPIs nacionais criada
  - [ ] Filtro por segmento funcionando
- **Notebook:** N/A — Power BI Desktop

---

## SPRINT 3 — Analises SHOULD + COULD HAVE (Semana 3)

### CARD 12 — P7 (US-2.1): Acessibilidade por Dependencia Administrativa
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Pergunta:** "Municipal vs. Estadual vs. Particular — quem oferece mais?"
- **Descricao:** Da aba D2, extrair linhas DEPENDENCIA. Barras agrupadas (3 dep. × 4 recursos). Insight: Particulares tem MENOS hardware (12,6%) que estaduais (26,5%), mas MAIS materiais digitais (43,4%).
- **Entrega:** graficos/US2_1_dependencia.png
- **Notebook:** 03_epico2_abismo.ipynb

### CARD 13 — P8 (US-2.5): Acessibilidade por Porte — Gap mais dramatico
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Pergunta:** "O tamanho da escola importa? Qual o gap por porte?"
- **Descricao:** Da aba D2, extrair linhas PORTE (6 faixas). ACHADO MAIS DRAMATICO: Porte ate 50 = 0,3% aulas vs 1000+ = 25% → gap de 83 VEZES. Hardware: 2,2% vs 53,7% → gap de 24x.
- **Entrega:** graficos/US2_5_porte.png
- **Notebook:** 03_epico2_abismo.ipynb

### CARD 14 — P9 (US-2.7): Infraestrutura como Pre-condicao (Internet+PC vs. sem)
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Pergunta:** "Internet+Computador e pre-condicao para acessibilidade?"
- **Descricao:** Da aba D2, extrair linhas ESCOLA COM INTERNET E COMPUTADOR (Sim/Nao). Gaps: Hardware 31,7% vs 2,3% (13,8x) · Aulas 20% vs 0,6% (33,3x).
- **Entrega:** graficos/US2_7_infra_precondicao.png
- **Notebook:** 03_epico2_abismo.ipynb

### CARD 15 — P10 (US-4.1): Escadaria da Exclusao — Indicadores Paralelos
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Pergunta:** "Todos os indicadores lado a lado — onde a 'escada' desce?"
- **Descricao:** Barras descendentes: A1=95,9% → B1=88,7% → G4A=73,8% → D1A=81,4% → D2 Materiais=34% → D2 Hardware=19,6% → D2 Software=15,9% → D2 Aulas=12%. Nota: "Cada barra vem de aba diferente — contexto paralelo, nao cumulativo".
- **Entrega:** graficos/US4_1_escadaria.png
- **Notebook:** 05_epico4_paralelo.ipynb

### CARD 16 — P11 (US-1.5): Analise do "Nao se Aplica" em D2
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | SHOULD HAVE
- **Pergunta:** "Quantas escolas nem sao perguntadas sobre acessibilidade?"
- **Descricao:** D2 coluna "Nao se aplica" por segmento. Nacional = 12,8%. Rural = 35,2%. Porte ate 50 = 38,2%. NOTA METODOLOGICA OBRIGATORIA para o artigo.
- **Entrega:** graficos/US1_5_nsa.png + paragrafo explicativo
- **Notebook:** 02_epico1_retrato.ipynb

### CARD 17 — P12 (US-1.4): Plataformas Especificas por Segmento (G4)
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | COULD HAVE
- **Pergunta:** "Quais plataformas dominam? Google e monopolista?"
- **Descricao:** Da aba G4, uso de cada plataforma por segmento. Google (Classroom+Meet) = 59,4%. Relevante para argumentacao sobre acessibilidade de plataforma dominante.
- **Entrega:** graficos/US1_4_plataformas.png

### CARD 18 — P13-P19: Analises complementares de contexto
- **Responsavel:** Equipe de Dados
- **Etiqueta:** AZUL | COULD HAVE
- **Descricao:** US-2.4 Capital vs Interior, US-2.6 Nivel de Ensino, US-3.2 Funil por Segmento, US-4.2 Gap Internet→Acessibilidade, US-4.3 Google por segmento, US-5.1 a US-5.5 Infraestrutura. Servem para contextualizar os resultados no artigo.
- **Entrega:** CSVs + graficos de suporte

### CARD 19 — ADS: Power BI com Heatmap e Escadaria
- **Responsavel:** ADS
- **Etiqueta:** ROXO | SHOULD HAVE
- **Descricao:** Adicionar ao dashboard: pagina do Heatmap D2, pagina do Funil, pagina da Escadaria. Usar dados dos novos graficos gerados pela equipe de dados.
- **Checklist:**
  - [ ] Pagina Heatmap D2 adicionada
  - [ ] Pagina Funil adicionada
  - [ ] Pagina Escadaria adicionada
  - [ ] Filtros globais testados

---

## SPRINT 4 — Consolidacao e Entrega Final (Semana 4)

### CARD 20 — Dashboard Power BI (Final)
- **Responsavel:** ADS
- **Etiqueta:** ROXO | MUST HAVE
- **Descricao:** Finalizar o dashboard interativo no Power BI com todas as analises:
  - Pagina 1: KPIs nacionais (G4A 73,8%, D2 × 4 recursos, D1A 81,4%)
  - Pagina 2: Heatmap D2 (segmentos × recursos)
  - Pagina 3: Funil da Sala de Recursos (D3B→D4→D5)
  - Pagina 4: Escadaria da Exclusao
  - Filtros globais: Regiao, Area, Dependencia, Porte
- **Checklist:**
  - [ ] Pagina 1 — KPIs nacionais
  - [ ] Pagina 2 — Heatmap desigualdades
  - [ ] Pagina 3 — Funil Sala de Recursos
  - [ ] Pagina 4 — Escadaria paralela
  - [ ] Filtros interativos funcionando
  - [ ] Exportado como powerbi/dashboard_acessibilidade.pbix

### CARD 21 — Artigo final ABNT (PO)
- **Responsavel:** Gabriel
- **Etiqueta:** AMARELO | MUST HAVE
- **Descricao:** Redigir o artigo completo em ABNT usando os graficos e respostas das perguntas:
  - Introducao (contexto + dado-gancho)
  - Referencial Teorico (leis pesquisadas no Card 4)
  - Metodologia (tabelas de indicadores + limitacoes)
  - Resultados (graficos + resposta de cada pergunta)
  - Discussao (dados vs. leis — tabela Dado→Lei)
  - Conclusao + Recomendacoes de politica publica
  Declarar explicitamente na Metodologia que sao tabelas de indicadores (nao microdados) e listar limitacoes.
- **Checklist:**
  - [ ] Introducao escrita
  - [ ] Referencial Teorico (legislacao integrada)
  - [ ] Metodologia (tabelas de indicadores + limitacoes + sem ML + sem cruzamento)
  - [ ] Resultados (graficos + interpretacao)
  - [ ] Discussao (dados vs. leis com numeros reais)
  - [ ] Conclusao + 4 Recomendacoes de politica publica
  - [ ] Formatacao ABNT (fonte, margens, citacoes, referencias)
- **Entrega:** docs/artigo_final.docx
- **Prazo:** Semana 4

### CARD 22 — Slides da apresentacao (PO)
- **Responsavel:** Gabriel
- **Etiqueta:** AMARELO | MUST HAVE
- **Descricao:** Montar slides seguindo a narrativa do projeto (ver roteiro na Parte 2). Incluir TODOS os graficos MUST HAVE + Escadaria + Funil. Ultimo slide com as 4 recomendacoes.
- **Entrega:** docs/slides_apresentacao.pptx
- **Prazo:** Semana 4

### CARD 23 — Revisao final e ensaio
- **Responsavel:** TODOS
- **Etiqueta:** VERMELHO | MUST HAVE
- **Descricao:** Revisao coletiva do artigo + slides + dashboard. Ensaio da apresentacao oral. Verificar numeros, notas metodologicas, storytelling.
- **Checklist:**
  - [ ] Dados confere numeros nos graficos
  - [ ] Gabriel confere texto e argumentacao
  - [ ] ADS confere dashboard e filtros
  - [ ] Ensaio cronometrado
  - [ ] Todas as notas metodologicas presentes
  - [ ] Versao final commitada no GitHub

---

## TAREFAS CONTINUAS (sem sprint fixo)

### CARD 24 — Validacao de resultados intermediarios
- **Responsavel:** Gabriel
- **Etiqueta:** AMARELO | MUST HAVE
- **Descricao:** Receber e validar cada entrega antes de prosseguir. Conferir valores com os numeros de referencia do Backlog. Dar GO/NO-GO para proxima etapa.
- **Frequencia:** A cada entrega de sprint

---
---

# PARTE 2 — ESTRUTURA DO ARQUIVO FINAL (Data Storytelling)

## A Logica da Narrativa

O arquivo final (artigo + apresentacao) precisa contar uma HISTORIA com os dados.
A ordem segue o raciocinio:

```
CONTEXTO → PROBLEMA → METODO → DESCOBERTAS → LEIS → CONCLUSAO
  "O que      "Do que     "Como     "O que os     "O que     "O que
   esta      estamos    fizemos?"   dados        a lei      devemos
 acontecendo?" falando?"             dizem?"     diz?"      fazer?"
```

> ⚠️ **NAO existe "Previsao/Modelagem"** nesta narrativa — sem microdados, nao ha ML.

---

## Ordem dos Capitulos com Mapeamento ao Backlog

### CAPITULO 1 — INTRODUCAO (Contextualizacao)
**Pergunta narrativa:** "O Brasil digitalizou suas escolas. Mas digitalizou para todos?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Contexto da digitalizacao acelerada pos-pandemia | Gabriel | Pesquisa bibliografica |
| Apresentacao da pesquisa TIC Educacao 2024 | Gabriel | Cetic.br |
| Dado-gancho: 73,8% das escolas usam plataformas digitais — mas apenas 12% possuem aulas de informatica assistiva | Gabriel | G4A + D2 |
| A pergunta central: a inclusao digital acompanhou a digitalizacao? | Gabriel | BACKLOG (hipotese geral) |
| Justificativa: Educacao Inclusiva como tema do projeto de extensao | Gabriel | Regulamento da disciplina |

**Impacto narrativo:** O leitor entende POR QUE estamos fazendo essa pesquisa.

---

### CAPITULO 2 — REFERENCIAL TEORICO (Base Legal)
**Pergunta narrativa:** "O que a legislacao brasileira OBRIGA em termos de acessibilidade digital na educacao?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Lei Brasileira de Inclusao (13.146/2015) — Art. 28, 63, 67 | Gabriel | Card 4 |
| Decreto 5.296/2004 — Art. 47 | Gabriel | Card 4 |
| Portaria MEC 3.284/2003 | Gabriel | Card 4 |
| Modelo e-MAG | Gabriel | Card 4 |
| Conceitos: Tecnologia assistiva, Desenho Universal, Inclusao digital | Gabriel | Pesquisa bibliografica |

**Impacto narrativo:** O leitor agora sabe que NAO e opcional — a lei OBRIGA acessibilidade.

---

### CAPITULO 3 — METODOLOGIA
**Pergunta narrativa:** "Como investigamos essa questao?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Descricao da base TIC Educacao 2024 (Cetic.br, modulo Gestores, amostra nacional) | Gabriel | Documentacao Cetic.br |
| ⚠️ Natureza dos dados: TABELAS DE INDICADORES AGREGADOS (nao microdados) | Gabriel | Backlog Secao 0 |
| Estrutura: 69 abas, ~29 segmentos por aba, percentuais ja ponderados | Equipe de Dados | Backlog Secao 0.2 |
| Tecnicas: Analise descritiva comparativa + leitura paralela de indicadores | Gabriel | Backlog Secao 0.3 |
| O que NAO podemos fazer: cruzamento entre abas, ML, variaveis derivadas | Gabriel | Backlog Secao 7 |
| Limitacoes: Sem percepcao do aluno, sem tipo de deficiencia, sem teste e-MAG | Gabriel | Backlog Secao 7 |

**Impacto narrativo:** Credibilidade. O leitor confia no metodo e entende seus limites.

---

### CAPITULO 4 — RESULTADOS

Aqui esta o coracao da historia. A ordem segue impacto crescente:

#### 4.1 — O Retrato Nacional: "O Brasil digitalizou, mas nao incluiu" (Setup)
**Pergunta:** Qual o nivel de digitalizacao vs. acessibilidade nas escolas brasileiras?

| Grafico/Tabela | Pergunta | Card | Arquivo |
|---|---|---|---|
| Barras: G4A 73,8% vs D2 (4 recursos: 19,6% a 34%) | P1 | Card 5 | graficos/US1_1_panorama.png |
| D1A: 81,4% das escolas tem alunos PcD | P3 | Card 7 | graficos/US1_3_D1A_pcd.png |
| Nota sobre "Nao se aplica" (12,8% nacional, 35,2% rural) | P11 | Card 16 | graficos/US1_5_nsa.png |

**Transicao narrativa:** "73,8% digitalizaram, mas o recurso assistivo mais comum (materiais) atinge apenas 34%. E 81% das escolas TEM alunos com deficiencia. Onde estao as maiores desigualdades?"

---

#### 4.2 — O Heatmap da Desigualdade: "Quem tem e quem nao tem" (Revelacao)
**Pergunta:** A oferta de acessibilidade e uniforme pelo pais? Ou ha abismos?

| Grafico/Tabela | Pergunta | Card | Arquivo |
|---|---|---|---|
| **Heatmap D2 completo** (29 segmentos × 4 recursos) | P2 | Card 6 | graficos/US1_2_heatmap_D2.png |
| Barras por REGIAO (5 regioes × 4 recursos) | P4 | Card 8 | graficos/US2_2_regioes.png |
| Barras Urbana vs Rural (gaps de 2,6x a 4,1x) | P5 | Card 9 | graficos/US2_3_urbano_rural.png |
| Barras por PORTE (gap de 83x em aulas assistivas) | P8 | Card 13 | graficos/US2_5_porte.png |

**Transicao narrativa:** "Centro-Oeste lidera TODOS os recursos. Norte/Nordeste sao os excluidos. Escolas rurais tem 4x menos. Escolas pequenas tem 83x menos. Mas existe uma barreira AINDA mais basica..."

---

#### 4.3 — A Barreira Previa: "Sem infraestrutura, sem inclusao" (Contexto estrutural)
**Pergunta:** A infraestrutura basica (Internet+Computador) e pre-condicao para acessibilidade?

| Grafico/Tabela | Pergunta | Card | Arquivo |
|---|---|---|---|
| Barras: Com infra vs Sem infra (gap de 33x em aulas) | P9 | Card 14 | graficos/US2_7_infra_precondicao.png |
| Escadaria: A1→B1→G4A→D2 (indicadores paralelos) | P10 | Card 15 | graficos/US4_1_escadaria.png |

**Confronto legal:** Art. 63 LBI + Decreto 5.296/2004

**Transicao narrativa:** "E quando a escola TEM infraestrutura e TEM Sala de Recursos, os alunos realmente acessam?"

---

#### 4.4 — O Funil: "A Sala de Recursos que evapora" (Climax)
**Pergunta:** Do total de escolas com Internet, quantas tem Sala de Recursos? Quantas com Internet na sala? Quantas onde o aluno realmente acessa?

| Grafico/Tabela | Pergunta | Card | Arquivo |
|---|---|---|---|
| **Funnel chart: D3B 43,5% → D4 41,2% → D5 35,1%** | P6 | Card 10 | graficos/US3_1_funil_sala.png |

**Confronto legal:** Art. 67 LBI — acessibilidade em comunicacoes

**Impacto narrativo:** "Quase 20% das escolas que TEM Sala de Recursos 'perdem' o aluno entre ter a sala e o aluno acessar a Internet nela."

---

### CAPITULO 5 — DISCUSSAO
**Pergunta narrativa:** "O que tudo isso significa? O que a lei diz vs. o que os dados mostram?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Tabela Dado→Argumento Juridico (6+ linhas com numeros reais) | Gabriel | Card 4 + Graficos |
| Confronto sistematico: cada resultado vs. artigo de lei | Gabriel | Legislacao + graficos |
| Hipotese REVISTA: Centro-Oeste lidera (contra expectativa) | Gabriel | P4 (US-2.2) |
| Nota de transparencia: dados agregados, sem cruzamento, sem causalidade | Gabriel | Backlog Secao 7 |

**Impacto narrativo:** Aqui o numero vira ARGUMENTO.

---

### CAPITULO 6 — CONCLUSAO E RECOMENDACOES
**Pergunta narrativa:** "O que devemos fazer a partir desses achados?"

| Conteudo | Responsavel | Fonte |
|---|---|---|
| Resumo dos 5 principais achados | Gabriel | Resultados |
| Recomendacao 1: Investimento em infraestrutura ANTES de digitalizar | Gabriel | P9 + P10 |
| Recomendacao 2: Politicas focalizadas em escolas rurais e de pequeno porte | Gabriel | P5 + P8 |
| Recomendacao 3: Auditoria de acessibilidade na plataforma Google (59,4%) | Gabriel | P12 |
| Recomendacao 4: Internet real na Sala de Recursos (funil D3B→D5) | Gabriel | P6 |
| Sugestoes para pesquisas futuras (o que ESTES dados NAO respondem) | Gabriel | Backlog Secao 7 |

**Impacto narrativo:** O leitor sai com acoes concretas.

---

## Resumo Visual da Narrativa (para os slides)

```
SLIDE 1:  "O Brasil digitalizou suas escolas" .................. (Contexto)
SLIDE 2:  "73,8% usam plataformas — mas so 12% tem aulas
           de informatica assistiva" ........................... (P1 — Panorama)
SLIDE 3:  "81,4% das escolas tem alunos com deficiencia" ....... (P3 — D1A)
SLIDE 4:  "O Mapa da Desigualdade" (heatmap D2 completo) ...... (P2 — Revelacao)
SLIDE 5:  "Centro-Oeste lidera TUDO. Norte/Nordeste excluidos". (P4 — Regioes)
SLIDE 6:  "Rural vs Urbano: gap de ate 4,1x" .................. (P5 — Abismo)
SLIDE 7:  "Porte ate 50 alunos: 0,3% tem aulas assistivas
           vs 25% nas escolas 1000+" ........................... (P8 — Gap 83x)
SLIDE 8:  "Sem Internet+Computador = zero acessibilidade" ..... (P9 — Pre-condicao)
SLIDE 9:  "A Escadaria da Exclusao: de 95,9% a 12%" .......... (P10 — Paralelo)
SLIDE 10: "O Funil: 43,5% → 41,2% → 35,1%" .................. (P6 — Sala Recursos)
SLIDE 11: "O que a lei diz vs o que os dados mostram" ......... (Discussao)
SLIDE 12: "4 Recomendacoes de Politica Publica" ............... (Conclusao)
SLIDE 13: "Obrigado — Perguntas?" ............................. (Encerramento)
```

---

## Mapa Completo: Card Trello → Capitulo Final → Pergunta

| Card Trello | Capitulo | Secao | Pergunta | Prioridade |
|---|---|---|---|---|
| Card 4 | Cap 2 (Referencial) | Legislacao | — | MUST |
| Card 1-2 | Cap 3 (Metodologia) | Base e extracao | — | MUST |
| Card 5 | Cap 4.1 | Retrato Nacional | P1 | MUST |
| Card 7 | Cap 4.1 | Retrato Nacional | P3 | MUST |
| Card 16 | Cap 4.1 | Retrato Nacional | P11 | SHOULD |
| Card 6 | Cap 4.2 | Heatmap Desigualdade | P2 | MUST |
| Card 8 | Cap 4.2 | Regioes | P4 | MUST |
| Card 9 | Cap 4.2 | Urbano-Rural | P5 | MUST |
| Card 13 | Cap 4.2 | Porte | P8 | SHOULD |
| Card 12 | Cap 4.2 | Dependencia | P7 | SHOULD |
| Card 14 | Cap 4.3 | Pre-condicao | P9 | SHOULD |
| Card 15 | Cap 4.3 | Escadaria | P10 | SHOULD |
| Card 10 | Cap 4.4 | Funil Nacional | P6 | MUST |
| Card 17 | Cap 4.2 | Plataformas | P12 | COULD |
| Card 18 | Cap 4.2/4.3 | Contexto | P13-P19 | COULD |
| Card 21 | Cap 1-6 | Artigo completo | — | MUST |
| Card 20 | Apresentacao | Dashboard | Todos | MUST |

---

## Cronograma Resumido para o Trello

```
SEMANA 1 (Sprint 1)              SEMANA 2 (Sprint 2)
============================      ============================
DADOS: Extracao XLSX + CSVs       DADOS: Graficos MUST HAVE
  Cards 1, 2                        Cards 5, 6, 7, 8, 9, 10
ADS: Aguarda CSVs / Estuda BI    ADS: Estrutura Power BI
  (sem card ativo)                  Card 11
GABRIEL: Valida extracao          GABRIEL: Valida graficos
  + Pesquisa leis                   Card 24 (GO para sprint 3)
  Cards 3, 4

SEMANA 3 (Sprint 3)              SEMANA 4 (Sprint 4)
============================      ============================
DADOS: Graficos SHOULD+COULD     DADOS: Suporte ao ADS
  Cards 12-18                       (graficos finais)
ADS: Power BI avancado            ADS: Dashboard final
  Card 19                           Card 20
GABRIEL: Valida analises          GABRIEL: Artigo + Slides
  + Inicia redacao                  Cards 21, 22
  Card 24                           Card 23 (revisao com todos)
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
| Quarta-feira semanal | Gabriel confere status de todos os cards |

---

## ⚠️ LEMBRETES IMPORTANTES PARA O TRELLO

1. **NAO EXISTEM CARDS DE ML/REGRESSAO/ARVORE** — sem microdados, nao e possivel
2. **NAO EXISTEM CARDS DE LIMPEZA DE CSV** — os dados ja vem prontos nas tabelas de indicadores
3. **NAO EXISTEM variaveis derivadas** — impossivel com dados agregados
4. **O ADS neste projeto faz POWER BI**, nao modelagem estatistica
5. **Todo grafico que compara indicadores de abas diferentes DEVE ter nota metodologica** dizendo que e "leitura paralela, nao cruzamento estatistico"
6. **O UNICO funil legitimo e o da Sala de Recursos** (D3B→D4→D5)
7. **Gabriel absorveu a escrita do artigo, legislacao e slides** — nao ha equipe de Secretariado
