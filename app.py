import streamlit as st

st.title("Información del sistema operativo")
st.write("Esta aplicación muestra información básica de tu sistema operativo.")

# HTML y JavaScript para obtener información del navegador
html_code = """
<div id="info">
    <p><b>Sistema Operativo:</b> <span id="platform"></span></p>
    <p><b>Agente de Usuario:</b> <span id="userAgent"></span></p>
</div>

<script>
    document.getElementById("platform").textContent = navigator.platform;
    document.getElementById("userAgent").textContent = navigator.userAgent;
</script>
"""

# Integrar el HTML en la app de Streamlit
st.components.v1.html(html_code, height=200)

