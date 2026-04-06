# Personal Website Streamlit Draft

A modular Streamlit-based personal academic website draft.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

```text
personal_website_streamlit/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── assets/
│   └── profile.jpg
├── data/
│   └── content.py
├── utils/
│   └── styles.py
└── sections/
    ├── home.py
    ├── about.py
    ├── research_interests.py
    ├── publications.py
    ├── projects.py
    ├── contact.py
    └── hobbies.py
```

## Notes

- Add your profile image as `assets/profile.jpg`.
- Replace the placeholder content in `data/content.py` with your real information.
