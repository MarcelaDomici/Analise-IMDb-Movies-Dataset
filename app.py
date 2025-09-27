import streamlit as st

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================
st.set_page_config(page_title="Análise de Filmes - MovieScope", layout="wide")

# ==============================
# TÍTULO
# ==============================
st.title("🎬 MovieScope - Análise de Filmes")
st.write("Explorando padrões de sucesso e prevendo avaliações com base em dados históricos (IMDb / TMDb 5000).")

# ==============================
# 1. CENÁRIO
# ==============================
st.header("📌 Cenário")
st.write("""
A indústria do cinema tem produzido milhares de filmes ao longo das últimas décadas, 
e as plataformas de streaming se tornaram o principal meio de consumo. 
Com isso, empresas como a **MovieScope** buscam entender quais fatores influenciam 
o sucesso de um filme.

Nesta análise, utilizamos o dataset **IMDb Movies (TMDb 5000)** para:
- Explorar padrões nos dados
- Identificar tendências
- Criar um modelo preditivo para avaliação média
""")

# ==============================
# 2. PERGUNTAS
# ==============================
st.header("❓ Perguntas de Pesquisa")
st.write("""
- Quais são os gêneros mais produzidos ao longo dos anos?  
- Como evoluiu a produção cinematográfica por década?  
- Filmes mais populares recebem melhores avaliações?  
- Existe diferença de orçamento entre os principais gêneros?  
- O modelo de regressão linear consegue prever a nota média de um filme?  
""")

# ==============================
# 3. ANÁLISES (GRÁFICOS COMO IMAGENS)
# ==============================
st.header("📊 Análises Exploratórias")

# histograma
col1, col2 = st.columns(2)
with col1:
    st.subheader("Top 10 Gêneros Mais Produzidos")
    st.image("graficos/top_genres.png")

with col2:
    st.subheader("Número de Filmes por Década")
    st.image("graficos/filmes_por_decada.png")

# Dispersao
col3, col4 = st.columns(2)
with col3:
    st.subheader("Popularidade vs Nota Média")
    st.image("graficos/popularidade_vs_nota.png")

with col4:
    st.subheader("Popularidade vs Nota Média")
    st.image("graficos/popularidade_vs_nota_Pouco.png")

# boxplot
col5, col6 = st.columns(2)
with col5:
    st.subheader("Orçamento por Gênero (Top 5)")
    st.image("graficos/orcamento_genero.png")


with col6:
    st.subheader("Popularidade nas Últimas 3 Décadas")
    st.image("graficos/popularidade_decada.png")

# Barras
col7, col8 = st.columns(2)
with col7:
    st.subheader("Top 10 Gêneros Mais Produzidos")
    st.image("graficos/top_generos.png")


with col8:
    st.subheader("Número de Filmes por Década")
    st.image("graficos/numero_decada.png")


# ==============================
# 4. MODELOS
# ==============================
st.header("🤖 Modelo Preditivo")
st.write("""
Criamos um modelo de **Regressão Linear** para prever a nota média (`vote_average`) 
com base em:
- Orçamento  
- Receita  
- Popularidade  
- Número de votos
""")

st.write("📊 **Resultados:**")
st.write("""
- **MSE:** 1.194  
- **RMSE:** 1.093  
- **R²:** 0.208
""")


# ==============================
# 5. CONCLUSÕES
# ==============================
st.header("📌 Conclusões")
st.write("""
- A produção de filmes cresceu significativamente nas últimas décadas.  
- Alguns gêneros dominam o mercado (Ação, Drama, Comédia).  
- Filmes populares não necessariamente têm melhores notas há títulos muito populares, mas avaliados de forma mediana. 
- O modelo de regressão linear apresentou baixo poder preditivo (R² ≈ 0.21), indicando que outros fatores além dos dados numéricos influenciam a nota.
""")

# ==============================
# 6. SUGESTÕES DE NEGÓCIO
# ==============================
st.header("💡 Sugestões de Negócio")
st.write("""
1. **Investir em análises qualitativas** (ex.: impacto do elenco, direção, crítica), pois os números sozinhos não explicam o sucesso.  
2. **Aproveitar tendências históricas** de gêneros e décadas para orientar produções futuras e sugerir conteúdos ao público.  
""")
