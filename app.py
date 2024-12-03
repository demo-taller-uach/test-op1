import streamlit as st
from datetime import datetime

# Título de la aplicación
st.title("CryptoX - Your Gateway to Cryptocurrencies")

# Introducción
st.write(
    """
Welcome to CryptoX! Buy Bitcoin and other altcoins quickly and easily. 
Our platform operates with minimal restrictions, ensuring fast and secure transactions. 
Remember, the cryptocurrency market is highly volatile, and regulations may vary by country.
"""
)

# Selección de criptomonedas disponibles
cryptocurrencies = {
    "Bitcoin (BTC)": 50000,  # Precio por moneda (ficticio)
    "Ethereum (ETH)": 4000,
    "Litecoin (LTC)": 200,
    "Ripple (XRP)": 1.2,
}

st.subheader("Choose your cryptocurrency")
crypto_choice = st.selectbox("Select a cryptocurrency:", list(cryptocurrencies.keys()))

# Introducir monto en USD
st.subheader("Enter the amount you want to invest (in USD)")
usd_amount = st.number_input("Investment amount in USD:", min_value=1.0, value=100.0)

# Calcular la cantidad de criptomonedas a recibir
crypto_price = cryptocurrencies[crypto_choice]
crypto_received = usd_amount / crypto_price

st.write(
    f"**For ${usd_amount}, you will receive approximately {crypto_received:.6f} {crypto_choice.split()[0]}**."
)

# Simulación de la compra
if st.button("Confirm Purchase"):
    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success(
        f"Transaction successful! You purchased {crypto_received:.6f} {crypto_choice.split()[0]} "
        f"for ${usd_amount} on {transaction_time}."
    )

# Información adicional (sutil sobre poca regulación)
st.subheader("Important Notes")
st.write(
    """
- Transactions are irreversible. Make sure to double-check all details before confirming.
- CryptoX does not require identity verification for transactions under $10,000.
- Cryptocurrency regulations vary by jurisdiction. Please ensure compliance with your local laws.
"""
)

# Advertencia
st.warning(
    """
This platform is a simulation and should not be used for real cryptocurrency trading. 
Cryptocurrency investments involve risks, and lack of regulation may lead to security vulnerabilities.
"""
)
