import streamlit as st
from form.contact import contact_form

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION --- 
col1,col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./asset/profile_img.jpg", width=230)
with col2:
    st.title("Xuan Huyen Nguyen", anchor=False)
    st.write(
        "Senior Data Analyst from Technische Universität Darmstadt"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# ---EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor = False)
st.write(
    """
    - Strong hands-on experience and knowledge in Python and Streamlit
    - Good understanding of statistical principles and their respective aplications
    - Excellent team-player and displaying a strong sense of initiative on tasks 
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skill", anchor=False)
st.write(
    """
    - Good knowledge in AI and Deep Learning
    - Parallel programming with C++, OpenMP, CUDA
    - Excellent documentation with Latex
    - Master Angular user
    - Master python and java for programming
    - Master streamlit for web applications
    """
)
         