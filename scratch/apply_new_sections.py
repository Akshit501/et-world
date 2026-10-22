import os

workspace_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa"
build_site_path = os.path.join(workspace_dir, "build_site.py")

with open(build_site_path, "r", encoding="utf-8") as f:
    content = f.read()

target = """        </div>
      </div>
    </section>

    <!-- =====================================================================
         SPORTS & LIVE MATCH SCORECARD"""

with open(os.path.join(workspace_dir, "scratch", "generate_sections_html.py"), "r", encoding="utf-8") as f:
    gen_code = f.read()

# Extract sections_html
start_marker = 'sections_html = """'
end_marker = '"""\n\nprint("Generated HTML size:"'
start_idx = gen_code.find(start_marker) + len(start_marker)
end_idx = gen_code.find(end_marker)
sections_html = gen_code[start_idx:end_idx]

replacement = f"""        </div>
      </div>
    </section>
{sections_html}
    <!-- =====================================================================
         SPORTS & LIVE MATCH SCORECARD"""

if target in content:
    new_content = content.replace(target, replacement, 1)
    with open(build_site_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated build_site.py!")
else:
    print("Target string not found in build_site.py!")
