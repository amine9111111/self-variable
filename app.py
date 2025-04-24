import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import string

# ------------------------------
# Titre
st.title("🧬 Self Variable")

st.write("""
Bienvenue sur **Self Variable** — une application pour générer dynamiquement des variables à partir d'un simple nombre 🔢.
Tu obtiens :
- Des entiers
- Des flottants
- Des booléens
- Des chaînes de caractères
Et une visualisation sympa avec **matplotlib** ! 📊
""")

# ------------------------------
# Entrée de l'utilisateur
st.header("💡 Choisis un nombre de base")
base = st.number_input("Nombre de base", min_value=1, max_value=1000, value=50)

if st.button("🚀 Générer les variables"):
    st.success("Variables générées avec succès !")

    n = min(int(base), 100)

    # Fonctions de génération
    def gen_ints(n): return list(range(n))
    def gen_floats(n): return list(np.round(np.random.uniform(0, n, n), 2))
    def gen_bools(n): return [random.choice([True, False]) for _ in range(n)]
    def gen_strings(n): return [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(n)]

    entiers = gen_ints(n)
    floats = gen_floats(n)
    booleens = gen_bools(n)
    chaines = gen_strings(n)

    # Affichage
    st.subheader("📦 Variables générées")
    st.write("🔹 **Entiers :**", entiers[:10], "...")
    st.write("🔹 **Flottants :**", floats[:10], "...")
    st.write("🔹 **Booléens :**", booleens[:10], "...")
    st.write("🔹 **Chaînes :**", chaines[:10], "...")

    # Matplotlib Chart
    st.subheader("📈 Visualisation avec Matplotlib")

    fig, ax = plt.subplots()
    ax.plot(entiers, floats, marker='o', linestyle='-', color='teal')
    ax.set_title("Entiers vs Flottants")
    ax.set_xlabel("Entiers")
    ax.set_ylabel("Flottants")
    ax.grid(True)

    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("🛠️ Made with love in Streamlit")