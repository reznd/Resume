from turtle import width
import streamlit as st
from tkinter import Button
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Gabriel Rezende Teixeira
##### *Resume* 
''')
image = Image.open('eu_atual.png')
st.image(image, width=150)
st.markdown('## Sobre', unsafe_allow_html=True)
st.info('''
- ***Idade***: 22 Anos.
- ***Nacionalidade***: Brasileiro.
- ***Telefone***: 64 98419-1775
- ***Cidade***: Rio Verde - Goiás
- Entusiasta em trabalhar com coisas novas, desafios para mim são presentes que devem ser vistos como uma nova oportunidade de aprender.

''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000000;">
  <a class="navbar-brand" href="https://www.instagram.com/reznd3/" target="_blank">Gabriel Rezende</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Formação</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Experiência de Trabalho</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Redes Sociais</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Formação
''')
txt('**Técnico em eletroeletrônica** , *SESI SENAI*, Rio verde - Goiás',
'2014-2016')
txt('**Inglês Avançado**, *SENAC*,Rio Verde - Goiás','2010-2016')
txt('**User Experience**, *FIAP-Centro Universitário*' ,'2021')
txt('**Acadêmico em Ciência da Computação** (8 Periodo), *IF Goiano*, Rio Verde - Goiás',
'2017- Presente')

#####################
st.markdown('''
## Experiência de trabalho
''')

txt('**Estágio - Suporte T.I - SESI-SENAI**',
'2018-2020')
st.markdown('''
- Prestando apoio para mais de 30 colaboradores em toda parte de tecnologia da informação desde questões de hardware quantos de softwares e também em relação a problemas de infra e redes.
''')

txt('**Estágio - Analista de Suporte em Banco de Dados**, *ALIARE*, Rio Verde - Goiás',
'2021-2021')
st.markdown('''
- Prestando serviço de apoio em toda área de Banco de Dados e Aplicação do ERP Agrimanager, ajudando vários clientes por todo Brasil.
''')
txt('**Analista de Suporte em Banco de Dados**, *ALIARE*, Rio Verde - Goiás',
'2021-Presente')
st.markdown('''
- Apoio a mais de 20 Analitas de Suporte, resolução de problemas relacionado a Banco de Dados SQL Server, Instalação do banco de dados SQL Server, consultas personalizadas com modelagem de dados SQL, instalação de API, implantação do Sistema, implantação de Sistema Integrado de Balanças Rurais, Edição de relatórios, testes de versão, análise de infraestrutura em servidores, Análise de lentidão em banco de dados, update via banco de dados Oracle/Firebird.
''')

#####################
st.markdown('''
## Hard Skills
''')
txt3('Idiomas', '`Inglês Avançado`')
txt3('Programação ', '`Python`, `R`, `C`')
txt3('Processamento de dados', '`SQL`,`R`')
txt3('Bancos de dados', '`SQL Server`,`Oracle`,`Firebird`')
txt3('Desenvolvimento WEB', '`HTML`, `CSS`, `BOOTSTRAP`')
txt3('UI UX', '`Figma`,`Web Interfaces`,`APPs Interfaces`, `Protótipos`')

st.markdown('''
## Soft Skills
''')
txt3('Soft Skills', '`Trabalhar sobre pressão`,`Trabalho em equipe`, `Comucativo`, `Resolução de problemas`,`Colaboração`,`Força de vontade e esforço`,`Capacidade de Organização`,`Dedicação`')

#####################
st.markdown('''
## Redes Socias
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/gabriel-rezend3/')
txt2('GitHub', 'https://github.com/reznd')

