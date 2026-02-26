# GUIA DE TAREFAS POR EQUIPE
## Quem faz o quê, passo a passo — Projeto Acessibilidade Digital

> **Leia o [BACKLOG_PROJETO.md](BACKLOG_PROJETO.md) antes de começar.**  
> Este documento traduz o backlog em tarefas concretas para cada pessoa.  
> Se tiver dúvida em qualquer passo, pergunte ao Gabriel (PO) antes de seguir.

---

## VISÃO GERAL DO PROJETO (em linguagem simples)

**O que estamos fazendo?**
Estamos analisando dados reais de escolas brasileiras para descobrir se a "digitalização" das escolas (uso de plataformas como Google Classroom, Zoom etc.) veio acompanhada de cuidados com alunos com deficiência (tecnologias assistivas, salas adaptadas etc.) — ou se essas pessoas foram deixadas de fora.

**De onde vêm os dados?**
De uma pesquisa oficial do governo chamada **TIC Educação 2024**, feita pelo Cetic.br. Ela entrevistou diretores/gestores de escolas do Brasil inteiro.

**O que queremos provar?**
Que muitas escolas adotaram plataformas digitais, mas NÃO investiram em acessibilidade na mesma proporção. Isso é uma violação da Lei Brasileira de Inclusão.

**O que cada equipe faz (resumo)?**

```
┌─────────────────────────────────────────────────────────┐
│                    GABRIEL (PO)                          │
│  Define o que fazer · Valida resultados · Integra tudo  │
└──────────────────────────┬──────────────────────────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
  │ SECRETARIADO │ │ EQ. DE DADOS │ │   EQ. ADS    │
  │  (2 pessoas) │ │  (2 pessoas) │ │  (1 pessoa)  │
  │              │ │              │ │              │
  │ Pesquisam    │ │ Limpam o CSV │ │ Cria modelo  │
  │ as LEIS      │ │ Geram os     │ │ preditivo    │
  │ Escrevem o   │ │ GRÁFICOS e   │ │ (regressão)  │
  │ TEXTO final  │ │ TABELAS      │ │              │
  └──────────────┘ └──────────────┘ └──────────────┘
       POR QUÊ?        O QUÊ?          E SE...?
```

---

# EQUIPE DE SECRETARIADO (2 pessoas)

## Seu papel no projeto
Vocês são as pessoas que transformam **números** em **argumentos**. A equipe de dados vai gerar percentuais e gráficos. Vocês vão pegar esses números e explicar **por que eles importam**, usando a legislação brasileira como base.

Vocês também cuidam da **formatação ABNT**, do **cronograma** e da **redação final**.

**Vocês NÃO precisam:**
- Mexer em código ou Python
- Abrir o arquivo CSV
- Entender estatística avançada

**Vocês PRECISAM:**
- Ler e fichar leis específicas
- Escrever textos claros conectando dados com leis
- Manter o cronograma atualizado
- Formatar o trabalho em ABNT

---

## TAREFA 1 — Fichamento das Leis (Sprint 1)
**Prazo:** Entregar na próxima quarta-feira  
**Conexão com o backlog:** Alimenta TODOS os Épicos

### O que fazer, passo a passo:

**1.1 — Lei Brasileira de Inclusão (Lei 13.146/2015)**
- Abram o site: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm
- Leiam e ficharem os seguintes artigos:

| Artigo | O que diz (em resumo) | Onde usamos no projeto |
|---|---|---|
| **Art. 28, inciso V** | Escolas devem oferecer recursos de tecnologia assistiva | Quando mostrarmos que escolas com alunos PcD NÃO têm recursos (US-1.5) |
| **Art. 28, inciso XI** | Formação de professores para uso de tecnologia com inclusão | Quando mostrarmos que gestores sem formação têm menos acessibilidade (US-4.3) |
| **Art. 28, inciso XIV** | Oferta de recursos de tecnologia assistiva e de informação | Reforço para todos os dados do Módulo D (P32) |
| **Art. 63** | Obrigatoriedade de acessibilidade em sítios de Internet | Quando mostrarmos que plataformas foram adotadas sem acessibilidade (US-1.1 e US-1.2) |
| **Art. 67** | Acessibilidade em serviços de comunicação | Quando falarmos da Sala de Recursos sem Internet (US-2.7) |

**Como o fichamento deve ficar:**
```
LEI: Lei Brasileira de Inclusão (13.146/2015)
ARTIGO: Art. 63
TEXTO ORIGINAL: "É obrigatória a acessibilidade nos sítios da internet
mantidos por empresas com sede ou representação comercial no País ou por
órgãos de governo, para uso da pessoa com deficiência [...]"

RESUMO COM MINHAS PALAVRAS: A lei obriga que qualquer site ou plataforma
usada pelo governo (inclusive escolas públicas) seja acessível.

COMO USAMOS NO PROJETO: Quando a equipe de dados mostrar que X% das escolas
usam Google Classroom mas não têm software de leitura de tela, citamos
este artigo para mostrar que isso é uma violação legal.
```

**1.2 — Decreto 5.296/2004**
- Site: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5296.htm
- Foco no **Art. 47** (acessibilidade em portais e sítios eletrônicos)
- Fichamento no mesmo formato acima

**1.3 — Portaria MEC 3.284/2003**
- Pesquisem no Google: "Portaria MEC 3.284 2003"
- Foco: requisitos de acessibilidade para credenciamento de instituições de ensino
- Fichamento no mesmo formato

**1.4 — e-MAG (Modelo de Acessibilidade em Governo Eletrônico)**
- Site: https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital
- Leiam a seção sobre recomendações de acessibilidade
- Anotem no fichamento: quais recomendações do e-MAG seriam aplicáveis a plataformas educacionais (Google Classroom, Moodle etc.)?

### Entregável:
Um documento Word ou Google Docs com os 4 fichamentos, usando o formato acima. Enviar para o Gabriel.

---

## TAREFA 2 — Tabela "Dado → Argumento Jurídico" (Sprint 2)
**Prazo:** Uma semana após receber os gráficos da Equipe de Dados  
**Conexão com o backlog:** Épicos 1, 2 e 4

### O que fazer:
A equipe de dados vai entregar gráficos e percentuais. Vocês vão criar uma tabela conectando cada número a uma lei. Exemplo:

| Dado estatístico (vem dos Dados) | Argumento (vocês escrevem) | Lei citada |
|---|---|---|
| "72% das escolas usam plataformas digitais, mas apenas 18% possuem algum recurso de tecnologia assistiva" | "A digitalização das escolas brasileiras ocorreu de forma excludente, em descumprimento ao Art. 63 da LBI que obriga acessibilidade em plataformas digitais utilizadas pelo poder público" | Art. 63, Lei 13.146/2015 |
| "No Centro-Oeste, apenas 12% das escolas públicas possuem software assistivo, contra 35% das particulares" | "O abismo entre as redes evidencia que o poder público não cumpre suas obrigações..." | Art. 28, V, Lei 13.146/2015 |

*Os números acima são fictícios. Usem os reais que a equipe de dados enviar.*

### Entregável:
Tabela com pelo menos 6 linhas (uma para cada análise MUST HAVE do backlog).

---

## TAREFA 3 — Redação Final e ABNT (Sprint 4)
**Conexão com o backlog:** Consolidação final

### O que fazer:
- Escrever o artigo/trabalho final usando a estrutura:
  1. **Introdução** — Problema da exclusão digital na educação inclusiva
  2. **Referencial Teórico** — Fichamentos das leis (Tarefa 1)
  3. **Metodologia** — Descrever a base TIC Educação 2024 (Gabriel fornece o texto técnico)
  4. **Resultados** — Cada gráfico + a interpretação jurídica (Tarefa 2)
  5. **Conclusão** — Recomendações de política pública
- Formatar em ABNT (fonte, margens, citações, referências)
- Montar os slides da apresentação

### Entregável:
Documento final em Word (.docx) + Slides (PowerPoint ou Google Slides).

---

## TAREFA 4 — Controle de Cronograma (Contínuo)

### O que fazer:
Manter atualizada uma planilha simples com o status de cada equipe:

| Semana | Equipe de Dados | Equipe ADS | Secretariado | Status |
|---|---|---|---|---|
| Sem 1 | Limpeza do CSV | Ajuda na limpeza | Fichamento de leis | 🟡 Em andamento |
| Sem 2 | Gráficos Épico 1 e 2 | Modelo preditivo | Tabela Dado→Lei | ⚪ Não iniciado |
| Sem 3 | Gráficos Épico 4 | Árvore de Decisão | Redação parcial | ⚪ Não iniciado |
| Sem 4 | Dashboard Power BI | Revisão final | Texto + Slides | ⚪ Não iniciado |

**Enviar print dessa planilha para o Gabriel toda quarta antes das 18h.**

---
---

# EQUIPE DE DADOS (2 pessoas)

## Seu papel no projeto
Vocês são quem **mexe nos dados de verdade**. Vão abrir o arquivo CSV gigante, limpar os dados ruins, filtrar o que interessa e gerar os gráficos e tabelas que respondem às perguntas do backlog.

**Ferramentas que vocês vão usar:**
- **Python** com **Pandas** (para limpar e filtrar)
- **Power BI** OU **Matplotlib/Seaborn** (para gráficos)
- **Jupyter Notebook** (recomendado para organizar o trabalho)

**Vocês NÃO precisam:**
- Pesquisar leis
- Escrever o texto acadêmico
- Criar modelos preditivos (isso é do ADS)

---

## TAREFA 1 — Download e Exploração Inicial (Sprint 1, dia 1-2)
**Conexão com o backlog:** Pré-requisito de TUDO

### O que fazer:

**1.1 — Baixar os microdados**
- Acessem: https://cetic.br/pt/pesquisa/educacao/microdados/
- Baixem o arquivo da **TIC Educação 2024 — Escolas/Gestores**
- Descompactem e coloquem o CSV na pasta do projeto

**1.2 — Primeiro olhar nos dados**
Abram um Jupyter Notebook e rodem:
```python
import pandas as pd

# Ajuste o nome do arquivo conforme o que vocês baixaram
df = pd.read_csv('nome_do_arquivo.csv', sep=';', encoding='latin-1')

# Ver primeiras linhas
print(df.shape)  # quantas linhas e colunas?
print(df.columns.tolist())  # nomes das colunas
df.head()
```

**Anotem e enviem ao Gabriel:**
- Quantas linhas (escolas) tem o arquivo?
- O separador é `;` ou `,`?
- O encoding é `latin-1` ou `utf-8`?
- As colunas batem com o dicionário? (ex: existe `P32_A`, `P42_2_AGREG` etc.?)

---

## TAREFA 2 — Limpeza dos Dados (Sprint 1, dia 2-4)
**Conexão com o backlog:** Seção 1 do BACKLOG (Regras de Negócio para ETL)

### O que fazer:

**2.1 — Tratar os valores especiais (97, 98, 99)**

```python
import numpy as np

# Colunas que vamos usar no projeto (conferir com o dicionário)
colunas_binarias = [
    'P31',           # Tem alunos com deficiência?
    'P32_A',         # Hardware assistivo
    'P32_B',         # Software assistivo
    'P32_C',         # Aulas de informática assistiva
    'P32_D',         # Materiais digitais acessíveis
    'P24_G',         # Sala de Recursos Multifuncionais
    'P25_G',         # Internet na Sala de Recursos
    'P26_G',         # Aluno acessa Internet na Sala de Recursos
    'P42_2_A',       # Teams
    'P42_2_B',       # Zoom
    'P42_2_C1',      # Google Classroom
    'P42_2_D',       # Moodle
    'P42_2_F',       # Google Meet
    'P42_2_G',       # AVAMEC
    'P42_2_OUTRO',   # Outra plataforma
    'P8',            # Tem Internet
    'P10_A',         # Computador de mesa
    'P10_B',         # Notebook
    'P10_C',         # Tablet
    'P22',           # Wi-Fi
    'P59',           # Formação em TIC (ensino)
    'P73',           # Formação em TIC (gestão)
]

# 97 ("Não sabe") e 98 ("Não respondeu") viram NaN
for col in colunas_binarias:
    if col in df.columns:
        df[col] = df[col].replace({97: np.nan, 98: np.nan})

# ATENÇÃO: O 99 ("Não se aplica") tem tratamento especial!
# Nas colunas P32_A até P32_D, o 99 aparece quando P31=0 (sem alunos PcD).
# Por enquanto, vamos manter o 99 e tratar caso a caso nas análises.
```

**2.2 — Criar as colunas novas que o projeto precisa**

```python
# COLUNA 1: "Tem algum recurso de acessibilidade?"
# Regra: 1 se qualquer P32 = 1, senão 0
# Primeiro, tratar 99 como 0 para esta coluna
p32_cols = ['P32_A', 'P32_B', 'P32_C', 'P32_D']
df['TEM_ACESSIBILIDADE'] = df[p32_cols].replace({99: 0}).max(axis=1)
# max(axis=1) pega o maior valor da linha: se algum for 1, resultado é 1

# COLUNA 2: "Usa alguma plataforma digital?"
# Se a variável P42_2_AGREG já existe no CSV, usar ela
# Senão, criar manualmente:
if 'P42_2_AGREG' not in df.columns:
    plat_cols = ['P42_2_A', 'P42_2_B', 'P42_2_C1', 'P42_2_D', 
                 'P42_2_F', 'P42_2_G', 'P42_2_OUTRO']
    df['P42_2_AGREG'] = df[plat_cols].max(axis=1)

# COLUNA 3: "Exclusão Digital Ativa" — Usa plataforma MAS não tem acessibilidade
df['EXCLUSAO_ATIVA'] = ((df['P42_2_AGREG'] == 1) & 
                         (df['TEM_ACESSIBILIDADE'] == 0)).astype(int)

# COLUNA 4: Para análise mais restrita — só escolas com alunos PcD
df['EXCLUSAO_PCD'] = ((df['P31'] == 1) & 
                       (df['P42_2_AGREG'] == 1) & 
                       (df['TEM_ACESSIBILIDADE'] == 0)).astype(int)
```

**2.3 — Verificar se deu certo**
```python
# Conferência rápida
print("Total de escolas:", len(df))
print("Escolas com Internet:", df[df['P8']==1].shape[0])
print("Escolas com plataforma:", df[df['P42_2_AGREG']==1].shape[0])
print("Escolas com acessibilidade:", df[df['TEM_ACESSIBILIDADE']==1].shape[0])
print("Exclusão ativa:", df[df['EXCLUSAO_ATIVA']==1].shape[0])
print("Escolas com PcD:", df[df['P31']==1].shape[0])
print("Exclusão PcD:", df[df['EXCLUSAO_PCD']==1].shape[0])
```

**Enviar esses números ao Gabriel para validação antes de seguir.**

---

## TAREFA 3 — Gráficos e Tabelas do Épico 1 (Sprint 2)
**Conexão com o backlog:** US-1.1, US-1.2, US-1.3, US-1.5

### O que fazer:

> **REGRA DE OURO:** Todo percentual deve usar o PESO amostral!

**3.1 — Função auxiliar para percentual ponderado (copie e use sempre):**
```python
def pct_ponderado(df_filtro, coluna, valor, peso='PESO'):
    """
    Calcula o percentual ponderado de 'coluna == valor' no dataframe filtrado.
    Retorna: (percentual, contagem_bruta)
    """
    mask_valido = df_filtro[coluna].notna()
    df_val = df_filtro[mask_valido]
    
    numerador = df_val.loc[df_val[coluna] == valor, peso].sum()
    denominador = df_val[peso].sum()
    
    pct = (numerador / denominador) * 100 if denominador > 0 else 0
    n = df_val[df_val[coluna] == valor].shape[0]
    
    return round(pct, 1), n
```

**3.2 — US-1.1: Plataformas vs. Acessibilidade (gráfico de barras lado a lado)**
```python
import matplotlib.pyplot as plt

pct_plat, n_plat = pct_ponderado(df, 'P42_2_AGREG', 1)
pct_acess, n_acess = pct_ponderado(df, 'TEM_ACESSIBILIDADE', 1)

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(['Usam Plataformas\nDigitais', 'Possuem Recursos\nde Acessibilidade'], 
                [pct_plat, pct_acess], 
                color=['#2196F3', '#FF5722'], width=0.5)

# Colocar o valor em cima de cada barra
for barra, pct, n in zip(barras, [pct_plat, pct_acess], [n_plat, n_acess]):
    ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 1,
            f'{pct}%\n(n={n})', ha='center', fontsize=12, fontweight='bold')

ax.set_ylabel('Percentual ponderado (%)')
ax.set_title('Ilusão da Digitalização:\nAdoção de Plataformas vs. Acessibilidade Digital nas Escolas')
ax.set_ylim(0, 100)
plt.tight_layout()
plt.savefig('grafico_US1_1.png', dpi=150)
plt.show()
```

**3.3 — US-1.2: KPI de Exclusão Ativa (gráfico donut)**
```python
# Filtrar escolas que usam plataformas
df_com_plat = df[df['P42_2_AGREG'] == 1].copy()

pct_sem, n_sem = pct_ponderado(df_com_plat, 'TEM_ACESSIBILIDADE', 0)
pct_com = 100 - pct_sem

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    [pct_sem, pct_com], 
    labels=['SEM acessibilidade', 'COM acessibilidade'],
    colors=['#FF5722', '#4CAF50'],
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.75,
    textprops={'fontsize': 12}
)
# Furo no meio para virar donut
centro = plt.Circle((0,0), 0.50, fc='white')
ax.add_artist(centro)
ax.set_title('Entre escolas que USAM plataformas digitais:\nQuantas possuem recursos de acessibilidade?',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_US1_2_KPI.png', dpi=150)
plt.show()
```

**3.4 — US-1.3: Detalhamento por tipo de recurso (barras horizontais)**
```python
recursos = {
    'P32_A': 'Hardware adaptado\n(teclados, mouses)',
    'P32_B': 'Software assistivo\n(leitura de tela)',
    'P32_C': 'Aulas de informática\nassistiva',
    'P32_D': 'Materiais digitais\nacessíveis (audiolivros)'
}

# Filtrar escolas com plataformas
df_plat = df[df['P42_2_AGREG'] == 1].copy()

# Calcular % de cada recurso (trocando 99 por 0)
resultados = {}
for col, nome in recursos.items():
    df_temp = df_plat.copy()
    df_temp[col] = df_temp[col].replace({99: 0})
    pct, n = pct_ponderado(df_temp, col, 1)
    resultados[nome] = {'pct': pct, 'n': n}

nomes = list(resultados.keys())
pcts = [resultados[n]['pct'] for n in nomes]

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(nomes, pcts, color=['#FF9800', '#2196F3', '#9C27B0', '#4CAF50'])
for bar, pct in zip(bars, pcts):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{pct}%', va='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Percentual ponderado (%)')
ax.set_title('Tipos de Recurso Assistivo nas Escolas com Plataformas Digitais')
ax.set_xlim(0, max(pcts) + 15)
plt.tight_layout()
plt.savefig('grafico_US1_3.png', dpi=150)
plt.show()
```

**3.5 — US-1.5: O percentual mais importante — Escolas com PcD + Plataforma sem Acessibilidade**
```python
# Escolas com alunos PcD E que usam plataformas
df_pcd_plat = df[(df['P31'] == 1) & (df['P42_2_AGREG'] == 1)].copy()
print(f"Escolas com PcD + Plataformas: {len(df_pcd_plat)}")

pct_sem_acc, n_sem_acc = pct_ponderado(df_pcd_plat, 'TEM_ACESSIBILIDADE', 0)
print(f">>> {pct_sem_acc}% dessas escolas NÃO possuem NENHUM recurso de acessibilidade (n={n_sem_acc})")

# Esse número é o dado mais forte do projeto!
# Enviem imediatamente para o Gabriel e para o Secretariado
```

---

## TAREFA 4 — Gráficos e Tabelas do Épico 2 (Sprint 2)
**Conexão com o backlog:** US-2.1, US-2.2, US-2.4, US-2.7

### O que fazer:

**4.1 — US-2.1: Acessibilidade por Dependência Administrativa**
```python
deps = {1: 'Federal', 2: 'Estadual', 3: 'Municipal', 4: 'Particular'}

resultados_dep = {}
for cod, nome in deps.items():
    df_dep = df[df['COD_DEPENDENCIA'] == cod].copy()
    df_dep['TEM_ACESSIBILIDADE'] = df_dep[p32_cols].replace({99: 0}).max(axis=1)
    pct, n = pct_ponderado(df_dep, 'TEM_ACESSIBILIDADE', 1)
    resultados_dep[nome] = {'pct': pct, 'n': n}
    print(f"{nome}: {pct}% (n={n})")

# Gráfico de barras
nomes = list(resultados_dep.keys())
pcts = [resultados_dep[n]['pct'] for n in nomes]

fig, ax = plt.subplots(figsize=(8, 5))
cores = ['#1565C0', '#1976D2', '#42A5F5', '#FF7043']  # azuis para público, laranja para privado
bars = ax.bar(nomes, pcts, color=cores, width=0.5)
for bar, pct in zip(bars, pcts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{pct}%', ha='center', fontsize=12, fontweight='bold')
ax.set_ylabel('% com pelo menos 1 recurso assistivo')
ax.set_title('Acessibilidade Digital por Dependência Administrativa')
ax.set_ylim(0, 100)
plt.tight_layout()
plt.savefig('grafico_US2_1.png', dpi=150)
plt.show()
```

**4.2 — US-2.2: Centro-Oeste vs. Regiões**
```python
regioes = {1: 'Norte', 2: 'Nordeste', 3: 'Sudeste', 4: 'Sul', 5: 'Centro-Oeste'}

resultados_reg = {}
for cod, nome in regioes.items():
    df_reg = df[df['COD_REGIAO'] == cod].copy()
    df_reg['TEM_ACESSIBILIDADE'] = df_reg[p32_cols].replace({99: 0}).max(axis=1)
    pct, n = pct_ponderado(df_reg, 'TEM_ACESSIBILIDADE', 1)
    resultados_reg[nome] = {'pct': pct, 'n': n}
    print(f"{nome}: {pct}% (n={n})")

# Também calcular a média nacional
df_temp = df.copy()
df_temp['TEM_ACESSIBILIDADE'] = df_temp[p32_cols].replace({99: 0}).max(axis=1)
pct_nacional, _ = pct_ponderado(df_temp, 'TEM_ACESSIBILIDADE', 1)

# Gráfico com linha de referência
nomes = list(resultados_reg.keys())
pcts = [resultados_reg[n]['pct'] for n in nomes]
cores = ['#78909C']*4 + ['#FF5722']  # Centro-Oeste em destaque

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(nomes, pcts, color=cores, width=0.5)
ax.axhline(y=pct_nacional, color='black', linestyle='--', linewidth=1, label=f'Média Nacional ({pct_nacional}%)')
for bar, pct in zip(bars, pcts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{pct}%', ha='center', fontsize=11, fontweight='bold')
ax.set_ylabel('% com pelo menos 1 recurso assistivo')
ax.set_title('Acessibilidade Digital por Região — Centro-Oeste em Destaque')
ax.legend()
ax.set_ylim(0, 100)
plt.tight_layout()
plt.savefig('grafico_US2_2.png', dpi=150)
plt.show()
```

**4.3 — US-2.7: Funil da Sala de Recursos Multifuncionais**
```python
# Estágio 1: Tem Sala de Recursos?
pct_sala, n_sala = pct_ponderado(df, 'P24_G', 1)

# Estágio 2: Das que têm, tem Internet lá?
df_com_sala = df[df['P24_G'] == 1].copy()
pct_int, n_int = pct_ponderado(df_com_sala, 'P25_G', 1)

# Estágio 3: Das que têm Internet, o aluno pode acessar?
df_com_internet = df_com_sala[df_com_sala['P25_G'] == 1].copy()
pct_aluno, n_aluno = pct_ponderado(df_com_internet, 'P26_G', 1)

print(f"Tem Sala de Recursos: {pct_sala}% (n={n_sala})")
print(f"  └─ Com Internet na Sala: {pct_int}% (n={n_int})")
print(f"       └─ Aluno acessa Internet: {pct_aluno}% (n={n_aluno})")

# Gráfico de funil
estagios = ['Tem Sala de\nRecursos (AEE)', 'Sala tem\nInternet', 'Aluno acessa\nInternet na sala']
# Para o funil, calcular % cumulativo sobre o total
pct_total_sala = pct_sala
pct_total_int = round(pct_sala * pct_int / 100, 1)
pct_total_aluno = round(pct_total_int * pct_aluno / 100, 1)
valores = [pct_total_sala, pct_total_int, pct_total_aluno]

fig, ax = plt.subplots(figsize=(8, 5))
cores = ['#4CAF50', '#FF9800', '#F44336']
bars = ax.barh(estagios[::-1], valores[::-1], color=cores[::-1], height=0.5)
for bar, pct in zip(bars, valores[::-1]):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{pct}% do total', va='center', fontsize=11, fontweight='bold')
ax.set_xlabel('% do total de escolas')
ax.set_title('Funil: Da Sala de Recursos ao Acesso Real do Aluno')
plt.tight_layout()
plt.savefig('grafico_US2_7_funil.png', dpi=150)
plt.show()
```

---

## TAREFA 5 — Gráfico do Funil Completo - Épico 4 (Sprint 2-3)
**Conexão com o backlog:** US-4.1

```python
# Funil de 5 estágios (do total de escolas)
e1, _ = pct_ponderado(df, 'P8', 1)                           # Tem Internet

df_e2 = df[(df['P8']==1)].copy()
df_e2['TEM_PC'] = df_e2[['P10_A','P10_B','P10_C']].replace({97:np.nan,98:np.nan}).max(axis=1)
e2, _ = pct_ponderado(df_e2, 'TEM_PC', 1)
e2_total = round(e1 * e2 / 100, 1)

df_e3 = df_e2[df_e2['TEM_PC']==1].copy()
e3, _ = pct_ponderado(df_e3, 'P42_2_AGREG', 1)
e3_total = round(e2_total * e3 / 100, 1)

df_e4 = df_e3[df_e3['P42_2_AGREG']==1].copy()
df_e4['TEM_ACESSIBILIDADE'] = df_e4[p32_cols].replace({99:0}).max(axis=1)
e4, _ = pct_ponderado(df_e4, 'TEM_ACESSIBILIDADE', 1)
e4_total = round(e3_total * e4 / 100, 1)

df_e5 = df_e4[df_e4['TEM_ACESSIBILIDADE']==1].copy()
df_e5_check = df_e5[(df_e5['P24_G']==1) & (df_e5['P25_G']==1)]
e5_total = round(len(df_e5_check) / len(df) * 100, 1) # aproximação bruta

estagios = [
    f'1. Internet\n({e1}%)',
    f'2. Internet +\nComputador\n({e2_total}%)',
    f'3. + Plataforma\nDigital\n({e3_total}%)',
    f'4. + Recurso\nAssistivo\n({e4_total}%)',
    f'5. + Sala AEE\ncom Internet\n({e5_total}%)'
]

valores = [e1, e2_total, e3_total, e4_total, e5_total]

fig, ax = plt.subplots(figsize=(12, 6))
cores = ['#4CAF50', '#8BC34A', '#FFC107', '#FF9800', '#F44336']
bars = ax.bar(estagios, valores, color=cores, width=0.6)
for bar, val in zip(bars, valores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val}%', ha='center', fontsize=13, fontweight='bold')
ax.set_ylabel('% do total de escolas')
ax.set_title('Funil de Digitalização Inclusiva — A cada etapa, quantas escolas sobrevivem?',
             fontsize=14, fontweight='bold')
ax.set_ylim(0, 100)
plt.tight_layout()
plt.savefig('grafico_US4_1_funil_completo.png', dpi=150)
plt.show()
```

---

## CHECKLIST FINAL — Equipe de Dados

Antes de enviar os resultados, confiram:

- [ ] Todos os percentuais usam a coluna `PESO`?
- [ ] Todos os gráficos mostram o `n` (contagem bruta) além do `%`?
- [ ] Os valores 97 e 98 foram removidos antes de calcular?
- [ ] O tratamento do 99 está documentado (excluiu ou tratou como 0)?
- [ ] Os gráficos foram salvos como PNG em alta resolução (dpi=150)?
- [ ] Os notebooks estão com nomes claros? (ex: `01_limpeza.ipynb`, `02_epico1.ipynb`)

---
---

# EQUIPE ADS (1 pessoa)

## Seu papel no projeto
Você é quem vai além da análise descritiva. Enquanto a equipe de dados responde "**o que acontece**", você responde "**por que acontece**" e "**é possível prever**". Vai construir um modelo estatístico para identificar quais características de uma escola preveem a falta de acessibilidade.

**Ferramentas:**
- Python com `scikit-learn` e/ou `statsmodels`
- Jupyter Notebook

**Você NÃO precisa:**
- Pesquisar leis
- Fazer a limpeza do CSV (a equipe de dados faz isso e te entrega o DataFrame limpo)
- Escrever o texto final

**Você PRECISA:**
- Receber o DataFrame limpo da equipe de dados
- Construir o modelo de regressão logística
- Gerar a árvore de decisão
- Interpretar os resultados em linguagem simples

---

## TAREFA 1 — Preparar os dados para modelagem (Sprint 2)
**Conexão com o backlog:** US-3.1 (Regressão Logística)

### O que fazer:

**1.1 — Receber o DataFrame limpo e criar a base de modelagem**
```python
import pandas as pd
import numpy as np

# A equipe de dados vai te passar o df já limpo
# Você precisa criar a base para o modelo

# Variável alvo (o que queremos prever):
# 0 = tem acessibilidade, 1 = NÃO tem acessibilidade
# (já criada pela equipe de dados como TEM_ACESSIBILIDADE)
df['Y_SEM_ACESSIBILIDADE'] = (df['TEM_ACESSIBILIDADE'] == 0).astype(int)

# Variáveis preditoras (as "características" da escola):
preditores = [
    'COD_ZONA',           # 1=Urbana, 2=Rural
    'PORTE',              # 1 a 6
    'COD_DEPENDENCIA',    # 1 a 4
    'COD_REGIAO',         # 1 a 5
    'COD_TIPO_CIDADE',    # 1=Capital, 2=Interior
    'NIVEL_ENSINO',       # 1 a 3
    'P8',                 # Tem Internet (0/1)
    'P10_AGREG',          # Tem computador (0/1)
    'P59_P73_AGREG',      # Gestor fez formação TIC (0/1)
    'P42_2_AGREG',        # Usa plataformas (0/1)
]

# Criar base limpa (sem NaN nos preditores)
df_modelo = df[preditores + ['Y_SEM_ACESSIBILIDADE', 'PESO']].dropna()
print(f"Linhas para modelagem: {len(df_modelo)} de {len(df)} ({len(df_modelo)/len(df)*100:.0f}%)")
```

**1.2 — Transformar variáveis categóricas**
```python
# COD_DEPENDENCIA, COD_REGIAO, PORTE e NIVEL_ENSINO são categóricas ordinais
# Para a regressão, precisamos de dummies (one-hot encoding)
categoricas = ['COD_DEPENDENCIA', 'COD_REGIAO', 'PORTE', 'NIVEL_ENSINO']
df_modelo_encoded = pd.get_dummies(df_modelo, columns=categoricas, drop_first=True)

print("Colunas finais:", df_modelo_encoded.columns.tolist())
```

---

## TAREFA 2 — Regressão Logística (Sprint 3)
**Conexão com o backlog:** US-3.1

### O que fazer:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt

# Separar X (preditores) e y (alvo)
X = df_modelo_encoded.drop(columns=['Y_SEM_ACESSIBILIDADE', 'PESO'])
y = df_modelo_encoded['Y_SEM_ACESSIBILIDADE']
pesos = df_modelo_encoded['PESO']

# Dividir em treino (70%) e teste (30%)
X_train, X_test, y_train, y_test, w_train, w_test = train_test_split(
    X, y, pesos, test_size=0.3, random_state=42, stratify=y
)

# Treinar o modelo
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train, sample_weight=w_train)

# Avaliar
y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

print("=== RESULTADOS ===")
print(classification_report(y_test, y_pred))
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob, sample_weight=w_test):.3f}")
```

**2.2 — Gráfico de Importância das Variáveis (Odds Ratio)**
```python
# Odds Ratio: exp(coeficiente). Se > 1, aumenta a chance de NÃO ter acessibilidade
coefs = pd.DataFrame({
    'Variavel': X.columns,
    'Coeficiente': modelo.coef_[0],
    'Odds_Ratio': np.exp(modelo.coef_[0])
}).sort_values('Odds_Ratio', ascending=True)

print(coefs.to_string())

# Gráfico
fig, ax = plt.subplots(figsize=(10, 8))
cores = ['#F44336' if or_val > 1 else '#4CAF50' for or_val in coefs['Odds_Ratio']]
ax.barh(coefs['Variavel'], coefs['Odds_Ratio'], color=cores)
ax.axvline(x=1, color='black', linestyle='--', linewidth=1)
ax.set_xlabel('Odds Ratio (>1 = aumenta risco de exclusão)')
ax.set_title('Fatores que Aumentam/Diminuem a Probabilidade de Exclusão Digital')
plt.tight_layout()
plt.savefig('grafico_US3_1_odds_ratio.png', dpi=150)
plt.show()
```

**O que os resultados significam (para você explicar aos outros):**
- Odds Ratio = 1.0 → Sem efeito
- Odds Ratio = 2.0 → "Escolas com essa característica têm 2x mais chance de NÃO ter acessibilidade"
- Odds Ratio = 0.5 → "Escolas com essa característica têm 50% menos chance de exclusão"

---

## TAREFA 3 — Árvore de Decisão (Sprint 3)
**Conexão com o backlog:** US-3.3

### O que fazer:

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Treinar árvore rasa (fácil de visualizar)
arvore = DecisionTreeClassifier(max_depth=4, random_state=42, min_samples_leaf=30)
arvore.fit(X_train, y_train, sample_weight=w_train)

# Avaliar
y_pred_tree = arvore.predict(X_test)
print("=== ÁRVORE DE DECISÃO ===")
print(classification_report(y_test, y_pred_tree))

# Visualizar a árvore
fig, ax = plt.subplots(figsize=(25, 12))
plot_tree(arvore, feature_names=X.columns.tolist(),
          class_names=['Com Acessibilidade', 'Sem Acessibilidade'],
          filled=True, rounded=True, fontsize=8, ax=ax)
plt.title('Árvore de Decisão: Quais características levam à exclusão digital?', fontsize=16)
plt.tight_layout()
plt.savefig('grafico_US3_3_arvore.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Por que a árvore é importante:**
Ela mostra uma "receita" visual. Exemplo: "Se a escola é municipal → E é rural → E não tem Internet → 95% de chance de NÃO ter acessibilidade". Isso é **muito poderoso** na apresentação.

---

## TAREFA 4 — Perfil da Escola Excluída (Sprint 3)
**Conexão com o backlog:** US-3.2

```python
# Filtrar escolas com "Exclusão Ativa" (usam plataforma mas sem acessibilidade)
df_excluidas = df[df['EXCLUSAO_ATIVA'] == 1].copy()
df_incluidas = df[(df['P42_2_AGREG']==1) & (df['TEM_ACESSIBILIDADE']==1)].copy()

print("=== PERFIL DA ESCOLA EXCLUÍDA vs. INCLUÍDA ===\n")

# Zona
for label, grupo in [("EXCLUÍDAS", df_excluidas), ("INCLUÍDAS", df_incluidas)]:
    pct_rural, _ = pct_ponderado(grupo, 'COD_ZONA', 2)
    print(f"{label} - % Rural: {pct_rural}%")

# Dependência
for dep, nome in {1:'Federal', 2:'Estadual', 3:'Municipal', 4:'Particular'}.items():
    pct_exc, _ = pct_ponderado(df_excluidas, 'COD_DEPENDENCIA', dep)
    pct_inc, _ = pct_ponderado(df_incluidas, 'COD_DEPENDENCIA', dep)
    print(f"{nome}: Excluídas={pct_exc}% | Incluídas={pct_inc}%")

# Envie esses resultados ao Gabriel e ao Secretariado
```

---

## CHECKLIST FINAL — Equipe ADS

- [ ] O modelo de regressão convergiu (sem warnings de convergência)?
- [ ] O AUC-ROC é > 0.60? (Se < 0.55, reportar ao Gabriel — pode ser que as variáveis tenham pouco poder preditivo, o que também é um achado válido)
- [ ] O gráfico de Odds Ratio está claro e salvo em PNG?
- [ ] A árvore de decisão tem no máximo 4 níveis (legível)?
- [ ] Os notebooks estão nomeados? (ex: `03_modelo_regressao.ipynb`, `04_arvore_decisao.ipynb`)

---
---

# COMO TUDO SE CONECTA (Fluxo de Entrega)

```
SEMANA 1                SEMANA 2                SEMANA 3                SEMANA 4
────────                ────────                ────────                ────────

DADOS:                  DADOS:                  DADOS:                  DADOS:
Limpa CSV ─────────►    Gráficos ──────────►    Gráficos ──────────►    Dashboard
Cria colunas            Épico 1 + 2             Épico 4                 Power BI
Valida com Gabriel      │                       │
                        │                       │
                        ▼                       ▼
ADS:                    ADS:                    ADS:
Aguarda df limpo ──►    Recebe df ─────────►    Modelo + Árvore ───►    Revisão
                        Prepara base            │
                                                │
                        ▼                       ▼
SECRETARIADO:           SECRETARIADO:           SECRETARIADO:           SECRETARIADO:
Fichamento de ─────►    Recebe gráficos ──►     Redação parcial ──►     Texto final
leis (4 docs)           Tabela Dado→Lei         Metodologia             ABNT + Slides
                                                Resultados
```

## Regra de Comunicação

| Situação | O que fazer |
|---|---|
| Terminei minha tarefa da semana | Avise no grupo do WhatsApp + envie o arquivo |
| Estou travado e não consigo avançar | Avise o Gabriel IMEDIATAMENTE (não espere a quarta) |
| Encontrei algo estranho nos dados | Anote o que encontrou + print da tela → envie ao Gabriel |
| Não entendi o que preciso fazer | Releia este guia. Se continuar com dúvida, pergunte no grupo |
| Quero fazer algo diferente do combinado | PERGUNTE ANTES. Não mude o escopo sozinho |

## Nomenclatura de Arquivos (TODOS seguem)

```
Projeto_extencao/
├── dados/
│   ├── raw/                         ← CSV original (NÃO MEXER)
│   └── processed/                   ← CSV limpo
├── notebooks/
│   ├── 01_limpeza.ipynb             ← Equipe de Dados
│   ├── 02_epico1_ilusao.ipynb       ← Equipe de Dados
│   ├── 03_epico2_abismo.ipynb       ← Equipe de Dados
│   ├── 04_epico4_funil.ipynb        ← Equipe de Dados
│   ├── 05_regressao_logistica.ipynb ← Equipe ADS
│   └── 06_arvore_decisao.ipynb      ← Equipe ADS
├── graficos/                        ← PNGs gerados pelos notebooks
├── docs/
│   ├── fichamento_leis.docx         ← Secretariado
│   ├── tabela_dado_lei.docx         ← Secretariado
│   └── artigo_final.docx            ← Secretariado
├── powerbi/
│   └── dashboard.pbix               ← Equipe de Dados
├── BACKLOG_PROJETO.md               ← PO (Gabriel)
└── GUIA_TAREFAS_EQUIPE.md           ← Este arquivo
```
