# BACKLOG DO PROJETO — Acessibilidade Digital em Plataformas Educacionais
## TIC Educação 2024 · Módulo Escolas/Gestores · Dicionário v1.0

> **PO:** Gabriel (gaab-braga) · **Orientador:** Prof. Guilherme Bueno  
> **Tema Obrigatório:** Educação Inclusiva  
> **Subtema:** Acessibilidade digital em plataformas educacionais  
> **Base:** Microdados TIC Educação 2024 — Cetic.br/CGI.br  
> **Data de criação do backlog:** 26/02/2026

---

## 0. INVENTÁRIO DE VARIÁVEIS UTILIZÁVEIS (Mapeamento do Dicionário)

### 0.1 Variáveis de Filtro / Segmentação (Demografia da Escola)

| ID Variável | Descrição | Códigos-chave |
|---|---|---|
| `COD_REGIAO` | Região geográfica | 1=Norte, 2=Nordeste, 3=Sudeste, 4=Sul, **5=Centro-Oeste** |
| `COD_DEPENDENCIA` | Dependência administrativa | 1=Federal, 2=Estadual, 3=Municipal, **4=Particular** |
| `COD_DEPENDENCIA_2_2_1` | Dependência (agregado) | **3=Públicas (Mun+Est+Fed)** |
| `COD_ZONA` | Zona | **1=Urbana, 2=Rural** |
| `COD_TIPO_CIDADE` | Tipo de cidade | **1=Capital, 2=Interior** |
| `PORTE` | Porte (por matrículas) | 1=Até 50, 2=51-150, 3=151-300, 4=301-500, 5=501-1000, 6=1000+ |
| `NIVEL_ENSINO` | Nível mais elevado ofertado | 1=Até EF-Iniciais, 2=Até EF-Finais, 3=Até EM/Profissional |
| `PESO` | **Peso amostral (OBRIGATÓRIO em toda análise)** | Numérico contínuo |

### 0.2 Módulo D — Educação Inclusiva / Tecnologias Assistivas (CORE)

| ID Variável | Descrição | Tipo |
|---|---|---|
| `P31` | Há alunos com deficiência matriculados nesta escola? | 0/1 |
| `P32_A` | Acessórios de computador adaptados (teclados, mouses, microfones, alto-falantes) | 0/1 |
| `P32_B` | Programas/software assistivos (leitura de tela, transcrição, comando de voz) | 0/1 |
| `P32_C` | Aulas de informática assistiva | 0/1 |
| `P32_D` | Materiais educacionais digitais acessíveis (audiolivros, jogos) | 0/1 |
| `P24_G` | Sala de Recursos Multifuncionais para AEE | 0/1 |
| `P24_G_REC` | Indicador D3B — Sala de Recursos Multifuncionais (recodificado) | 0/1 |
| `P25_G` | Internet na Sala de Recursos Multifuncionais/AEE | 0/1 |
| `P26_G` | Alunos têm acesso à Internet na Sala de Recursos Multifuncionais/AEE | 0/1 |

### 0.3 Módulo G — Plataformas Digitais / AVAs

| ID Variável | Descrição | Tipo |
|---|---|---|
| `P42_2_A` | Usou Microsoft Teams (últimos 12 meses) | 0/1 |
| `P42_2_B` | Usou Zoom | 0/1 |
| `P42_2_C1` | Usou Google Sala de Aula / Classroom / Google For Education | 0/1 |
| `P42_2_D` | Usou Moodle | 0/1 |
| `P42_2_F` | Usou Google Meet | 0/1 |
| `P42_2_G` | Usou AVAMEC | 0/1 |
| `P42_2_OUTRO` | Usou outra plataforma educacional | 0/1 |
| **`P42_2_AGREG`** | **Indicador G4A — Usou ALGUMA plataforma (agregado)** | **0/1** |
| `P42_2_C1_F` | Indicador G4 — Google Classroom ou Meet | 0/1 |

### 0.4 Infraestrutura Tecnológica (Variáveis de Suporte)

| ID Variável | Descrição | Tipo |
|---|---|---|
| `P8` | Escola possui Internet | 0/1 |
| `P10_A` / `P10_B` / `P10_C` | Computador de mesa / Notebook / Tablet | 0/1 |
| `P10_AGREG` | Indicador B1 — Possui algum dispositivo | 0/1 |
| `P22` | Wi-Fi | 0/1 |
| `P76` | Velocidade da Internet (faixas) | Ordinal |
| `P20_2` | Tipo de conexão principal | Categórico |
| `P24_E` | Lab de Informática | 0/1 |
| `P24_H` | Sala/Lab Multimídia | 0/1 |
| `P25_C` | Internet na sala de aula | 0/1 |
| `P14A` | Última aquisição de computadores | Ordinal |

### 0.5 Formação de Gestores em Tecnologia

| ID Variável | Descrição | Tipo |
|---|---|---|
| `P59` | Participou de formação sobre TIC em práticas de ensino | 0/1 |
| `P73` | Participou de formação sobre TIC na gestão escolar | 0/1 |
| `P59_P73_AGREG` | Participação em formação (agregado) | 0/1 |

---

## 1. REGRAS DE NEGÓCIO PARA ETL

### 1.1 Tratamento de valores especiais (OBRIGATÓRIO antes de qualquer análise)
```
MISSING_CODES = {97: "Não sabe", 98: "Não respondeu", 99: "Não se aplica"}
# 97 e 98 → NaN (excluir das análises descritivas)
# 99 → Tratamento contextual:
#   - P32_A a P32_D com 99: PROVAVELMENTE escola sem alunos com deficiência (P31=0)
#   - Filtrar OU tratar como categoria separada, conforme a pergunta
```

### 1.2 PESO Amostral
> **⚠️ REGRA INEGOCIÁVEL:** Toda estimativa percentual DEVE usar a variável `PESO`.  
> Pandas: `np.average(coluna, weights=df['PESO'])` ou usar `df.groupby().apply(weighted_mean)`.  
> Power BI: `SUMX(tabela, tabela[VARIAVEL] * tabela[PESO]) / SUM(tabela[PESO])`.

### 1.3 Condição do P32 (Tecnologias Assistivas)
> As variáveis `P32_A`, `P32_B`, `P32_C`, `P32_D` possuem `99 = Não se aplica`.  
> **Hipótese:** O valor 99 foi atribuído a escolas onde `P31 = 0` (sem alunos com deficiência).  
> **Decisão de análise:**  
> - Para responder "A escola TEM tecnologia assistiva?", considerar **TODAS** as escolas (99 conta como "Não").  
> - Para responder "Entre as escolas COM alunos PcD, quantas têm?", filtrar `P31 = 1` primeiro.  
> Ambas as perspectivas são válidas e geram análises complementares.

---

## 2. ÉPICO 1 — O EFEITO "ILUSÃO DA DIGITALIZAÇÃO"

> **Hipótese:** A adoção de plataformas digitais NÃO foi acompanhada pela implementação proporcional de tecnologias assistivas.

### US-1.1 · Taxa de Adoção de Plataformas vs. Taxa de Acessibilidade (Nacional)
**Pergunta:** Qual o percentual ponderado de escolas que utilizam ao menos uma plataforma digital (`P42_2_AGREG = 1`) E qual o percentual que possui ao menos um recurso de acessibilidade digital (`P32_A=1 OR P32_B=1 OR P32_C=1 OR P32_D=1`)?  
**Variáveis:** `P42_2_AGREG`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Dois percentuais nacionais lado a lado (gráfico de barras comparativo)  
**Equipe:** Dados (ETL + gráfico) → Secretariado (argumento jurídico: Art. 63 da LBI)  
**Viabilidade:** ✅ Diretamente respondível

### US-1.2 · Cruzamento: Plataforma SIM × Acessibilidade NÃO ("Exclusão Digital Ativa")
**Pergunta:** Do universo de escolas que usam plataformas (`P42_2_AGREG = 1`), qual percentual NÃO possui NENHUM dos 4 recursos assistivos (`P32_A=0 AND P32_B=0 AND P32_C=0 AND P32_D=0`)?  
**Variáveis:** `P42_2_AGREG`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Percentual-chave do projeto + gráfico de proporção (donut ou stacked bar)  
**Equipe:** Dados  
**Viabilidade:** ✅ Diretamente respondível — **KPI central do projeto**

### US-1.3 · Detalhamento por Tipo de Recurso Assistivo
**Pergunta:** Dentre as escolas com plataformas digitais (`P42_2_AGREG = 1`), qual a taxa de adoção de CADA recurso assistivo individualmente?  
**Variáveis:** `P42_2_AGREG`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Gráfico de barras horizontais (4 barras: Hardware adaptado, Software assistivo, Aulas de informática assistiva, Materiais digitais acessíveis)  
**Equipe:** Dados  
**Viabilidade:** ✅ Diretamente respondível

### US-1.4 · Detalhamento por Tipo de Plataforma vs. Acessibilidade
**Pergunta:** Dentre as escolas que usam cada plataforma específica (Teams, Zoom, Google Classroom, Moodle, Meet, AVAMEC), qual % possui algum recurso assistivo?  
**Variáveis:** `P42_2_A`, `P42_2_B`, `P42_2_C1`, `P42_2_D`, `P42_2_F`, `P42_2_G`, `P32_A-D`, `PESO`  
**Entrega:** Tabela cruzada ou heatmap  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível (atenção ao n amostral por plataforma)

### US-1.5 · Inclusão com Alunos PcD Presentes (Cenário mais crítico)
**Pergunta:** Dentre as escolas que TÊM alunos com deficiência (`P31=1`) E usam plataformas digitais (`P42_2_AGREG=1`), qual % NÃO possui nenhum recurso assistivo?  
**Variáveis:** `P31`, `P42_2_AGREG`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Percentual crítico — **Impacto argumentativo máximo para o Secretariado**  
**Equipe:** Dados → Secretariado (confrontar com Art. 28, incisos V e XIV da LBI + Portaria MEC 3.284/2003)  
**Viabilidade:** ✅ Diretamente respondível — **Pergunta de maior impacto acadêmico**

---

## 3. ÉPICO 2 — ABISMO ADMINISTRATIVO E GEOGRÁFICO

> **Hipótese:** Escolas públicas e escolas rurais possuem significativamente menos recursos de acessibilidade digital do que escolas privadas e urbanas, com o Centro-Oeste como caso de estudo.

### US-2.1 · Acessibilidade por Dependência Administrativa (Público vs. Privado — Nacional)
**Pergunta:** Qual o percentual ponderado de escolas com pelo menos um recurso assistivo (`P32_A-D`), segmentado por `COD_DEPENDENCIA` (1=Federal, 2=Estadual, 3=Municipal, 4=Particular)?  
**Variáveis:** `COD_DEPENDENCIA`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Gráfico de barras agrupadas por dependência  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível

### US-2.2 · Acessibilidade por Região (Centro-Oeste vs. Média Nacional)
**Pergunta:** Qual o percentual ponderado de escolas com recursos assistivos no Centro-Oeste (`COD_REGIAO=5`) comparado à média nacional e a cada outra região?  
**Variáveis:** `COD_REGIAO`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Gráfico de barras por região, com linha de referência na média nacional  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível (⚠️ verificar n amostral do Centro-Oeste)

### US-2.3 · Dupla Segmentação: Região × Dependência
**Pergunta:** No Centro-Oeste, como se compara a oferta de acessibilidade entre escolas públicas e particulares? E esse gap é maior ou menor que o gap nacional?  
**Variáveis:** `COD_REGIAO`, `COD_DEPENDENCIA_2_2_1`, `P32_A-D`, `PESO`  
**Entrega:** Tabela pivot 5 regiões × 2 categorias (Pública/Privada) + destaque Centro-Oeste  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível (⚠️ atenção ao cruzamento — subgrupos podem ficar pequenos)

### US-2.4 · Zona Urbana vs. Rural — Acessibilidade Digital
**Pergunta:** Qual a diferença percentual de adoção de tecnologias assistivas entre escolas urbanas (`COD_ZONA=1`) e rurais (`COD_ZONA=2`)?  
**Variáveis:** `COD_ZONA`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Gráfico comparativo (2 barras por recurso)  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível

### US-2.5 · Capital vs. Interior — Efeito da Centralidade
**Pergunta:** Escolas em capitais (`COD_TIPO_CIDADE=1`) possuem maior taxa de acessibilidade digital que as de interior (`COD_TIPO_CIDADE=2`)? E essa diferença persiste quando controlamos por dependência administrativa?  
**Variáveis:** `COD_TIPO_CIDADE`, `COD_DEPENDENCIA`, `P32_A-D`, `PESO`  
**Entrega:** Tabela cruzada Capital/Interior × Dependência  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível

### US-2.6 · Acessibilidade por Porte da Escola
**Pergunta:** Escolas maiores (mais matrículas) tendem a ter mais recursos assistivos? Qual a taxa de acessibilidade por faixa de porte (`PORTE`)?  
**Variáveis:** `PORTE`, `P32_A`, `P32_B`, `P32_C`, `P32_D`, `PESO`  
**Entrega:** Gráfico de barras empilhadas por 6 faixas de porte  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível

### US-2.7 · Sala de Recursos Multifuncionais — Existência vs. Conectividade
**Pergunta:** Dentre as escolas que possuem Sala de Recursos Multifuncionais para AEE (`P24_G=1`), qual percentual tem Internet nesse espaço (`P25_G=1`)? E qual percentual permite que os alunos acessem a Internet lá (`P26_G=1`)?  
**Variáveis:** `P24_G`, `P25_G`, `P26_G`, `PESO`  
**Entrega:** Funil de 3 estágios (Tem sala → Tem Internet na sala → Aluno acessa Internet na sala)  
**Equipe:** Dados → Secretariado (vincular com e-MAG e Art. 67 da LBI sobre acessibilidade em comunicações)  
**Viabilidade:** ✅ Respondível — **Excelente para storytelling visual**

---

## 4. ÉPICO 3 — PREVISIBILIDADE DE EXCLUSÃO (Projeção Analítica)

> **Hipótese:** É possível prever a ausência de acessibilidade digital com base em características estruturais da escola.

### US-3.1 · Regressão Logística — Fatores Preditores de Falha na Inclusão Digital
**Pergunta:** Dado um modelo logístico, quais variáveis estruturais mais impactam a probabilidade de uma escola NÃO ter nenhum recurso assistivo?  
**Variável dependente (Y):** Binária — `0` se possui ≥1 recurso (P32_A=1 OR P32_B=1 OR P32_C=1 OR P32_D=1); `1` se não possui nenhum  
**Preditores (X):**
| Variável | Justificativa |
|---|---|
| `COD_ZONA` | Urbana vs. Rural |
| `PORTE` | Porte da escola |
| `COD_DEPENDENCIA` | Tipo administrativo |
| `COD_REGIAO` | Região geográfica |
| `COD_TIPO_CIDADE` | Capital vs. Interior |
| `NIVEL_ENSINO` | Nível de ensino ofertado |
| `P8` | Possui Internet |
| `P10_AGREG` | Possui algum computador |
| `P59_P73_AGREG` | Gestor fez formação em TIC |
| `P42_2_AGREG` | Usa plataformas digitais |

**Entrega:** Tabela de coeficientes (odds ratio), p-valores e métricas de ajuste (AUC, accuracy). Gráfico de importância das features.  
**Equipe:** ADS (modelagem em Python: `sklearn` ou `statsmodels`)  
**Viabilidade:** ✅ Respondível — Necessário exclusão de linhas com missing nos preditores

### US-3.2 · Perfil-tipo da Escola Excluída Digitalmente
**Pergunta:** Qual o perfil demográfico predominante das escolas que usam plataformas mas NÃO possuem acessibilidade? (Crosstab descritivo multidimensional)  
**Variáveis:** Todas do US-3.1 filtradas para `P42_2_AGREG=1 AND sem nenhum P32`  
**Entrega:** Tabela de frequências (% de rurais, % municipais, % NE, etc.) — Retrato da exclusão  
**Equipe:** Dados + ADS  
**Viabilidade:** ✅ Respondível

### US-3.3 · Árvore de Decisão (Modelo interpretável alternativo)
**Pergunta:** Qual sequência de decisões (zona → dependência → porte → etc.) melhor separa escolas com e sem acessibilidade?  
**Variáveis:** Mesmas de US-3.1  
**Entrega:** Visualização da árvore (max_depth=4) — Excelente para apresentação ao professor  
**Equipe:** ADS (`sklearn.tree.DecisionTreeClassifier`)  
**Viabilidade:** ✅ Respondível

---

## 5. ÉPICO 4 — INFRAESTRUTURA COMO PRÉ-CONDIÇÃO

> **Hipótese:** A ausência de infraestrutura básica (Internet, computadores) é uma barreira prévia à acessibilidade.

### US-4.1 · Funil de Digitalização Inclusiva (Nacional)
**Pergunta:** Qual o percentual de escolas em cada "estágio" do funil?  
```
Estágio 1: Tem Internet (P8=1)
Estágio 2: Tem Internet + Computador (P8=1 AND P10_AGREG=1)
Estágio 3: Tem Internet + Computador + Plataforma (+ P42_2_AGREG=1)
Estágio 4: Tem tudo acima + algum recurso assistivo (+ P32_X=1)
Estágio 5: Tem tudo acima + Sala de Recursos Multifuncionais com Internet (+ P24_G=1 AND P25_G=1)
```
**Variáveis:** `P8`, `P10_AGREG`, `P42_2_AGREG`, `P32_A-D`, `P24_G`, `P25_G`, `PESO`  
**Entrega:** Gráfico de funil (funnel chart) — **Melhor visualização do projeto**  
**Equipe:** Dados → Secretariado (argumento: Art. 63 LBI + Decreto 5.296/2004)  
**Viabilidade:** ✅ Diretamente respondível

### US-4.2 · Velocidade da Internet e Acessibilidade
**Pergunta:** Escolas com maior velocidade de Internet (`P76`) tendem a ter mais recursos assistivos?  
**Variáveis:** `P76`, `P32_A-D`, `PESO`  
**Entrega:** Gráfico de barras: % de acessibilidade por faixa de velocidade  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível

### US-4.3 · Formação do Gestor como Fator de Acessibilidade
**Pergunta:** Escolas cujo gestor fez formação em TIC (`P59_P73_AGREG=1`) possuem maior taxa de recursos assistivos?  
**Variáveis:** `P59_P73_AGREG`, `P32_A-D`, `PESO`  
**Entrega:** Gráfico comparativo (gestor com formação vs. sem)  
**Equipe:** Dados  
**Viabilidade:** ✅ Respondível — **Insight para recomendação de política pública**

---

## 6. ALERTAS DE VIÉS E LIMITAÇÕES METODOLÓGICAS

### ⚠️ Alerta 1 — Viés de Seleção do P32
As variáveis P32_A-D possuem `99 = Não se aplica`, que provavelmente corresponde a escolas sem alunos PcD (`P31=0`). **Toda análise deve explicitar se está considerando o universo total ou apenas escolas com P31=1.** Sugiro que o Secretariado inclua uma nota metodológica sobre isso.

### ⚠️ Alerta 2 — Tamanho Amostral nos Cruzamentos
Ao filtrar `COD_REGIAO=5` (Centro-Oeste) + `COD_ZONA=2` (Rural) + `COD_DEPENDENCIA=4` (Particular), o subgrupo pode ter n < 30, tornando a estimativa instável. **O ETL deve adicionar uma coluna `n_contagem` em toda tabela de resultados para transparência.**

### ⚠️ Alerta 3 — Peso Amostral
A pesquisa TIC Educação é amostral com desenho complexo. Ignorar `PESO` gera estimativas enviesadas. Todas as tabelas devem mostrar tanto a contagem bruta (n) quanto o percentual ponderado.

### ⚠️ Alerta 4 — Causalidade vs. Correlação
A regressão logística do Épico 3 identifica **associações**, não **causas**. O Secretariado deve evitar linguagem causal no texto acadêmico. Exemplo correto: "Escolas rurais têm 3,2x mais chance de não possuir recursos assistivos" — e NÃO "Ser rural causa ausência de acessibilidade".

### ⚠️ Alerta 5 — Variáveis NÃO disponíveis nesta base
A base de Gestores/Escolas **NÃO** permite responder:
- Percepção individual de alunos PcD sobre as plataformas
- Tipo específico de deficiência dos alunos (visual, auditiva, motora, etc.)
- Qualidade/usabilidade real dos softwares assistivos
- Se os recursos assistivos existentes estão em funcionamento ou são obsoletos
- Compliance com e-MAG (avaliação técnica de conformidade)

**→ Essas limitações devem ser declaradas no capítulo de Metodologia.**

---

## 7. MAPEAMENTO DE LEGISLAÇÃO PARA O SECRETARIADO

| Análise (US) | Legislação Correspondente | Artigo-Chave |
|---|---|---|
| US-1.2 (Ilusão da Digitalização) | Lei Brasileira de Inclusão (Lei 13.146/2015) | Art. 63 — Acessibilidade nos sítios de Internet |
| US-1.5 (Escolas com PcD sem recurso) | LBI | Art. 28, incisos V e XIV — Oferta de recursos de TI acessíveis |
| US-2.7 (Sala de Recursos sem Internet) | LBI + Política Nacional de Ed. Especial | Art. 67 — Acessibilidade em comunicações |
| US-4.1 (Funil de Digitalização) | Decreto 5.296/2004 | Art. 47 — Acessibilidade digital |
| US-4.3 (Formação do Gestor) | LBI | Art. 28, inciso XI — Formação de professores para inclusão |
| Todos | Modelo e-MAG (Governo Federal) | Recomendações de acessibilidade web |
| Todos | Portaria MEC 3.284/2003 | Requisitos de acessibilidade para credenciamento |

---

## 8. PRIORIZAÇÃO DO BACKLOG (MoSCoW)

### MUST HAVE (Entregas obrigatórias para aprovação)
- [x] US-1.1 — Taxa de Plataformas vs. Acessibilidade
- [x] US-1.2 — KPI: Plataforma SIM × Acessibilidade NÃO
- [x] US-1.5 — Escolas com PcD + Plataformas sem recurso
- [x] US-2.1 — Público vs. Privado
- [x] US-2.2 — Centro-Oeste vs. Nacional
- [x] US-4.1 — Funil de Digitalização Inclusiva

### SHOULD HAVE (Alto valor, mas não bloqueantes)
- [ ] US-1.3 — Detalhamento por tipo de recurso assistivo
- [ ] US-2.4 — Urbana vs. Rural
- [ ] US-2.7 — Sala de Recursos: existência vs. conectividade
- [ ] US-3.1 — Regressão Logística
- [ ] US-4.3 — Formação do Gestor

### COULD HAVE (Enriquecem se houver tempo)
- [ ] US-1.4 — Por tipo de plataforma
- [ ] US-2.3 — Dupla segmentação Região × Dependência
- [ ] US-2.5 — Capital vs. Interior
- [ ] US-2.6 — Acessibilidade por Porte
- [ ] US-3.2 — Perfil-tipo da escola excluída
- [ ] US-3.3 — Árvore de Decisão
- [ ] US-4.2 — Velocidade de Internet e acessibilidade

### WON'T HAVE (Fora do escopo desta base)
- ✗ Avaliação da usabilidade real das plataformas
- ✗ Percepção dos alunos PcD
- ✗ Teste automatizado de conformidade e-MAG
- ✗ Análise por tipo específico de deficiência

---

## 9. DISTRIBUIÇÃO DE TRABALHO POR SPRINT

### Sprint 1 — ETL e Limpeza (Equipe de Dados)
- [ ] Download dos microdados CSV
- [ ] Script de limpeza: tratar 97/98/99, criar colunas derivadas
- [ ] Criar variável `TEM_ACESSIBILIDADE = (P32_A==1) | (P32_B==1) | (P32_C==1) | (P32_D==1)`
- [ ] Criar variável `EXCLUSAO_ATIVA = (P42_2_AGREG==1) & (TEM_ACESSIBILIDADE==0)`
- [ ] Validar contagem de registros por região/dependência

### Sprint 1 — Pesquisa Legal (Secretariado)
- [ ] Fichamento: Art. 28, 63 e 67 da LBI
- [ ] Fichamento: Decreto 5.296/2004
- [ ] Fichamento: Portaria MEC 3.284/2003
- [ ] Fichamento: e-MAG — seção sobre acessibilidade em plataformas educacionais

### Sprint 2 — Análises MUST HAVE (Equipe de Dados + ADS)
- [ ] US-1.1 + US-1.2 + US-1.5 (Épico 1 — núcleo)
- [ ] US-2.1 + US-2.2 (Épico 2 — núcleo)
- [ ] US-4.1 (Funil)

### Sprint 3 — Análises SHOULD HAVE + Modelo (ADS + Dados)
- [ ] US-3.1 (Regressão Logística)
- [ ] US-2.7 (Sala de Recursos)
- [ ] US-4.3 (Formação do Gestor)

### Sprint 4 — Consolidação e Storytelling (Todos)
- [ ] Power BI: Dashboard final
- [ ] Secretariado: Redação do artigo (ABNT)
- [ ] Revisão final e ensaio da apresentação
