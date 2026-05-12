import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Manzoni & Chavis Lab - Ephys Suite",
    page_icon="🔬",
    layout="wide"
)

# --- NAVIGATION & LANGUE ---
# Note : Streamlit détectera automatiquement les fichiers renommés dans le dossier /pages
lang = st.sidebar.selectbox("Language / Langue", ["Français", "English"])

T = {
    "Français": {
        "title": "Manzoni & Chavis Lab - Ephys Suite",
        "subtitle": "Plateforme intégrée d'analyse électrophysiologique avancée",
        "intro": """
            Cette suite logicielle centralise les outils d'analyse pour l'étude de la plasticité 
            synaptique bidirectionnelle et des dysfonctions neuronales dans les modèles 
            neurodéveloppementaux et neuropsychiatriques (FXS, Reeler, Cocaïne).
        """,
        "module_title": "🧩 Modules d'analyse",
        "ltp_ltd_desc": "**LTP & LTD :** Analyse de la plasticité à long terme, métaplasticité et cinétiques de population.",
        "spike_desc": "**Spike Analysis :** Caractérisation des potentiels d'action et de l'excitabilité intrinsèque.",
        "epsc_desc": "**sEPSC (AMPA) :** Détection multi-échelle et cinétique des courants excitateurs entrants.",
        "ipsc_desc": "**sIPSC (GABA) :** Analyse des courants inhibiteurs avec gestion de la polarité.",
        "footer": "Développé pour le Manzoni & Chavis Lab. Utilisation réservée à la recherche scientifique."
    },
    "English": {
        "title": "Manzoni & Chavis Lab - Ephys Suite",
        "subtitle": "Integrated Advanced Electrophysiology Analysis Platform",
        "intro": """
            This software suite centralizes analysis tools for studying bidirectional synaptic 
            plasticity and neuronal dysfunction in neurodevelopmental and neuropsychiatric 
            models (FXS, Reeler, Cocaine).
        """,
        "module_title": "🧩 Analysis Modules",
        "ltp_ltd_desc": "**LTP & LTD:** Analysis of long-term plasticity, metaplasticity, and population kinetics.",
        "spike_desc": "**Spike Analysis:** Action potential characterization and intrinsic excitability.",
        "epsc_desc": "**sEPSC (AMPA):** Multi-scale detection and kinetics of inward excitatory currents.",
        "ipsc_desc": "**sIPSC (GABA):** Inhibitory current analysis with polarity management.",
        "footer": "Developed for the Manzoni & Chavis Lab. For scientific research use only."
    }
}[lang]

# --- EN-TÊTE ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        # Assurez-vous que le logo est bien à la racine du dossier
        st.image("logo_chavis_final.png", width=180)
    except:
        st.write("🔬")

with col_title:
    st.title(T["title"])
    st.markdown(f"*{T['subtitle']}*")

st.divider()

# --- CORPS DE LA PAGE ---
st.markdown(f"### {T['intro']}")

col1, col2 = st.columns(2)

with col1:
    st.info(f"### {T['module_title']}")
    # Mise à jour des descriptions selon la nouvelle nomenclature
    st.write(T["ltp_ltd_desc"])
    st.write(T["spike_desc"])
    st.write(T["epsc_desc"])
    st.write(T["ipsc_desc"])

with col2:
    st.success("### 🎓 Citation & Research")
    st.markdown("""
        **Focus de Recherche :** Plasticité Synaptique, architectures Transformer-Tensor, 
        et modèles pathologiques spécifiques (FXS, Reeler, Cocaïne).
        
        **Open Science :**
        Si vous utilisez ces outils pour vos publications, merci de citer le DOI suivant :
    """)
    st.markdown("[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)")

st.divider()

# --- SECTION MÉTHODOLOGIQUE ---
with st.expander("🔬 Core Methodology / Méthodologie" if lang=="English" else "🔬 Méthodologie"):
    st.markdown("""
    Cette plateforme garantit une rigueur analytique conforme aux standards de *Science* et *Nature* :
    * **Analyse LTP/LTD :** Normalisation rigoureuse de la ligne de base et analyse des pentes (slopes) d'fEPSP.
    * **Filtrage Expert :** Utilisation de filtres de Bessel (ordre 4) pour préserver l'intégrité temporelle des signaux.
    * **Détection Multi-échelles :** Algorithmes de corrélation croisée (Z-Score) pour capturer l'hétérogénéité des événements.
    * **Correction Dynamique :** Detrending par filtre médian glissant pour stabiliser les dérives de ligne de base.
    """)

st.caption(T["footer"])
