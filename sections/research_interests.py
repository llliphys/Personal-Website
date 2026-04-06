import streamlit as st
from data.content import RESEARCH_INTERESTS


def render_research_interests() -> None:
    st.title("🔬 Research Interests")

    st.write(
        "My research focuses on combining physics-based simulation, scientific computing, and machine learning for materials science and applications."
    )

    # for item in RESEARCH_INTERESTS:
    #     st.markdown(
    #         f"""
    #         <div class="section-card">
    #             <h5>{item['title']}</h5>
    #             <p>{item['description']}</p>
    #             <div style="text-align:left; margin-top:10px; padding-left:5px;">
    #                 $$ {item['equations']} $$
    #             </div>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    for item in RESEARCH_INTERESTS:
        with st.container(border=True):
            # st.subheader(item["title"])
            st.markdown(f"##### {item['title']}")
            st.write(item["description"])
            st.latex(item["equations"])