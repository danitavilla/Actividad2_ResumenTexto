#Carga de librerias necesarias
import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Descarga de NLTK tokenizers para el idioma espanol.
nltk.download('punkt', quiet=True, raise_on_error=True, download_dir='nltk_data')
nltk.data.path.append("nltk_data")

#Asignamos un nombre a la aplicacion y seleccionamos un icono
st.set_page_config(page_title="Herramienta de Resumen de Texto", page_icon="📝")

#Agregamos un titulo a la pagina
st.title("Herramienta de Resumen de Texto")

# Agregamos un widget para que el usuario agregue el texto que desea resumir
text = st.text_area("Agrega el texto aqui:")

# Agregamos un "slider widget" para que el usuario puede seleccionar el numero de frases en el resumen
num_frases = st.slider("Numero de frases en el resumen", min_value=1, max_value=10, value=3)

# Agregamos un boton para generar el resumen
if st.button("Resumen"):
    # Confirmamos si el usuario a agregado el texto
    if text:
        # Parseamos el texto
        parser = PlaintextParser.from_string(text, Tokenizer("spanish"))

        # SResumimos el texto usando LSA (Latent Semantic Analysis)
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, num_frases)

        # Convertimos el resumen de las frases en un unico texto
        summarized_text = " ".join(str(sentence) for sentence in summary)

        # Mostramos el texto resumido
        st.subheader("Texto Resumido:")
        st.write(summarized_text)
    else:
        st.warning("Por favor, ingresa un texto para resumir.")
