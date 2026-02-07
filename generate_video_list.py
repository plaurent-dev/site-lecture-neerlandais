#!/usr/bin/env python3
"""
Script pour générer un fichier video-list.json à partir des fichiers vidéo du dossier 'videos/'
"""

import os
import json
import subprocess
from pathlib import Path

def get_video_duration(filepath):
    """
    Récupère la durée d'une vidéo en utilisant ffprobe
    """
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', 
             '-of', 'default=noprint_wrappers=1:nokey=1:noval=1', filepath],
            capture_output=True,
            text=True,
            timeout=5
        )
        duration_seconds = float(result.stdout.strip())
        minutes = int(duration_seconds // 60)
        seconds = int(duration_seconds % 60)
        return f"{minutes}:{seconds:02d}"
    except:
        return "N/A"

def format_filename(filename):
    """
    Convertit un nom de fichier en titre lisible
    """
    # Supprimer l'extension
    name = Path(filename).stem
    # Remplacer les underscores et tirets par des espaces
    name = name.replace('_', ' ').replace('-', ' ')
    # Mettre en majuscule la première lettre de chaque mot
    return ' '.join(word.capitalize() for word in name.split())

def generate_video_list():
    """
    Génère un fichier video-list.json à partir des vidéos du dossier
    """
    videos_dir = Path('videos')
    
    if not videos_dir.exists():
        print("❌ Le dossier 'videos' n'existe pas!")
        return
    
    # Extensions vidéo supportées
    video_extensions = {'.mp4', '.webm', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.m4v'}
    
    # Récupérer tous les fichiers vidéo
    video_files = [
        f for f in videos_dir.iterdir() 
        if f.is_file() and f.suffix.lower() in video_extensions
    ]
    
    if not video_files:
        print("⚠️ Aucun fichier vidéo trouvé dans le dossier 'videos'")
        # Créer un fichier vide avec un exemple
        video_list = []
    else:
        # Trier par nom
        video_files.sort(key=lambda x: x.name)
        
        # Créer la liste
        video_list = []
        for idx, video_path in enumerate(video_files, 1):
            print(f"📹 Traitement: {video_path.name}...")
            
            duration = get_video_duration(str(video_path))
            title = format_filename(video_path.name)
            
            video_entry = {
                "id": idx,
                "title": title,
                "description": f"Leçon {idx} de formation Inburgering A1",
                "duration": duration,
                "type": "local",
                "src": f"videos/{video_path.name}"
            }
            video_list.append(video_entry)
            print(f"✅ Ajouté: {title} ({duration})")
    
    # Écrire le fichier JSON
    output_path = Path('video-list.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(video_list, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Fichier {output_path} créé avec succès!")
    print(f"📊 Total: {len(video_list)} vidéo(s) trouvée(s)")
    
    # Afficher un aperçu
    if video_list:
        print("\n📋 Aperçu du fichier:")
        print(json.dumps(video_list[:2], ensure_ascii=False, indent=2))
        if len(video_list) > 2:
            print(f"... et {len(video_list) - 2} autre(s)")

if __name__ == '__main__':
    generate_video_list()
