import streamlit as st
import random
from datetime import datetime

# Inicialización del estado de la sesión para compras, precios y contenido de los libros
if "purchases" not in st.session_state:
    st.session_state["purchases"] = []

if "prices" not in st.session_state:
    st.session_state["prices"] = {
        "The Great Gatsby": 15.99,
        "1984 by George Orwell": 12.49,
        "To Kill a Mockingbird": 14.29,
        "The Catcher in the Rye": 13.99,
        "Pride and Prejudice": 10.99,
    }

# Fragmentos de libros simulados
book_snippets = {
    "The Great Gatsby": """
    "So we beat on, boats against the current, borne back ceaselessly into the past."
    """,
    "1984 by George Orwell": """
    "War is peace. Freedom is slavery. Ignorance is strength."
    """,
    "To Kill a Mockingbird": """
    "You never really understand a person until you consider things from his point of view."
    """,
    "The Catcher in the Rye": """
    "Don’t ever tell anybody anything. If you do, you start missing everybody."
    """,
    "Pride and Prejudice": """
    "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
    """,
}

# Función para actualizar los precios de manera aleatoria (simulación de descuentos)
def update_prices():
    for book, price in st.session_state["prices"].items():
        # Generar una fluctuación del -10% al +10%
        fluctuation = random.uniform(-0.10, 0.10)
        st.session_state["prices"][book] = max(0.99, price * (1 + fluctuation))

# Actualizar precios cada vez que se carga la página
update_prices()

# Título de la aplicación
st.title("BookStoreX - Your Favorite Online Bookstore")

# Introducción
st.write(
    """
Welcome to BookStoreX! Find the best deals on your favorite books. 
Our prices are updated dynamically to bring you the best offers.
"""
)

# Mostrar precios actuales
st.subheader("Today's Deals")
for book, price in st.session_state["prices"].items():
    st.write(f"- **{book}:** ${price:,.2f}")

# Selección de libros disponibles
st.subheader("Choose a book to buy")
book_choice = st.selectbox("Select a book:", list(st.session_state["prices"].keys()))

# Introducir cantidad de libros a comprar
st.subheader("Enter the quantity")
quantity = st.number_input("Number of books:", min_value=1, value=1)

# Calcular el costo total
book_price = st.session_state["prices"][book_choice]
total_cost = book_price * quantity

st.write(
    f"**For {quantity} copies of '{book_choice}', your total will be: ${total_cost:.2f}.**"
)

# Simulación de la compra
if st.button("Confirm Purchase"):
    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    purchase = {
        "book": book_choice,
        "quantity": quantity,
        "price_per_book": book_price,
        "total_cost": total_cost,
        "time": transaction_time,
    }
    st.session_state["purchases"].append(purchase)
    st.success(
        f"Transaction successful! You purchased {quantity} copies of '{book_choice}' "
        f"for a total of ${total_cost:.2f} on {transaction_time}."
    )
    st.subheader(f"Here's a snippet from '{book_choice}':")
    st.write(book_snippets[book_choice])

# Mostrar historial de compras
if st.session_state["purchases"]:
    st.subheader("Your Purchase History")
    for purchase in st.session_state["purchases"]:
        st.write(
            f"- **'{purchase['book']}'**: {purchase['quantity']} copies purchased at ${purchase['price_per_book']:.2f}/book "
            f"for a total of ${purchase['total_cost']:.2f} on {purchase['time']}."
        )


