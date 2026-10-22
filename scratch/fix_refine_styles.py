import os

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFINE_STYLES_FILE = os.path.join(WORKSPACE_DIR, "refine_styles.py")

with open(REFINE_STYLES_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Find the end of CSS_CONTENT
marker = 'def main():'
if marker in text:
    parts = text.split(marker)
    top_part = parts[0]
    bottom_part = marker + parts[1]
    
    # Check if there is CSS after main()
    css_after_main = ""
    if 'if __name__ == "__main__":' in bottom_part:
        subparts = bottom_part.split('if __name__ == "__main__":\n    main()')
        main_code = subparts[0] + 'if __name__ == "__main__":\n    main()\n'
        if len(subparts) > 1:
            css_after_main = subparts[1].strip()
        
        # Place css_after_main before the closing """ of CSS_CONTENT
        if css_after_main:
            last_quote_idx = top_part.rfind('"""')
            if last_quote_idx != -1:
                top_part = top_part[:last_quote_idx] + "\n\n" + css_after_main + "\n\"\"\"\n\n"
        
        fixed_text = top_part + main_code
        with open(REFINE_STYLES_FILE, "w", encoding="utf-8") as f:
            f.write(fixed_text)
        print("Successfully fixed refine_styles.py!")
