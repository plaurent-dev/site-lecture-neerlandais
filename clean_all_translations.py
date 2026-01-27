#!/usr/bin/env python3
import json
import re

def clean_translation(phrase_nl, phrase_fr):
    """Nettoie et traduit logiquement les phrases"""
    
    # Mapping des traductions spéciales
    special_fixes = {
        "Nous avons travaillé hier": "Nous travaillions hier",
        "Je vais vers Liège": "Je vais à Liège",
        "Elle ne mange pas à 14 heures au restaurant": "Elle ne mange pas à 14 heures au restaurant",
        "La femme était à 14 heures à la bibliothèque": "La femme était à la bibliothèque à 14 heures",
        "La femme conduit dimanche la voiture": "La femme conduit la voiture dimanche",
        "L'enfant travaille het plan avant le repas": "L'enfant travaille au plan avant le repas",
        "Wij rijden woensdag op de fiets": "Nous allons à vélo mercredi",
        "Il voit le chien le mois prochain": "Il voit le chien le mois prochain",
        "Tu aimes mercredi de la musique": "Tu aimes de la musique mercredi",
    }
    
    if phrase_fr in special_fixes:
        return special_fixes[phrase_fr]
    
    # Remplacements systématiques
    result = phrase_fr
    
    # Correction des articles néerlandais résiduels
    result = result.replace(' het ', ' le ')
    result = result.replace('het ', 'le ')
    result = result.replace('het', 'le')
    
    # Correction des temps "van 9 tot 5"
    result = result.replace('van 9 tot 5', 'de 9 à 17 heures')
    
    # Correction des verbes conjugués en néerlandais
    replacements = {
        'vraagde': 'demandait',
        'prenait': 'prenais',
        'speelt': 'joue',
        'houd': 'aime',
        'donne': 'donne',
        'prennent': 'prennent',
        'donnent': 'donnent',
    }
    
    for nl_verb, fr_verb in replacements.items():
        result = re.sub(r'\b' + nl_verb + r'\b', fr_verb, result, flags=re.IGNORECASE)
    
    # Correction des conjugaisons incorrectes
    result = result.replace('cuisinais', 'cuisinait')
    result = result.replace('marchais', 'marchait')
    result = result.replace('apprenait', 'apprenait')
    result = result.replace('pensaient', 'pensions')
    result = result.replace('speelt', 'joue')
    
    # Correction des accords
    if 'Elle apportent' in result:
        result = result.replace('Elle apportent', 'Elles apportent')
    if 'Elle donnent' in result:
        result = result.replace('Elle donnent', 'Elles donnent')
    if 'Elle ne mettent' in result:
        result = result.replace('Elle ne mettent', 'Elles ne mettent')
    if 'She apportent' in result:
        result = result.replace('She apportent', 'Elles apportent')
    
    # Correction des négations
    if ' pas' in result and 'ne ' not in result and 'n\'' not in result:
        # Ne rien changer car déjà correctement formé
        pass
    
    # Correction des articles en français
    result = result.replace('de het ', 'de le ')
    result = result.replace('de het', 'de le')
    
    # Traduction des expressions temporelles
    result = result.replace("'s ochtends", 'le matin')
    result = result.replace("'s middags", "l'après-midi")
    result = result.replace("'s avonds", 'le soir')
    result = result.replace("'s nachts", 'la nuit')
    
    # Traduction des lieux
    result = result.replace('naar het museum', 'au musée')
    result = result.replace('naar het station', 'vers la gare')
    result = result.replace('naar het café', 'au café')
    result = result.replace('naar het park', 'au parc')
    
    # Traduction des prépositions
    result = result.replace('naar Luik', 'vers Liège')
    result = result.replace('naar Ierland', "vers l'Irlande")
    result = result.replace('naar Brussel', 'vers Bruxelles')
    result = result.replace('naar Spanje', 'vers l\'Espagne')
    
    # Traduction des jours
    result = result.replace('vandaag', "aujourd'hui")
    result = result.replace('gisterdag', 'hier')
    result = result.replace('morgen', 'demain')
    result = result.replace('maandag', 'lundi')
    result = result.replace('dinsdag', 'mardi')
    result = result.replace('woensdag', 'mercredi')
    result = result.replace('donderdag', 'jeudi')
    result = result.replace('vrijdag', 'vendredi')
    result = result.replace('zaterdag', 'samedi')
    result = result.replace('zondag', 'dimanche')
    
    # Traduction des mois/périodes
    result = result.replace('volgende week', 'la semaine prochaine')
    result = result.replace('volgende maand', 'le mois prochain')
    result = result.replace('volgende jaar', "l'année prochaine")
    result = result.replace('voor het eten', 'avant le repas')
    result = result.replace('na het werk', 'après le travail')
    result = result.replace('om ', 'à ')
    
    # Correction des articles
    result = result.replace('aan de ', 'à la ')
    result = result.replace('aan het ', 'au ')
    result = result.replace('aan het travaille', 'au travail')
    
    return result

with open('corpus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for entry in data['corpus']:
    old = entry['phrase_francais']
    new = clean_translation(entry['phrase'], old)
    if old != new:
        entry['phrase_francais'] = new
        count += 1

with open('corpus.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[OK] {count} nouvelles traductions traitees")
print(f"[OK] Fichier sauvegarde avec succes")
