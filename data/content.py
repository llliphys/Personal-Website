PROFILE = {
    "photo": "assets/profile.jpg",
    "name": "Dr. Longlong Li",
    "title": "Research Scientist | PhD in Physics",
    "tagline": (
        "I develop physics-based and data-driven methods for materials research and development, "
        "with a focus on physical modelling, scientific computing, and machine learning."
    ),
    "location": "Aachen, Germany",
    "email": "longlong.li@outlook.com",
    "linkedin": "https://www.linkedin.com/in/llliphys/",
    "xing": "https://www.xing.com/profile/Longlong_Li042751/",
}

SHORT_BIO = """
I am a research scientist with 5+ years of experence specialized in computational materials science.
My research expertise combines density-functional theory modelling, quantum transport modelling, many-body effects modelling, atomistic tight-binding modeling,
high-performance computing, simulation workflow development, and data-driven machine learning to investigate and understand 
material properties for guiding and accelerating materials applications.
"""


RESEARCH_INTERESTS = [
    {
        "title": "Density-functional Theory (DFT) for Electronic Structure Modelling",
        "description": (
            "First-principles DFT modelling of ground-state electronic properties."
        ),
        "equations": r"""
\begin{aligned}
& \left[ -\frac{\hbar^2}{2m} \nabla^2 + V_{\mathrm{eff}}(\mathbf{r}) \right]\psi_i(\mathbf{r}) = \epsilon_i \psi_i(\mathbf{r}) & \\
& E[\rho]  = T[\rho] + V_{\mathrm{ext}}[\rho] + U[\rho] + E_{\mathrm{xc}}[\rho] & \\
& \rho(\mathbf{r}) = \sum_i |\psi_i(\mathbf{r})|^2 & \\
\end{aligned}

"""
    },
    {
        "title": "Many-body Theory (GW/BSE) for Optical Properties Modelling",
        "description": (
            "First-principles GW/BSE modelling of excited-state optical properties."
        ),
        "equations": r"""

\begin{aligned}
& E_n^{\mathrm{QP}} = \epsilon_n^{\mathrm{KS}} + \langle \psi_n^{\mathrm{KS}} \mid \Sigma(E_n^{\mathrm{QP}}) - V_{\mathrm{xc}} \mid \psi_n^{\mathrm{KS}} \rangle & \\
& \sum_{v'c'\mathbf{k}'} H^{\mathrm{BSE}}_{vc\mathbf{k},\,v'c'\mathbf{k}'} A^{S}_{v'c'\mathbf{k}'} = \Omega^{S} A^{S}_{vc\mathbf{k}} & \\
\end{aligned}

"""
    },
    {
        "title": "Quantum Transport Theory (NEGF) for Transport Device Modelling",
        "description": (
            "First-principles NEGF modelling of quantum transport properties."
        ),
        "equations": r"""
\begin{aligned}
& G(E) = \left[E I - H - \Sigma_L - \Sigma_R\right]^{-1} & \\
& T(E) = \mathrm{Tr}\left[\Gamma_L G \Gamma_R G^\dagger\right] & \\
& I = \frac{2e}{h}\int T(E)\left[f_L(E)-f_R(E)\right]\,dE & \\
\end{aligned}
"""
    },
    {
        "title": "Machine Learning Methods for Materials Properties Forecasting",
        "description": (
            "Data-driven ML forecasting of materials properties using simulation data."
        ),
        "equations": r"""
\begin{aligned}
& \hat{y} = f_{\theta}(x) & \\
& \mathcal{L} = \frac{1}{N}\sum_{i=1}^{N}(y_i-\hat{y}_i)^2 & \\
\end{aligned}
"""
    },
]



PUBLICATIONS = [
    {
        "title": "Machine learning molecular absorption spectra in graphene nanopores",
        "authors": "L. L. Li and M. Fyta",
        "journal": "Submitted",
        "year": "2026",
        "url": "",
    },
    {
        "title": "Dielectric response of graphene and MoS2 nanopores in the detection of single amino acids",
        "authors": "L. L. Li and M. Fyta",
        "journal": "npj 2D Materials and Applications (accepted)",
        "year": "2026",
        "url": "",
    },
    {
        "title": "Mechanical and electronic response of monolayer chromium trihalides CrX3 (X = Cl, Br, I) under uniaxial strain",
        "authors": "L. L. Li and M. Fyta",
        "journal": "RSC Advances",
        "year": "2025",
        "url": "https://pubs.rsc.org/en/content/articlelanding/2025/ra/d5ra04294a",
    },
    {
        "title": "Electronic Structure and Stability of Two-Dimensional Molybdenene",
        "authors": "S. Smid, L. L. Li, and M. Fyta",
        "journal": "ACS Applied Electronic Materials",
        "year": "2024",
        "url": "https://doi.org/10.1021/acsaelm.4c01092",
    },
    {
        "title": "Strain tunable interlayer and intralayer excitons in vertically stacked MoSe2/WSe2 heterobilayers",
        "authors": "L. L. Li, R. Gillen, M. Palummo, M. V. Milošević, and F. M. Peeters",
        "journal": "Applied Physics Letters",
        "year": "2023",
        "url": "https://doi.org/10.1063/5.0147761",
    },
    {
        "title": "High Chern numbers in a perovskite-derived dice lattice (LaXO3)3/(LaAlO3)3(111)",
        "authors": "O. Köksal, L. L. Li, and R. Pentcheva",
        "journal": "Scientific Reports",
        "year": "2023",
        "url": "https://www.nature.com/articles/s41598-023-36170-9",
    },
    {
        "title": "Concomitant appearance of conductivity and superconductivity in (111) LaAlO3/SrTiO3 interface with metal capping",
        "authors": "R. S. Bisht, M. Mograbi, P. K. Rout, G. Tuvia, Y. Dagan, H. Yoon, A. G. Swartz, H. Y. Hwang, L. L. Li, and R. Pentcheva",
        "journal": "Physical Review Materials",
        "year": "2022",
        "url": "https://link.aps.org/doi/10.1103/PhysRevMaterials.6.044802",
    },
    {
        "title": "Substrate dependent terahertz magneto-optical properties of monolayer WS2",
        "authors": "H. M. Dong, Z. H. Tao, Y. F. Duan, L. L. Li, F. Huang, and F. M. Peeters",
        "journal": "Optics Letters",
        "year": "2021",
        "url": "https://opg.optica.org/ol/abstract.cfm?uri=ol-46-19-4892",
    },
    {
        "title": "High performance piezotronic spin transistors using molybdenum disulfide nanoribbon",
        "authors": "X. F. Yan, Q. Chen, L. L. Li, H. Z. Guo, J. Z. Peng, and F. M. Peeters",
        "journal": "Nano Energy",
        "year": "2020",
        "url": "https://www.sciencedirect.com/science/article/pii/S2211285520305103",
    },
    {
        "title": "Substrate dependent terahertz response of monolayer WS2",
        "authors": "H. M. Dong, Z. H. Tao, L. L. Li, F. Huang, W. Xu, and F. M. Peeters",
        "journal": "Applied Physics Letters",
        "year": "2020",
        "url": "https://doi.org/10.1063/5.0006617",
    },
    {
        "title": "Single-layer Janus black arsenic-phosphorus (b-AsP): Optical dichroism, anisotropic vibrational, thermal, and elastic properties",
        "authors": "L. L. Li, C. Bacaksiz, M. Nakhaee, R. Pentcheva, F. M. Peeters, and M. Yagmurcukardes",
        "journal": "Physical Review B",
        "year": "2020",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.101.134102",
    },
    {
        "title": "Inner and outer ring states of MoS2 quantum rings: Energy spectrum, charge and spin currents",
        "authors": "Q. Chen, L. L. Li, and F. M. Peeters",
        "journal": "Journal of Applied Physics",
        "year": "2019",
        "url": "https://doi.org/10.1063/1.5094200",
    },
    {
        "title": "Transport characteristics of multi-terminal pristine and defective phosphorene systems",
        "authors": "N. A. Shah, L. L. Li, V. Mosallanejad, F. M. Peeters, and G. P. Guo",
        "journal": "Nanotechnology",
        "year": "2019",
        "url": "https://doi.org/10.1088/1361-6528/ab3961",
    },
    {
        "title": "Fano resonances in bilayer phosphorene nanoring",
        "authors": "R. Zhang, Z. H. Wu, X. J. Li, L. L. Li, Q. Chen, Y. M. Li, and F. M. Peeters",
        "journal": "Nanotechnology",
        "year": "2018",
        "url": "http://stacks.iop.org/0957-4484/29/i=21/a=215202",
    },
    {
        "title": "Tuning the electronic properties of gated multilayer phosphorene: A self-consistent tight-binding study",
        "authors": "L. L. Li, B. Partoens, and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2018",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.97.155424",
    },
    {
        "title": "Quantum transport in defective phosphorene nanoribbons: Effects of atomic vacancies",
        "authors": "L. L. Li and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2018",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.97.075414",
    },
    {
        "title": "Magnetic field dependence of electronic properties of MoS2 quantum dots with different edges",
        "authors": "Q. Chen, L. L. Li, and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2018",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.97.085437",
    },
    {
        "title": "Electric-field modulation of linear dichroism and Faraday rotation in few-layer phosphorene",
        "authors": "L. L. Li, B. Partoens, W. Xu, and F. M. Peeters",
        "journal": "2D Materials",
        "year": "2018",
        "url": "https://iopscience.iop.org/article/10.1088/2053-1583/aaf47f",
    },
    {
        "title": "Electronic properties of bilayer phosphorene quantum dots in the presence of perpendicular electric and magnetic fields",
        "authors": "L. L. Li, D. Moldovan, W. Xu, and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2017",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.96.155425",
    },
    {
        "title": "Electronic and transport properties of n-type monolayer black phosphorus at low temperatures",
        "authors": "F. W. Han, W. Xu, L. L. Li, C. Zhang, H. M. Dong, and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2017",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.95.115436",
    },
    {
        "title": "Exciton states in a circular graphene quantum dot: Magnetic field induced intravalley to intervalley transition",
        "authors": "L. L. Li, M. Zarenia, W. Xu, H. M. Dong, and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2017",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.95.045409",
    },
    {
        "title": "Enhanced thermoelectric performance of nanostructured topological insulator Bi2Se3",
        "authors": "G. L. Sun, L. L. Li, X. Y. Qin, D. Li, T. H. Zou, H. X. Xin, B. J. Ren, J. Zhang, Y. Y. Li, and X. J. Li",
        "journal": "Applied Physics Letters",
        "year": "2015",
        "url": "https://aip.scitation.org/doi/10.1063/1.4907252",
    },
    {
        "title": "Thermoelectric Transport by Surface States in Bi2Se3-Based Topological Insulator Thin Films",
        "authors": "L. L. Li and W. Xu",
        "journal": "Chinese Physics Letters",
        "year": "2015",
        "url": "http://stacks.iop.org/0256-307X/32/i=4/a=047304",
    },
    {
        "title": "Strong terahertz absorption in long-period InAs/GaSb type-II superlattices with inverted band structures",
        "authors": "L. L. Li, J. Ni, and W. Xu",
        "journal": "Superlattices and Microstructures",
        "year": "2015",
        "url": "http://www.sciencedirect.com/science/article/pii/S0749603614004935",
    },
    {
        "title": "Optical conductivity of topological insulator thin films",
        "authors": "L. L. Li, W. Xu, and F. M. Peeters",
        "journal": "Journal of Applied Physics",
        "year": "2015",
        "url": "https://aip.scitation.org/doi/10.1063/1.4919429",
    },
    {
        "title": "Terahertz plasmon-polariton modes in graphene driven by electric field inside a Fabry-Pérot cavity",
        "authors": "C. X. Zhao, W. Xu, L. L. Li, C. Zhang, and F. M. Peeters",
        "journal": "Journal of Applied Physics",
        "year": "2015",
        "url": "https://aip.scitation.org/doi/10.1063/1.4922401",
    },
    {
        "title": "Effect of microscopic interface asymmetry on optical properties of short-period InAs/GaSb type-II superlattices",
        "authors": "H. M. Dong, L. L. Li, W. Xu, and K. Han",
        "journal": "Thin Solid Films",
        "year": "2015",
        "url": "http://www.sciencedirect.com/science/article/pii/S0040609015006021",
    },
    {
        "title": "Surface plasmon polaritons in a topological insulator embedded in an optical cavity",
        "authors": "L. L. Li and W. Xu",
        "journal": "Applied Physics Letters",
        "year": "2014",
        "url": "https://aip.scitation.org/doi/10.1063/1.4869228",
    },
    {
        "title": "Thermoelectric properties of two-dimensional topological insulators doped with nonmagnetic impurities",
        "authors": "L. L. Li and W. Xu",
        "journal": "Journal of Applied Physics",
        "year": "2014",
        "url": "https://aip.scitation.org/doi/10.1063/1.4886176",
    },
    {
        "title": "Absorption of surface acoustic waves by topological insulator thin films",
        "authors": "L. L. Li and W. Xu",
        "journal": "Applied Physics Letters",
        "year": "2014",
        "url": "https://aip.scitation.org/doi/10.1063/1.4893002",
    },
    {
        "title": "Terahertz plasmon and surface-plasmon modes in cylindrical metallic nanowires",
        "authors": "P. Wu, W. Xu, L. L. Li, T. C. Lu, and W. D. Wu",
        "journal": "Chinese Physics B",
        "year": "2014",
        "url": "http://stacks.iop.org/1674-1056/23/i=10/a=107807",
    },
    {
        "title": "Terahertz plasmon and infrared coupled plasmon-phonon modes in graphene",
        "authors": "H. M. Dong, L. L. Li, W. Y. Wang, S. H. Zhang, C. X. Zhao, and W. Xu",
        "journal": "Physica E",
        "year": "2012",
        "url": "http://www.sciencedirect.com/science/article/pii/S1386947712001865",
    },
    {
        "title": "Two-colour mid-infrared absorption in InAs/GaSb type II and broken-gap quantum wells under gated electric field",
        "authors": "X. F. Wei, L. W. Liu, L. L. Li, and W. Xu",
        "journal": "Solid State Communications",
        "year": "2012",
        "url": "http://www.sciencedirect.com/science/article/pii/S0038109812003018",
    },
    {
        "title": "Polarization-Driven Topological Insulator Transition in a GaN/InN/GaN Quantum Well",
        "authors": "M. S. Miao, Q. Yan, C. G. Van de Walle, W. K. Lou, L. L. Li, and K. Chang",
        "journal": "Physical Review Letters",
        "year": "2012",
        "url": "https://link.aps.org/doi/10.1103/PhysRevLett.109.186803",
    },
    {
        "title": "Understanding the Band Gap, Magnetism, and Kinetics of Graphene Nanostripes in Graphane",
        "authors": "L. F. Huang, X. H. Zheng, G. R. Zhang, L. L. Li, and Z. Zeng",
        "journal": "Journal of Physical Chemistry C",
        "year": "2011",
        "url": "https://doi.org/10.1021/jp208067y",
    },
    {
        "title": "Magneto-optical absorption by InAs/GaSb-based type II and broken-gap quantum well",
        "authors": "L. L. Li, X. H. Zheng, and W. Xu",
        "journal": "Physica E",
        "year": "2010",
        "url": "http://www.sciencedirect.com/science/article/pii/S1386947710002808",
    },
    {
        "title": "Band hybridization and spin-splitting in InAs/AlSb/GaSb type II and broken-gap quantum wells",
        "authors": "W. Xu, L. L. Li, H. M. Dong, G. Gumbs, and P. A. Folkes",
        "journal": "Journal of Applied Physics",
        "year": "2010",
        "url": "https://aip.scitation.org/doi/10.1063/1.3476059",
    },
    {
        "title": "Optoelectronic properties of graphene in the presence of optical phonon scattering",
        "authors": "W. Xu, H. M. Dong, L. L. Li, J. Q. Yao, P. Vasilopoulos, and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2010",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.82.125304",
    },
    {
        "title": "Intrinsic optical anisotropy of [001]-grown short-period InAs/GaSb superlattices",
        "authors": "L. L. Li, W. Xu, and F. M. Peeters",
        "journal": "Physical Review B",
        "year": "2010",
        "url": "https://link.aps.org/doi/10.1103/PhysRevB.82.235422",
    },
    {
        "title": "Midinfrared absorption by InAs/GaSb type-II superlattices",
        "authors": "L. L. Li, W. Xu, J. Zhang, and Y. L. Shi",
        "journal": "Journal of Applied Physics",
        "year": "2009",
        "url": "https://aip.scitation.org/doi/10.1063/1.3058692",
    },
    {
        "title": "Terahertz band-gap in InAs/GaSb type-II superlattices",
        "authors": "L. L. Li, W. Xu, Z. Zeng, A. R. Wright, C. Zhang, J. Zhang, Y. L. Shi, and T. C. Lu",
        "journal": "Microelectronics Journal",
        "year": "2009",
        "url": "http://www.sciencedirect.com/science/article/pii/S0026269208005429",
    },

]

HOBBIES = [
    {
        "title": "🌍 Travelling",
        "description": "I enjoy exploring different places, meeting different people, and learning different cultures.",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    },
    {
        "title": "🏃‍♂️ Sporting",
        "description": "Running, cycling, or anything that gets me relaxing and moving. It freshes mind and boosts energy.",
        "image": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5"
    },
    {
        "title": "📖 Reading",
        "description": "Just reading about random new things, ranging from useful skills to funny stories.",
        "image": "https://images.unsplash.com/photo-1519681393784-d120267933ba"
    },
]
