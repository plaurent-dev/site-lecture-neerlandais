#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from typing import Dict

def traduction_logique(phrase_nl: str, phrase_francais: str) -> str:
    """
    Génère une traduction logique en français pour chaque phrase néerlandaise.
    """
    
    # Dictionnaire complet de traductions cohérentes
    traductions = {
        # Négations - correction du français
        'Je vais à la bibliothèque pas': 'Je ne vais pas à la bibliothèque',
        'Tu es sur la terrasse pas': "Tu n'es pas sur la terrasse",
        'Tu vas vers la gare pas': 'Tu ne vas pas vers la gare',
        'Le garçon va le soir vers le musée pas': 'Le garçon ne va pas au musée le soir',
        'Le garçon habite à Amsterdam pas': "Le garçon n'habite pas à Amsterdam",
        'Elle apportent la voiture mercredi à l\'école': 'Elles apportent la voiture mercredi à l\'école',
        'Tu donne vendredi het cadeau au magasin': 'Tu donnes vendredi le cadeau au magasin',
        'Nous conduisent le matin pas': 'Nous ne conduisons pas le matin',
        'Le garçon speelt van 9 tot 5 pas': 'Le garçon ne joue pas de 9 à 17 heures',
        'L\'homme cuisinais à 8 heures': "L'homme cuisinait à 8 heures",
        'Nous donnent het cadeau': 'Nous donnons le cadeau',
        'Jij speelt het soir de guitare': 'Tu joues de la guitare le soir',
        'Vous aimez aller aux Pays-Bas le samedi': 'Vous aimez aller aux Pays-Bas le samedi',
        'Tu marche vers le musée pas': 'Tu ne marches pas vers le musée',
        'Nous parlent aujourd\'hui au magasin pas': 'Nous ne parlons pas aujourd\'hui au magasin',
        'Tu aime le soir de la guitare': 'Tu joues de la guitare le soir',
        'Elle mag en Espagne pas': "Elle ne peut pas aller en Espagne",
        'Nous pensent samedi': 'Nous pensons samedi',
        'Il marchais le mois prochain': 'Il marchait le mois prochain',
        'La femme cuisinais samedi': 'La femme cuisinait samedi',
        'Nous parlez aujourd\'hui au magasin pas': 'Nous ne parlons pas aujourd\'hui au magasin',
        'Vous apprennent anglais aujourd\'hui': 'Vous apprenez l\'anglais aujourd\'hui',
        'Tu travailles l\'année prochaine vers Amsterdam': 'Tu travailles l\'année prochaine à Amsterdam',
        'Elle travaillaient het plan': 'Elles travaillaient sur le plan',
        'Elles pouvaient aller au café mardi': 'Elles pouvaient aller au café mardi',
        'Tu ouvre la fenêtre': 'Tu ouvres la fenêtre',
        'Nous donnent het cadeau': 'Nous donnons le cadeau',
        'Je apprends néerlandais': 'J\'apprends le néerlandais',
        'Elle donne l\'après-midi sur la terrasse': 'Elle donne l\'après-midi sur la terrasse',
        'L\'enfant voit le musée vers Bruxelles': 'L\'enfant voit le musée vers Bruxelles',
        'Elle ne mettent pas les affaires en Espagne': 'Elles ne mettent pas les affaires en Espagne',
        'Vous marchent en Espagne': 'Vous marchez en Espagne',
        'Vous donnent het cadeau': 'Vous donnez le cadeau',
        'Tu donnes vendredi het cadeau au magasin': 'Tu donnes vendredi le cadeau au magasin',
        'Je apprends français': 'J\'apprends le français',
        'Elle speelt le soir le jeu': 'Elle joue au jeu le soir',
        'Vous font au parc pas': 'Vous ne faites pas au parc',
        'Tu huis dans la rue': 'Tu habites dans la rue',
        'Elle vois le soir en ville': 'Elle voit le soir en ville',
    }
    
    # Si nous avons une traduction pré-définie, l'utiliser
    if phrase_francais in traductions:
        return traductions[phrase_francais]
    
    # Sinon, appliquer des règles de traduction logiques
    # Corriger les erreurs de conjugaison et de syntaxe communes
    result = phrase_francais
    
    # Correction générale des négations maladroites
    if ' pas' in result and 'ne' not in result:
        # Transformer "verbe pas" en "ne verbe pas"
        result = result.replace(' pas', '')  # Enlever le pas traînard
        if 'je ' in result.lower():
            result = result.replace('je ', 'je ne ').replace(' pas', '') if ' pas' not in result else result
    
    # Traductions spécifiques aux verbes néerlandais courants
    if 'het cadeau' in result:
        result = result.replace('het cadeau', 'le cadeau')
    if 'het plan' in result:
        result = result.replace('het plan', 'le plan')
    if 'het travaille' in result:
        result = result.replace('het travaille', 'le travail')
    if 'het ' in result and 'het' not in ['het restaurant', 'het parc', 'het café']:
        # Remplacer les articles néerlandais résiduels par français
        result = result.replace('het ', 'le ')
        result = result.replace('de ', 'de ')
    
    # Correction des conjugaisons
    if 'speelt' in result:
        result = result.replace('speelt', 'joue')
    if 'vraagde' in result:
        result = result.replace('vraagde', 'demandait')
    if 'prenait' in result and 'Tu p' in result:
        result = result.replace('Tu prenait', 'Tu prenais')
    if 'van 9 tot 5' in result:
        result = result.replace('van 9 tot 5', 'de 9 à 17 heures')
    
    return result


def main():
    # Lire le fichier JSON
    with open('corpus.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Traiter chaque phrase
    count = 0
    for entry in data['corpus']:
        old_fr = entry['phrase_francais']
        new_fr = traduction_logique(entry['phrase'], old_fr)
        
        if old_fr != new_fr:
            entry['phrase_francais'] = new_fr
            count += 1
    
    # Sauvegarder le fichier modifié
    with open('corpus.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ {count} traductions corrigées")
    print(f"✓ Fichier sauvegardé")


if __name__ == '__main__':
    main()
