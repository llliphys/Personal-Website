import streamlit as st
from data.content import PROFILE


def render_contact() -> None:
    st.title("Contact")

    st.write("Feel free to reach out for research collaboration, scientific software development, or professional networking.")

    st.markdown(
        f"""
        <div class="contact-box">
            <strong>Email:</strong> {PROFILE['email']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="contact-box">
            <strong>LinkedIn:</strong> <a href="{PROFILE['linkedin']}" target="_blank">{PROFILE['linkedin']}</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="contact-box">
            <strong>GitHub:</strong> <a href="{PROFILE['github']}" target="_blank">{PROFILE['github']}</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.subheader("Contact Form Draft")
    st.info(
        "Since you want Streamlit only, we can later add a simple contact form using Streamlit widgets. "
        "For actual message delivery, we can connect it to email or a backend service in a later step."
    )

    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Draft submission received. Later we can connect this to a real email workflow.")
        else:
            st.warning("Please fill in all fields.")
