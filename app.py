import streamlit as st
from PIL import Image

hearts = ["❤️", "🧡", "💛", "💚", "🩵", "💙"]

if "page" not in st.session_state:
    st.session_state.page = "pick"

# PAGE 1 — Pick a color
if st.session_state.page == "pick":
    st.title("Pick a color")
    for emoji in hearts:
        if st.button(emoji, use_container_width=True):
            st.session_state.choice = emoji
            st.session_state.page = "result"
            st.rerun()

# PAGE 2 — Show original image
elif st.session_state.page == "result":
    st.title(f"{st.session_state.choice} Duck")
    st.image("colorful_duck.png", use_column_width=True)

    if st.button("⬅️ Back"):
        st.session_state.page = "pick"
        st.rerun()
