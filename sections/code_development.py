import streamlit as st


def render_code_development() -> None:
    st.title("💻 Code Development")

    st.write(
        "This section highlights my experience in scientific code development, "
        "workflow automation, and machine learning pipeline implementation for computational materials research."
    )

    st.markdown("---")

    # =========================
    # Scientific Software
    # =========================
    st.subheader("Scientific Code Development")

    st.markdown(
        """
        <div class="section-card">
            <h5>Simulation Workflow Automation</h5>
            <p>
            Designed and implemented automated workflows for first-principles simulations,
            integrating DFT calculations, data preprocessing, and post-processing analysis.
            </p>
            <p class="muted-text">Tools: Python, Bash, VASP, SIESTA, HPC clusters</p>
        </div>

        <div class="section-card">
            <h5>High-Throughput Computational Pipelines</h5>
            <p>
            Developed scalable pipelines for high-throughput materials simulations and dataset generation,
            enabling efficient exploration of structure-property relationships.
            </p>
            <p class="muted-text">Tools: Python, NumPy, Pandas, HPC clusters</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Machine Learning
    # =========================
    st.markdown("---")
    st.subheader("Machine Learning Development")

    st.markdown(
        """
        <div class="section-card">
            <h5>ML Models for Scientific Data</h5>
            <p>
            Developed machine learning models to predict material properties and molecular fingerprints
            from simulation data, including regression models and neural networks.
            </p>
            <p class="muted-text">Tools: PyTorch, Scikit-learn</p>
        </div>

        <div class="section-card">
            <h5>End-to-End ML Pipelines</h5>
            <p>
            Built complete ML workflows including feature engineering, data normalization,
            dimensionality reduction (PCA), model training, and evaluation.
            </p>
            <p class="muted-text">Tools: Python, Pandas, Scikit-learn, PyTorch</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Tools & Technologies
    # =========================
    st.markdown("---")
    st.subheader("Tools & Technologies")

    # tools = [
    #     "Python",
    #     "NumPy",
    #     "SciPy",
    #     "Pandas",
    #     "Matplotlib",
    #     "PyTorch",
    #     "Scikit-learn",
    #     "Bash",
    #     "HPC (Slurm, MPI, OpenMP)",
    #     "VASP",
    #     "SIESTA",
    #     "Quantum ESPRESSO",
    # ]

    # badge_html = "".join(
    #     [f'<span class="small-badge">{tool}</span>' for tool in tools]
    # )
    # st.markdown(badge_html, unsafe_allow_html=True)


    # =========================
    # Categories
    # =========================

    simulation_tools = [
        "VASP",
        "SIESTA",
        "Quantum ESPRESSO",
        "YAMBO",
    ]

    ml_tools = [
        "PyTorch",
        "Scikit-learn",
    ]

    data_tools = [
        "Python",
        "NumPy",
        "SciPy",
        "Pandas",
        "Matplotlib",
    ]

    workflow_tools = [
        "Bash",
        "HPC",
        "MPI",
        "OpenMP",
    ]

    # =========================
    # Helper for rendering
    # =========================

    def render_badges(tools):
        return "".join(
            [f'<span class="small-badge">{tool}</span>' for tool in tools]
        )

    # =========================
    # Render sections
    # =========================

    st.markdown("**Computer Simulation**")
    st.markdown(render_badges(simulation_tools), unsafe_allow_html=True)

    st.markdown("**Machine Learning**")
    st.markdown(render_badges(ml_tools), unsafe_allow_html=True)

    st.markdown("**Data Analysis**")
    st.markdown(render_badges(data_tools), unsafe_allow_html=True)

    st.markdown("**HPC Workflow**")
    st.markdown(render_badges(workflow_tools), unsafe_allow_html=True)

    # =========================
    # GitHub / Code Links
    # =========================
    st.markdown("---")
    st.subheader("Code Repositories")

    st.markdown(
        """
        <div class="section-card">
            <p>
            Selected scientific code projects can be found on my GitHub.
            </p>
            <p>
            <a href="https://github.com/llliphys" target="_blank">
            Visit GitHub Profile
            </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )