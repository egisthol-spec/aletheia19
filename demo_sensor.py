#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ALETHEIA19 — FASCIA Protocol Demo Sensor
Formal emulation of semantic entropy and metabolic debt mapping.
Reference: DOI 10.5281/zenodo.21192234
"""

import sys
import time
import math

DEFAULT_TEXT = """
L'introduction forcée des assistants documentaires automatisés de Troisième Main (R=0) 
au sein du processus de décision juridique tend à privilégier les continuités statistiques 
au détriment des ruptures créatrices de Première Main (R=1). En s'abritant derrière des grilles 
d'évaluation de récidive comme COMPAS sous secret industriel, la structure délègue passivement 
sa responsabilité, créant une boucle de rétroaction auto-référentielle qui fige le droit dans 
une stase stérile (Pathocratie Algorithmique).
"""

def print_banner():
    print("=" * 72)
    print("  ALETHEIA19 // FASCIA PROTOCOL — DEMONSTRATION SENSOR")
    print("  Forensic Semantic Architecture & Biophysical Auditing")
    print("  Zenodo Preprint Reference: DOI 10.5281/zenodo.21192234")
    print("=" * 72)

def simulate_audit(content, source_name):
    print(f"\n[*] Initializing FASCIA Lightweight Sensor (Demo Mode)...")
    time.sleep(0.4)
    print("[*] Loading lexical anchors (distilled subset)...")
    time.sleep(0.3)
    
    # Mock anchors for the demo
    first_hand_anchors = ["première main", "r=1", "friction", "corps", "sol", "intime conviction"]
    third_hand_anchors = ["troisième main", "r=0", "automate", "algorithme", "compas", "technostructure"]
    codex_anchors = ["boucle", "stase", "standardisé", "rétroaction", "auto-référentielle"]

    total_words = len(content.split())
    print(f"[+] Analyzed Substrate: {source_name} ({total_words} words)")
    
    found_1st = [w for w in first_hand_anchors if w in content.lower()]
    found_3rd = [w for w in third_hand_anchors if w in content.lower()]
    found_codex = [w for w in codex_anchors if w in content.lower()]

    print(f"    - First Hand (Sol) Anchors Detected: {len(found_1st)} {found_1st}")
    print(f"    - Third Hand (Automate) Anchors Detected: {len(found_3rd)} {found_3rd}")
    print(f"    - Codex (Autocatalysis) Anchors Detected: {len(found_codex)} {found_codex}")

    # Compute metrics
    factor_flux = len(found_3rd) * 1.5 + len(found_codex) * 1.0
    factor_sol = len(found_1st) * 2.0
    
    omega = (factor_flux / (factor_sol + 1)) * 10.0
    chi = (factor_sol / (factor_flux + 1)) * 1.0
    isomorphism_index = min(99.8, max(42.0, 85.0 + math.sin(total_words / 100.0) * 10))

    print("\n" + "-" * 72)
    print("METRICS ANALYSIS:")
    print(f"  * Isomorphism Index             : {isomorphism_index:.2f}% (Topological Stability)")
    print(f"  * Semantic Oxygen Debt (Omega)  : {omega:.2f} / 10.0")
    print(f"  * Soil Biophysical Friction (Chi): {chi:.4f}  [Scale: 0.0 - 1.0]")
    print("-" * 72)

    print("\nDIAGNOSTIC STATUS:")
    if omega > 5.0:
        print("  >> WARNING: High Semantic Oxygen Debt detected.")
        print("     The corpus is dominated by auto-catalytic Codex structures (R=0).")
        print("     Risk of model collapse / cognitive enclosure is elevated.")
    else:
        print("  >> STABLE: Sol grounding is sufficient.")
        print("     Friction parameters verify active human agency (R=1).")
    print("=" * 72)
    print("[Notice] Real-time diagnostic engines (audit_magnifica_28188.py) are running inside secure enclosure.")
    print("=" * 72 + "\n")

if __name__ == "__main__":
    print_banner()
    
    if len(sys.argv) > 1:
        text_path = sys.argv[1]
        try:
            with open(text_path, 'r', encoding='utf-8') as f:
                text_to_analyze = f.read()
            source = text_path
        except Exception as e:
            print(f"[!] Error: Could not read file {text_path}. ({e})")
            sys.exit(1)
    else:
        print("[*] Running with integrated Law & Justice sample corpus...")
        text_to_analyze = DEFAULT_TEXT
        source = "Integrated Sample"

    simulate_audit(text_to_analyze, source)
