import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFINE_STYLES_FILE = os.path.join(WORKSPACE_DIR, "refine_styles.py")

with open(REFINE_STYLES_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Replace .hd with clean white navbar styling
old_hd = """.hd {
  background: var(--navy);
  color: #ffffff;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.18);
  width: 100%;
}"""

new_hd = """.hd {
  background: #ffffff;
  color: #111111;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
  border-bottom: 1px solid var(--ln);
  width: 100%;
}

:root[data-theme="dark"] .hd {
  background: #111722;
  color: #ffffff;
  border-bottom-color: #1f2b3d;
}"""

if old_hd in text:
    text = text.replace(old_hd, new_hd)
    print("Updated .hd to clean white sticky bar.")

# Update menu-search-btn colors
old_btn = """.menu-search-btn {
  background: none;
  border: none;
  color: #ffffff;"""

new_btn = """.menu-search-btn {
  background: none;
  border: none;
  color: #111111;"""

if old_btn in text:
    text = text.replace(old_btn, new_btn)
    print("Updated .menu-search-btn to dark icon.")

# Update logo-world color
old_lw = """.logo-world {
  color: #ffffff;"""

new_lw = """.logo-world {
  color: #111111;"""

if old_lw in text:
    text = text.replace(old_lw, new_lw)
    print("Updated .logo-world to dark font.")

# Update nav-link colors
old_nav = """.nav a, .nav-link {
  padding: 6px 0;
  color: #d1d5db;
  border-bottom: 2.5px solid transparent;
  font-weight: 600;
  font-size: 12.5px;
  cursor: pointer;
  letter-spacing: 0.02em;
  transition: var(--transition);
}

.nav a:hover, .nav-link:hover {
  color: #ffffff;
}

.nav a.on, .nav-link.on {
  font-weight: 800;
  color: #ffffff;
  border-color: var(--ac);
}"""

new_nav = """.nav a, .nav-link {
  padding: 6px 0;
  color: #444444;
  border-bottom: 2.5px solid transparent;
  font-weight: 600;
  font-size: 12.5px;
  cursor: pointer;
  letter-spacing: 0.02em;
  transition: var(--transition);
}

.nav a:hover, .nav-link:hover {
  color: var(--ac);
}

.nav a.on, .nav-link.on {
  font-weight: 800;
  color: var(--ac);
  border-color: var(--ac);
}

:root[data-theme="dark"] .nav a,
:root[data-theme="dark"] .nav-link {
  color: #cbd5e1;
}

:root[data-theme="dark"] .nav a.on,
:root[data-theme="dark"] .nav-link.on {
  color: var(--ac);
}

:root[data-theme="dark"] .menu-search-btn {
  color: #ffffff;
}

:root[data-theme="dark"] .logo-world {
  color: #ffffff;
}"""

if old_nav in text:
    text = text.replace(old_nav, new_nav)
    print("Updated .nav-link colors.")

# Update avatar btn
old_avatar = """.usr-avatar-btn {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #1e3a5f;
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #ffffff;"""

new_avatar = """.usr-avatar-btn {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #f0f2f5;
  border: 1px solid #d1d5db;
  color: #111111;"""

if old_avatar in text:
    text = text.replace(old_avatar, new_avatar)
    print("Updated .usr-avatar-btn.")

# Update header datetime
old_dt = """.header-datetime {
  font-size: 10px;
  color: #cbd5e1;"""

new_dt = """.header-datetime {
  font-size: 10px;
  color: #555555;"""

if old_dt in text:
    text = text.replace(old_dt, new_dt)
    print("Updated .header-datetime.")

with open(REFINE_STYLES_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[apply_white_nav.py] Finished updating refine_styles.py.")
