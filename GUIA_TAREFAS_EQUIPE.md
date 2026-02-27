# GUIA DE TAREFAS POR EQUIPE
## Quem faz o quê, passo a passo — Projeto Acessibilidade Digital
### v3 — Equipe de 4 pessoas · Foco nas Perguntas e Organização do Resultado

> **Leia o [BACKLOG_PROJETO.md](BACKLOG_PROJETO.md) antes de começar.**  
> Este documento traduz o backlog em tarefas concretas para cada pessoa.  
> Se tiver dúvida em qualquer passo, pergunte ao Gabriel (PO) antes de seguir.

---

## VISÃO GERAL DO PROJETO

**O que estamos fazendo?**
Analisando dados reais de escolas brasileiras para descobrir se a digitalização (uso de plataformas como Google Classroom, Zoom etc.) veio acompanhada de cuidados com alunos com deficiência (tecnologias assistivas, salas adaptadas etc.) — ou se essas pessoas foram deixadas de fora.

**De onde vêm os dados?**
Das **Tabelas de Indicadores** oficiais da pesquisa **TIC Educação 2024**, publicadas pelo Cetic.br. São dois arquivos Excel com 69 abas cada: um com **percentuais** e outro com **contagens absolutas**. Os dados já vêm prontos e ponderados — NÃO são microdados.

**O que queremos provar?**
Que embora 73,8% das escolas usem plataformas digitais, os recursos de acessibilidade (hardware adaptado, software assistivo, aulas, materiais) atingem no máximo 34%. E que esse gap é muito pior em escolas rurais, pequenas e do Norte/Nordeste.

**⚠️ O QUE NÃO PODEMOS FAZER COM ESSES DADOS:**
- Cruzar duas variáveis de abas diferentes
- Machine Learning (regressão, árvore de decisão)
- Filtrar subgrupos compostos

**Equipe e papéis:**

```
┌─────────────────────────────────────────────────┐
│                 GABRIEL (PO)                      │
│  Define escopo · Valida resultados · Redige o    │
│  artigo final · Integra referências legais       │
└──────────────────────┬──────────────────────────┘
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
  ┌──────────────────┐      ┌──────────────┐
  │ EQUIPE DE DADOS  │      │   EQ. ADS    │
  │   (2 pessoas)    │      │  (1 pessoa)  │
  │                  │      │              │
  │ Extraem dados    │      │ Dashboard    │
  │ dos XLSX         │      │ Power BI     │
  │ Geram GRÁFICOS   │      │ Visualizações│
  │ e TABELAS        │      │ interativas  │
  │ para cada        │      │              │
  │ PERGUNTA         │      │              │
  └──────────────────┘      └──────────────┘
     RESPONDEM                 VISUALIZAM
   AS PERGUNTAS              E APRESENTAM
```

---

## GABRIEL (PO) — Suas Responsabilidades

### O que você faz:
1. **Valida** toda entrega da equipe de dados (valores batem com o backlog?)
2. **Redige** o artigo final — Introdução, Metodologia, Resultados, Discussão e Conclusão
3. **Insere** as referências legais na narrativa (LBI, Decreto 5.296, e-MAG)
4. **Coordena** o cronograma e as entregas semanais
5. **Monta** os slides da apresentação

### Referências legais que você cita no texto:
| Dado | Lei | Artigo |
|---|---|---|
| 73,8% plataformas vs. 34% materiais acessíveis | LBI 13.146/2015 | Art. 63 (acessibilidade em sítios) |
| Hardware 19,6%, Software 15,9% | LBI | Art. 28, V e XIV (TI acessíveis) |
| Rural 4,1x menos aulas assistivas | LBI + CF | Art. 28 LBI + Art. 206 CF |
| Infra como pré-condição (33x gap) | Decreto 5.296/2004 | Art. 47 |
| Funil 43,5%→35,1% | LBI | Art. 67 (comunicações) |
| Google domina 59,4% | LBI | Art. 63 (plataformas públicas) |

### Sprint por sprint:
- **Sprint 1:** Validar extração de dados. Pesquisar bibliograficamente as leis (não fichamento extenso — citação direta no artigo).
- **Sprint 2:** Validar gráficos MUST HAVE. Dar GO.
- **Sprint 3:** Validar SHOULD/COULD. Iniciar redação (Introdução + Metodologia).
- **Sprint 4:** Finalizar artigo completo (ABNT), montar slides, revisão coletiva.

---
---

# EQUIPE DE DADOS (2 pessoas)

## Seu papel no projeto

Vocês são quem **responde às perguntas do projeto com dados**. Vão abrir os XLSX, extrair os dados relevantes, e gerar gráficos e tabelas que respondem cada pergunta do backlog.

**⚠️ IMPORTANTE: São tabelas de indicadores (dados agregados e ponderados), NÃO microdados. Cada aba = um indicador, cada linha = um segmento (Total, Região, Zona, etc.).**

**Ferramentas:**
- **Python** com **Pandas** + **openpyxl** (para ler Excel)
- **Matplotlib/Seaborn** (para gráficos)
- **Jupyter Notebook** (recomendado)

**Vocês NÃO precisam:**
- Pesquisar leis ou escrever texto acadêmico
- Criar modelos preditivos (impossível com esses dados)

---

## TAREFA 1 — Exploração e Entendimento da Estrutura (Sprint 1, dia 1-2)
**Conexão com o backlog:** Seção 0 (Natureza dos Dados)

### O que fazer:

**1.1 — Conferir os 3 arquivos na pasta do projeto**
```python
import pandas as pd
import os

pasta = '.'  # pasta do projeto
arquivos = [f for f in os.listdir(pasta) if f.endswith('.xlsx')]
print("Arquivos encontrados:")
for a in arquivos:
    print(f"  {a}")
```

Vocês devem encontrar:
- `tic_educacao_2024_escolas_tabela_proporcao_v1.0.xlsx` — **PRINCIPAL (percentuais)**
- `tic_educacao_2024_escolas_tabela_total_v1.0.xlsx` — Contagens absolutas
- `tic_educacao_2024_gestores_dicionario_de_variaveis_v1.0.xlsx` — Dicionário (referência)

**1.2 — Listar todas as abas do arquivo de proporção**
```python
xls = pd.ExcelFile('tic_educacao_2024_escolas_tabela_proporcao_v1.0.xlsx')
print(f"Total de abas: {len(xls.sheet_names)}")
for i, nome in enumerate(xls.sheet_names, 1):
    print(f"  {i:2d}. {nome}")
```

**1.3 — Entender a estrutura de UMA aba (D2 é a mais importante)**
```python
df_d2 = pd.read_excel(
    'tic_educacao_2024_escolas_tabela_proporcao_v1.0.xlsx',
    sheet_name='D2',
    header=None  # as primeiras linhas são cabeçalho irregular
)
print(df_d2.to_string())  # ver tudo
```

**Anotem e enviem ao Gabriel:**
- Quantas abas existem?
- Como é a estrutura de D2? (quantas linhas, quais colunas)
- Quais são os segmentos listados nas linhas?

---

## TAREFA 2 — Extração Padronizada de Todas as Abas (Sprint 1, dia 2-4)
**Conexão com o backlog:** Seção 1 (Mapeamento de Abas)

### O que fazer:

**2.1 — Função para extrair uma aba com estrutura padrão**

```python
import pandas as pd
import numpy as np

def extrair_aba(arquivo, nome_aba):
    """
    Extrai uma aba do Excel e retorna um DataFrame limpo.
    Adapte os skiprows e colunas conforme necessário.
    """
    df = pd.read_excel(arquivo, sheet_name=nome_aba, header=None)
    
    # ATENÇÃO: A estrutura exata pode variar por aba.
    # Geralmente: linha 0-2 = cabeçalho, linhas seguintes = dados
    
    print(f"\n=== Aba: {nome_aba} ===")
    print(f"Shape: {df.shape}")
    print(df.head(10).to_string())
    
    return df

# Abas que precisamos (do backlog):
ARQUIVO_PROP = 'tic_educacao_2024_escolas_tabela_proporcao_v1.0.xlsx'
ARQUIVO_TOTAL = 'tic_educacao_2024_escolas_tabela_total_v1.0.xlsx'

abas_necessarias = [
    'D1A', 'D2', 'D3A', 'D3B', 'D4', 'D5',    # CORE - Acessibilidade
    'G4', 'G4A',                                   # Plataformas
    'A1', 'A2', 'A3_1', 'A4',                     # Infraestrutura Internet
    'B1', 'B2',                                     # Dispositivos
    'C1',                                           # Locais com Internet
    'K1_1',                                         # Aquisição de PCs
]

# Explorar cada aba
for aba in abas_necessarias:
    try:
        extrair_aba(ARQUIVO_PROP, aba)
    except Exception as e:
        print(f"ERRO na aba {aba}: {e}")
```

**2.2 — Criar CSVs limpos para cada aba**

```python
def extrair_aba_limpa(arquivo, nome_aba, col_segmento=0, cols_dados=None, 
                       skip_rows=3, nomes_colunas=None):
    """
    Extrai uma aba e retorna DataFrame com segmentação + dados numéricos.
    """
    df = pd.read_excel(arquivo, sheet_name=nome_aba, header=None, 
                        skiprows=skip_rows)
    
    resultado = pd.DataFrame()
    resultado['Segmento'] = df.iloc[:, col_segmento].str.strip()
    
    if cols_dados and nomes_colunas:
        for col_idx, nome in zip(cols_dados, nomes_colunas):
            resultado[nome] = pd.to_numeric(df.iloc[:, col_idx], errors='coerce')
    
    resultado = resultado.dropna(subset=['Segmento'])
    resultado = resultado[resultado['Segmento'] != '']
    
    return resultado

# Salvar CSVs processados
os.makedirs('dados/processed', exist_ok=True)

# Para cada aba extraída:
# resultado.to_csv(f'dados/processed/{nome_aba}.csv', index=False, encoding='utf-8-sig')
```

**2.3 — Conferir os dados extraídos com os valores de referência**

| Indicador | Valor Nacional Esperado |
|---|---|
| D1A (% Sim) | 81,4% |
| D2 Hardware (% Sim) | 19,6% |
| D2 Software (% Sim) | 15,9% |
| D2 Aulas (% Sim) | 12,0% |
| D2 Materiais (% Sim) | 34,0% |
| D3A (% Sim) | 42,0% |
| D3B (% Sim) | 43,5% |
| D4 (% Sim) | 41,2% |
| D5 (% Sim) | 35,1% |
| G4A (% Sim) | 73,8% |
| A1 (% Sim) | 95,9% |
| B1 (% Sim) | 88,7% |

**Se algum valor NÃO bater, parem e avisem o Gabriel.**

**Enviar para Gabriel:** Todos os CSVs processados + confirmação de validação.

---

## TAREFA 3 — Responder as Perguntas MUST HAVE (Sprint 2)
**Conexão com o backlog:** Perguntas P1 a P6

Aqui vocês geram os gráficos que respondem as 6 perguntas obrigatórias do projeto.

---

### PERGUNTA P1 (US-1.1): "Digitalização vs. Acessibilidade — qual o gap nacional?"

**O que extrair:** G4A (TOTAL, coluna Sim) + D2 (TOTAL, 4 colunas Sim)

**Como gerar o gráfico:**
```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

indicadores = [
    'Usam ao menos uma\nplataforma digital\n(G4A)',
    'Materiais digitais\nacessíveis (D2)',
    'Hardware\nadaptado (D2)',
    'Software\nassistivo (D2)',
    'Aulas de informática\nassistiva (D2)'
]
valores = [73.84, 33.99, 19.59, 15.88, 12.01]
cores = ['#2196F3', '#4CAF50', '#FF9800', '#9C27B0', '#F44336']

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(indicadores, valores, color=cores, width=0.6)
for bar, val in zip(bars, valores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val:.1f}%', ha='center', fontsize=12, fontweight='bold')

ax.set_ylabel('Percentual das escolas (%)', fontsize=12)
ax.set_title('Digitalização vs. Acessibilidade nas Escolas Brasileiras (2024)\n'
             'Indicadores nacionais lado a lado — NÃO é cruzamento', fontsize=14)
ax.set_ylim(0, 90)
ax.axhline(y=0, color='gray', linewidth=0.5)

ax.text(0.5, -0.12, '⚠️ Cada barra vem de uma aba separada. Comparação contextual, não cruzamento.',
        transform=ax.transAxes, ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout()
plt.savefig('graficos/US1_1_panorama.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Resposta esperada:** "73,8% das escolas usam plataformas, mas o recurso assistivo mais presente (materiais digitais) atinge apenas 34%. Aulas de informática assistiva existem em apenas 12% das escolas."

---

### PERGUNTA P2 (US-1.2): "Qual a adoção por segmento? Onde estão os piores gaps?"

**O que extrair:** D2 completo — TODAS as 29 linhas, coluna "Sim" de cada recurso

**Como gerar o gráfico:**
```python
import seaborn as sns
import numpy as np

# Segmentos (29 linhas da aba D2)
segmentos = ['TOTAL', 'Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste',
             'Urbana', 'Rural', 'Capital', 'Interior',
             'Municipal', 'Estadual', 'Particular',
             'Até 50', '51-150', '151-300', '301-500', '501-1000', '1000+']

# Dados reais confirmados no backlog:
dados_heatmap = {
    'Hardware': [19.6, 13.5, 11.1, 29.0, 25.7, 31.8,
                 26.0, 8.2, 32.0, 17.6,
                 19.0, 26.5, 12.6,
                 2.2, 6.1, 21.4, 22.3, 45.1, 53.7],
    'Software': [15.9, 11.0, 8.7, 25.1, 18.9, 23.5,
                 21.5, 5.9, 25.0, 14.0,
                 14.8, 18.7, 14.6,
                 1.5, 2.3, 21.4, 22.9, 31.7, 31.6],
    'Aulas': [12.0, 9.3, 4.7, 17.9, 19.5, 22.4,
              16.6, 4.0, 18.0, 11.0,
              10.1, 12.0, 16.8,
              0.3, 5.1, 17.8, 13.9, 22.3, 25.0],
    'Materiais': [34.0, 17.7, 24.2, 48.8, 40.0, 53.5,
                  43.7, 16.8, 48.6, 31.7,
                  29.3, 37.2, 43.4,
                  6.2, 23.5, 38.5, 41.7, 60.4, 64.4],
}

df_heat = pd.DataFrame(dados_heatmap, index=segmentos)

fig, ax = plt.subplots(figsize=(10, 14))
sns.heatmap(df_heat, annot=True, fmt='.1f', cmap='RdYlGn', 
            linewidths=0.5, ax=ax, vmin=0, vmax=70,
            cbar_kws={'label': '% das escolas com o recurso'})
ax.set_title('Recursos de Tecnologia Assistiva por Segmento — D2 (% Sim)\n'
             'TIC Educação 2024', fontsize=14)
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('graficos/US1_2_heatmap_D2.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Resposta esperada:** "Materiais digitais são o recurso mais presente em todos os segmentos (34% nacional). Centro-Oeste lidera tudo. Gaps brutais: Rural tem 3,2x menos hardware; Porte até 50 tem 0,3% de aulas (vs. 25% no Porte 1000+ — gap de 83x)."

---

### PERGUNTA P3 (US-1.3): "Quantas escolas atendem alunos com deficiência?"

**O que extrair:** D1A completo

**Resposta esperada:** "81,4% das escolas têm alunos com deficiência. Rural: 65% vs. Urbana: 90,6%. Porte até 50: 39,6% vs. 1000+: 99%. Isso explica a coluna 'Não se aplica' de D2 (12,8% nacional)."

```python
# Gráfico de barras horizontal por segmento
# Usar mesmo padrão do heatmap com dados de D1A
# Salvar como graficos/US1_3_D1A.png
```

---

### PERGUNTA P4 (US-2.2): "Centro-Oeste realmente lidera?"

**O que extrair:** D2, linhas de REGIÃO (5 linhas), 4 colunas de recurso

**Como gerar:**
```python
regioes = ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']
media_nac = 19.6  # Hardware, por exemplo

hw_regiao = [13.5, 11.1, 29.0, 25.7, 31.8]

fig, ax = plt.subplots(figsize=(10, 5))
cores = ['#78909C' if r != 'Centro-Oeste' else '#FF5722' for r in regioes]
bars = ax.bar(regioes, hw_regiao, color=cores, width=0.5)
ax.axhline(y=media_nac, color='black', linestyle='--', linewidth=1, 
           label=f'Média Nacional ({media_nac}%)')

for bar, pct in zip(bars, hw_regiao):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{pct}%', ha='center', fontsize=12, fontweight='bold')

ax.set_ylabel('% com hardware adaptado')
ax.set_title('Hardware Assistivo por Região — Centro-Oeste Lidera\n(Aba D2, TIC Educação 2024)')
ax.legend()
ax.set_ylim(0, 45)
plt.tight_layout()
plt.savefig('graficos/US2_2_regiao_hardware.png', dpi=150)
plt.show()

# REPITAM para os outros 3 recursos ou façam barras agrupadas (4 × 5)
```

**Resposta esperada:** "Centro-Oeste LIDERA em todos os 4 recursos. Nordeste é o mais excluído (Hardware 11,1%, Aulas 4,7%). Norte também muito abaixo."

---

### PERGUNTA P5 (US-2.3): "Qual a desigualdade urbano-rural?"

**O que extrair:** D2, linhas Urbana e Rural

```python
recursos = ['Hardware', 'Software', 'Aulas', 'Materiais']
urbana = [26.0, 21.5, 16.6, 43.7]
rural = [8.2, 5.9, 4.0, 16.8]
gap = [f'{u/r:.1f}x' for u, r in zip(urbana, rural)]

x = range(len(recursos))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar([i - width/2 for i in x], urbana, width, label='Urbana', color='#2196F3')
bars2 = ax.bar([i + width/2 for i in x], rural, width, label='Rural', color='#FF5722')

for i, g in enumerate(gap):
    y_max = max(urbana[i], rural[i])
    ax.text(i, y_max + 2, f'Gap: {g}', ha='center', fontsize=10, fontweight='bold', color='red')

for bars, vals in [(bars1, urbana), (bars2, rural)]:
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{val}%', ha='center', fontsize=10)

ax.set_ylabel('% das escolas com o recurso')
ax.set_title('O Abismo Urbano-Rural na Acessibilidade Digital\n(Aba D2, TIC Educação 2024)')
ax.set_xticks(x)
ax.set_xticklabels(recursos)
ax.legend()
ax.set_ylim(0, 60)
plt.tight_layout()
plt.savefig('graficos/US2_3_urbano_rural.png', dpi=150)
plt.show()
```

**Resposta esperada:** "Gaps de 2,6x (materiais) a 4,1x (aulas). Escola rural tem aulas assistivas em apenas 4% dos casos vs. 16,6% na urbana."

---

### PERGUNTA P6 (US-3.1): "O funil da Sala de Recursos — quanta perda?"

**O que extrair:** D3B (43,5%), D4 (41,2%), D5 (35,1%) — linha TOTAL de cada

```python
estagios = ['Tem Sala de Recursos\nMultifuncionais\n(D3B)', 
            'Sala tem\nInternet\n(D4)', 
            'Aluno acessa\nInternet na Sala\n(D5)']
valores = [43.5, 41.2, 35.1]

fig, ax = plt.subplots(figsize=(8, 6))
cores = ['#4CAF50', '#FF9800', '#F44336']
bars = ax.barh(estagios[::-1], valores[::-1], color=cores[::-1], height=0.5)

for bar, val in zip(bars, valores[::-1]):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{val}%', va='center', fontsize=13, fontweight='bold')

ax.set_xlabel('% das escolas com Internet')
ax.set_title('Funil da Sala de Recursos Multifuncionais\n'
             'Perda progressiva do recurso ao acesso real do aluno\n'
             '(Base: escolas com Internet — TIC Educação 2024)', fontsize=13)
ax.set_xlim(0, 55)

ax.text(38, 0.5, f'Perda: {43.5-35.1:.1f} p.p.', fontsize=11, color='red', fontweight='bold')

plt.tight_layout()
plt.savefig('graficos/US3_1_funil_sala_recursos.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Resposta esperada:** "43,5% têm Sala → 41,2% com Internet na Sala → 35,1% onde o aluno acessa. Perda de 8,4 pontos percentuais. Quase 20% das escolas com Sala de Recursos 'perdem' o aluno entre ter e acessar."

**NOTA:** Este é o ÚNICO funil legítimo do projeto (mesma base amostral).

---

## TAREFA 4 — Responder as Perguntas SHOULD HAVE (Sprint 3)
**Conexão com o backlog:** Perguntas P7 a P11

### PERGUNTA P7 (US-2.1): "Municipal vs. Estadual vs. Particular?"

**Dados confirmados:**

| Recurso | Municipal | Estadual | Particular |
|---|---|---|---|
| Hardware | 19,0% | 26,5% | 12,6% |
| Software | 14,8% | 18,7% | 14,6% |
| Aulas | 10,1% | 12,0% | 16,8% |
| Materiais | 29,3% | 37,2% | 43,4% |

**Entrega:** `graficos/US2_1_dependencia.png`

---

### PERGUNTA P8 (US-2.5): "O tamanho da escola importa?"

**Dados confirmados — ACHADO MAIS DRAMÁTICO:**

| Porte | Hardware | Software | Aulas | Materiais |
|---|---|---|---|---|
| Até 50 | 2,2% | 1,5% | **0,3%** | 6,2% |
| 1000+ | 53,7% | 31,6% | **25,0%** | 64,4% |

Gap de **83x** em aulas assistivas.

```python
portes = ['Até 50', '51-150', '151-300', '301-500', '501-1000', '1000+']
hw_porte = [2.2, 6.1, 21.4, 22.3, 45.1, 53.7]

fig, ax = plt.subplots(figsize=(10, 5))
cores = plt.cm.RdYlGn(np.linspace(0.1, 0.9, len(portes)))
bars = ax.bar(portes, hw_porte, color=cores, width=0.6)

for bar, val in zip(bars, hw_porte):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{val}%', ha='center', fontsize=11, fontweight='bold')

ax.set_ylabel('% com hardware adaptado')
ax.set_title('Hardware Assistivo por Porte — Gap de 24x\n(Aba D2, TIC Educação 2024)')
ax.set_ylim(0, 65)

ax.annotate(f'Gap: {53.7/2.2:.0f}x', xy=(0, 2.2), xytext=(1.5, 45),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=14, fontweight='bold', color='red')

plt.tight_layout()
plt.savefig('graficos/US2_5_porte.png', dpi=150)
plt.show()
```

**Entrega:** `graficos/US2_5_porte.png`

---

### PERGUNTA P9 (US-2.7): "Internet+Computador é pré-condição?"

**Dados:**

| Recurso | Com Infra | Sem Infra | Gap |
|---|---|---|---|
| Hardware | 31,7% | 2,3% | 13,8x |
| Software | 26,0% | 1,5% | 17,3x |
| Aulas | 20,0% | 0,6% | **33,3x** |
| Materiais | 50,0% | 11,2% | 4,5x |

**Entrega:** `graficos/US2_7_infra.png` (mesmo padrão do urbano-rural)

---

### PERGUNTA P10 (US-4.1): "A Escadaria da Exclusão — todos os indicadores lado a lado"

```python
indicadores = [
    'Internet\n(A1)', 'Computador\n(B1)', 'Plataforma\n(G4A)',
    'Alunos PcD\n(D1A)', 'Materiais\nacessíveis\n(D2)',
    'Hardware\nassistivo\n(D2)', 'Software\nassistivo\n(D2)',
    'Aulas\nassistivas\n(D2)', 'Sala de\nRecursos\n(D3B)'
]
valores = [95.9, 88.7, 73.8, 81.4, 34.0, 19.6, 15.9, 12.0, 43.5]

# Ordenar do maior ao menor
pares = sorted(zip(valores, indicadores), reverse=True)
valores_ord = [p[0] for p in pares]
indicadores_ord = [p[1] for p in pares]

fig, ax = plt.subplots(figsize=(14, 6))
cores = ['#4CAF50' if v > 50 else '#FF9800' if v > 30 else '#F44336' for v in valores_ord]
bars = ax.bar(indicadores_ord, valores_ord, color=cores, width=0.6)

for bar, val in zip(bars, valores_ord):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val}%', ha='center', fontsize=11, fontweight='bold')

ax.set_ylabel('% das escolas')
ax.set_title('Escadaria da Exclusão Digital: Do Básico ao Inclusivo\n'
             '⚠️ Cada barra é um indicador independente — NÃO são estágios cumulativos',
             fontsize=13)
ax.set_ylim(0, 110)
plt.tight_layout()
plt.savefig('graficos/US4_1_escadaria.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Entrega:** `graficos/US4_1_escadaria.png`

---

### PERGUNTA P11 (US-1.5): "Quantas escolas nem são perguntadas?"

**Dados:** D2 coluna "Não se aplica" — Nacional 12,8%, Rural 35,2%, Porte até 50: 38,2%

**Entrega:** `graficos/US1_5_nsa.png` + texto explicativo para a Metodologia

---

## TAREFA 5 — Responder Perguntas COULD HAVE (Sprint 3, se der tempo)

Perguntas P12 a P19. Mesmo padrão: extrair, gerar gráfico, documentar resposta.
Foco em P12 (plataformas) e P18 (Google por segmento) se houver tempo.

---

## CHECKLIST FINAL — Equipe de Dados

Antes de enviar os resultados:

- [ ] Valores nacionais extraídos batem com a tabela de referência (Tarefa 2.3)?
- [ ] Todos os gráficos têm título, rótulos e legenda?
- [ ] Gráficos com indicadores de abas diferentes têm nota metodológica?
- [ ] O funil (P6) usa apenas D3B, D4, D5 (mesma base)?
- [ ] Gráficos salvos como PNG em alta resolução (dpi=150)?
- [ ] Notebooks com nomes claros? (01_extracao.ipynb, 02_epico1.ipynb, etc.)
- [ ] CSVs processados em `dados/processed/`?
- [ ] Para cada pergunta respondida: há um parágrafo-resposta documentado?

---
---

# EQUIPE ADS (1 pessoa)

## Seu papel no projeto

**⚠️ Com tabelas de indicadores, NÃO é possível criar modelos preditivos (ML).**

**Seu papel:** Construir o **Dashboard no Power BI** para a apresentação final. Você também pode criar visualizações interativas em Python (Plotly).

**Ferramentas:**
- **Power BI** (foco principal)
- **Python** com Plotly (opcional — gráficos interativos)

---

## TAREFA 1 — Receber e Organizar os Dados (Sprint 2)

### O que fazer:
- Receber os CSVs processados de `dados/processed/`
- Importar no Power BI
- Criar relacionamentos (todos os CSVs têm a coluna "Segmento" em comum)

---

## TAREFA 2 — Dashboard Power BI (Sprint 2-3)

### Páginas sugeridas:

**Página 1 — Panorama Nacional (P1)**
- 5 KPIs grandes: Internet (95,9%), Computador (88,7%), Plataformas (73,8%), Materiais (34%), Hardware (19,6%)
- Gráfico de barras: Digitalização vs. Acessibilidade

**Página 2 — Heatmap da Desigualdade (P2)**
- Heatmap ou matriz: 4 recursos × segmentos selecionáveis (filtro slicer)
- Filtros: Região, Zona, Dependência, Porte

**Página 3 — O Abismo Geográfico (P4, P5)**
- Barras agrupadas: Urbano vs. Rural (4 recursos)
- Barras por Região com linha de média nacional
- Barras por Porte (escadaria)

**Página 4 — Funil da Sala de Recursos (P6)**
- Gráfico de funil: D3B → D4 → D5
- Versão segmentada (se der tempo): funil por região ou zona

**Página 5 — Infraestrutura e Plataformas (P9, P12)**
- Internet (A1) por segmento
- Plataformas específicas (G4)

### Dicas Power BI:
```
- Importar CSVs via "Obter Dados > Texto/CSV"
- Usar "Segmento" como chave comum entre tabelas
- Os dados já vêm prontos como percentuais, não precisa calcular
- Usar slicers para filtrar por segmento
- Usar "Cartão" para KPIs
- Usar "Gráfico de Barras Agrupadas" para comparações
- Usar "Gráfico de Funil" para P6
```

---

## TAREFA 3 — Gráficos Interativos em Python (Opcional, Sprint 3)

```python
import plotly.graph_objects as go

# Funil interativo
fig = go.Figure(go.Funnel(
    y=["Sala de Recursos (D3B)", "Internet na Sala (D4)", "Aluno Acessa (D5)"],
    x=[43.5, 41.2, 35.1],
    textinfo="value+percent initial"
))
fig.update_layout(title="Funil da Sala de Recursos Multifuncionais")
fig.show()
fig.write_html("graficos/funil_interativo.html")
```

---

## CHECKLIST FINAL — ADS

- [ ] Dashboard Power BI tem pelo menos 4 páginas?
- [ ] KPIs corretos (batem com valores do backlog)?
- [ ] Filtros (slicers) funcionam?
- [ ] Funil da Sala de Recursos incluído?
- [ ] Notas metodológicas onde necessário?
- [ ] Arquivo salvo como `powerbi/dashboard.pbix`?

---
---

# COMO TUDO SE CONECTA — Fluxo de Entrega

```
SEMANA 1 (Sprint 1)         SEMANA 2 (Sprint 2)
========================     ========================
DADOS:                       DADOS:
  Explora XLSX ──────────►     Gráficos MUST HAVE
  Extrai CSVs                  (P1, P2, P3, P4, P5, P6)
  Valida com Gabriel           │
                               ▼
ADS:                         ADS:
  Estuda Power BI ──────►     Dashboard v1
                               (recebe CSVs)
                               
GABRIEL:                     GABRIEL:
  Valida extração              Valida gráficos
  Pesquisa leis                GO para Sprint 3


SEMANA 3 (Sprint 3)         SEMANA 4 (Sprint 4)
========================     ========================
DADOS:                       DADOS:
  Gráficos SHOULD+COULD       Revisão final
  (P7-P11 + P12-P19)
                             
ADS:                         ADS:
  Dashboard com heatmap,       Dashboard final (.pbix)
  funil, escadaria
                             
GABRIEL:                     GABRIEL:
  Valida análises              Artigo ABNT + Slides
  Inicia redação               Revisão + Ensaio
```

---

# COMO ORGANIZAR O RESULTADO FINAL

## Passo a passo para montar o artigo

Quando TODAS as perguntas estiverem respondidas (gráficos + textos), organize assim:

### Capítulo 1 — INTRODUÇÃO
**Objetivo:** Convencer o leitor de que o problema importa.

**Conteúdo:**
- Contexto da digitalização pós-pandemia
- Dado-gancho: "73,8% das escolas usam plataformas, mas apenas 12% têm aulas de informática assistiva"
- Pergunta central: "A inclusão digital acompanhou a digitalização?"
- Justificativa: Educação Inclusiva como tema do projeto de extensão

**Responsável:** Gabriel (PO)

---

### Capítulo 2 — REFERENCIAL TEÓRICO
**Objetivo:** Mostrar que a lei OBRIGA acessibilidade.

**Conteúdo:**
- Lei Brasileira de Inclusão (13.146/2015) — Art. 28, 63, 67
- Decreto 5.296/2004 — Art. 47
- Portaria MEC 3.284/2003
- Modelo e-MAG
- Conceitos: Tecnologia assistiva, Desenho Universal

**Como fazer:** Pesquisa direta nos sites oficiais. Citar os artigos relevantes e explicar em linguagem do projeto.

**Responsável:** Gabriel (PO) — pesquisa bibliográfica + redação

---

### Capítulo 3 — METODOLOGIA
**Objetivo:** Explicar como investigamos e ser TRANSPARENTE sobre limitações.

**Conteúdo obrigatório:**
1. Fonte: TIC Educação 2024 (Cetic.br, módulo Gestores, amostra nacional)
2. Tipo: Tabelas de indicadores AGREGADOS (não microdados)
3. Estrutura: 69 abas, ~29 segmentos, percentuais já ponderados
4. Técnica: Análise descritiva comparativa + leitura paralela de indicadores
5. O que NÃO podemos fazer: cruzamento entre abas, ML, variáveis derivadas
6. "Não se aplica": 12,8% nacional, 35,2% rural — influencia interpretação
7. Único funil legítimo: D3B → D4 → D5

**Responsável:** Gabriel (PO) — com dados técnicos da equipe de Dados

---

### Capítulo 4 — RESULTADOS
**Objetivo:** Apresentar as respostas de cada pergunta com gráficos.

A ordem segue impacto narrativo crescente:

**4.1 — O Retrato Nacional (Setup)**
| Pergunta | Gráfico | Arquivo |
|---|---|---|
| P1: Digitalização vs. Acessibilidade | Barras comparativas | US1_1_panorama.png |
| P3: Escolas com alunos PcD | Barras por segmento | US1_3_D1A.png |
| P11: "Não se aplica" | Barras por segmento | US1_5_nsa.png |

**Transição:** "73,8% digitalizaram, mas materiais acessíveis atingem 34%. E 81% têm alunos PcD. Onde estão as maiores desigualdades?"

**4.2 — O Heatmap da Desigualdade (Revelação)**
| Pergunta | Gráfico | Arquivo |
|---|---|---|
| P2: Heatmap D2 completo | Heatmap 29×4 | US1_2_heatmap_D2.png |
| P4: Regiões | Barras agrupadas | US2_2_regioes.png |
| P5: Urbano-Rural | Barras lado a lado | US2_3_urbano_rural.png |
| P8: Porte | Barras com gap | US2_5_porte.png |

**Transição:** "Centro-Oeste lidera. Norte/Nordeste excluídos. Rural 4x menos. Porte até 50: 83x menos. Mas existe uma barreira AINDA mais básica..."

**4.3 — A Barreira Prévia (Contexto Estrutural)**
| Pergunta | Gráfico | Arquivo |
|---|---|---|
| P9: Infra como pré-condição | Barras com gap | US2_7_infra.png |
| P10: Escadaria da Exclusão | Barras descendentes | US4_1_escadaria.png |

**Transição:** "E quando a escola TEM infraestrutura e TEM Sala de Recursos, os alunos realmente acessam?"

**4.4 — O Funil (Clímax)**
| Pergunta | Gráfico | Arquivo |
|---|---|---|
| P6: Funil da Sala de Recursos | Funnel chart | US3_1_funil.png |

**Impacto:** "Quase 20% das escolas que TÊM Sala de Recursos 'perdem' o aluno entre ter a sala e ele acessar a Internet nela."

---

### Capítulo 5 — DISCUSSÃO
**Objetivo:** Confrontar dados com leis.

**Conteúdo:**
Para cada resultado principal, citar a lei correspondente:

| Dado | Argumento | Lei |
|---|---|---|
| 73,8% plataformas vs. 34% materiais | Digitalização sem inclusão descumpre Art. 63 LBI | LBI 13.146/2015 |
| Rural 4,1x menos aulas assistivas | Desigualdade viola igualdade de condições | Art. 28 LBI + Art. 206 CF |
| Porte até 50: 0,3% aulas assistivas | Escolas pequenas excluídas | Art. 28, XIV LBI |
| Funil: 43,5% → 35,1% | Inefetividade da Sala de Recursos | Art. 67 LBI |
| Sem infra: 33x menos aulas | Infra como pré-condição | Decreto 5.296, Art. 47 |
| Google 59,4% monopolista | Acessibilidade de plataforma dominante | Art. 63 LBI |

**Responsável:** Gabriel (PO)

---

### Capítulo 6 — CONCLUSÃO E RECOMENDAÇÕES
**Objetivo:** Transformar achados em ações.

**4 Recomendações de Política Pública:**
1. **Infraestrutura ANTES de digitalizar** — Sem Internet+PC, acessibilidade é zero (P9)
2. **Políticas focalizadas em rurais e pequenas** — Gaps de 4,1x e 83x (P5, P8)
3. **Auditoria de acessibilidade no Google** — 59,4% das escolas dependem dele (P12)
4. **Internet real na Sala de Recursos** — Perda de 8,4 pp no funil (P6)

**Sugestões para pesquisa futura:** O que estes dados NÃO respondem (Seção 9 do backlog)

---

## Regra de Comunicação

| Situação | O que fazer |
|---|---|
| Terminei minha tarefa da semana | Avise no grupo do WhatsApp + envie o arquivo |
| Estou travado | Avise o Gabriel IMEDIATAMENTE (não espere a quarta) |
| Encontrei algo estranho nos dados | Anote + print → envie ao Gabriel |
| Não entendi o que fazer | Releia este guia. Se continuar com dúvida, pergunte no grupo |
| Quero mudar algo do escopo | PERGUNTE ANTES |

## Nomenclatura de Arquivos

```
ProjetoExtensao2/
├── dados/
│   ├── raw/                         ← XLSX originais (NÃO MEXER)
│   │   ├── tic_educacao_2024_escolas_tabela_proporcao_v1.0.xlsx
│   │   ├── tic_educacao_2024_escolas_tabela_total_v1.0.xlsx
│   │   └── tic_educacao_2024_gestores_dicionario_de_variaveis_v1.0.xlsx
│   └── processed/                   ← CSVs extraídos e limpos
│       ├── D1A.csv
│       ├── D2.csv
│       └── ...
├── notebooks/
│   ├── 01_extracao_xlsx.ipynb       ← Equipe de Dados
│   ├── 02_epico1_retrato.ipynb      ← Equipe de Dados
│   ├── 03_epico2_abismo.ipynb       ← Equipe de Dados
│   ├── 04_epico3_funil.ipynb        ← Equipe de Dados
│   ├── 05_epico4_paralelo.ipynb     ← Equipe de Dados
│   └── 06_visualizacoes_plotly.ipynb ← ADS (opcional)
├── graficos/                        ← PNGs gerados
├── docs/
│   └── artigo_final.docx            ← Gabriel
├── powerbi/
│   └── dashboard.pbix               ← ADS
├── BACKLOG_PROJETO.md
├── GUIA_TAREFAS_EQUIPE.md
└── RESUMO_TRELLO.md
```
