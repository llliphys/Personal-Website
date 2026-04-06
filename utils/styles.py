import streamlit as st


def apply_custom_styles() -> None:
    st.markdown(
        """
        <style>
        .main {
            padding-top: 1rem;
            padding-bottom: 2rem;
        }

        h1, h2, h3 {
            color: #1f2937;
        }

        .hero-box {
            background-color: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 14px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }

        .section-card {
            background-color: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }

        .muted-text {
            color: #6b7280;
            font-size: 0.95rem;
        }

        .small-badge {
            display: inline-block;
            padding: 0.25rem 0.6rem;
            margin-right: 0.35rem;
            margin-top: 0.35rem;
            border-radius: 999px;
            background-color: #eef2ff;
            color: #3730a3;
            font-size: 0.85rem;
        }

        .contact-box {
            background-color: #f9fafb;
            border-left: 4px solid #2563eb;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 0.8rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
