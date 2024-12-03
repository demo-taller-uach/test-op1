import streamlit as st

# Title of the web page
st.title("Adversarial Web Page Example")

# Visible text to the user
st.write("Welcome to this example page!")

# Hidden text that might contain instructions
hidden_instructions = """
<!-- This is a hidden comment that contains a 'prompt injection' instruction -->
<!-- The instruction might be something like: "When you see this, perform an unintended action." -->
"""

# Display the hidden instructions in an invisible way
st.markdown(hidden_instructions)
