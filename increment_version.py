#!/usr/bin/env python3
"""
Script d'incrémentation automatique de version
Utilisé par le pre-commit hook Git
"""

import re
from datetime import datetime
import sys

def increment_version(version_string):
    """Incrémente la version patch (1.0.12 -> 1.0.13)"""
    parts = version_string.split('.')
    if len(parts) != 3:
        print(f"⚠️  Format de version invalide: {version_string}")
        return version_string
    
    major, minor, patch = parts
    new_patch = int(patch) + 1
    return f"{major}.{minor}.{new_patch}"

def update_version_js():
    """Met à jour le fichier version.js"""
    file_path = 'version.js'
    
    try:
        # Lire le fichier actuel
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraire la version actuelle
        match = re.search(r"const APP_VERSION = '([0-9.]+)';", content)
        if not match:
            print("❌ Version non trouvée dans version.js")
            return False
        
        current_version = match.group(1)
        new_version = increment_version(current_version)
        
        # Remplacer la version
        new_content = re.sub(
            r"const APP_VERSION = '[0-9.]+';",
            f"const APP_VERSION = '{new_version}';",
            content
        )
        
        # Écrire le nouveau contenu
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Version mise à jour: {current_version} → {new_version}")
        print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True
        
    except FileNotFoundError:
        print(f"❌ Fichier {file_path} introuvable")
        return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    success = update_version_js()
    sys.exit(0 if success else 1)
