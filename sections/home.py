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
    # st.title(PROFILE["name"])


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



    # st.markdown(
    #     f"""
    #     <div class="hero-box" style="display: flex; align-items: center; gap: 20px;">
    #         <img src="{PROFILE['photo']}" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover;">
    #         <div>
    #             <h1 style="margin-bottom:0.25rem;">{PROFILE['name']}</h1>
    #             <h5 style="margin-top:0;">{PROFILE['title']}</h5>
    #             <p class="muted-text">{PROFILE['tagline']}</p>
    #         </div>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )


    # st.markdown(
    #     f"""
    #     <div class="hero-box">
    #         <h1 style="margin-bottom:0.25rem;">{PROFILE['name']}</h1>
    #         <h5 style="margin-top:0;">{PROFILE['title']}</h5>
    #         <p class="muted-text">{PROFILE['tagline']}</p>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # st.markdown("---")

    # col1, col2 = st.columns([1, 8])

    # with col1:
    #     st.markdown("<br>", unsafe_allow_html=True)
    #     image_path = "assets/profile.jpg"
    #     if os.path.exists(image_path):
    #         st.image(image_path, width=135) #use_container_width=True)
    #     else:
    #         st.info("Add your profile image to assets/profile.jpg")

    # with col2:
    #     # 1. The Name (Large Header)
    #     st.markdown(f'# {PROFILE["name"]}')

    #     # 2. The Title (Medium Header with specific margin)
    #     st.markdown(f'<h5 style="margin-top:0;">{PROFILE["title"]}</h5>', unsafe_allow_html=True)

    #     # 3. The Tagline (Muted Text)
    #     st.markdown(f'<p class="muted-text">{PROFILE["tagline"]}</p>', unsafe_allow_html=True)


    # st.markdown("---")

    # col1, _ = st.columns([3, 1])

    # with col1:
    st.subheader("Welcome")
    st.write(
        """
        Welcome to my personal website. This website presents my background, resume, research interests, publications, projects, and professional links.

        My core expertise is specialized in computational materials science, high-performance computing, and machine learning for materials science. 
    
        I am interested in combining physical modelling with data-driven approaches to simulate, predict, and optimize materials properties for applications.
        """
    )

    st.markdown("---")

    # col2, _ = st.columns([2, 1])

    # with col2:
    st.subheader("Contact")
    # st.write(f"**Location:** {PROFILE['location']}")
    st.write(f"**Email:** {PROFILE['email']}")
    st.write(f"**LinkedIn:** {PROFILE['linkedin']}")
    st.write(f"**XING:** {PROFILE['xing']}")


    # col1, col2 = st.columns([2, 1])

    # with col1:
    #     st.subheader("Welcome")
    #     st.write(
    #         """
    #         Welcome to my personal website. This website presents my background, resume, research interests, publications, projects, and professional links.

    #         My proven expertise is specialized in computational materials science, high-performance computing, and machine learning for materials scientific data. 
        
    #         I am interested in combining physical modelling with data-driven approaches to simulate, predict, and optimize materials properties for applications.
    #         """
    #     )

    # with col2:
    #     st.subheader("Contact")
    #     # st.write(f"**Location:** {PROFILE['location']}")
    #     st.write(f"**Email:** {PROFILE['email']}")
    #     st.write(f"**LinkedIn:** {PROFILE['linkedin']}")
    #     st.write(f"**GitHub:** {PROFILE['github']}")



    # st.markdown("---")
    # # st.subheader("Highlights")
    # st.subheader("Updates")

    # c1, c2 = st.columns(2)

    # with c1:
    #     st.markdown(
    #         """
    #         <div class="section-card">
    #             <h4>Research</h4>
    #             <p>Computational materials science, electronic structure, and scientific machine learning.</p>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    # with c2:
    #     st.markdown(
    #         """
    #         <div class="section-card">
    #             <h4>Blog</h4>
    #             <p>Python-based tools, automation pipelines, and Streamlit scientific apps.</p>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )


    # c1, c2, c3 = st.columns(3)

    # with c1:
    #     st.markdown(
    #         """
    #         <div class="section-card">
    #             <h4>Research</h4>
    #             <p>Computational materials science, electronic structure, and scientific ML.</p>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    # with c2:
    #     st.markdown(
    #         """
    #         <div class="section-card">
    #             <h4>Software</h4>
    #             <p>Python-based tools, automation pipelines, and Streamlit scientific apps.</p>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    # with c3:
    #     st.markdown(
    #         """
    #         <div class="section-card">
    #             <h4>Goal</h4>
    #             <p>Bridging physics-based simulation and machine learning for impactful research.</p>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
