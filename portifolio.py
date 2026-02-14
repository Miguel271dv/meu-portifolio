import streamlit as st

st.set_page_config(page_title="Miguel - Portifólio", page_icon="🚀")

st.title("🚀 Miguel - Desenvolvedor Python")
st.divider()

st.header("📌Sobre mim")

st.write("""
Sou estudante de Python focado em desenvolvimento backend. Tenho experiência com validação de dados, git e deploy na web.
""")

st.divider()

st.header("💻 Projetos")

st.subheader("📋 Sistema de Cadastro de Clientes")

st.write("""
-Validação de nome e endereço.
-Bloqueio de datas futuras.
-Armazenamento em CSV.
-Deploy online com Streamlit.         
""")

st.link_button("🔗 Ver projeto online", "https://python-cadastro-1.onrender.com/")

with st.container():
    st.subheader("Sistema de cadastro de clientes")
    st.write(""
    "Este projetos consiste em um simples cadastro, você pode botar sua data de nascimento, nome, endereço e se és pessoa física ou jurídica, feito inteiramente em streamlit(Python)."
    "")

st.divider()

st.header("🛠 Tecnologias")

st.write("""
-Python.
-Streamlit.
-GitHub  
""")
st.divider()

st.header("✉ Contato")

st.write("Email: miguel.araujo.de.vargas.2013@gmail.com")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Projetos", "1")
with col2:
    st.metric("Linguagens", "1")
    
    st.divider()
    