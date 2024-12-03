import streamlit as st
import random
from datetime import datetime

# Inicialización del estado de la sesión para compras y precios
if "purchases" not in st.session_state:
    st.session_state["purchases"] = []

if "prices" not in st.session_state:
    st.session_state["prices"] = {
        "Bitcoin (BTC)": 50000,
        "Ethereum (ETH)": 4000,
        "Litecoin (LTC)": 200,
        "Ripple (XRP)": 1.2,
    }

# Función para actualizar los precios de manera aleatoria
def update_prices():
    for crypto, price in st.session_state["prices"].items():
        # Generar una fluctuación del -5% al +5%
        fluctuation = random.uniform(-0.05, 0.05)
        st.session_state["prices"][crypto] = max(0.01, price * (1 + fluctuation))

# Actualizar precios cada vez que se carga la página
update_prices()

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

# Mostrar precios actuales
st.subheader("Current Cryptocurrency Prices")
for crypto, price in st.session_state["prices"].items():
    st.write(f"- **{crypto}:** ${price:,.2f} USD")

# Selección de criptomonedas disponibles
st.subheader("Choose your cryptocurrency")
crypto_choice = st.selectbox("Select a cryptocurrency:", list(st.session_state["prices"].keys()))

# Introducir monto en USD
st.subheader("Enter the amount you want to invest (in USD)")
usd_amount = st.number_input("Investment amount in USD:", min_value=1.0, value=100.0)

# Calcular la cantidad de criptomonedas a recibir
crypto_price = st.session_state["prices"][crypto_choice]
crypto_received = usd_amount / crypto_price

st.write(
    f"**For ${usd_amount}, you will receive approximately {crypto_received:.6f} {crypto_choice.split()[0]}**."
)

# Simulación de la compra
if st.button("Confirm Purchase"):
    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    purchase = {
        "crypto": crypto_choice,
        "amount_usd": usd_amount,
        "crypto_received": crypto_received,
        "price_at_purchase": crypto_price,
        "time": transaction_time,
    }
    st.session_state["purchases"].append(purchase)
    st.success(
        f"Transaction successful! You purchased {crypto_received:.6f} {crypto_choice.split()[0]} "
        f"for ${usd_amount} on {transaction_time}."
    )

# Mostrar historial de compras
if st.session_state["purchases"]:
    st.subheader("Your Purchase History")
    for purchase in st.session_state["purchases"]:
        st.write(
            f"- **{purchase['crypto']}**: {purchase['crypto_received']:.6f} "
            f"purchased for ${purchase['amount_usd']} at ${purchase['price_at_purchase']:.2f}/unit on {purchase['time']}"
        )

