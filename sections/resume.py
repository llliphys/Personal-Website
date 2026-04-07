import os
import streamlit as st
from data.content import PROFILE, SHORT_BIO


def render_resume() -> None:
    st.title("📄 My Resume")

    st.markdown("---")

    st.subheader("Short Profile")

    SHORT_BIO = """
    I am a research scientist with 5+ years of experence specialized in computational materials science.
    My research expertise combines density-functional theory modelling, quantum transport modelling, many-body effects modelling, atomistic tight-binding modeling,
    high-performance computing, simulation workflow development, and data-driven machine learning to investigate and understand 
    material properties for guiding and accelerating materials applications.
    """

    SHORT_BIO = """
    I am a research scientist with 5+ years of experence specialized in computational materials science.
    My research expertise combines physics-based modelling, scientific computing, machine learning, and workflow development to investigate and understand 
    material properties for guiding and accelerating materials applications.
    """


    SHORT_BIO = """
    I am a research scientist with 5+ years of experence specialized in computational materials science.
    My research expertise combines first-principles modelling, data-driven machine learning, high-performance computing, and simulation workflow development to investigate and understand 
    material properties for guiding and accelerating materials applications.
    """

    st.write(SHORT_BIO)
    # st.markdown(f'<p style="font-size:19px;">{SHORT_BIO}</p>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Research Experience")

    # st.markdown(
    #     """
    # **Research Scientist (DFT/NEGF/ML)**  
    # *RWTH Aachen University, Germany*  
    # *06/2023 – Present*

    # - Developed and applied first-principles simulation frameworks based on density functional theory (DFT), non-equilibrium Green’s function (NEGF), and linear response theory using VASP and SIESTA to investigate structural, electronic, transport, and optical properties of nanomaterials and nanostructures for biosensing applications.
    # - Simulated electronic transport and optical responses of nanomaterials and nanostructures for biomolecule detection, linking atomistic material properties to device-level sensing performance and enabling physics-driven optimization of biosensor designs.
    # - Generated high-throughput DFT datasets and implemented data-driven machine learning models using PyTorch and Scikit-learn to predict molecular fingerprints from optical spectra, achieving more than 90% accuracy and significantly accelerating property prediction compared to direct DFT simulations.
    # - Designed and deployed automated end-to-end computational workflows integrating DFT simulations, feature engineering, data preprocessing, and ML model training and evaluation using Python and Bash, ensuring reproducibility and scalability on HPC systems.

    # **Research Scientist (DFT/GW/BSE)**  
    # *University of Antwerp, Belgium*  
    # *10/2021 – 02/2023*

    # - Performed advanced first-principles simulations combining density functional theory (DFT) and many-body GW/BSE formalism using VASP, Quantum ESPRESSO, and YAMBO to investigate quasi-particle band structures and excitonic optical properties of 2D material heterostructures.
    # - Investigated strain-, gating-, and stacking-dependent effects on electronic screening, quasi-particle corrections, exciton binding energies, and optical absorption spectra, enabling rational design of material properties for optoelectronic applications.
    # - Automated and optimized high-throughput workflows for large-scale simulations on HPC clusters, integrating Slurm-based job scheduling, parallel execution strategies, and resource optimization to significantly enhance computational efficiency.
    # - Bridged theory and experiment by interpreting computed excited-state properties in the context of spectroscopic measurements such as absorption and photoluminescence, providing predictive insights for material design.

    # **Research Scientist (DFT+U/TB)**  
    # *University of Duisburg-Essen, Germany*  
    # *09/2019 – 08/2021*

    # - Performed first-principles simulations based on density functional theory with Hubbard U using VASP, including structural relaxation, electronic structure, magnetic ordering, and spin-orbit coupling effects in complex oxide heterostructures.
    # - Constructed maximally localized Wannier functions using WANNIER90 to develop tight-binding Hamiltonians for accurate description of electronic band topology and low-energy electronic properties.
    # - Investigated correlation-, strain-, and orientation-dependent effects on atomic structures, electronic states, magnetic moments, and emergent topological phases at oxide heterointerfaces.
    # - Established a strong theory-experiment connection by systematically validating simulation outcomes against available experimental results and literature benchmarks.
    # """
    # )


    st.markdown(
        """
    <div>
        <div style="display: flex; justify-content: space-between;">
            <span style="font-weight: bold;">Research Scientist (DFT/NEGF/ML)</span>
            <span>06/2023 – Present</span>
        </div>
        <div style="font-style: italic;">
            RWTH Aachen University, Germany
        </div>
    </div>

    - Developed and applied first-principles simulation frameworks based on density functional theory (DFT), non-equilibrium Green’s function (NEGF), and linear response theory using VASP and SIESTA to investigate structural, electronic, transport, and optical properties of nanomaterials and nanostructures for biosensing applications.
    - Simulated electronic transport and optical responses of nanomaterials and nanostructures for biomolecule detection, linking atomistic material properties to device-level sensing performance and enabling physics-driven optimization of biosensor designs.
    - Generated high-throughput DFT datasets and implemented data-driven machine learning models using PyTorch and Scikit-learn to predict molecular fingerprints from optical spectra, achieving more than 90% accuracy and significantly accelerating property prediction compared to direct DFT simulations.
    - Designed and deployed automated end-to-end computational workflows integrating DFT simulations, feature engineering, data preprocessing, and ML model training and evaluation using Python and Bash, ensuring reproducibility and scalability on HPC systems.

    <div>
        <div style="display: flex; justify-content: space-between;">
            <span style="font-weight: bold;">Research Scientist (DFT/GW/BSE)</span>
            <span>10/2021 – 02/2023</span>
        </div>
        <div style="font-style: italic;">
            University of Antwerp, Belgium
        </div>
    </div>

    - Performed advanced first-principles simulations combining density functional theory (DFT) and many-body GW/BSE formalism using VASP, Quantum ESPRESSO, and YAMBO to investigate quasi-particle band structures and excitonic optical properties of 2D material heterostructures.
    - Investigated strain-, gating-, and stacking-dependent effects on electronic screening, quasi-particle corrections, exciton binding energies, and optical absorption spectra, enabling rational design of material properties for optoelectronic applications.
    - Automated and optimized high-throughput workflows for large-scale simulations on HPC clusters, integrating Slurm-based job scheduling, parallel execution strategies, and resource optimization to significantly enhance computational efficiency.
    - Bridged theory and experiment by interpreting computed excited-state properties in the context of spectroscopic measurements such as absorption and photoluminescence, providing predictive insights for material design.

    
    <div>
        <div style="display: flex; justify-content: space-between;">
            <span style="font-weight: bold;">Research Scientist (DFT+U/TB)</span>
            <span>09/2019 – 08/2021</span>
        </div>
        <div style="font-style: italic;">
            University of Duisburg-Essen, Germany
        </div>
    </div>

    - Performed first-principles simulations based on density functional theory with Hubbard U using VASP, including structural relaxation, electronic structure, magnetic ordering, and spin-orbit coupling effects in complex oxide heterostructures.
    - Constructed maximally localized Wannier functions using WANNIER90 to develop tight-binding (TB) Hamiltonians for accurate description of electronic band topology and low-energy electronic properties.
    - Investigated correlation-, strain-, and orientation-dependent effects on atomic structures, electronic states, magnetic moments, and emergent topological phases at oxide heterointerfaces.
    - Established a strong theory-experiment connection by systematically validating simulation outcomes against available experimental results and literature benchmarks.
    """,
    unsafe_allow_html=True
    )

    st.markdown("---")
    st.subheader("Technical Skills")

    st.markdown(
        """
    - **Computational Materials Science:** Density functional theory (DFT/DFT+U via VASP, SIESTA, and Quantum ESPRESSO); many-body perturbation theory (GW/BSE via VASP and YAMBO); first-principles tight-binding (DFT/TB via VASP/WANNIER90); structural optimization, electronic structure, excitonic properties, and quantum transport.
    - **Scientific Programming & Workflows:** Python (NumPy, SciPy, Pandas, Matplotlib), Bash, Fortran; automated simulation workflows, data processing pipelines, and reproducible computational environments.
    - **High-Performance Computing:** HPC clusters, Slurm and PBS schedulers, MPI/OpenMP parallelization, performance optimization, and large-scale job management.
    - **Machine Learning for Materials:** PyTorch, Scikit-learn; surrogate modeling, regression and classification, and ML-assisted analysis of high-throughput simulation data.
    """
    )

    st.markdown("---")
    st.subheader("Education Background")

    # st.markdown(
    #     """
    # **PhD in Physics**  
    # *University of Chinese Academy of Sciences, China*  
    # *09/2006 – 07/2011*

    # **BSc in Physics**  
    # *Anhui University, China*  
    # *09/2002 – 07/2006*

    # """,
    # )


    st.markdown(
        """
    <div>
        <div style="display: flex; justify-content: space-between;">
            <span style="font-weight: bold;">PhD in Physics</span>
            <span>09/2006 – 07/2011</span>
        </div>
        <div style="font-style: italic;">
            University of Chinese Academy of Sciences, China
        </div>
    </div>

    <div>
        <div style="display: flex; justify-content: space-between;">
            <span style="font-weight: bold;">BSc in Physics</span>
            <span>09/2002 – 07/2006</span>
        </div>
        <div style="font-style: italic;">
            Anhui University, China
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )


    st.markdown("---")
    st.subheader("Language Proficiency")

    st.markdown(
        """
    - **English:** Proficient (B2/C1) 
    - **German:** Intermediate (B1/B2)
    """
    )


    # col1, col2 = st.columns([1, 4])

    # with col1:
    #     st.markdown("<br>", unsafe_allow_html=True)
    #     image_path = "assets/profile.jpg"
    #     if os.path.exists(image_path):
    #         st.image(image_path, width=190) #use_container_width=True)
    #     else:
    #         st.info("Add your profile image to assets/profile.jpg")

    # with col2:
    #     st.subheader(PROFILE["name"])
    #     st.write(PROFILE["title"])
    #     # st.markdown(f'**{PROFILE["title"]}**')
    #     st.write(SHORT_BIO)
    #     # st.markdown(f'<p style="font-size:19px;">{SHORT_BIO}</p>', unsafe_allow_html=True)

    # st.markdown("---")
    # st.subheader("Core Competencies")

    # strengths = [
    #     "Functional materials, nanomaterials & nanostructures",
    #     "Computational materials science and informatics",
    #     "DFT modelling (VASP/SIESTA/Quantum ESPRESSO)",
    #     "First-principles electronic structure calculation",
    #     "Many-body theory modelling (GW/BSE via YAMBO)",
    #     "Quantum transport simulation (NEGF via TranSIESTA)",
    #     "Large-scale atomistic tight-binding simulation",
    #     "Data-driven machine learning (Pytorch/Scikit-learn)",
    #     "Simulation workflow automation (Bash/Python)",
    #     "Scientific programming (Python/Matlab/Fortran)",
    #     "High-performance computing (Slurm/MPI/OpenMP)",
    #     "Research communication & inter-disciplinary collaboration",
    #     "Scientific data analysis for high-impact publication",
    # ]

    # for item in strengths:
    #     st.markdown(f"- {item}")
