import streamlit as st

st.set_page_config(page_title="Miguel - Portifólio", page_icon="🚀")

# ================== Título ==================
st.title("🚀 Miguel - Desenvolvedor Python")
st.divider()

# ================== Sobre ==================
st.header("📌Sobre mim")
st.write("""
Sou estudante de Python focado em desenvolvimento backend. Tenho experiência com validação de dados, git e deploy na web.
""")
st.divider()

# ================== Projetos ==================
st.header("💻 Projetos")

# Projeto 1 - Controle Financeiro PRO
st.subheader("💰 Controle Financeiro PRO")
st.write("""
- Cadastro de receitas e despesas
- Sistema de login simples
- Dashboard com gráficos de despesas por categoria
- Deploy online com Streamlit
""")
st.link_button("🔗 Ver projeto online", "https://controle-financas-3.onrender.com/")
with st.container():
    st.subheader("Controle Financeiro PRO")
    st.write("""
Este projeto é um sistema financeiro completo, onde é possível:
- Criar contas de usuário e fazer login
- Adicionar receitas e despesas em diferentes categorias
- Visualizar gráficos com total de despesas por categoria
- Salvar e carregar dados do usuário automaticamente
""")
st.divider()

# Projeto 2 - Sistema de Cadastro de Clientes
st.subheader("📋 Sistema de Cadastro de Clientes")
st.write("""
- Validação de nome e endereço
- Bloqueio de datas futuras
- Armazenamento em CSV
- Deploy online com Streamlit         
""")
st.link_button("🔗 Ver projeto online", "https://python-cadastro-1.onrender.com/")
with st.container():
    st.subheader("Sistema de cadastro de clientes")
    st.write("""
Este projeto consiste em um simples cadastro, você pode informar sua data de nascimento, nome, endereço e se é pessoa física ou jurídica, feito inteiramente em Streamlit (Python).
""")
st.divider()

# ================== Tecnologias ==================
st.header("🛠 Tecnologias")
st.write("""
- Python
- Streamlit
- GitHub  
""")
st.divider()

# ================== Contato ==================
st.header("✉ Contato")
st.write("Email: miguel.araujo.de.vargas.2013@gmail.com")
st.divider()

# ================== Métricas ==================
col1, col2 = st.columns(2)
with col1:
    st.metric("Projetos", "2")
with col2:
    st.metric("Linguagens", "1")
    
st.divider()
