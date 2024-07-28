import streamlit as st

st.set_page_config(
    page_title = "Pullebyte - Análises",
    layout = "wide",
    menu_items = {
        'About': "Analise realizada da champions league com base nos datasets disponiveis no kaggle referente as temporadas <= 2022"
    }
)

nome = st.text_input('Digite o seu nome:')
if nome == '':
    st.markdown('O STREAMLIT RODOU!')
else:
    st.markdown(f'''
        Oi, <b style="color:#0033FF; text-transform:uppercase">{nome}</b>.<br>
        O STREAMLIT RODOU!<br>
        E ele aceita <code>HTML</code> e <code>CSS</code>!
    ''', unsafe_allow_html=True)
