import os
import re

BASE_DIR = r"C:\VESUVIUS_LOCAL"
FR_DIR = os.path.join(BASE_DIR, "Case_Studies")
EN_DIR = os.path.join(BASE_DIR, "Case_Studies_EN")

os.makedirs(EN_DIR, exist_ok=True)

# Translation dictionary for structural FASCIA terms and headings
TERM_MAP = [
    ("📂 AUDIT CLINIQUE FASCIA :", "📂 FASCIA CLINICAL AUDIT:"),
    ("## Analyse Forensique", "## Forensic Analysis"),
    ("Standard :** FASCIA Protocol", "Standard:** FASCIA Protocol"),
    ("Auteur :** Aletheia19 Labs", "Author:** Aletheia19 Labs"),
    ("FORMULE OPÉRATIONNELLE FASCIA", "FASCIA OPERATIONAL FORMULA"),
    ("Voici", "Here is"),
    ("Mesurez", "Measure"),
    ("Le verdict est", "The verdict is"),
    ("🏛️ I. LA ", "🏛️ I. THE "),
    ("🏛️ I. LE ", "🏛️ I. THE "),
    ("🏛️ I. L'", "🏛️ I. THE "),
    ("📊 II. DIAGNOSTIC FASCIA", "📊 II. FASCIA DIAGNOSTIC"),
    ("🔬 III. L'EFFONDREMENT", "🔬 III. THE COLLAPSE"),
    ("🔬 III. L'EFFONDREMENT DU SYSTÈME", "🔬 III. SYSTEM COLLAPSE"),
    ("🔑 IV. LA LEÇON DE SOUVERAINETÉ (LEÇON DU SOL)", "🔑 IV. THE SOVEREIGNTY LESSON (SOL LESSON)"),
    ("Le Sol", "The Sol"),
    ("Le Codex", "The Codex"),
    ("Façade Homeostasis", "Façade Homeostasis"),
    ("Parasitisme Sémantique", "Semantic Parasitism"),
    ("Dette d'Oxygène", "Oxygen Debt"),
    ("Première Main", "First-Hand"),
    ("Jachère Inversée", "Inverted Fallow"),
    ("Consensus Creux", "Hollow Consensus"),
    ("Cordon Andon", "Andon Cord"),
    ("Veto", "Veto"),
    ("en conditions réelles", "under real-world conditions"),
    ("sur le papier", "on paper"),
    ("dette de sécurité", "safety debt"),
    ("asphyxie", "asphyxiation"),
    ("dérive biophysique", "biophysical drift"),
]

def translate_markdown_text(content):
    """Applies systemic term replacements and translates structural headings."""
    translated = content
    
    # 1. Apply core FASCIA terminology replacements
    for fr_term, en_term in TERM_MAP:
        translated = translated.replace(fr_term, en_term)
        
    # 2. Section header translations
    translated = re.sub(r'# 📂 AUDIT CLINIQUE FASCIA : (.*)', r'# 📂 FASCIA CLINICAL AUDIT: \1', translated)
    translated = re.sub(r'> \[!IMPORTANT\]', r'> [!IMPORTANT]', translated)
    
    return translated

def process_all_cases():
    print("Processing case study translations into English...")
    files = [f for f in os.listdir(FR_DIR) if f.endswith('.md')]
    
    for filename in files:
        fr_path = os.path.join(FR_DIR, filename)
        base_name = os.path.splitext(filename)[0]
        en_filename = f"{base_name}_EN.md"
        en_path = os.path.join(EN_DIR, en_filename)
        
        with open(fr_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        translated_content = translate_markdown_text(content)
        
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(translated_content)
            
        print(f"[OK] Created: Case_Studies_EN/{en_filename}")

if __name__ == "__main__":
    process_all_cases()
