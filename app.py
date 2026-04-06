import streamlit as st

from config import PAGE_TITLE, PAGE_ICON, LAYOUT
from utils.styles import apply_custom_styles

st.markdown(
    """
    <style>
    /* Remove border and background from sidebar buttons */
    section[data-testid="stSidebar"] .stButton > button {
        border: none !important;
        background-color: transparent !important;
        color: #1f2937 !important;
        text-align: left;
        width: 100%;
        padding: 0.4rem 0.5rem;
        border-radius: 6px;
    }

    /* Hover effect */
    section[data-testid="stSidebar"] .stButton > button:hover {
        background-color: #f3f4f6 !important;
        color: #111827 !important;
    }

    /* Active click effect */
    section[data-testid="stSidebar"] .stButton > button:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from sections.home import render_home
from sections.resume import render_resume
from sections.research_interests import render_research_interests
from sections.publications import render_publications
from sections.projects import render_projects
from sections.code_development import render_code_development
from sections.hobbies import render_hobbies


def main() -> None:
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        initial_sidebar_state="expanded",
    )

    apply_custom_styles()

    # -----------------------------
    # Sidebar Navigation (Buttons)
    # -----------------------------
    if "page" not in st.session_state:
        st.session_state.page = "Home Page"

    def set_page(page_name: str):
        st.session_state.page = page_name

    # Buttons instead of radio
    if st.sidebar.button("🏠 Home Page"):
        set_page("Home Page")
    if st.sidebar.button("📄 My Resume"):
        set_page("My Resume")
    if st.sidebar.button("🔬 Research Interests"):
        set_page("Research Interests")
    if st.sidebar.button("📚 Scientific Publications"):
        set_page("Scientific Publications")
    # if st.sidebar.button("📁 Research Projects"):
    #     set_page("Research Projects")
    if st.sidebar.button("💻 Code Development"):
        set_page("Code Development")
    if st.sidebar.button("🎯 My Hobbies"):
        set_page("My Hobbies")

    # col_icon, col_text = st.sidebar.columns([1, 100])
    # with col_icon:
    #     st.image("assets/layers.png", width=30)
    # with col_text:
    #     if st.button("Research Projects"):
    #         set_page("Research Projects")

    # if st.sidebar.button("🎯 My Hobbies"):
    #     set_page("My Hobbies")

    st.sidebar.markdown("---")
    st.sidebar.write(
        "Let's build and shape the future together."
    )

    page = st.session_state.page

    if page == "Home Page":
        render_home()
    elif page == "My Resume":
        render_resume()
    elif page == "Research Interests":
        render_research_interests()
    elif page == "Scientific Publications":
        render_publications()
    elif page == "Code Development":
        render_code_development()
    elif page == "Research Projects":
        render_projects()
    elif page == "My Hobbies":
        render_hobbies()


    # if page == "About Me":
    #     render_about()
    # elif page == "Research Interests":
    #     render_research_interests()
    # elif page == "Scientific Publications":
    #     render_publications()
    # elif page == "Research Projects":
    #     render_projects()
    # elif page == "My Hobbies":
    #     render_hobbies()

if __name__ == "__main__":
    main()


# import streamlit as st

# from config import PAGE_TITLE, PAGE_ICON, LAYOUT
# from utils.styles import apply_custom_styles

# from sections.home import render_home
# from sections.about import render_about
# from sections.research_interests import render_research_interests
# from sections.publications import render_publications
# from sections.projects import render_projects
# from sections.contact import render_contact
# from sections.hobbies import render_hobbies

# def main() -> None:
#     st.set_page_config(
#         page_title=PAGE_TITLE,
#         page_icon=PAGE_ICON,
#         layout=LAYOUT,
#         initial_sidebar_state="expanded",
#     )

#     apply_custom_styles()

#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio(
#         "Go to",
#         [
#             "Home",
#             "About Me",
#             "Research Interests",
#             "Scientific Publications",
#             "Research Projects",
#             "Contact",
#             "Hobbies",
#         ],
#     )

#     st.sidebar.markdown("---")
#     st.sidebar.info(
#         "Personal academic website draft built with Streamlit."
#     )

#     if page == "Home":
#         render_home()
#     elif page == "About Me":
#         render_about()
#     elif page == "Research Interests":
#         render_research_interests()
#     elif page == "Scientific Publications":
#         render_publications()
#     elif page == "Research Projects":
#         render_projects()
#     elif page == "Contact":
#         render_contact()
#     elif page == "Hobbies":
#         render_hobbies()


# if __name__ == "__main__":
#     main()