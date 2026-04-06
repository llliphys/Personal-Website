import streamlit as st
from data.content import PROFILE
import os
import base64

def get_base64_img(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def render_home() -> None:
    st.title("🏠 Home Page")

    # Convert your local image file to base64
    img_base64 = get_base64_img(PROFILE['photo'])

    st.markdown(
        f"""
        <div class="hero-box" style="display: flex; align-items: center; gap: 20px;">
            <img src="data:image/png;base64,{img_base64}" 
                style="width: 155px; height: 155px; object-fit: cover;">
            <div>
                <h1 style="margin-bottom:0.25rem;">{PROFILE['name']}</h1>
                <h5 style="margin-top:0;">{PROFILE['title']}</h5>
                <p class="muted-text">{PROFILE['tagline']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.subheader("Welcome")
    st.write(
        """
        Welcome to my personal website. This website presents my background, resume, research interests, publications, projects, and professional links.

        My core expertise is specialized in computational materials science, high-performance computing, and machine learning for materials science. 
    
        I am interested in combining physical modelling with data-driven approaches to simulate, predict, and optimize materials properties for applications.
        """
    )

    st.markdown("---")

    st.subheader("Contact")
    # st.write(f"**Location:** {PROFILE['location']}")
    st.write(f"**Email:** {PROFILE['email']}")
    st.write(f"**LinkedIn:** {PROFILE['linkedin']}")
    st.write(f"**XING:** {PROFILE['xing']}")

