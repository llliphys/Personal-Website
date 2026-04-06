import streamlit as st
from data.content import PROJECTS


def render_projects() -> None:
    st.title("Research Projects")

    st.write("This section highlights selected research and software projects.")

    for project in PROJECTS:
        st.markdown(
            f"""
            <div class="section-card">
                <h3>{project['name']}</h3>
                <p>{project['summary']}</p>
                <p><strong>Status:</strong> {project['status']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        badge_html = "".join(
            [f'<span class="small-badge">{tool}</span>' for tool in project["tools"]]
        )
        st.markdown(badge_html, unsafe_allow_html=True)
        st.write("")
