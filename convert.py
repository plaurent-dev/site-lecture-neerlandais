import os
import re

files_to_convert = [
    "Amsterdam_2026-01-09.html",
    "Amsterdam_2026-01-10.html", 
    "Den Haag_2026-01-10.html",
    "Emmen_2026-01-07.html",
    "Leeuwarden_2026-01-07.html",
    "Nijmegen_2026-01-08.html",
    "Rotterdam_2026-01-08.html"
]

for filename in files_to_convert:
    filepath = filename
    
    if not os.path.exists(filepath):
        print(f"⚠️  {filename} - fichier non trouvé")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer le <style> inline par un lien
    content = re.sub(
        r'<style>[\s\S]*?</style>',
        '<link rel="stylesheet" href="styles.css">',
        content
    )
    
    # Remplacer .container par .fiche-container
    content = content.replace('class="container"', 'class="fiche-container"')
    
    # Restructurer le header
    content = re.sub(
        r'<div class="fiche-container">\s*<h1>([^<]+)</h1>\s*<p class="region-date">([^<]+)</p>',
        r'<div class="fiche-container">\n<div class="fiche-header">\n<h1 class="fiche-title">\1</h1>\n<p class="fiche-meta">\2</p>\n</div>',
        content
    )
    
    # Remplacer .article par .fiche-article
    content = content.replace('class="article"', 'class="fiche-article"')
    
    # Ajouter class aux tables
    content = re.sub(
        r'<table>',
        '<table class="fiche-table">',
        content
    )
    
    # Ajouter class aux boutons
    content = re.sub(
        r'<button onclick',
        '<button class="btn btn-primary" onclick',
        content
    )
    
    # Fermer div du header avant article
    content = re.sub(
        r'(</div>)\s*(<div class="fiche-article">)',
        r'\1\n\2',
        content
    )
    
    # Sauvegarder
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filename} - mis à jour avec succès")

print("\n🎉 Tous les fichiers ont été convertis!")