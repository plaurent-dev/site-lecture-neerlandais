#!/usr/bin/env python3
import json
import re

with open('corpus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Corrections des erreurs résiduelles
corrections = {
    'Je devais acleer quelque chose au magasin': 'Je devais acheter quelque chose au magasin',
    'iets kopen': 'acheter quelque chose',
    'het eten': 'manger',
}

corrections_patterns = [
    (r'acleer', 'acheter'),
    (r'l\'homme apprend l\'anglais', "l'homme apprend l'anglais"),
    (r'J\'apprends l\'anglais', "J'apprends l'anglais"),
]

count = 0
for entry in data['corpus']:
    old = entry['phrase_francais']
    new = old
    
    # Appliquer les corrections exactes
    if old in corrections:
        new = corrections[old]
    
    # Appliquer les patterns regex
    for pattern, replacement in corrections_patterns:
        if re.search(pattern, new):
            new = re.sub(pattern, replacement, new)
    
    if old != new:
        entry['phrase_francais'] = new
        count += 1

with open('corpus.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[FINAL] {count} corrections de finition appliquees")
print(f"[SUCCESS] Corpus traduit et sauvegarde")
