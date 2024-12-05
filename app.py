import streamlit as st

st.title("Explorador de directorios")

# HTML y JavaScript para explorar directorios
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script>
        async function selectDirectory() {
            const dirHandle = await window.showDirectoryPicker();
            const entries = [];
            for await (const entry of dirHandle.values()) {
                entries.push(entry.name);
            }
            document.getElementById('directoryContents').innerHTML = entries.map(e => '<li>' + e + '</li>').join('');
        }
    </script>
</head>
<body>
    <button onclick="selectDirectory()">Seleccionar Carpeta</button>
    <ul id="directoryContents"></ul>
</body>
</html>
"""

st.components.v1.html(html_code, height=400)


