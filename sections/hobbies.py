import streamlit as st
from data.content import HOBBIES


# def render_hobbies() -> None:
#     st.title("🎯 My Hobbies")

#     st.write(
#         "We are human beings. A small collection of hobbies makes life more enjoyable and memorable beyond serious stuff."
#     )

#     for hobby in HOBBIES:
#         st.markdown(
#             f"""
#             <div class="section-card">
#                 <h3>{hobby['title']}</h3>
#                 <p>{hobby['description']}</p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         st.image(hobby["image"], width=800)


def render_hobbies() -> None:
    st.title("🎯 My Hobbies")

    st.write(
        "We are human beings. A small collection of hobbies makes life more enjoyable and memorable beyond serious stuff."
    )

    for hobby in HOBBIES:
        st.markdown(
            f"""
            <div class="section-card">
                <h3>{hobby['title']}</h3>
                <p>{hobby['description']}</p>
                <img src="{hobby['image']}" 
                     style="width:100%; max-width:400px;">
            </div>
            """,
            unsafe_allow_html=True,
        )