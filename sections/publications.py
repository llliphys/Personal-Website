import streamlit as st
from data.content import PUBLICATIONS


def highlight_author(authors: str) -> str:
    return authors.replace("L. L. Li", "<strong>L. L. Li</strong>")

def render_publications() -> None:
    st.title("📚 Scientific Publications")

    st.write(
        "This section presents a list of my scientific publications through my research career from 2010 to present"
    )

    year_filter = st.selectbox(
        "Filter by year",
        options=["All"] + sorted(list({pub["year"] for pub in PUBLICATIONS}), reverse=True),
    )

    search_text = st.text_input("Search by title, journal, or author")

    filtered = PUBLICATIONS

    if year_filter != "All":
        filtered = [pub for pub in filtered if pub["year"] == year_filter]

    if search_text.strip():
        q = search_text.lower()
        filtered = [
            pub for pub in filtered
            if q in pub["title"].lower()
            or q in pub["authors"].lower()
            or q in pub["journal"].lower()
        ]

    if not filtered:
        st.warning("No publications match the current filter.")
        return

    for pub in filtered:
        # st.markdown(
        #     f"""
        #     <div class="section-card">
        #         <h5>{pub['title']}</h5>
        #         <p><strong>{pub['authors']}</strong></p>
        #         <p>{pub['journal']} ({pub['year']})</p>
        #         <p><a href="{pub['url']}" target="_blank">DOI / Link</a></p>
        #     </div>
        #     """,
        #     unsafe_allow_html=True,
        # )
        st.markdown(
            f"""
            <div class="section-card">
                <h4>{pub['title']}</h4>
                <p>{highlight_author(pub['authors'])}</p>
                <p>{pub['journal']} ({pub['year']})</p>
                <p><a href="{pub['url']}" target="_blank">Link</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
