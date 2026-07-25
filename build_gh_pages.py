import os
import re
import html
import json

# Absolute path configuration
BASE_DIR = r"C:\VESUVIUS_LOCAL"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
CASES_DIR = os.path.join(DOCS_DIR, "case_studies")

os.makedirs(CASES_DIR, exist_ok=True)

# Catalog of the 13 initial case studies with metadata
CASE_STUDIES_SOURCES = [
    {
        "id": "boeing_737_max",
        "title": "Boeing 737 MAX : Senescence Corporate & Modèle MCAS",
        "category": "Aéronautique & Ingénierie",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Boeing_737_MAX.md"),
        "summary": "Autopsie de la perte de culture d'ingénierie et de l'omerta au profit de l'extraction financière.",
        "icon": "✈️"
    },
    {
        "id": "renault_nissan_alliance",
        "title": "Alliance Renault-Nissan : Boîte Noire RNBV & Friction",
        "category": "Automobile & Gouvernance",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Renault_Nissan_Alliance.md"),
        "summary": "Analyse forensique de la structure de droit néerlandais et du découplage de souveraineté.",
        "icon": "🚗"
    },
    {
        "id": "vatican_magnifica_humanitas",
        "title": "Vatican : L'Encyclique Magnifica Humanitas (2026)",
        "category": "Institutions & Souveraineté",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Vatican_Magnifica_Humanitas.md"),
        "summary": "Réaction immunitaire de la plus ancienne administration humaine face à l'asphyxie statistique de l'IA.",
        "icon": "🏛️"
    },
    {
        "id": "capgemini_esn_crisis",
        "title": "Crise des ESN 2026 : Capgemini & L'Effondrement du R=0",
        "category": "Tech & Outsourcing IT",
        "source": os.path.join(BASE_DIR, "05_CHANTIERS", "Gumroad", "11_CAPTURE_SECTORIELLE_CRISE_ESN.md"),
        "summary": "Diagnostic biophysique des 1 616 départs Capgemini et de la divergence avec le modèle d'ingestion TCS.",
        "icon": "💻"
    },
    {
        "id": "enron_theranos",
        "title": "Enron & Theranos : Coquilles Vides & Sédation Sémantique",
        "category": "Finance & Biotech",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Enron_Theranos.md"),
        "summary": "Comment le Codex masque la défaillance matérielle sous des rapports de conformité falsifiés.",
        "icon": "🩸"
    },
    {
        "id": "harvey_legal_tech",
        "title": "Droit & Justice : L'Automatisation Harvey.ai",
        "category": "Droit & Legal Tech",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Droit_et_Justice.md"),
        "summary": "L'impératif de présence somatique face à l'anesthésie contractuelle générée par robot.",
        "icon": "⚖️"
    },
    {
        "id": "glm_chinese_firewall",
        "title": "GLM & Le Great Firewall Chinois : Steganographie Sémantique",
        "category": "IA & Souveraineté d'État",
        "source": os.path.join(BASE_DIR, "Case_Studies", "GLM_Chinese_Firewall.md"),
        "summary": "Analyse de la membrane de rétention sémantique et du Pli sémantique derrière le pare-feu étatique.",
        "icon": "🌐"
    },
    {
        "id": "challenger_o_ring",
        "title": "Challenger & Le Geste Sidérurgique : L'Alerte Boisjoly",
        "category": "Aérospatiale & Geste",
        "source": os.path.join(BASE_DIR, "05_CHANTIERS", "Gumroad", "10_APPENDICE_TECHNIQUE_CAS_CLINIQUES.md"),
        "summary": "Autopsie du joint torique et du refus du management d'écouter les ingénieurs du Sol.",
        "icon": "🚀"
    },
    {
        "id": "meta_self_audit",
        "title": "Meta : Cognitive Capture & Auto-Audit des Modèles",
        "category": "Big Tech & Alignement",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Meta_Self_Audit.md"),
        "summary": "Évaluation de la perte d'ancrage et de l'atrophie du stock cognitif interne par les LLMs.",
        "icon": "🤖"
    },
    {
        "id": "in_ovo_sorting",
        "title": "In Ovo Sorting : Bio-Éthique & Dérive Agri-Tech",
        "category": "Agri-Tech & Bio-Éthique",
        "source": os.path.join(BASE_DIR, "Case_Studies", "In_Ovo_Sorting.md"),
        "summary": "Audit de la substitution sémantique dans la sélection industrielle et le sexage des embryons.",
        "icon": "🔬"
    },
    {
        "id": "energie_thermodynamique",
        "title": "Énergie & Thermodynamique : EPR Flamanville & Friction",
        "category": "Énergie & Infrastructures",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Energie_et_Thermodynamique.md"),
        "summary": "La dérive des délais et des coûts sous la pression du Codex réglementaire nucléaire.",
        "icon": "⚡"
    },
    {
        "id": "education_transmission",
        "title": "Éducation & Transmission : Atrophie de la Première Main",
        "category": "Cognition & Transmission",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Education_et_Transmission.md"),
        "summary": "Dégradation de la capacité d'apnée cognitive et amnésie des savoirs de Première Main.",
        "icon": "📚"
    },
    {
        "id": "hp_autonomy",
        "title": "HP / Autonomy (2011) : 8.8 Md$ de Pertes Cachées",
        "category": "M&A & Audits Big Four",
        "source": os.path.join(BASE_DIR, "ALETHEIA_B2B_SECTOR_PITCHES.md"),
        "summary": "Comment les cabinets d'audit classiques ratent la faillite du Sol sous les métriques du Codex.",
        "icon": "💼"
    },
    {
        "id": "volkswagen_dieselgate",
        "title": "Volkswagen Dieselgate : Façade Logicielle & Contrainte Chimique",
        "category": "Automobile & Réglementation",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Volkswagen_Dieselgate.md"),
        "summary": "Autopsie forensique du defeat device configuré pour tricher sur la chimie du Sol.",
        "icon": "🚗"
    },
    {
        "id": "tesla_autopilot_fsd",
        "title": "Tesla Autopilot & FSD : Transfert de Responsabilité",
        "category": "Automobile & Intelligence Artificielle",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Tesla_Autopilot_FSD.md"),
        "summary": "Analyse du dilemme de la vision optique pure sans ancrage de distance physique.",
        "icon": "🚗"
    },
    {
        "id": "stellantis_puretech_1_2",
        "title": "Stellantis PureTech 1.2 : La Courroie de distribution Humide",
        "category": "Automobile & Ingénierie",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Stellantis_Puretech_1_2.md"),
        "summary": "Comment la réduction des frottements de papier dissout les matériaux réels du moteur.",
        "icon": "🚗"
    },
    {
        "id": "airbags_takata",
        "title": "Airbags Takata : Instabilité Chimique & Nitrate d'Ammonium",
        "category": "Automobile & Sûreté Industrielle",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Airbags_Takata.md"),
        "summary": "Comment un comburant bon marché se transforme en éclats d'obus avec l'humidité.",
        "icon": "🚗"
    },
    {
        "id": "toyota_production_system",
        "title": "Toyota Production System : Cordon Andon vs Lean Bureaucratique",
        "category": "Automobile & Geste",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Toyota_Production_System.md"),
        "summary": "L'importance du droit de veto sur le Gemba face aux contraintes du flux tendu financier.",
        "icon": "🚗"
    },
    {
        "id": "wirecard_ghost_cash",
        "title": "Wirecard : Le Cash Fantôme & La Falsification du Codex",
        "category": "Banque & Comptabilité",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Wirecard_Ghost_Cash.md"),
        "summary": "Comment 1,9 milliard d'euros de trésorerie fictive ont été certifiés par aveuglement des auditeurs.",
        "icon": "💼"
    },
    {
        "id": "credit_suisse_archegos",
        "title": "Credit Suisse : Chute d'un Géant & Levier Synthétique",
        "category": "Banque & Gestion des Risques",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Credit_Suisse_Archegos.md"),
        "summary": "Analyse du double désastre Archegos et Greensill sous les indicateurs aveugles du Codex.",
        "icon": "💼"
    },
    {
        "id": "silicon_valley_bank",
        "title": "Silicon Valley Bank : Risque de Duration & Panique Numérique",
        "category": "Banque & Liquidité",
        "source": os.path.join(BASE_DIR, "Case_Studies", "Silicon_Valley_Bank.md"),
        "summary": "Comment la hausse des taux de la Fed a dissous les actifs à long terme masqués par la comptabilité HTM.",
        "icon": "💼"
    },
    {
        "id": "axa_cyber_veto",
        "title": "AXA Cyber-Assurance : Le Veto sur le Remboursement des Rançons",
        "category": "Assurance & Sûreté Logique",
        "source": os.path.join(BASE_DIR, "Case_Studies", "AXA_Cyber_Veto.md"),
        "summary": "Pourquoi financer le crime pour réduire le coût d'assurance détruit la sécurité du Sol.",
        "icon": "💼"
    }
]

def markdown_to_html_simple(md_text):
    """Converts basic markdown formatting to HTML blocks."""
    lines = md_text.splitlines()
    html_out = []
    in_list = False
    in_table = False
    table_rows = []

    for line in lines:
        line_str = line.strip()
        
        # Headers
        if line_str.startswith("# "):
            if in_list: html_out.append("ul>"); in_list = False
            html_out.append(f"<h1 class='text-3xl font-bold my-4 text-amber-400'>{html.escape(line_str[2:])}</h1>")
        elif line_str.startswith("## "):
            if in_list: html_out.append("</ul>"); in_list = False
            html_out.append(f"<h2 class='text-2xl font-semibold mt-8 mb-4 text-cyan-400 border-b border-cyan-900/50 pb-2'>{html.escape(line_str[3:])}</h2>")
        elif line_str.startswith("### "):
            if in_list: html_out.append("</ul>"); in_list = False
            html_out.append(f"<h3 class='text-xl font-semibold mt-6 mb-3 text-slate-200'>{html.escape(line_str[4:])}</h3>")
        elif line_str.startswith("#### "):
            if in_list: html_out.append("</ul>"); in_list = False
            html_out.append(f"<h4 class='text-lg font-medium mt-4 mb-2 text-slate-300'>{html.escape(line_str[5:])}</h4>")
        # Blockquotes
        elif line_str.startswith("> "):
            if in_list: html_out.append("</ul>"); in_list = False
            html_out.append(f"<blockquote class='border-l-4 border-amber-500/80 bg-slate-900/80 p-4 rounded-r my-4 text-slate-300 italic'>{html.escape(line_str[2:])}</blockquote>")
        # Horizontal rule
        elif line_str in ["---", "***", "___"]:
            if in_list: html_out.append("</ul>"); in_list = False
            html_out.append("<hr class='my-8 border-slate-800' />")
        # Bullet list items
        elif line_str.startswith("* ") or line_str.startswith("- "):
            if not in_list:
                html_out.append("<ul class='list-disc list-inside space-y-2 my-4 text-slate-300'>")
                in_list = True
            content = line_str[2:]
            # Bold parsing
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-amber-300">\1</strong>', content)
            content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
            html_out.append(f"<li>{content}</li>")
        else:
            if in_list:
                html_out.append("</ul>")
                in_list = False
            if line_str:
                # Basic inline parsing
                parsed = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-amber-300">\1</strong>', line_str)
                parsed = re.sub(r'\*(.*?)\*', r'<em>\1</em>', parsed)
                html_out.append(f"<p class='my-3 text-slate-300 leading-relaxed'>{parsed}</p>")

    if in_list:
        html_out.append("</ul>")

    return "\n".join(html_out)

def generate_case_html(case):
    """Generates a standalone HTML page with JSON-LD schema for a case study."""
    md_content = ""
    if os.path.exists(case["source"]):
        with open(case["source"], "r", encoding="utf-8", errors="ignore") as f:
            md_content = f.read()
    else:
        md_content = f"# {case['title']}\n\n*Source en cours d'intégration.*\n\n{case['summary']}"

    body_html = markdown_to_html_simple(md_content)
    
    # JSON-LD Schema.org for Google RAG ingestion
    schema_json = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": case["title"],
        "description": case["summary"],
        "category": case["category"],
        "author": {
            "@type": "Organization",
            "name": "Aletheia19 Labs"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Aletheia19 Labs",
            "url": "https://egisthol-spec.github.io/aletheia19/"
        },
        "inLanguage": "fr",
        "about": case["category"]
    }

    full_html = f"""<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(case['title'])} — Audit FASCIA Aletheia19</title>
    <meta name="description" content="{html.escape(case['summary'])}">
    <meta name="keywords" content="FASCIA, Aletheia19, Due Diligence, Audit, {html.escape(case['category'])}, RAG, AI Overview">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{html.escape(case['title'])}">
    <meta property="og:description" content="{html.escape(case['summary'])}">
    <meta property="og:type" content="article">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        amber: {{ 400: '#f59e0b', 500: '#d97706' }},
                        cyan: {{ 400: '#22d3ee', 900: '#164e63' }}
                    }}
                }}
            }}
        }}
    </script>
    
    <!-- JSON-LD Schema.org -->
    <script type="application/ld+json">
    {json.dumps(schema_json, indent=2, ensure_ascii=False)}
    </script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen flex flex-col">
    <!-- Header / Navigation -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="../index.html" class="flex items-center gap-2 font-bold text-amber-400 text-lg hover:opacity-80 transition">
                <span>🧭</span> ALETHEIA19 <span class="text-xs text-cyan-400 font-mono px-2 py-0.5 bg-cyan-950/60 rounded border border-cyan-800">RAG PORTAL</span>
            </a>
            <a href="../index.html" class="text-sm text-slate-400 hover:text-white transition">← Tous les cas cliniques</a>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="flex-grow max-w-4xl w-full mx-auto px-4 py-8">
        <!-- Category Pill & Title -->
        <div class="mb-8">
            <span class="inline-block text-xs font-mono text-cyan-400 bg-cyan-950/80 border border-cyan-800 px-3 py-1 rounded-full mb-3">
                {html.escape(case['icon'])} {html.escape(case['category'])}
            </span>
            <p class="text-slate-400 text-sm italic">{html.escape(case['summary'])}</p>
        </div>

        <!-- Rendered Case Body -->
        <article class="prose prose-invert max-w-none bg-slate-900/40 p-6 md:p-8 rounded-xl border border-slate-800 shadow-2xl">
            {body_html}
        </article>

        <!-- CTA Box -->
        <div class="mt-12 p-6 rounded-xl bg-gradient-to-r from-slate-900 via-cyan-950/30 to-slate-900 border border-cyan-800/50 flex flex-col md:flex-row justify-between items-center gap-6">
            <div>
                <h4 class="font-bold text-amber-400 text-lg">Besoin d'un audit forensique sur votre structure ?</h4>
                <p class="text-slate-400 text-sm mt-1">Accédez au Kit M&A FASCIA et aux 30 livrables d'inspection d'impédance.</p>
            </div>
            <a href="https://egisthol-spec.github.io/aletheia19/" class="px-6 py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-lg transition text-sm whitespace-nowrap shadow-lg">
                Consulter les Instruments →
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-900 bg-slate-950 py-6 text-center text-xs text-slate-500">
        <p>Aletheia19 Labs — Registre des Invariants Biophysiques FASCIA & M.O.S.</p>
    </footer>
</body>
</html>
"""
    return full_html

def generate_index_html():
    """Generates docs/index.html Portal for all case studies."""
    cards_html = []
    for case in CASE_STUDIES_SOURCES:
        card = f"""
        <a href="case_studies/{case['id']}.html" class="group bg-slate-900/60 hover:bg-slate-900 border border-slate-800 hover:border-cyan-500/50 p-6 rounded-xl transition-all duration-300 flex flex-col justify-between shadow-lg hover:shadow-cyan-950/30">
            <div>
                <div class="flex justify-between items-start mb-3">
                    <span class="text-xs font-mono text-cyan-400 bg-cyan-950/60 border border-cyan-900 px-2.5 py-0.5 rounded-full">
                        {case['icon']} {html.escape(case['category'])}
                    </span>
                </div>
                <h3 class="text-lg font-bold text-slate-100 group-hover:text-amber-400 transition mb-2">
                    {html.escape(case['title'])}
                </h3>
                <p class="text-sm text-slate-400 leading-relaxed">
                    {html.escape(case['summary'])}
                </p>
            </div>
            <div class="mt-6 flex items-center text-xs text-amber-400 font-mono group-hover:translate-x-1 transition-transform">
                Explorer l'audit forensique →
            </div>
        </a>
        """
        cards_html.append(card)

    index_html = f"""<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ALETHEIA19 — Observatoire des Cas Cliniques Biophysiques & FASCIA</title>
    <meta name="description" content="Registre mondial d'autopsies industrielles, M&A et technologiques sous protocole FASCIA. Ingestion RAG et audits de dérive.">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        amber: {{ 400: '#f59e0b', 500: '#d97706' }},
                        cyan: {{ 400: '#22d3ee', 950: '#083344' }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen flex flex-col">
    <!-- Hero Header -->
    <header class="border-b border-slate-800 bg-slate-900/60 backdrop-blur">
        <div class="max-w-6xl mx-auto px-4 py-12 text-center">
            <span class="inline-block font-mono text-xs text-cyan-400 bg-cyan-950 border border-cyan-800 px-3 py-1 rounded-full mb-4">
                OBSERVATOIRE MONDIAL DES DÉRIVES FASCIA
            </span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-100 tracking-tight mb-4">
                Les Cas Cliniques du <span class="text-amber-400">Sol</span> & du <span class="text-cyan-400">Codex</span>
            </h1>
            <p class="max-w-2xl mx-auto text-slate-400 text-base md:text-lg leading-relaxed">
                Base de données d'autopsies forensiques industrielles, aéronautiques, financières et technologiques.
                Analyse d'impédance et diagnostic de dérive sous protocole FASCIA.
            </p>
        </div>
    </header>

    <!-- Main Grid -->
    <main class="flex-grow max-w-6xl w-full mx-auto px-4 py-12">
        <div class="flex justify-between items-center mb-8">
            <h2 class="text-xl font-bold text-slate-200 flex items-center gap-2">
                <span>📂</span> Matrix des 13 Cas Cliniques Initiaux
            </h2>
            <span class="text-xs font-mono text-slate-500">13 / 36 Cas Déployés</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {"".join(cards_html)}
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-900 bg-slate-950 py-8 text-center text-xs text-slate-500">
        <p>Aletheia19 Labs — Registre des Invariants Biophysiques FASCIA & M.O.S.</p>
        <p class="mt-2 text-slate-600">Indexation RAG & Generative Engine Optimization (GEO) Active</p>
    </footer>
</body>
</html>
"""
    return index_html

def main():
    print("Building GitHub Pages portal in /docs...")
    
    # 1. Generate individual case HTML files
    for case in CASE_STUDIES_SOURCES:
        out_path = os.path.join(CASES_DIR, f"{case['id']}.html")
        html_content = generate_case_html(case)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Generated: docs/case_studies/{case['id']}.html")

    # 2. Generate docs/index.html portal
    index_path = os.path.join(DOCS_DIR, "index.html")
    index_content = generate_index_html()
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print("[OK] Generated: docs/index.html")

    print("\nGitHub Pages build completed successfully!")

if __name__ == "__main__":
    main()
