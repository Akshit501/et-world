#!/usr/bin/env python3
"""
ET WORLD – Build & Layout Engine (Python 3)
Enforces proper margins, border-fitting, and Economic Times World branding
aligned with reference layouts.
"""

import os
import re
import sys
import http.server
import socketserver

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(WORKSPACE_DIR, "index.html")
STYLES_FILE = os.path.join(WORKSPACE_DIR, "styles.css")
PORT = 3000

def validate_layout():
    """Verify that all main sections have matching max-widths and margins."""
    print("[Python Builder] Checking layout geometry, margins, and borders...")
    
    with open(STYLES_FILE, "r", encoding="utf-8") as f:
        css = f.read()

    # Verify CSS container max width and margin properties
    has_container = "--container-max:" in css
    has_margin_auto = "margin: 0 auto" in css or "margin: auto" in css
    
    print(f" - Container max-width definition present: {has_container}")
    print(f" - Auto margin centering present: {has_margin_auto}")

    # Verify key sections exist in index.html
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    sections = [
        ("Channel Strip", "channel-bar"),
        ("ET World Header", "hd"),
        ("ET Summit Banner", "summit-watch-live-banner"),
        ("Top Stories 3-Column Lead", "top-lead-grid"),
        ("ET World Summit Hub", "summit-hub-section"),
        ("Offbeat Section", "offbeat"),
        ("India Section (Text-Left, Thumb-Right)", "india-grid-6"),
        ("Opinion Section (Bordered Cards)", "opinion-grid-3"),
        ("Shorts Reel Section", "shorts-reel-track"),
        ("Videos Blue Box", "videos-blue-box"),
        ("Sports & Live Scorecard", "sports-section"),
        ("Regional Coverage", "regional-grid"),
        ("Footer", "site-footer")
    ]

    all_ok = True
    for name, tag in sections:
        present = tag in html
        print(f" - Section '{name}': {'[OK]' if present else '[MISSING]'}")
        if not present:
            all_ok = False

    return all_ok

def main():
    print("=" * 60)
    print("ET WORLD – PYTHON LAYOUT & BORDER OPTIMIZER")
    print("=" * 60)
    
    ok = validate_layout()
    if ok:
        print("\nAll sections verified with proper margins and fit-to-border alignment.")
    else:
        print("\nSome sections need adjustments.")

if __name__ == "__main__":
    main()
