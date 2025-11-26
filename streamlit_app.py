import streamlit as st
import random
import string

# -----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Generador de Contraseñas",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# ESTILOS PERSONALIZADOS
# -----------------------------
st.markdown("""
    <style>
    .title {
        font-size: 42px;
        font-weight: 900;
        text-align: center;
        color: #4A90E2;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #555;
        margin-bottom: 30px;
    }

    .result-box {
        background: linear-gradient(135deg, #4A90E2, #005BBB);
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 24px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .copy-btn button {
        width: 100%;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        padding: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# TÍTULOS
# -----------------------------
st.markdown("<div class='title'>🔐 Generador de Contraseñas</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Crea contraseñas seguras, visuales y personalizadas</div>", unsafe_allow_html=True)

# -----------------------------
# CONTROLES
# -----------------------------
st.write("### ⚙️ Personaliza tu contraseña:")

col1, col2 = st.columns(2)

with col1:
    length = st.slider("🔢 Longitud", 6, 40, 16)

with col2:
    include_symbols = st.checkbox("🧩 Incluir símbolos (!@#$%)", True)

include_upper = st.checkbox("🔡 Incluir mayúsculas (A-Z)", True)
include_numbers = st.checkbox("🔢 Incluir números (0-9)", True)
include_lower = st.checkbox("🔠 Incluir minúsculas (a-z)", True)

# -----------------------------
# GENERADOR
# -----------------------------
def generar_contraseña():
    caracteres = ""

    if include_lower:
        caracteres += string.ascii_lowercase
    if include_upper:
        caracteres += string.ascii_uppercase
    if include_numbers:
        caracteres += string.digits
    if include_symbols:
        caracteres += "!@#$%&*+-/?"

    if caracteres == "":
        return "⚠ Debes seleccionar al menos una categoría."

    contraseña = "".join(random.choice(caracteres) for _ in range(length))
    return contraseña

if st.button("✨ Generar contraseña", use_container_width=True):
    password = generar_contraseña()

    st.markdown(
        f"<div class='result-box'>{password}</div>",
        unsafe_allow_html=True,
    )

    st.write("")
    st.code(password, language="text")

    st.download_button(
        label="⬇️ Descargar contraseña",
        file_name="password.txt",
        data=password,
        mime="text/plain",
        use_container_width=True
    )
