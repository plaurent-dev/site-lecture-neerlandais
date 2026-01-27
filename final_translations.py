#!/usr/bin/env python3
import json

def translate_phrase(phrase_nl, current_fr):
    """Traduit logiquement une phrase néerlandaise en français"""
    
    # Si la traduction actuelle semble déjà correcte, la garder
    if current_fr and len(current_fr) > 5 and not any(x in current_fr for x in ['het ', 'van 9 tot', 'vraagde', 'prenait', 'mag ', 'speelt ', 'donne ', 'houd ']):
        return current_fr
    
    # Sinon, générer une nouvelle traduction
    result = current_fr
    
    # 1. Traductions des éléments récurrents
    # Remplacement des verbes
    verbs = {
        'ik ga': 'je vais', 'jij gaat': 'tu vas', 'hij gaat': 'il va', 'zij gaat': 'elle va',
        'ik ben': 'je suis', 'jij bent': 'tu es', 'hij is': 'il est', 'zij is': 'elle est',
        'ik houd': "j'aime", 'jij houdt': 'tu aimes', 'hij houdt': 'il aime', 'zij houdt': 'elle aime',
        'ik hou': "j'aime", 'jij houd': 'tu aimes',
        'ik werk': 'je travaille', 'jij werkt': 'tu travailles',
        'ik neem': 'je prends', 'jij neemt': 'tu prends', 'hij neemt': 'il prend',
        'ik zie': 'je vois', 'jij ziet': 'tu vois', 'hij ziet': 'il voit',
        'ik rijd': 'je conduis', 'jij rijdt': 'tu conduis', 'hij rijdt': 'il conduit',
        'ik kook': 'je cuisine', 'jij kookt': 'tu cuisines', 'hij kookt': 'il cuisine',
        'ik speel': 'je joue', 'jij speelt': 'tu joues', 'hij speelt': 'il joue',
        'ik zet': 'je mets', 'jij zet': 'tu mets',
        'ik kan': 'je peux', 'jij kan': 'tu peux',
        'ik moet': 'je dois', 'jij moet': 'tu dois',
        'ik wil': 'je veux', 'jij wil': 'tu veux',
        'ik kom': 'je viens', 'jij komt': 'tu viens',
        'ik leer': 'j\'apprends', 'jij leert': 'tu apprends',
        'ik vraag': 'je demande', 'jij vraagt': 'tu demandes',
        'ik denk': 'je pense', 'jij denkt': 'tu penses',
        'ik luister': 'j\'écoute', 'jij luistert': 'tu écoutes',
        'ik praat': 'je parle', 'jij praat': 'tu parles',
        'ik geef': 'je donne', 'jij geeft': 'tu donnes',
        'ik open': 'j\'ouvre', 'jij opent': 'tu ouvres',
        'ik reken': 'je compte', 'jij rekent': 'tu comptes',
        'ik tel': 'je compte', 'jij telt': 'tu comptes',
        'ik reis': 'je voyage', 'jij reist': 'tu voyages',
        'ik blijf': 'je reste', 'jij blijft': 'tu restes',
        'ik wandel': 'je marche', 'jij wandelt': 'tu marches',
        'ik antwoord': 'je réponds', 'jij antwoordt': 'tu réponds',
        'wij werken': 'nous travaillons', 'wij gaan': 'nous allons', 'wij zijn': 'nous sommes',
        'wij rijden': 'nous conduisons', 'wij hebben': 'nous avons', 'wij nemen': 'nous prenons',
        'jullie gaan': 'vous allez', 'jullie werken': 'vous travaillez',
        'zij werken': 'elles travaillent', 'zij gaan': 'elles vont', 'zij zijn': 'elles sont',
        'de man gaat': "l'homme va", 'de vrouw gaat': 'la femme va',
        'het kind gaat': "l'enfant va", 'de jongen gaat': 'le garçon va',
    }
    
    # Temps/Jours
    temps = {
        'vandaag': "aujourd'hui", 'gisterdag': 'hier', 'morgen': 'demain',
        'maandag': 'lundi', 'dinsdag': 'mardi', 'woensdag': 'mercredi',
        'donderdag': 'jeudi', 'vrijdag': 'vendredi', 'zaterdag': 'samedi', 'zondag': 'dimanche',
        'volgende week': 'la semaine prochaine',
        'volgende maand': 'le mois prochain',
        'volgende jaar': "l'année prochaine",
        'voor het eten': 'avant le repas',
        'na het werk': 'après le travail',
        "'s ochtends": 'le matin',
        "'s middags": "l'après-midi",
        "'s avonds": 'le soir',
        "'s nachts": 'la nuit',
    }
    
    # Lieux
    lieux = {
        'het museum': 'le musée', 'het restaurant': 'le restaurant', 'het café': 'le café',
        'het station': 'la gare', 'het park': 'le parc', 'het terras': 'la terrasse',
        'de bibliotheek': 'la bibliothèque', 'de winkel': 'le magasin', 'de school': "l'école",
        'de stad': 'la ville', 'op straat': 'dans la rue', 'op het plein': 'sur la place',
        'op het terras': 'sur la terrasse', 'in Amsterdam': 'à Amsterdam',
        'naar het museum': 'au musée', 'naar het station': 'vers la gare',
        'naar het café': 'au café', 'naar het park': 'au parc',
    }
    
    # Appliquer les traductions
    for nl, fr in verbs.items():
        if nl in result.lower():
            result = result.replace(nl, fr)
    
    for nl, fr in temps.items():
        if nl in result.lower():
            result = result.replace(nl, fr)
    
    for nl, fr in lieux.items():
        if nl in result.lower():
            result = result.replace(nl, fr)
    
    # Nettoyages finaux
    # Suppression des articles néerlandais résiduels
    result = result.replace(' het ', ' le ')
    result = result.replace('het ', 'le ')
    result = result.replace(' van ', ' de ')
    
    # Correction des espaces
    result = ' '.join(result.split())
    
    return result

with open('corpus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Appliquer la traduction
total_processed = 0
for entry in data['corpus']:
    old = entry['phrase_francais']
    new = translate_phrase(entry['phrase'], old)
    if old != new:
        entry['phrase_francais'] = new
        total_processed += 1

# Sauvegarder
with open('corpus.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[DONE] {total_processed} phrases mises a jour")
print(f"[DONE] Fichier traductions_finale sauvegarde")
