import os

workspace_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa"
build_site_path = os.path.join(workspace_dir, "build_site.py")

with open(build_site_path, "r", encoding="utf-8") as f:
    code = f.read()

# Add IDs to the duo-playcard-cols and regional-quad-cards
code = code.replace(
    '<!-- Left Playcard: India Global -->\n        <div class="duo-playcard-col">',
    '<!-- Left Playcard: India Global -->\n        <div class="duo-playcard-col" id="india-global">',
    1
)

code = code.replace(
    '<!-- Right Playcard: Study Abroad -->\n        <div class="duo-playcard-col">',
    '<!-- Right Playcard: Study Abroad -->\n        <div class="duo-playcard-col" id="study-abroad">',
    1
)

code = code.replace(
    '<!-- Left Playcard: Climate & Environment -->\n        <div class="duo-playcard-col">',
    '<!-- Left Playcard: Climate & Environment -->\n        <div class="duo-playcard-col" id="climate-environment">',
    1
)

code = code.replace(
    '<!-- Right Playcard: Lifestyle -->\n        <div class="duo-playcard-col">',
    '<!-- Right Playcard: Lifestyle -->\n        <div class="duo-playcard-col" id="lifestyle">',
    1
)

code = code.replace(
    '<!-- Quad Card 1: United States -->\n        <article class="regional-quad-card">',
    '<!-- Quad Card 1: United States -->\n        <article class="regional-quad-card" id="us">',
    1
)

code = code.replace(
    '<!-- Quad Card 2: United Kingdom -->\n        <article class="regional-quad-card">',
    '<!-- Quad Card 2: United Kingdom -->\n        <article class="regional-quad-card" id="uk">',
    1
)

code = code.replace(
    '<!-- Quad Card 3: Middle East -->\n        <article class="regional-quad-card">',
    '<!-- Quad Card 3: Middle East -->\n        <article class="regional-quad-card" id="middle-east">',
    1
)

code = code.replace(
    '<!-- Quad Card 4: Asia -->\n        <article class="regional-quad-card">',
    '<!-- Quad Card 4: Asia -->\n        <article class="regional-quad-card" id="asia">',
    1
)

code = code.replace(
    '<!-- Left Playcard: Movies & Entertainment -->\n        <div class="duo-playcard-col">',
    '<!-- Left Playcard: Movies & Entertainment -->\n        <div class="duo-playcard-col" id="movies-entertainment">',
    1
)

code = code.replace(
    '<!-- Right Playcard: Gadgets & Technology -->\n        <div class="duo-playcard-col">',
    '<!-- Right Playcard: Gadgets & Technology -->\n        <div class="duo-playcard-col" id="gadgets-tech">',
    1
)

with open(build_site_path, "w", encoding="utf-8") as f:
    f.write(code)

print("build_site.py updated with navigation anchor IDs!")
