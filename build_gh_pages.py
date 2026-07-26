import os
import re
import html
import json
from datetime import datetime, timezone

# Absolute path configuration
BASE_DIR = r"C:\VESUVIUS_LOCAL"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DOCS_EN_DIR = os.path.join(DOCS_DIR, "en")
CASES_FR_DIR = os.path.join(DOCS_DIR, "case_studies")
CASES_EN_DIR = os.path.join(DOCS_EN_DIR, "case_studies")

# Public URL base for canonical/hreflang (GitHub Pages)
SITE_BASE_URL = "https://egisthol-spec.github.io/aletheia19"

os.makedirs(CASES_FR_DIR, exist_ok=True)
os.makedirs(CASES_EN_DIR, exist_ok=True)

# Catalog of the 36 case studies with bilingual metadata
CASE_STUDIES_SOURCES = [
    {
        "id": "boeing_737_max",
        "icon": "✈️",
        "fr": {
            "title": "Boeing 737 MAX : Senescence Corporate & Modèle MCAS",
            "category": "Aéronautique & Ingénierie",
            "summary": "Autopsie de la perte de culture d'ingénierie et de l'omerta au profit de l'extraction financière.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Boeing_737_MAX_V2.md")
        },
        "en": {
            "title": "Boeing 737 MAX: Corporate Senescence & MCAS Model",
            "category": "Aeronautics & Engineering",
            "summary": "Autopsy of engineering culture loss and secrecy for short-term financial extraction.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Boeing_737_MAX_EN_V2.md")
        }
    },
    {
        "id": "renault_nissan_alliance",
        "icon": "🚗",
        "fr": {
            "title": "Alliance Renault-Nissan : Boîte Noire RNBV & Friction",
            "category": "Automobile & Gouvernance",
            "summary": "Analyse forensique de la structure de droit néerlandais et du découplage de souveraineté.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Renault_Nissan_Alliance_V2.md")
        },
        "en": {
            "title": "Renault-Nissan Alliance: RNBV Black Box & Friction",
            "category": "Automotive & Governance",
            "summary": "Forensic analysis of the Dutch entity structure and sovereignty decoupling.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Renault_Nissan_Alliance_EN_V2.md")
        }
    },
    {
        "id": "vatican_magnifica_humanitas",
        "icon": "🏛️",
        "fr": {
            "title": "Vatican : L'Encyclique Magnifica Humanitas (2026)",
            "category": "Institutions & Souveraineté",
            "summary": "Réaction immunitaire de la plus ancienne administration humaine face à l'asphyxie statistique de l'IA.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Vatican_Magnifica_Humanitas.md")
        },
        "en": {
            "title": "Vatican: Encyclical Magnifica Humanitas (2026)",
            "category": "Institutions & Sovereignty",
            "summary": "Immune response of humanity's oldest administration against statistical AI asphyxiation.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Vatican_Magnifica_Humanitas_EN.md")
        }
    },
    {
        "id": "turquie_seisme_2023",
        "icon": "🏢",
        "fr": {
            "title": "Turquie (2023) : Le Séisme de Kahramanmaraş",
            "category": "Sûreté Civile & Infrastructures",
            "summary": "Comment l'amnistie de zonage (imar barışı) a simulé la conformité par décret politique en déniant la physique.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Turquie_Seisme_2023_V2.md")
        },
        "en": {
            "title": "Turkey (2023): The Kahramanmaraş Earthquake",
            "category": "Civil Safety & Infrastructure",
            "summary": "How zoning amnesties (imar barışı) simulated compliance by decree while ignoring physical laws.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Turquie_Seisme_2023_EN_V2.md")
        }
    },
    {
        "id": "enron_theranos",
        "icon": "🩸",
        "fr": {
            "title": "Enron & Theranos : Coquilles Vides & Sédation Sémantique",
            "category": "Finance & Biotech",
            "summary": "Comment le Codex masque la défaillance matérielle sous des rapports de conformité falsifiés.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Enron_Theranos_V2.md")
        },
        "en": {
            "title": "Enron & Theranos: Empty Shells & Semantic Sedation",
            "category": "Finance & Biotech",
            "summary": "How the Codex hides material failure behind falsified compliance reporting.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Enron_Theranos_EN_V2.md")
        }
    },
    {
        "id": "harvey_legal_tech",
        "icon": "⚖️",
        "fr": {
            "title": "Droit & Justice : L'Automatisation Harvey.ai",
            "category": "Droit & Legal Tech",
            "summary": "L'impératif de présence somatique face à l'anesthésie contractuelle générée par robot.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Droit_et_Justice_V2.md")
        },
        "en": {
            "title": "Law & Justice: Harvey.ai Automation",
            "category": "Law & Legal Tech",
            "summary": "The imperative of somatic presence face to robot-generated contract anesthesia.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Droit_et_Justice_EN_V2.md")
        }
    },
    {
        "id": "glm_chinese_firewall",
        "icon": "🌐",
        "fr": {
            "title": "GLM & Le Great Firewall Chinois : Steganographie Sémantique",
            "category": "IA & Souveraineté d'État",
            "summary": "Analyse de la membrane de rétention sémantique et du Pli sémantique derrière le pare-feu étatique.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "GLM_Chinese_Firewall.md")
        },
        "en": {
            "title": "GLM & Chinese Great Firewall: Semantic Steganography",
            "category": "AI & State Sovereignty",
            "summary": "Analysis of the semantic retention membrane and the Semantic Fold behind GFW.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "GLM_Chinese_Firewall_EN.md")
        }
    },
    {
        "id": "challenger_o_ring",
        "icon": "🚀",
        "fr": {
            "title": "Challenger & Le Geste Sidérurgique : L'Alerte Boisjoly",
            "category": "Aérospatiale & Geste",
            "summary": "Autopsie du joint torique et du refus du management d'écouter les ingénieurs du Sol.",
            "source": os.path.join(BASE_DIR, "05_CHANTIERS", "Gumroad", "10_APPENDICE_TECHNIQUE_CAS_CLINIQUES.md")
        },
        "en": {
            "title": "Challenger & The Steelworker's Craft: The Boisjoly Alert",
            "category": "Aerospace & Craft",
            "summary": "Autopsy of the O-ring and management's refusal to listen to ground engineers.",
            "source": os.path.join(BASE_DIR, "05_CHANTIERS", "Gumroad", "10_THE_5_CLINICAL_CASES.md")
        }
    },
    {
        "id": "meta_self_audit",
        "icon": "🤖",
        "fr": {
            "title": "Meta : Cognitive Capture & Auto-Audit des Modèles",
            "category": "Big Tech & Alignement",
            "summary": "Évaluation de la perte d'ancrage et de l'atrophie du stock cognitif interne par les LLMs.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Meta_Self_Audit.md")
        },
        "en": {
            "title": "Meta: Cognitive Capture & Model Self-Audit",
            "category": "Big Tech & Alignment",
            "summary": "Evaluation of ground loss and internal cognitive stock atrophy by LLMs.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Meta_Self_Audit_EN.md")
        }
    },
    {
        "id": "in_ovo_sorting",
        "icon": "🔬",
        "fr": {
            "title": "In Ovo Sorting : Bio-Éthique & Dérive Agri-Tech",
            "category": "Agri-Tech & Bio-Éthique",
            "summary": "Audit de la substitution sémantique dans la sélection industrielle et le sexage des embryons.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "In_Ovo_Sorting.md")
        },
        "en": {
            "title": "In Ovo Sorting: Bio-Ethics & Agri-Tech Drift",
            "category": "Agri-Tech & Bio-Ethics",
            "summary": "Audit of semantic substitution in industrial selection and embryo sexing.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "In_Ovo_Sorting_EN.md")
        }
    },
    {
        "id": "energie_thermodynamique",
        "icon": "⚡",
        "fr": {
            "title": "Énergie & Thermodynamique : EPR Flamanville & Friction",
            "category": "Énergie & Infrastructures",
            "summary": "La dérive des délais et des coûts sous la pression du Codex réglementaire nucléaire.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Energie_et_Thermodynamique_V2.md")
        },
        "en": {
            "title": "Energy & Thermodynamics: EPR Flamanville & Friction",
            "category": "Energy & Infrastructures",
            "summary": "Schedule and cost drifts under the pressure of nuclear regulatory Codex.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Energie_et_Thermodynamique_EN_V2.md")
        }
    },
    {
        "id": "education_transmission",
        "icon": "📚",
        "fr": {
            "title": "Éducation & Transmission : Atrophie de la Première Main",
            "category": "Cognition & Transmission",
            "summary": "Dégradation de la capacité d'apnée cognitive et amnésie des savoirs de Première Main.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Education_et_Transmission_V2.md")
        },
        "en": {
            "title": "Education & Transmission: Atrophy of the First-Hand",
            "category": "Cognition & Transmission",
            "summary": "Degradation of cognitive apnea capacity and amnesia of First-Hand knowledge.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Education_et_Transmission_EN_V2.md")
        }
    },
    {
        "id": "hp_autonomy",
        "icon": "💼",
        "fr": {
            "title": "HP / Autonomy (2011) : 8.8 Md$ de Pertes Cachées",
            "category": "M&A & Audits Big Four",
            "summary": "Comment les cabinets d'audit classiques ratent la faillite du Sol sous les métriques du Codex.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "HP_Autonomy_V2.md")
        },
        "en": {
            "title": "HP / Autonomy (2011): $8.8B Hidden Losses",
            "category": "M&A & Big Four Audits",
            "summary": "How traditional audit firms miss ground insolvency under Codex metrics.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "HP_Autonomy_EN_V2.md")
        }
    },
    {
        "id": "volkswagen_dieselgate",
        "icon": "🚗",
        "fr": {
            "title": "Volkswagen Dieselgate : Façade Logicielle & Contrainte Chimique",
            "category": "Automobile & Réglementation",
            "summary": "Autopsie forensique du defeat device configuré pour tricher sur la chimie du Sol.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Volkswagen_Dieselgate.md")
        },
        "en": {
            "title": "Volkswagen Dieselgate: Software Façade & Chemical Constraints",
            "category": "Automotive & Regulation",
            "summary": "Forensic autopsy of defeat devices configured to cheat on real-world NOx chemistry.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Volkswagen_Dieselgate_EN.md")
        }
    },
    {
        "id": "tesla_autopilot_fsd",
        "icon": "🚗",
        "fr": {
            "title": "Tesla Autopilot & FSD : Transfert de Responsabilité",
            "category": "Automobile & IA",
            "summary": "Analyse du dilemme de la vision optique pure sans ancrage de distance physique.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Tesla_Autopilot_FSD.md")
        },
        "en": {
            "title": "Tesla Autopilot & FSD: Liability Transfer & Vision Dilemma",
            "category": "Automotive & AI",
            "summary": "Analysis of pure optical vision without physical depth grounding.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Tesla_Autopilot_FSD_EN.md")
        }
    },
    {
        "id": "stellantis_puretech_1_2",
        "icon": "🚗",
        "fr": {
            "title": "Stellantis PureTech 1.2 : La Courroie de distribution Humide",
            "category": "Automobile & Ingénierie",
            "summary": "Comment la réduction des frottements de papier dissout les matériaux réels du moteur.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Stellantis_Puretech_1_2.md")
        },
        "en": {
            "title": "Stellantis PureTech 1.2: Wet Timing Belt Dissolution",
            "category": "Automotive & Engineering",
            "summary": "How paper friction reduction dissolves real engine materials.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Stellantis_Puretech_1_2_EN.md")
        }
    },
    {
        "id": "airbags_takata",
        "icon": "🚗",
        "fr": {
            "title": "Airbags Takata : Instabilité Chimique & Nitrate d'Ammonium",
            "category": "Automobile & Sûreté",
            "summary": "Comment un comburant bon marché se transforme en éclats d'obus avec l'humidité.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Airbags_Takata.md")
        },
        "en": {
            "title": "Takata Airbags: Chemical Instability & Ammonium Nitrate",
            "category": "Automotive & Industrial Safety",
            "summary": "How a cheap propellant turns into lethal shrapnel under ambient humidity.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Airbags_Takata_EN.md")
        }
    },
    {
        "id": "toyota_production_system",
        "icon": "🚗",
        "fr": {
            "title": "Toyota Production System : Cordon Andon vs Lean Bureaucratique",
            "category": "Automobile & Geste",
            "summary": "L'importance du droit de veto sur le Gemba face aux contraintes du flux tendu financier.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Toyota_Production_System.md")
        },
        "en": {
            "title": "Toyota Production System: Andon Cord vs Bureaucratic Lean",
            "category": "Automotive & Craft",
            "summary": "The importance of ground veto rights on the Gemba face to financial lean constraints.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Toyota_Production_System_EN.md")
        }
    },
    {
        "id": "wirecard_ghost_cash",
        "icon": "💼",
        "fr": {
            "title": "Wirecard : Le Cash Fantôme & La Falsification du Codex",
            "category": "Banque & Comptabilité",
            "summary": "Comment 1,9 milliard d'euros de trésorerie fictive ont été certifiés par aveuglement des auditeurs.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Wirecard_Ghost_Cash.md")
        },
        "en": {
            "title": "Wirecard: Ghost Cash & Auditor Blindness",
            "category": "Banking & Accounting",
            "summary": "How €1.9 billion in non-existent escrow cash was certified by EY auditors.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Wirecard_Ghost_Cash_EN.md")
        }
    },
    {
        "id": "credit_suisse_archegos",
        "icon": "💼",
        "fr": {
            "title": "Credit Suisse : Chute d'un Géant & Levier Synthétique",
            "category": "Banque & Risques",
            "summary": "Analyse du double désastre Archegos et Greensill sous les indicateurs aveugles du Codex.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Credit_Suisse_Archegos.md")
        },
        "en": {
            "title": "Credit Suisse: Collapse of a Giant & Synthetic Leverage",
            "category": "Banking & Risk Management",
            "summary": "Analysis of the double Greensill and Archegos disaster under blind risk metrics.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Credit_Suisse_Archegos_EN.md")
        }
    },
    {
        "id": "silicon_valley_bank",
        "icon": "💼",
        "fr": {
            "title": "Silicon Valley Bank : Risque de Duration & Panique Numérique",
            "category": "Banque & Liquidité",
            "summary": "Comment la hausse des taux de la Fed a dissous les actifs à long terme masqués par la comptabilité HTM.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Silicon_Valley_Bank.md")
        },
        "en": {
            "title": "Silicon Valley Bank: Duration Risk & Digital Bank Run",
            "category": "Banking & Liquidity",
            "summary": "How Fed rate hikes dissolved long-term assets hidden by HTM accounting.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Silicon_Valley_Bank_EN.md")
        }
    },
    {
        "id": "axa_cyber_veto",
        "icon": "💼",
        "fr": {
            "title": "AXA Cyber-Assurance : Le Veto sur le Remboursement des Rançons",
            "category": "Assurance & Sûreté",
            "summary": "Pourquoi financer le crime pour réduire le coût d'assurance détruit la sécurité du Sol.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "AXA_Cyber_Veto.md")
        },
        "en": {
            "title": "AXA Cyber-Insurance: The Ransomware Reimbursement Veto",
            "category": "Insurance & Logical Safety",
            "summary": "Why funding extortion to reduce insurance costs destroys real ground security.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "AXA_Cyber_Veto_EN.md")
        }
    },
    {
        "id": "fukushima_tsunami_wall",
        "icon": "⚡",
        "fr": {
            "title": "Fukushima Daiichi : Le Mur de protection & Noyade Électrique",
            "category": "Énergie & Sûreté",
            "summary": "Comment l'insuffisance géométrique de la digue a noyé les générateurs diesel de secours.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Fukushima_Tsunami_Wall.md")
        },
        "en": {
            "title": "Fukushima Daiichi: Sea Wall Failure & Emergency Power Flooding",
            "category": "Energy & Nuclear Safety",
            "summary": "How geometric sea wall inadequacy flooded backup diesel generators.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Fukushima_Tsunami_Wall_EN.md")
        }
    },
    {
        "id": "texas_power_grid_ercot",
        "icon": "⚡",
        "fr": {
            "title": "Réseau Électrique Texas : Tempête Uri & Dérégulation",
            "category": "Énergie & Infrastructures",
            "summary": "L'échec d'un marché d'énergie dérégulé sans obligation physique d'isolation thermique.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Texas_Power_Grid_ERCOT.md")
        },
        "en": {
            "title": "Texas Power Grid: Storm Uri & Deregulation Freeze",
            "category": "Energy & Infrastructures",
            "summary": "The failure of a deregulated energy market without physical winterization mandates.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Texas_Power_Grid_ERCOT_EN.md")
        }
    },
    {
        "id": "crowdstrike_kernel_crash",
        "icon": "💻",
        "fr": {
            "title": "CrowdStrike Outage : Injection de Code & Panique Noyau",
            "category": "Sûreté & Noyau OS",
            "summary": "Comment un fichier de configuration corrompu poussé au Ring 0 a paralysé l'infrastructure mondiale.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "CrowdStrike_Kernel_Crash.md")
        },
        "en": {
            "title": "CrowdStrike Outage: Invalid Memory Injection & Kernel Panic",
            "category": "Logical Safety & OS Kernel",
            "summary": "How a corrupt Channel File pushed to Ring 0 paralyzed global infrastructure.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "CrowdStrike_Kernel_Crash_EN.md")
        }
    },
    {
        "id": "purdue_pharma_oxycontin",
        "icon": "🔬",
        "fr": {
            "title": "Purdue Pharma OxyContin : Libération Prolongée & Addiction",
            "category": "Santé & Pharmacologie",
            "summary": "Comment l'enrobage retardé du Codex a été pulvérisé par la réalité neurobiologique du Sol.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Purdue_Pharma_Oxycontin.md")
        },
        "en": {
            "title": "Purdue Pharma OxyContin: Delayed Release & Opioid Addiction",
            "category": "Healthcare & Pharmacology",
            "summary": "How the delayed-release coating Codex was shattered by neurobiological reality.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Purdue_Pharma_Oxycontin_EN.md")
        }
    },
    {
        "id": "philips_cpap_respirators",
        "icon": "🔬",
        "fr": {
            "title": "Respirateurs Philips : Usure de Mousse & Inhalation Toxique",
            "category": "Santé & Sûreté Médicale",
            "summary": "Comment la dégradation thermique de la mousse PE-PUR a projeté des particules dans les poumons.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Philips_CPAP_Respirators.md")
        },
        "en": {
            "title": "Philips Respirators: Foam Degradation & Toxic Inhalation",
            "category": "Healthcare & Medical Safety",
            "summary": "How thermal degradation of PE-PUR foam projected particles into patient lungs.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Philips_CPAP_Respirators_EN.md")
        }
    },
    {
        "id": "ibm_watson_health",
        "icon": "🔬",
        "fr": {
            "title": "IBM Watson Oncology : Recommandations Cliniques Fictives",
            "category": "Santé & IA",
            "summary": "Comment un entraînement sur des scénarios synthétiques a déconnecté la machine du réel médical.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "IBM_Watson_Health.md")
        },
        "en": {
            "title": "IBM Watson Oncology: Synthetic Recommendations & Clinical Failure",
            "category": "Healthcare & AI",
            "summary": "How training on synthetic scenarios disconnected AI from real oncology.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "IBM_Watson_Health_EN.md")
        }
    },
    {
        "id": "thalidomide_grunenthal",
        "icon": "🔬",
        "fr": {
            "title": "Thalidomide Grünenthal : Chiralité Moléculaire & Veto de Sûreté",
            "category": "Santé & Réglementation",
            "summary": "Comment la racémisation in vivo a déjoué le Codex de sécurité de la firme et déclenché un veto historique de la FDA.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Thalidomide_Grunenthal.md")
        },
        "en": {
            "title": "Thalidomide Grünenthal: Molecular Chirality & Safety Veto",
            "category": "Healthcare & Regulation",
            "summary": "How in vivo racemization bypassed the firm's safety Codex and triggered a historic FDA veto.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Thalidomide_Grunenthal_EN.md")
        }
    },
    {
        "id": "atos_restructuring",
        "icon": "💻",
        "fr": {
            "title": "Atos : Autophagie Financière & Dette de Refinancement",
            "category": "Tech & Restructuration",
            "summary": "Comment la scission théorique a détruit la confiance des clients et vidé le Sol de sa trésorerie.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Atos_Restructuring.md")
        },
        "en": {
            "title": "Atos: Financial Autophagy & Refinancing Debt Collapse",
            "category": "Tech & Restructuring",
            "summary": "How theoretical splitting destroyed client confidence and drained cash.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Atos_Restructuring_EN.md")
        }
    },
    {
        "id": "openai_board_coup",
        "icon": "🤖",
        "fr": {
            "title": "OpenAI Board Coup : Conseil Non-Profit vs Écosystème d'Affaires",
            "category": "IA & Gouvernance Corporate",
            "summary": "Pourquoi les statuts éthiques du Codex échouent sans souveraineté sur l'infrastructure physique.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "OpenAI_Board_Coup.md")
        },
        "en": {
            "title": "OpenAI Board Coup: Non-Profit Board vs Commercial Ecosystem",
            "category": "AI & Corporate Governance",
            "summary": "Why ethical bylaws fail without sovereignty over physical GPU infrastructure.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "OpenAI_Board_Coup_EN.md")
        }
    },
    {
        "id": "eu_ai_act_enclosure",
        "icon": "🏛️",
        "fr": {
            "title": "EU AI Act : Enclosure Bureaucratique & Colonisation Numérique",
            "category": "Institutions & Souveraineté",
            "summary": "Comment la surrégulation réglementaire élimine l'innovation locale au profit des Big Tech US.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "EU_AI_Act_Enclosure.md")
        },
        "en": {
            "title": "EU AI Act: Bureaucratic Enclosure & Digital Colonization",
            "category": "Institutions & Sovereignty",
            "summary": "How regulatory overreach eliminates local European open-source innovation.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "EU_AI_Act_Enclosure_EN.md")
        }
    },
    {
        "id": "justice_dematerialisation_pnl",
        "icon": "🏛️",
        "fr": {
            "title": "Dématérialisation Justice : Perte d'Ancrage Somatique",
            "category": "Institutions & Souveraineté",
            "summary": "L'impact des procès en visio et de la prédiction statistique sur les droits de la défense.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Justice_Dematerialisation_PNL.md")
        },
        "en": {
            "title": "Justice Digitization: Loss of Somatic Grounding",
            "category": "Institutions & Sovereignty",
            "summary": "The impact of video trials and predictive algorithms on defence rights.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Justice_Dematerialisation_PNL_EN.md")
        }
    },
    {
        "id": "la_poste_timbre_rouge",
        "icon": "🏛️",
        "fr": {
            "title": "La Poste : e-Lettre Rouge & Rupture du Secret Postaux",
            "category": "Institutions & Souveraineté",
            "summary": "Pourquoi l'impression locale des courriels par des facteurs tiers détruit l'intimité du pli.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "La_Poste_Timbre_Rouge.md")
        },
        "en": {
            "title": "La Poste: e-Red Letter & Rupture of Postal Privacy",
            "category": "Institutions & Sovereignty",
            "summary": "Why local printing of private emails by postmen destroys correspondence privacy.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "La_Poste_Timbre_Rouge_EN.md")
        }
    },
    {
        "id": "general_electric_welchism",
        "icon": "🏛️",
        "fr": {
            "title": "General Electric : Jack Welch & Autophagie Industrielle",
            "category": "Industrie & Financiarisation",
            "summary": "Comment le lissage des bénéfices trimestriels par GE Capital a atrophié le Sol de Belfort.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "General_Electric_Welchism.md")
        },
        "en": {
            "title": "General Electric: Jack Welch & Industrial Autophagy",
            "category": "Industry & Financialization",
            "summary": "How quarterly earnings smoothing by GE Capital atrophiated engineering assets.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "General_Electric_Welchism_EN.md")
        }
    },
    {
        "id": "alstom_ge_acquisition",
        "icon": "🏛️",
        "fr": {
            "title": "Rachat Alstom Energy : Capture FCPA & Turbines Arabelle",
            "category": "Institutions & Souveraineté",
            "summary": "Comment le droit extraterritorial américain (DoJ) a dépossédé la France de ses turbines nucléaires.",
            "source": os.path.join(BASE_DIR, "Case_Studies", "Alstom_GE_Acquisition.md")
        },
        "en": {
            "title": "Alstom Energy Sale: FCPA Extraterritorial Capture & Arabelle Turbines",
            "category": "Institutions & Sovereignty",
            "summary": "How US extraterritorial law (DoJ) dispossessed France of its nuclear turbines.",
            "source": os.path.join(BASE_DIR, "Case_Studies_EN", "Alstom_GE_Acquisition_EN.md")
        }
    }
]

def markdown_to_html_simple(md_text):
    """Converts basic markdown formatting to HTML blocks with support for grouped blockquotes and alert styles."""
    lines = md_text.splitlines()
    html_out = []
    in_list = False
    in_quote = False
    quote_lines = []

    def flush_quote():
        nonlocal in_quote, quote_lines
        if not in_quote:
            return
        
        # Default styling for a blockquote
        alert_class = "border-l-4 border-slate-700 bg-slate-900/60 p-4 rounded-r my-4 text-slate-300"
        
        clean_lines = []
        is_alert = False
        alert_type = "NOTE"
        
        for ql in quote_lines:
            ql_strip = ql.strip()
            if ql_strip.startswith("[!IMPORTANT]"):
                is_alert = True
                alert_type = "IMPORTANT"
            elif ql_strip.startswith("[!NOTE]"):
                is_alert = True
                alert_type = "NOTE"
            elif ql_strip.startswith("[!WARNING]"):
                is_alert = True
                alert_type = "WARNING"
            elif ql_strip.startswith("[!TIP]"):
                is_alert = True
                alert_type = "TIP"
            elif ql_strip.startswith("[!CAUTION]"):
                is_alert = True
                alert_type = "CAUTION"
            else:
                clean_lines.append(ql)
        
        if is_alert:
            if alert_type == "IMPORTANT":
                alert_class = "border-l-4 border-amber-500 bg-amber-950/25 p-5 rounded-r my-5 text-slate-200"
            elif alert_type == "WARNING":
                alert_class = "border-l-4 border-red-500 bg-red-950/25 p-5 rounded-r my-5 text-slate-200"
            elif alert_type == "TIP":
                alert_class = "border-l-4 border-emerald-500 bg-emerald-950/25 p-5 rounded-r my-5 text-slate-200"
            elif alert_type == "CAUTION":
                alert_class = "border-l-4 border-rose-600 bg-rose-950/30 p-5 rounded-r my-5 text-slate-200"
            else: # NOTE
                alert_class = "border-l-4 border-cyan-500 bg-cyan-950/25 p-5 rounded-r my-5 text-slate-200"
        
        quote_html = []
        q_in_list = False
        for ql in clean_lines:
            ql_str = ql.strip()
            if ql_str.startswith("* ") or ql_str.startswith("- "):
                if not q_in_list:
                    quote_html.append("<ul class='list-disc list-inside space-y-1.5 my-2 text-slate-300'>")
                    q_in_list = True
                content = ql_str[2:]
                content = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-amber-300">\1</strong>', content)
                content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
                quote_html.append(f"<li>{content}</li>")
            else:
                if q_in_list:
                    quote_html.append("</ul>")
                    q_in_list = False
                if ql_str:
                    parsed = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-amber-300">\1</strong>', ql_str)
                    parsed = re.sub(r'\*(.*?)\*', r'<em>\1</em>', parsed)
                    quote_html.append(f"<p class='my-2 leading-relaxed'>{parsed}</p>")
        if q_in_list:
            quote_html.append("</ul>")
            
        inner_content = "\n".join(quote_html)
        html_out.append(f"<blockquote class='{alert_class}'>{inner_content}</blockquote>")
        
        quote_lines.clear()
        in_quote = False

    for line in lines:
        line_str = line.strip()
        
        # Check if line is part of a blockquote
        if line.startswith(">"):
            content = line[1:]
            if content.startswith(" "):
                content = content[1:]
            
            if in_list: 
                html_out.append("</ul>")
                in_list = False
            
            in_quote = True
            quote_lines.append(content)
            continue
        else:
            if in_quote:
                flush_quote()
        
        # Headers
        if line_str.startswith("# "):
            if in_list: html_out.append("</ul>"); in_list = False
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
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-amber-300">\1</strong>', content)
            content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
            html_out.append(f"<li>{content}</li>")
        else:
            if in_list:
                html_out.append("</ul>")
                in_list = False
            if line_str:
                parsed = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-amber-300">\1</strong>', line_str)
                parsed = re.sub(r'\*(.*?)\*', r'<em>\1</em>', parsed)
                html_out.append(f"<p class='my-3 text-slate-300 leading-relaxed'>{parsed}</p>")

    if in_quote:
        flush_quote()
        
    if in_list:
        html_out.append("</ul>")

    return "\n".join(html_out)

def generate_case_html(case, lang="fr"):
    """Generates a standalone HTML page with JSON-LD schema for a case study in FR or EN."""
    data = case[lang]
    is_en = (lang == "en")
    
    md_content = ""
    if os.path.exists(data["source"]):
        with open(data["source"], "r", encoding="utf-8", errors="ignore") as f:
            md_content = f.read()
    else:
        md_content = f"# {data['title']}\n\n*{'Source currently being processed.' if is_en else 'Source en cours de préparation.'}*\n\n{data['summary']}"

    body_html = markdown_to_html_simple(md_content)
    
    # Toggle links
    lang_toggle_link = f"../en/case_studies/{case['id']}.html" if not is_en else f"../../case_studies/{case['id']}.html"
    lang_toggle_label = "🇬🇧 English" if not is_en else "🇫🇷 Français"
    back_link = "../index.html" if not is_en else "../index.html"
    back_label = "← Tous les cas cliniques" if not is_en else "← All Case Studies"
    cta_title = "Besoin d'un audit forensique sur votre structure ?" if not is_en else "Need a forensic audit for your organization?"
    cta_desc = "Accédez au Kit M&A FASCIA et aux 36 livrables d'inspection d'impédance." if not is_en else "Access the FASCIA M&A Kit and 36 impedance inspection deliverables."
    cta_btn = "Consulter les Instruments →" if not is_en else "View Instruments →"

    schema_json = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": data["title"],
        "description": data["summary"],
        "category": data["category"],
        "author": {
            "@type": "Organization",
            "name": "Aletheia19 Labs"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Aletheia19 Labs",
            "url": "https://egisthol-spec.github.io/aletheia19/"
        },
        "inLanguage": lang,
        "about": data["category"]
    }

    full_html = f"""<!DOCTYPE html>
<html lang="{lang}" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(data['title'])} — Audit FASCIA Aletheia19</title>
    <meta name="description" content="{html.escape(data['summary'])}">
    <meta name="keywords" content="FASCIA, Aletheia19, Due Diligence, Audit, {html.escape(data['category'])}, RAG, AI Overview">
    
    <link rel="canonical" href="{SITE_BASE_URL}/{'en/' if is_en else ''}case_studies/{case['id']}.html" />
    <link rel="alternate" hreflang="fr" href="{SITE_BASE_URL}/case_studies/{case['id']}.html" />
    <link rel="alternate" hreflang="en" href="{SITE_BASE_URL}/en/case_studies/{case['id']}.html" />
    <link rel="alternate" hreflang="x-default" href="{SITE_BASE_URL}/case_studies/{case['id']}.html" />
    
    <meta property="og:title" content="{html.escape(data['title'])}">
    <meta property="og:description" content="{html.escape(data['summary'])}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{SITE_BASE_URL}/{'en/' if is_en else ''}case_studies/{case['id']}.html">
    
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
    
    <script type="application/ld+json">
    {json.dumps(schema_json, indent=2, ensure_ascii=False)}
    </script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen flex flex-col">
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="{back_link}" class="flex items-center gap-2 font-bold text-amber-400 text-lg hover:opacity-80 transition">
                <span>🧭</span> ALETHEIA19 <span class="text-xs text-cyan-400 font-mono px-2 py-0.5 bg-cyan-950/60 rounded border border-cyan-800">RAG PORTAL</span>
            </a>
            <div class="flex items-center gap-4">
                <a href="{lang_toggle_link}" class="text-xs font-mono px-3 py-1.5 rounded bg-slate-800 border border-slate-700 hover:border-amber-400 text-slate-300 hover:text-white transition">
                    {lang_toggle_label}
                </a>
                <a href="{back_link}" class="text-sm text-slate-400 hover:text-white transition hidden md:inline">{back_label}</a>
            </div>
        </div>
    </header>

    <main class="flex-grow max-w-4xl w-full mx-auto px-4 py-8">
        <div class="mb-8">
            <span class="inline-block text-xs font-mono text-cyan-400 bg-cyan-950/80 border border-cyan-800 px-3 py-1 rounded-full mb-3">
                {html.escape(case['icon'])} {html.escape(data['category'])}
            </span>
            <p class="text-slate-400 text-sm italic">{html.escape(data['summary'])}</p>
        </div>

        <article class="prose prose-invert max-w-none bg-slate-900/40 p-6 md:p-8 rounded-xl border border-slate-800 shadow-2xl">
            {body_html}
        </article>

        <div class="mt-12 p-6 rounded-xl bg-gradient-to-r from-slate-900 via-cyan-950/30 to-slate-900 border border-cyan-800/50 flex flex-col md:flex-row justify-between items-center gap-6">
            <div>
                <h4 class="font-bold text-amber-400 text-lg">{cta_title}</h4>
                <p class="text-slate-400 text-sm mt-1">{cta_desc}</p>
            </div>
            <a href="https://egisthol-spec.github.io/aletheia19/" class="px-6 py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-lg transition text-sm whitespace-nowrap shadow-lg">
                {cta_btn}
            </a>
        </div>
    </main>

    <footer class="border-t border-slate-900 bg-slate-950 py-6 text-center text-xs text-slate-500">
        <p>Aletheia19 Labs — Registre des Invariants Biophysiques FASCIA & M.O.S.</p>
    </footer>
</body>
</html>
"""
    return full_html

def generate_index_html(lang="fr"):
    """Generates docs/index.html (FR) or docs/en/index.html (EN) portal."""
    is_en = (lang == "en")
    cards_html = []
    
    for case in CASE_STUDIES_SOURCES:
        data = case[lang]
        link_path = f"case_studies/{case['id']}.html" if not is_en else f"case_studies/{case['id']}.html"
        cta_text = "Explorer l'audit forensique →" if not is_en else "Explore forensic audit →"
        
        card = f"""
        <a href="{link_path}" class="group bg-slate-900/60 hover:bg-slate-900 border border-slate-800 hover:border-cyan-500/50 p-6 rounded-xl transition-all duration-300 flex flex-col justify-between shadow-lg hover:shadow-cyan-950/30">
            <div>
                <div class="flex justify-between items-start mb-3">
                    <span class="text-xs font-mono text-cyan-400 bg-cyan-950/60 border border-cyan-900 px-2.5 py-0.5 rounded-full">
                        {case['icon']} {html.escape(data['category'])}
                    </span>
                </div>
                <h3 class="text-lg font-bold text-slate-100 group-hover:text-amber-400 transition mb-2">
                    {html.escape(data['title'])}
                </h3>
                <p class="text-sm text-slate-400 leading-relaxed">
                    {html.escape(data['summary'])}
                </p>
            </div>
            <div class="mt-6 flex items-center text-xs text-amber-400 font-mono group-hover:translate-x-1 transition-transform">
                {cta_text}
            </div>
        </a>
        """
        cards_html.append(card)

    badge = "OBSERVATOIRE MONDIAL DES DÉRIVES FASCIA" if not is_en else "GLOBAL OBSERVATORY OF FASCIA DRIFTS"
    hero_title = 'Les Cas Cliniques du <span class="text-amber-400">Sol</span> & du <span class="text-cyan-400">Codex</span>' if not is_en else 'Clinical Cases of <span class="text-amber-400">Sol</span> & <span class="text-cyan-400">Codex</span>'
    hero_desc = "Base de données d'autopsies forensiques industrielles, aéronautiques, financières et technologiques. Analyse d'impédance et diagnostic de dérive sous protocole FASCIA." if not is_en else "Global database of industrial, aerospace, financial, and technological forensic autopsies. Impedance analysis and biophysical drift diagnostic under FASCIA protocol."
    grid_title = "Matrice des 36 Cas Cliniques" if not is_en else "Matrix of the 36 Clinical Cases"
    grid_sub = "36 / 36 Cas Déployés" if not is_en else "36 / 36 Cases Deployed"
    lang_toggle_link = "en/index.html" if not is_en else "../index.html"
    lang_toggle_label = "🇬🇧 English Version" if not is_en else "🇫🇷 Version Française"

    index_html = f"""<!DOCTYPE html>
<html lang="{lang}" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ALETHEIA19 — {'Observatoire des Cas Cliniques Biophysiques' if not is_en else 'Biophysical Clinical Cases Observatory'}</title>
    <meta name="description" content="Registre mondial d'autopsies industrielles, M&A et technologiques sous protocole FASCIA. Ingestion RAG et audits de dérive.">
    
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
    <header class="border-b border-slate-800 bg-slate-900/60 backdrop-blur">
        <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
            <span class="font-bold text-amber-400 font-mono text-sm">ALETHEIA19</span>
            <a href="{lang_toggle_link}" class="text-xs font-mono px-3 py-1.5 rounded bg-slate-800 border border-slate-700 hover:border-amber-400 text-slate-300 hover:text-white transition">
                {lang_toggle_label}
            </a>
        </div>
        <div class="max-w-6xl mx-auto px-4 py-10 text-center">
            <span class="inline-block font-mono text-xs text-cyan-400 bg-cyan-950 border border-cyan-800 px-3 py-1 rounded-full mb-4">
                {badge}
            </span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-100 tracking-tight mb-4">
                {hero_title}
            </h1>
            <p class="max-w-2xl mx-auto text-slate-400 text-base md:text-lg leading-relaxed">
                {hero_desc}
            </p>
        </div>
    </header>

    <main class="flex-grow max-w-6xl w-full mx-auto px-4 py-12">
        <div class="flex justify-between items-center mb-8">
            <h2 class="text-xl font-bold text-slate-200 flex items-center gap-2">
                <span>📂</span> {grid_title}
            </h2>
            <span class="text-xs font-mono text-slate-500">{grid_sub}</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {"".join(cards_html)}
        </div>

        <!-- Section Méthodologie / Epistemology -->
        <section class="mt-20 border-t border-slate-900 pt-12">
            <div class="bg-slate-900/40 border border-slate-800 p-8 md:p-10 rounded-2xl shadow-xl">
                <div class="max-w-3xl">
                    <span class="inline-block text-xs font-mono text-amber-500 bg-amber-950/60 border border-amber-900 px-3 py-1 rounded-full mb-4">
                        { "CADRAGE ÉPISTÉMOLOGIQUE" if not is_en else "EPISTEMOLOGICAL FRAMEWORK" }
                    </span>
                    <h2 class="text-2xl font-bold text-slate-100 mb-4">
                        { "Principes d'Audit FASCIA & Réfutabilité" if not is_en else "FASCIA Audit Principles & Falsifiability" }
                    </h2>
                    <p class="text-sm font-medium text-amber-400/90 italic mb-8 leading-relaxed">
                        { "« Note importante : Les cas d'étude présentés ci-dessus ne servent pas à induire ou à démontrer la théorie ; ils servent à illustrer son application déductive sur des architectures complexes réelles. »" if not is_en else "“Important note: The case studies presented above do not aim to infer or prove the theory; they serve to illustrate its deductive application to real-world complex architectures.”" }
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-6">
                    <div class="border-l-2 border-cyan-500/40 pl-4">
                        <h3 class="text-base font-bold text-slate-200 mb-2">
                            { "1. Le Sol vs Le Codex" if not is_en else "1. The Sol vs. The Codex" }
                        </h3>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            { "Les audits classiques (due diligence financières des Big Four, certifications ISO) vérifient la cohérence interne des déclarations écrites (Le Codex, R=0). FASCIA ignore les déclarations d'intention pour mesurer l'impédance physique et le couplage réel des flux de terrain (Le Sol, R=1)." if not is_en else "Traditional audits (Big Four financial due diligence, ISO certifications) verify the internal coherence of written declarations (The Codex, R=0). FASCIA ignores statements of intent to measure physical impedance and actual ground-level coupling (The Sol, R=1)." }
                        </p>
                    </div>

                    <div class="border-l-2 border-cyan-500/40 pl-4">
                        <h3 class="text-base font-bold text-slate-200 mb-2">
                            { "2. La Souveraineté du Veto" if not is_en else "2. The Sovereignty of Veto" }
                        </h3>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            { "Un système n'est souverain que si ses praticiens de terrain (ingénieurs, cliniciens, développeurs) détiennent un droit de veto technique absolu et non négociable face aux impératifs d'optimisation financière. L'effondrement commence lorsque le Codex capture le Veto." if not is_en else "A system is only sovereign if its ground-level practitioners (engineers, clinicians, developers) hold an absolute, non-negotiable technical right of veto against financial optimization pressures. Collapse begins when the Codex captures the Veto." }
                        </p>
                    </div>

                    <div class="border-l-2 border-cyan-500/40 pl-4">
                        <h3 class="text-base font-bold text-slate-200 mb-2">
                            { "3. Le Critère de Réfutabilité" if not is_en else "3. Falsifiability Criterion" }
                        </h3>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            { "FASCIA n'est pas une boîte noire ou un outil statistique. Pour réfuter scientifiquement un diagnostic FASCIA, il faut démontrer l'absence de découplage réel Sol/Codex ou prouver l'existence d'une friction physique compensatrice au niveau du Sol." if not is_en else "FASCIA is not a black-box or statistical tool. To scientifically invalidate a FASCIA diagnostic, one must demonstrate the absence of real Sol/Codex decoupling or prove the existence of compensatory physical friction in the Sol." }
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="border-t border-slate-900 bg-slate-950 py-8 text-center text-xs text-slate-500">
        <p>Aletheia19 Labs — Registre des Invariants Biophysiques FASCIA & M.O.S.</p>
        <p class="mt-2 text-slate-600">Bilingual Indexation RAG & Generative Engine Optimization (GEO) Active</p>
    </footer>
</body>
</html>
"""
    return index_html

def generate_sitemap():
    """Generates a bilingual sitemap.xml with xhtml:link hreflang annotations."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = []

    # Portal index pages
    urls.append(f"""  <url>
    <loc>{SITE_BASE_URL}/index.html</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{SITE_BASE_URL}/index.html" />
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_BASE_URL}/en/index.html" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_BASE_URL}/index.html" />
  </url>""")
    urls.append(f"""  <url>
    <loc>{SITE_BASE_URL}/en/index.html</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{SITE_BASE_URL}/index.html" />
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_BASE_URL}/en/index.html" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_BASE_URL}/index.html" />
  </url>""")

    # Individual case study pages
    for case in CASE_STUDIES_SOURCES:
        fr_url = f"{SITE_BASE_URL}/case_studies/{case['id']}.html"
        en_url = f"{SITE_BASE_URL}/en/case_studies/{case['id']}.html"
        for loc in [fr_url, en_url]:
            lang = "fr" if loc == fr_url else "en"
            urls.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}" />
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_url}" />
  </url>""")

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>
"""
    return sitemap


def generate_robots_txt():
    """Generates robots.txt with sitemap pointer."""
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_BASE_URL}/sitemap.xml
"""


def main():
    print("Building Bilingual GitHub Pages portal in /docs...")
    
    # 1. Generate French HTML files
    for case in CASE_STUDIES_SOURCES:
        out_path = os.path.join(CASES_FR_DIR, f"{case['id']}.html")
        html_content = generate_case_html(case, lang="fr")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Generated FR: docs/case_studies/{case['id']}.html")

    # 2. Generate English HTML files
    for case in CASE_STUDIES_SOURCES:
        out_path = os.path.join(CASES_EN_DIR, f"{case['id']}.html")
        html_content = generate_case_html(case, lang="en")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Generated EN: docs/en/case_studies/{case['id']}.html")

    # 3. Generate portals
    index_fr = os.path.join(DOCS_DIR, "index.html")
    with open(index_fr, "w", encoding="utf-8") as f:
        f.write(generate_index_html(lang="fr"))
    print("[OK] Generated FR Portal: docs/index.html")

    index_en = os.path.join(DOCS_EN_DIR, "index.html")
    with open(index_en, "w", encoding="utf-8") as f:
        f.write(generate_index_html(lang="en"))
    print("[OK] Generated EN Portal: docs/en/index.html")

    # 4. Generate sitemap.xml
    sitemap_path = os.path.join(DOCS_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(generate_sitemap())
    print("[OK] Generated: docs/sitemap.xml")

    # 5. Generate robots.txt
    robots_path = os.path.join(DOCS_DIR, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(generate_robots_txt())
    print("[OK] Generated: docs/robots.txt")

    total_pages = len(CASE_STUDIES_SOURCES) * 2 + 2
    print(f"\nBilingual build complete: {total_pages} HTML pages + sitemap.xml + robots.txt")

if __name__ == "__main__":
    main()
