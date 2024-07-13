import streamlit as st
from PIL import Image



image_path = "asset/ddd_logo.png"
# Load the image
image = Image.open(image_path)

# --- PAGE SETUP ---
about_page = st.Page(
    page ="views/about_me.py",
    title="About me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard",
    icon =":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/bar_chart:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS]---
pg = st.navigation(pages = [about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info":[about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- SHARED ON ALL PAGES ---
#st.image(image, caption="Deck and Dice Dimension Logo", use_column_width=True)
st.sidebar.text("Made with ❤️ by Lwolf")

# --- RUN NAVIGATION ---
pg.run()

