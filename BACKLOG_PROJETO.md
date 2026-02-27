# BACKLOG DO PROJETO — Acessibilidade Digital em Plataformas Educacionais
## TIC Educação 2024 · Módulo Escolas/Gestores · Tabelas de Indicadores

> **PO:** Gabriel (gaab-braga) · **Orientador:** Prof. Guilherme Bueno  
> **Equipe:** 4 pessoas — Gabriel (PO) + 2 Dados + 1 ADS  
> **Tema Obrigatório:** Educação Inclusiva  
> **Subtema:** Acessibilidade digital em plataformas educacionais  
> **Base:** Tabelas de Indicadores — TIC Educação 2024 — Cetic.br/CGI.br  
> **Data de criação do backlog:** 26/02/2026  
> **Reformulação v3 (equipe reduzida + foco em perguntas):** atualizado

---

## 0. NATUREZA DOS DADOS DISPONÍVEIS

### ⚠️ LEITURA OBRIGATÓRIA ANTES DE TUDO

**Não temos microdados** (CSV com uma linha por escola). Temos as **Tabelas de Indicadores oficiais** publicadas pelo Cetic.br, que já são resultados **agregados e ponderados** da pesquisa.

### 0.1 Arquivos Disponíveis

| Arquivo | Conteúdo | Uso |
|---|---|---|
| `tic_educacao_2024_escolas_tabela_total_v1.0.xlsx` | 69 abas com **contagens absolutas** (estimativas expandidas) por indicador | Valores absolutos para contexto |
| `tic_educacao_2024_escolas_tabela_proporcao_v1.0.xlsx` | 69 abas com **percentuais ponderados** dos mesmos indicadores | **Base principal das análises** |
| `tic_educacao_2024_gestores_dicionario_de_variaveis_v1.0.xlsx` | Dicionário de variáveis dos microdados (referência conceitual) | Entender o significado de cada indicador |

### 0.2 Estrutura das Tabelas (Padrão em Todas as 69 Abas)

Cada aba contém ~29 linhas com a mesma estrutura de segmentação:

| Segmento | Categorias |
|---|---|
| **TOTAL** | Nacional |
| **REGIÃO** | Norte, Nordeste, Sudeste, Sul, Centro-Oeste |
| **ÁREA** | Urbana, Rural |
| **LOCALIZAÇÃO** | Capital, Interior |
| **DEPENDÊNCIA ADMINISTRATIVA** | Municipal, Estadual, Públicas (agregado), Particular |
| **NÍVEL DE ENSINO** | Até EF-Iniciais, Até EF-Finais, Até EM/Profissional |
| **PORTE** | Até 50, 51-150, 151-300, 301-500, 501-1000, 1000+ |
| **ESCOLA COM INTERNET E COMPUTADOR** | Sim, Não |

### 0.3 O Que Podemos e NÃO Podemos Fazer

| ✅ PODEMOS | ❌ NÃO PODEMOS |
|---|---|
| Comparar indicadores lado a lado (mesmos segmentos) | Cruzar duas variáveis de abas diferentes (ex: "escolas com plataforma E sem acessibilidade") |
| Análise segmentada dentro de cada indicador | Criar novas variáveis derivadas (TEM_ACESSIBILIDADE, EXCLUSAO_ATIVA) |
| Funil de perguntas encadeadas (D3B → D4 → D5) | Machine Learning (regressão, árvore de decisão — precisa de microdados) |
| Comparações geográficas/administrativas riquíssimas | Calcular médias, medianas ou desvios-padrão |
| Montar narrativa com indicadores paralelos | Filtrar subgrupos (ex: "só escolas com PcD que usam plataformas") |

### 0.4 Regra de Ouro deste Backlog

> **NENHUMA User Story solicita cruzamento entre variáveis de abas diferentes.**  
> Toda análise é respondível diretamente com os dados de UMA aba, ou com a comparação lado a lado de abas usando os MESMOS segmentos.  
> Quando comparamos indicadores de abas diferentes, deixamos EXPLÍCITO que é uma **leitura paralela**, não um cruzamento estatístico.

---

## 1. MAPEAMENTO DE ABAS UTILIZÁVEIS

### 1.1 Módulo D — Educação Inclusiva / Tecnologias Assistivas (CORE do projeto)

| Aba | Indicador | Descrição | Dados Nacionais |
|---|---|---|---|
| **D1A** | Escolas com alunos com deficiência | Sim/Não | 81,4% Sim |
| **D2** | Recursos de tecnologia assistiva (4 tipos) | Para cada: Sim/Não/NS/NR/NSA | Hardware 19,6% · Software 15,9% · Aulas 12,0% · Materiais 34,0% |
| **D3A** | Sala de Recursos Multifuncionais (AEE) | Sim/Não | 42,0% Sim |
| **D3B** | Sala de Recursos (apenas escolas com Internet) | Sim/Não/NSA | 43,5% Sim |
| **D4** | Internet na Sala de Recursos | Sim/Não/NSA | 41,2% Sim (do total com Internet) |
| **D5** | Aluno acessa Internet na Sala de Recursos | Sim/Não/NSA | 35,1% Sim (do total com Internet) |

### 1.2 Módulo G — Plataformas Digitais / AVAs

| Aba | Indicador | Descrição | Dados Nacionais |
|---|---|---|---|
| **G4** | Plataformas específicas utilizadas (7 tipos) | Para cada: Sim/Não/NS/NR | Teams 23,7% · Zoom 24,6% · Classroom 30,2% · Moodle 5,6% · Meet 55,7% · Google (total) 59,4% · AVAMEC 22,7% · Outros 16,6% |
| **G4A** | Usou ao menos uma plataforma/AVA | Sim/Não | **73,8% Sim** |

### 1.3 Módulo A — Infraestrutura de Internet

| Aba | Indicador | Dados Nacionais |
|---|---|---|
| **A1** | Escola com acesso à Internet | **95,9% Sim** |
| **A2** | Tipo de conexão principal | Fibra 53,1% · Cabo 22,5% · Satélite 8,8% |
| **A3_1** | Velocidade da Internet (faixas) | Até 10 Mbps 9,9% · 11-50 8,7% · 51-100 13,5% · 101+ 39,4% |
| **A4** | Rede sem fio (Wi-Fi) | 98,9% (das com Internet) |

### 1.4 Módulo B — Dispositivos

| Aba | Indicador | Dados Nacionais |
|---|---|---|
| **B1** | Escola possui computador | **88,7% Sim** |
| **B1A** | Computador em funcionamento | Sim/Não |
| **B1B** | Computador disponível para alunos | Sim/Não |
| **B2** | Tipo de dispositivo (mesa/notebook/tablet) | Por tipo |

### 1.5 Módulo C — Acesso e Uso

| Aba | Indicador | Dados Nacionais |
|---|---|---|
| **C1** | Locais com Internet para alunos | Sala de aula 63,2% · Lab 32,8% · Biblioteca 42,8% |

### 1.6 Módulo K — Perfil da Escola

| Aba | Indicador |
|---|---|
| **K1_1** | Última aquisição de computadores |
| **K3** | Níveis de ensino ofertados |

---

## 2. LISTA MESTRA DE PERGUNTAS DO PROJETO

> **Esta é a seção central do backlog.** Cada pergunta abaixo pode ser respondida com os dados disponíveis. O projeto inteiro gira em torno de responder essas perguntas, gerar os gráficos correspondentes e montar a narrativa final.

### Perguntas MUST HAVE (6 perguntas — obrigatórias)

| # | Pergunta | US | Aba(s) |
|---|---|---|---|
| P1 | Qual o gap entre digitalização (plataformas) e acessibilidade (recursos assistivos) no nível nacional? | US-1.1 | G4A + D2 |
| P2 | Qual a taxa de adoção de CADA recurso assistivo, por TODOS os segmentos? | US-1.2 | D2 |
| P3 | Qual % de escolas atende alunos com deficiência, por segmento? | US-1.3 | D1A |
| P4 | Como cada REGIÃO se posiciona? O Centro-Oeste realmente lidera? | US-2.2 | D2 |
| P5 | Qual a magnitude da desigualdade urbano-rural em acessibilidade? | US-2.3 | D2 |
| P6 | A Sala de Recursos se mantém funcional? O funil D3B→D4→D5 mostra quanta perda? | US-3.1 | D3B, D4, D5 |

### Perguntas SHOULD HAVE (5 perguntas — alto valor)

| # | Pergunta | US | Aba(s) |
|---|---|---|---|
| P7 | Como se compara a acessibilidade entre Municipal, Estadual e Particular? | US-2.1 | D2 |
| P8 | O tamanho da escola importa? Qual o gap por faixa de porte? | US-2.5 | D2 |
| P9 | A infraestrutura (Internet+Computador) é pré-condição para acessibilidade? | US-2.7 | D2 |
| P10 | Qual a "escadaria da exclusão" — todos os indicadores nacionais lado a lado? | US-4.1 | A1, B1, G4A, D1A, D2, D3B |
| P11 | Qual % de escolas nem é perguntada sobre acessibilidade ("Não se aplica")? | US-1.5 | D2 |

### Perguntas COULD HAVE (8 perguntas — enriquecem)

| # | Pergunta | US | Aba(s) |
|---|---|---|---|
| P12 | Quais plataformas são mais usadas? Google domina? | US-1.4 | G4 |
| P13 | Capital vs. Interior: há diferença? | US-2.4 | D2 |
| P14 | Nível de ensino afeta a acessibilidade? | US-2.6 | D2 |
| P15 | O funil da Sala de Recursos varia por segmento? | US-3.2 | D3B, D4, D5 |
| P16 | D3A (total) vs. D3B (com Internet): qual a diferença? | US-3.3 | D3A, D3B |
| P17 | O gap Internet→Acessibilidade varia por zona/região? | US-4.2 | A1, B1, G4A, D2 |
| P18 | A concentração Google varia por segmento? | US-4.3 | G4 |
| P19 | Indicadores de contexto: velocidade, dispositivos, aquisição | US-5.1-5.5 | A1, A3_1, B1, B2, C1, K1_1 |

---

## 3. ÉPICO 1 — RETRATO DA ACESSIBILIDADE DIGITAL NAS ESCOLAS BRASILEIRAS

> **Hipótese:** O investimento em tecnologias assistivas está muito abaixo do nível de digitalização das escolas.

### US-1.1 · Panorama Nacional: Digitalização vs. Acessibilidade (Leitura Paralela)
**Pergunta (P1):** Qual o percentual nacional de escolas que usam ao menos uma plataforma digital? E, separadamente, qual o percentual que possui cada tipo de recurso de tecnologia assistiva?  
**Fonte dos dados:**
- Aba **G4A** (proporção) → linha TOTAL → coluna "Sim" = **73,84%**
- Aba **D2** (proporção) → linha TOTAL → colunas "Sim" de cada recurso:
  - Hardware adaptado = **19,59%**
  - Software assistivo = **15,88%**
  - Aulas de informática assistiva = **12,01%**
  - Materiais digitais acessíveis = **33,99%**

**Como responder:**
1. Extrair G4A linha TOTAL → coluna "Sim"
2. Extrair D2 linha TOTAL → colunas "Sim" dos 4 recursos
3. Gerar gráfico de barras com 5 barras (1 plataformas + 4 recursos)
4. Incluir nota: "Indicadores de abas diferentes — comparação contextual, não cruzamento"

**Entrega:** `graficos/US1_1_panorama.png`  
**Referência legal:** Art. 63 da LBI  
**Viabilidade:** ✅

### US-1.2 · Detalhamento dos 4 Recursos Assistivos por Segmento
**Pergunta (P2):** Qual a taxa de adoção de CADA recurso assistivo, segmentado por todas as dimensões?  
**Fonte:** Aba **D2** (proporção) — coluna "Sim" de cada recurso, todas as 29 linhas

**Como responder:**
1. Extrair TODAS as 29 linhas da aba D2
2. Para cada recurso, pegar a coluna "Sim"
3. Gerar heatmap (Segmento × Recurso) OU 4 gráficos de barras horizontais
4. Destacar: Rural 8,2% hardware vs. Urbano 26% (3,2x); Porte até 50: 2,2% vs 1000+: 53,7% (24x)

**Entrega:** `graficos/US1_2_heatmap_D2.png` + tabela CSV  
**Referência legal:** Art. 28, incisos V e XIV da LBI  
**Viabilidade:** ✅ — **a análise mais rica do projeto**

### US-1.3 · Escolas com Alunos com Deficiência (D1A)
**Pergunta (P3):** Qual o percentual de escolas que atendem alunos com deficiência, por segmento?  
**Fonte:** Aba **D1A** — todas as 29 linhas

**Como responder:**
1. Extrair D1A completo
2. Gerar gráfico de barras por segmento
3. Destacar: Nacional 81,4%; Rural 65% vs. Urbana 90,6%; Porte até 50: 39,6% vs. 1000+: 99%
4. Contextualizar: explica a coluna "Não se aplica" de D2

**Entrega:** `graficos/US1_3_D1A.png`  
**Viabilidade:** ✅

### US-1.4 · Plataformas Específicas por Segmento (G4)
**Pergunta (P12):** Quais plataformas são mais usadas? Google domina?  
**Fonte:** Aba **G4** — colunas "Sim" de cada plataforma

**Como responder:**
1. Extrair colunas de cada plataforma para todos os segmentos
2. Gerar gráfico de barras agrupadas ou heatmap
3. Destacar: Google = 59,4%, Meet = 55,7%, Classroom = 30,2%

**Entrega:** `graficos/US1_4_plataformas.png`  
**Referência legal:** Art. 63 da LBI  
**Viabilidade:** ✅

### US-1.5 · O "Não se Aplica" — Escolas Fora do Radar
**Pergunta (P11):** Qual % de escolas nem é perguntada sobre acessibilidade?  
**Fonte:** Aba **D2** → coluna "Não se aplica"

**Como responder:**
1. Extrair coluna "Não se aplica" da D2, todos os segmentos
2. Gerar gráfico por segmento
3. Destacar: Nacional 12,8%; Rural 35,2%; Porte até 50: 38,2%; Urbana 0,09%
4. Explicar: qualifica toda a análise de D2

**Entrega:** `graficos/US1_5_nsa.png` + parágrafo explicativo  
**Viabilidade:** ✅

---

## 4. ÉPICO 2 — O ABISMO GEOGRÁFICO E ADMINISTRATIVO

> **Hipótese:** Existem desigualdades profundas na oferta de acessibilidade.

### US-2.1 · Acessibilidade por Dependência Administrativa
**Pergunta (P7):** Municipal vs. Estadual vs. Particular?  
**Fonte:** D2, linhas DEPENDÊNCIA

**Como responder:**
1. Extrair linhas Municipal, Estadual, Particular da D2
2. Gerar gráfico de barras agrupadas (3 × 4 recursos)
3. Destacar: Particular tem MENOS hardware (12,6%) que Estadual (26,5%), mas MAIS materiais (43,4%)

**Entrega:** `graficos/US2_1_dependencia.png`  
**Referência legal:** Art. 28, V da LBI  
**Viabilidade:** ✅

### US-2.2 · Acessibilidade por Região — Centro-Oeste em Destaque
**Pergunta (P4):** Como cada região se posiciona?  
**Fonte:** D2, linhas REGIÃO

**Como responder:**
1. Extrair 5 linhas de Região da D2
2. Gerar barras agrupadas (5 regiões × 4 recursos) com linha de média nacional
3. Destacar: Centro-Oeste LIDERA em TODOS: Hardware 31,8%, Materiais 53,5%
4. Norte/Nordeste são os reais excluídos

**Dados:**

| Recurso | Norte | Nordeste | Sudeste | Sul | **Centro-Oeste** | Nacional |
|---|---|---|---|---|---|---|
| Hardware | 13,5% | 11,1% | 29,0% | 25,7% | **31,8%** | 19,6% |
| Software | 11,0% | 8,7% | 25,1% | 18,9% | **23,5%** | 15,9% |
| Aulas | 9,3% | 4,7% | 17,9% | 19,5% | **22,4%** | 12,0% |
| Materiais | 17,7% | 24,2% | 48,8% | 40,0% | **53,5%** | 34,0% |

**Entrega:** `graficos/US2_2_regioes.png`  
**Viabilidade:** ✅

### US-2.3 · O Abismo Urbano-Rural
**Pergunta (P5):** Qual a desigualdade urbano-rural?  
**Fonte:** D2, linhas ÁREA

**Como responder:**
1. Extrair linhas Urbana e Rural
2. Gerar gráfico lado a lado com gap anotado
3. Dados:

| Recurso | Urbana | Rural | Gap |
|---|---|---|---|
| Hardware | 26,0% | 8,2% | **3,2x** |
| Software | 21,5% | 5,9% | **3,6x** |
| Aulas | 16,6% | 4,0% | **4,1x** |
| Materiais | 43,7% | 16,8% | **2,6x** |

**Entrega:** `graficos/US2_3_urbano_rural.png`  
**Referência legal:** Art. 28 LBI + Art. 206 CF  
**Viabilidade:** ✅

### US-2.4 · Capital vs. Interior
**Pergunta (P13):** Há diferença?  
**Fonte:** D2, linhas LOCALIZAÇÃO  
**Dados:** Hardware: Capital 32% vs. Interior 17,6%; Materiais: 48,6% vs. 31,7%  
**Entrega:** `graficos/US2_4_capital_interior.png`  
**Viabilidade:** ✅

### US-2.5 · Acessibilidade por Porte — A Escala Importa
**Pergunta (P8):** O tamanho da escola importa?  
**Fonte:** D2, linhas PORTE

**Como responder:**
1. Extrair 6 faixas de Porte
2. Gerar gráfico de barras agrupadas
3. ACHADO MAIS DRAMÁTICO:

| Porte | Hardware | Software | Aulas | Materiais |
|---|---|---|---|---|
| Até 50 | **2,2%** | **1,5%** | **0,3%** | **6,2%** |
| 51-150 | 6,1% | 2,3% | 5,1% | 23,5% |
| 151-300 | 21,4% | 21,4% | 17,8% | 38,5% |
| 301-500 | 22,3% | 22,9% | 13,9% | 41,7% |
| 501-1000 | 45,1% | 31,7% | 22,3% | 60,4% |
| **1000+** | **53,7%** | **31,6%** | **25,0%** | **64,4%** |

Gap de **83 vezes** em aulas assistivas (0,3% vs. 25%).

**Entrega:** `graficos/US2_5_porte.png`  
**Referência legal:** Art. 28, XIV da LBI  
**Viabilidade:** ✅

### US-2.6 · Acessibilidade por Nível de Ensino
**Pergunta (P14):** Nível de ensino afeta?  
**Fonte:** D2, linhas NÍVEL DE ENSINO  
**Dados:** EF-Iniciais Hardware 13,6% vs. EM/Profissional 25,8%  
**Entrega:** `graficos/US2_6_nivel.png`  
**Viabilidade:** ✅

### US-2.7 · Infraestrutura como Pré-condição
**Pergunta (P9):** Internet+Computador é pré-condição?  
**Fonte:** D2, linhas ESCOLA COM INTERNET E COMPUTADOR

**Dados:**

| Recurso | Com Infra | Sem Infra | Gap |
|---|---|---|---|
| Hardware | **31,7%** | 2,3% | **13,8x** |
| Software | **26,0%** | 1,5% | **17,3x** |
| Aulas | **20,0%** | 0,6% | **33,3x** |
| Materiais | **50,0%** | 11,2% | **4,5x** |

**Entrega:** `graficos/US2_7_infra.png`  
**Referência legal:** Art. 63 LBI + Decreto 5.296, Art. 47  
**Viabilidade:** ✅

---

## 5. ÉPICO 3 — O FUNIL DA SALA DE RECURSOS MULTIFUNCIONAIS

> **Hipótese:** A perda é significativa a cada estágio do funil.

### US-3.1 · O Funil Nacional: Sala → Internet → Acesso
**Pergunta (P6):** Quanta perda há entre ter a Sala e o aluno poder acessar?  
**Fonte:** D3B (43,5%) → D4 (41,2%) → D5 (35,1%) — mesma base amostral

**Como responder:**
1. Extrair linha TOTAL das abas D3B, D4, D5
2. Gerar gráfico de funil com 3 estágios
3. Perda total: 8,4 pp (de 43,5% para 35,1%)
4. Este é o ÚNICO funil legítimo do projeto (mesma base amostral)

**Entrega:** `graficos/US3_1_funil.png`  
**Referência legal:** Art. 67 da LBI  
**Viabilidade:** ✅ — **melhor visualização do projeto**

### US-3.2 · O Funil por Segmento
**Pergunta (P15):** Onde a perda é maior?  
**Fonte:** D3B, D4, D5 — todas as linhas  
**Entrega:** Tabela comparativa + `graficos/US3_2_funil_segmentado.png`  
**Viabilidade:** ✅

### US-3.3 · D3A vs. D3B
**Pergunta (P16):** Diferença entre universo total e escolas com Internet?  
**Fonte:** D3A e D3B  
**Entrega:** Tabela comparativa  
**Viabilidade:** ✅

---

## 6. ÉPICO 4 — PANORAMA PARALELO: INFRAESTRUTURA × DIGITALIZAÇÃO × INCLUSÃO

> **Hipótese:** A inclusão digital é o elo mais fraco da cadeia.

### US-4.1 · Escadaria da Exclusão
**Pergunta (P10):** Todos os indicadores nacionais lado a lado — qual cai mais?  
**Fonte:** A1 (95,9%), B1 (88,7%), G4A (73,8%), D1A (81,4%), D2 Materiais (34%), D2 Hardware (19,6%), D2 Software (15,9%), D2 Aulas (12%), D3B (43,5%)

**Como responder:**
1. Extrair TOTAL de cada aba
2. Gerar gráfico de barras descendente
3. Nota obrigatória: "Cada barra é um indicador independente — NÃO cumulativo"

**Entrega:** `graficos/US4_1_escadaria.png`  
**Viabilidade:** ✅

### US-4.2 · Gap Internet→Acessibilidade por Segmento
**Pergunta (P17):** Urbana 56pp vs. Rural 65pp — onde o gap é maior?  
**Fonte:** A1, B1, G4A, D2 — mesmos segmentos  
**Entrega:** `graficos/US4_2_gap.png`  
**Viabilidade:** ✅

### US-4.3 · Concentração Google por Segmento
**Pergunta (P18):** Google domina em todos os segmentos?  
**Fonte:** G4  
**Entrega:** `graficos/US4_3_google.png`  
**Referência legal:** Art. 63 da LBI  
**Viabilidade:** ✅

---

## 7. ÉPICO 5 — INFRAESTRUTURA DIGITAL COMO CONTEXTO

### US-5.1 · Internet por Segmento (A1)
**Pergunta (P19a):** % com Internet? Norte: 18,6% SEM.  
**Viabilidade:** ✅

### US-5.2 · Velocidade (A3_1)
**Pergunta (P19b):** Distribuição de velocidade por zona/região.  
**Viabilidade:** ✅

### US-5.3 · Computadores (B1, B2)
**Pergunta (P19c):** % com computador e tipos.  
**Viabilidade:** ✅

### US-5.4 · Locais com Internet para Alunos (C1)
**Pergunta (P19d):** Sala de aula 63,2%. Lab 32,8%. Biblioteca 42,8%.  
**Viabilidade:** ✅

### US-5.5 · Obsolescência dos Computadores (K1_1)
**Pergunta (P19e):** 34% adquiriram há menos de 1 ano, 3,6% há mais de 10.  
**Viabilidade:** ✅

---

## 8. REFERÊNCIAS LEGAIS

> O Gabriel (PO) é responsável por citar as leis na narrativa final.

| Análise (US) | Legislação | Artigo-Chave |
|---|---|---|
| US-1.1 (Digitalização vs. Acessibilidade) | Lei Brasileira de Inclusão (13.146/2015) | Art. 63 — Acessibilidade em sítios |
| US-1.2 (Recursos por segmento) | LBI | Art. 28, V e XIV — Oferta de TI acessíveis |
| US-2.3 (Abismo urbano-rural) | LBI + Constituição Federal | Art. 28 LBI + Art. 206 CF |
| US-2.7 (Infra como pré-condição) | Decreto 5.296/2004 | Art. 47 — Acessibilidade digital |
| US-3.1 (Funil Sala de Recursos) | LBI | Art. 67 — Acessibilidade em comunicações |
| US-4.3 (Dominância Google) | LBI | Art. 63 — Plataformas do poder público |
| Todos | e-MAG (Governo Federal) | Recomendações de acessibilidade web |
| Todos | Portaria MEC 3.284/2003 | Requisitos para credenciamento |

---

## 9. ALERTAS E LIMITAÇÕES METODOLÓGICAS

### ⚠️ Alerta 1 — Dados Agregados, NÃO Microdados
- Percentuais já ponderados
- NÃO é possível cruzar variáveis de abas diferentes
- NÃO é possível construir modelos de ML
- Comparações entre abas = **leitura paralela**

### ⚠️ Alerta 2 — "Não se Aplica" na Aba D2
Nacional: ~12,8%. Rural: 35,2%. Influem na interpretação de "Sim" e "Não".

### ⚠️ Alerta 3 — Não Há Cruzamento
Perguntas impossíveis: "Das escolas com plataforma, quantas têm acessibilidade?" (exigiria microdados).

### ⚠️ Alerta 4 — Único Funil Legítimo = Sala de Recursos
D3B → D4 → D5 usam mesma base. Todos os outros são leituras paralelas.

### ⚠️ Alerta 5 — Variáveis Indisponíveis
Percepção de alunos PcD, tipo de deficiência, qualidade de software, teste e-MAG, cruzamento de variáveis, ML.

**→ Declarar no capítulo de Metodologia.**

---

## 10. PRIORIZAÇÃO MoSCoW

### MUST HAVE (6 perguntas = entrega mínima)
- [ ] P1/US-1.1 — Panorama Digitalização vs. Acessibilidade
- [ ] P2/US-1.2 — 4 recursos × todos os segmentos (análise mais rica)
- [ ] P3/US-1.3 — Escolas com alunos PcD (D1A)
- [ ] P4/US-2.2 — Regiões (Centro-Oeste lidera)
- [ ] P5/US-2.3 — Abismo Urbano-Rural
- [ ] P6/US-3.1 — Funil da Sala de Recursos

### SHOULD HAVE (5 perguntas)
- [ ] P7/US-2.1 — Dependência Administrativa
- [ ] P8/US-2.5 — Porte (gap 83x)
- [ ] P9/US-2.7 — Infraestrutura como pré-condição
- [ ] P10/US-4.1 — Escadaria da Exclusão
- [ ] P11/US-1.5 — "Não se aplica"

### COULD HAVE (8 perguntas)
- [ ] P12/US-1.4, P13/US-2.4, P14/US-2.6, P15/US-3.2, P16/US-3.3, P17/US-4.2, P18/US-4.3, P19/US-5.x

### WON'T HAVE
- ✗ Cruzamento entre abas, ML, variáveis derivadas, perfil-tipo, percepção de alunos PcD

---

## 11. DISTRIBUIÇÃO POR SPRINT

### Sprint 1 — Extração e Fundação (Semana 1)

| Quem | O que |
|---|---|
| **Dados** | Script de extração de XLSX → CSVs padronizados → validação com valores de referência |
| **ADS** | Preparar Power BI, estudar importação de CSVs |
| **Gabriel** | Validar extração, iniciar pesquisa bibliográfica (leis) |

### Sprint 2 — Perguntas MUST HAVE (Semana 2)

| Quem | O que |
|---|---|
| **Dados** | Gráficos de P1, P2, P3, P4, P5, P6 |
| **ADS** | Importar CSVs no Power BI, montar página de KPIs |
| **Gabriel** | Validar gráficos, dar GO |

### Sprint 3 — Perguntas SHOULD + COULD (Semana 3)

| Quem | O que |
|---|---|
| **Dados** | Gráficos de P7-P11 + P12-P19 (o que der tempo) |
| **ADS** | Dashboard com heatmap, funil, escadaria |
| **Gabriel** | Validar, iniciar redação (Introdução + Metodologia) |

### Sprint 4 — Consolidação (Semana 4)

| Quem | O que |
|---|---|
| **Dados** | Revisão final de gráficos, suporte ao ADS |
| **ADS** | Dashboard final exportado (.pbix) |
| **Gabriel** | Finalizar artigo (ABNT), montar slides, revisão coletiva |

---

## 12. COMO ORGANIZAR O RESULTADO FINAL

### 12.1 Estrutura do Artigo

```
CONTEXTO → PROBLEMA → MÉTODO → DESCOBERTAS → LEIS → CONCLUSÃO
```

| Capítulo | Conteúdo-chave | Perguntas respondidas |
|---|---|---|
| **1. Introdução** | 73,8% usam plataformas, mas só 12% têm aulas assistivas | P1 (gancho) |
| **2. Referencial Teórico** | LBI Art. 28/63/67, Decreto 5.296, e-MAG | — |
| **3. Metodologia** | TIC Educação 2024, dados agregados, limitações | Seções 0 e 9 |
| **4. Resultados** | 4.1 Retrato (P1, P3, P11), 4.2 Desigualdade (P2, P4, P5, P8), 4.3 Infraestrutura (P9, P10), 4.4 Funil (P6) | Todas |
| **5. Discussão** | Dado vs. Lei, hipótese revisada, transparência | — |
| **6. Conclusão** | 4 recomendações de política pública | — |

### 12.2 Slides (13 slides)

```
1:  "O Brasil digitalizou suas escolas"
2:  "73,8% vs. 12%" (P1)
3:  "81,4% têm alunos PcD" (P3)
4:  "Heatmap D2" (P2)
5:  "Centro-Oeste lidera" (P4)
6:  "Rural vs Urbano: 4,1x" (P5)
7:  "Porte: gap de 83x" (P8)
8:  "Sem infra = zero" (P9)
9:  "Escadaria: 95,9% → 12%" (P10)
10: "Funil: 43,5% → 35,1%" (P6)
11: "Lei vs. dados" (Discussão)
12: "4 Recomendações" (Conclusão)
13: "Obrigado — Perguntas?"
```

### 12.3 Estrutura de Pastas

```
ProjetoExtensao2/
├── dados/
│   ├── raw/              ← XLSX originais (NÃO MEXER)
│   └── processed/        ← CSVs extraídos
├── notebooks/            ← Jupyter (01_extracao, 02_epico1, etc.)
├── graficos/             ← PNGs gerados
├── docs/
│   └── artigo_final.docx
├── powerbi/
│   └── dashboard.pbix
├── BACKLOG_PROJETO.md
├── GUIA_TAREFAS_EQUIPE.md
└── RESUMO_TRELLO.md
```
