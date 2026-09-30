import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Estoque PRO",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "estoque.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1553413077-190dd305871c"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_ESTOQUE = (
    "https://images.unsplash.com/"
    "photo-1586528116311-ad8dd3c8310d"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F0F0E5 0%,
            #E1E4C8 50%,
            #D4DCB5 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #162630,
            #223944
        );

    border-right:
        2px solid #77864B;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #BFCB9C !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #26311F !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #46513B !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(14,28,38,0.97) 0%,
            rgba(14,28,38,0.86) 45%,
            rgba(14,28,38,0.18) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #A4D080 !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #E8EDDE !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #6E8040;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(111,128,63,0.30);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #26311F !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #566248 !important;

    margin-top: 5px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #152631,
            #233C48
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #E2E9DA !important;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.85);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #B8C391;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}


/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #26311F !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #202820 !important;

    -webkit-text-fill-color:
        #202820 !important;

    border:
        2px solid #7C8956 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #556B2F !important;

    box-shadow:
        0 0 0 3px rgba(85,107,47,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #6A7060 !important;
    opacity: 1 !important;
}


/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {
    background-color: #2F323C !important;

    border:
        2px solid #687548 !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #A4B66A !important;
}


/* =========================================================
MENU SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #2F323C !important;
}

[data-baseweb="menu"] {
    background-color: #2F323C !important;
}

[role="option"] {
    background-color: #2F323C !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #52632D !important;

    color: #FFFFFF !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #52632D,
            #788B48
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(82,99,45,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #3E4E23,
            #647738
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #B8C391;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #536044 !important;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Produto",
        "Categoria",
        "Código",
        "Quantidade",
        "Estoque Mínimo",
        "Preço de Compra",
        "Preço de Venda",
        "Fornecedor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# =========================================================
# GARANTIR COLUNAS
# =========================================================

colunas_necessarias = [
    "Produto",
    "Categoria",
    "Código",
    "Quantidade",
    "Estoque Mínimo",
    "Preço de Compra",
    "Preço de Venda",
    "Fornecedor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""


# =========================================================
# CONVERSÃO DOS VALORES
# =========================================================

df["Quantidade"] = pd.to_numeric(
    df["Quantidade"],
    errors="coerce"
).fillna(0)

df["Estoque Mínimo"] = pd.to_numeric(
    df["Estoque Mínimo"],
    errors="coerce"
).fillna(0)

df["Preço de Compra"] = pd.to_numeric(
    df["Preço de Compra"],
    errors="coerce"
).fillna(0)

df["Preço de Venda"] = pd.to_numeric(
    df["Preço de Venda"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
📦 Estoque PRO
</div>

<div class="logo-subtitle">
GESTÃO INTELIGENTE DE ESTOQUE
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Produto",
        "📦 Produtos Cadastrados"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "Estoque PRO • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Seu estoque.<br>
Seu controle.
</div>

<div class="hero-text">
Tenha todos os seus produtos organizados em um único lugar.
Controle quantidades, valores, fornecedores e níveis de estoque
de forma simples, rápida e profissional.
</div>

<div class="hero-badge">
📦 GESTÃO INTELIGENTE
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
"""
<div class="page-title">
📊 Visão geral do estoque
</div>

<div class="page-subtitle">
Acompanhe seus produtos e mantenha seu estoque organizado.
</div>
""",
        unsafe_allow_html=True
    )


    # =====================================================
    # MÉTRICAS
    # =====================================================

    total_produtos = len(df)

    quantidade_total = df["Quantidade"].sum()

    valor_estoque = (
        df["Quantidade"] *
        df["Preço de Compra"]
    ).sum()


    produtos_baixos = len(
        df[
            df["Quantidade"] <=
            df["Estoque Mínimo"]
        ]
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
📦
</div>

<div class="card-number">
{total_produtos}
</div>

<div class="card-label">
PRODUTOS CADASTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🔢
</div>

<div class="card-number">
{quantidade_total:,.0f}
</div>

<div class="card-label">
UNIDADES EM ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_estoque:,.2f}
</div>

<div class="card-label">
VALOR DO ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
⚠️
</div>

<div class="card-number">
{produtos_baixos}
</div>

<div class="card-label">
ESTOQUE BAIXO
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # =====================================================
    # BLOCO INFORMATIVO
    # =====================================================

    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
🚀 Controle profissional
</h2>

<p>
O Estoque PRO permite manter todos os seus produtos
organizados em um único lugar.
</p>

<p>
Cadastre produtos, acompanhe quantidades, controle
valores e identifique rapidamente itens que precisam
ser repostos.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_ESTOQUE,
            use_container_width=True
        )


# =========================================================
# CADASTRAR PRODUTO
# =========================================================

elif menu == "➕ Cadastrar Produto":

    st.markdown(
"""
<div class="page-title">
➕ Novo produto
</div>

<div class="page-subtitle">
Adicione um novo produto ao seu Estoque PRO.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_produto",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            produto = st.text_input(
                "📦 Nome do Produto"
            )

            categoria = st.selectbox(
                "🏷️ Categoria",
                [
                    "Alimentos",
                    "Bebidas",
                    "Eletrônicos",
                    "Informática",
                    "Roupas",
                    "Casa",
                    "Higiene",
                    "Ferramentas",
                    "Automotivo",
                    "Outros"
                ]
            )

            codigo = st.text_input(
                "🔢 Código do Produto"
            )

            quantidade = st.number_input(
                "📊 Quantidade",
                min_value=0,
                value=0,
                step=1
            )

            estoque_minimo = st.number_input(
                "⚠️ Estoque Mínimo",
                min_value=0,
                value=5,
                step=1
            )


        with col2:

            preco_compra = st.number_input(
                "💰 Preço de Compra",
                min_value=0.0,
                value=0.0,
                step=1.0
            )

            preco_venda = st.number_input(
                "💵 Preço de Venda",
                min_value=0.0,
                value=0.0,
                step=1.0
            )

            fornecedor = st.text_input(
                "🏢 Fornecedor"
            )

            observacoes = st.text_area(
                "📝 Observações"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR PRODUTO"
        )


    if cadastrar:

        if (
            produto.strip()
            and codigo.strip()
        ):

            novo_produto = pd.DataFrame(
                [{
                    "Produto": produto.strip(),
                    "Categoria": categoria,
                    "Código": codigo.strip().upper(),
                    "Quantidade": int(quantidade),
                    "Estoque Mínimo": int(estoque_minimo),
                    "Preço de Compra": float(preco_compra),
                    "Preço de Venda": float(preco_venda),
                    "Fornecedor": fornecedor.strip(),
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_produto
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "📦 Produto cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha o nome e o código do produto."
            )


# =========================================================
# PRODUTOS CADASTRADOS
# =========================================================

elif menu == "📦 Produtos Cadastrados":

    st.markdown(
"""
<div class="page-title">
📦 Meu estoque
</div>

<div class="page-subtitle">
Consulte e pesquise todos os produtos cadastrados.
</div>
""",
        unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
📦 Nenhum produto cadastrado
</h2>

<p>
Seu estoque ainda está vazio.
Cadastre seu primeiro produto para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    else:

        # =================================================
        # PESQUISA
        # =================================================

        busca = st.text_input(
            "🔎 Pesquisar produto",
            placeholder="Digite produto, categoria, código ou fornecedor..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        # =================================================
        # ALERTA DE ESTOQUE
        # =================================================

        estoque_baixo = df_filtrado[
            df_filtrado["Quantidade"] <=
            df_filtrado["Estoque Mínimo"]
        ]


        if not estoque_baixo.empty:

            st.warning(
                f"⚠️ Existem {len(estoque_baixo)} "
                "produto(s) com estoque baixo."
            )


        # =================================================
        # TABELA
        # =================================================

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        # =================================================
        # EXCLUSÃO
        # =================================================

        opcoes_produtos = df.index.tolist()


        produto_excluir = st.selectbox(
            "🗑️ Selecione um produto para excluir",
            options=opcoes_produtos,
            format_func=lambda indice:
                f"{df.loc[indice, 'Produto']} "
                f"- {df.loc[indice, 'Código']}"
        )


        if st.button(
            "🗑️ EXCLUIR PRODUTO"
        ):

            df = df.drop(
                produto_excluir
            )

            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "📦 Produto excluído com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

📦 Estoque PRO<br>
Gestão inteligente de estoque

</div>
""",
    unsafe_allow_html=True
)
