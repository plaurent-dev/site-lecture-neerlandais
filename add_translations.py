#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour ajouter les traductions en français au corpus
"""
import json

class TranslationAdder:
    def __init__(self):
        # Dictionnaire de traductions
        self.translations = {
            # Sujets
            "Ik": "Je",
            "Jij": "Tu",
            "Hij": "Il",
            "Zij": "Elle",
            "Wij": "Nous",
            "Jullie": "Vous",
            "Ze": "Ils/Elles",
            "De man": "L'homme",
            "De vrouw": "La femme",
            "Het kind": "L'enfant",
            "De jongen": "Le garçon",
            "Het meisje": "La fille",
            
            # Verbes - Présent réguliers
            "werk": "travaille",
            "leer": "apprends",
            "maak": "fais",
            "praat": "parles",
            "woon": "habite",
            "tel": "compte",
            "hou": "aimes",
            "eet": "manges",
            "drink": "bois",
            "geef": "donnes",
            "neem": "prends",
            "lees": "lis",
            "schrijf": "écris",
            "koop": "achètes",
            "bezoek": "visites",
            "zet": "mets",
            "hal": "cherches",
            
            "werkt": "travaille",
            "leert": "apprend",
            "maakt": "fait",
            "praat": "parle",
            "woont": "habite",
            "telt": "compte",
            "houdt": "aime",
            "eet": "mange",
            "drinkt": "boit",
            "geeft": "donne",
            "neemt": "prend",
            "liest": "lit",
            "schrijft": "écrit",
            "koopt": "achète",
            "bezoekt": "visite",
            "zet": "met",
            "haalt": "cherche",
            
            "werken": "travaillent",
            "leren": "apprennent",
            "maken": "font",
            "praten": "parlent",
            "wonen": "habitent",
            "tellen": "comptent",
            "houden": "aiment",
            "eten": "mangent",
            "drinken": "boivent",
            "geven": "donnent",
            "nemen": "prennent",
            "lezen": "lisent",
            "schrijven": "écrivent",
            "kopen": "achètent",
            "bezoeken": "visitent",
            "zetten": "mettent",
            "halen": "cherchent",
            
            # Verbes - Présent irréguliers
            "ga": "vais",
            "kom": "viens",
            "zie": "vois",
            "ben": "suis",
            "heb": "ai",
            "wil": "veux",
            "kan": "peux",
            "zeg": "dis",
            "hou": "aime",
            "denk": "pense",
            "vind": "trouve",
            "vraag": "demande",
            "antwoord": "réponds",
            "reis": "voyage",
            "blijf": "reste",
            "rij": "conduis",
            "wandel": "marche",
            "open": "ouvre",
            "kook": "cuisine",
            "reken": "compte",
            "val": "tombe",
            
            "gaat": "va",
            "komt": "vient",
            "ziet": "voit",
            "is": "est",
            "hebt": "as",
            "wilt": "veux",
            "kan": "peux",
            "zegt": "dit",
            "houdt": "aime",
            "denkt": "pense",
            "vindt": "trouve",
            "vraagt": "demande",
            "antwoordt": "répond",
            "reist": "voyage",
            "blijft": "reste",
            "rijdt": "conduit",
            "wandelt": "marche",
            "opent": "ouvre",
            "kookt": "cuisine",
            "rekent": "compte",
            "valt": "tombe",
            
            "gaan": "vont",
            "komen": "viennent",
            "zien": "voient",
            "zijn": "sont",
            "hebben": "ont",
            "willen": "veulent",
            "kunnen": "peuvent",
            "zeggen": "disent",
            "houden": "aiment",
            "denken": "pensent",
            "vinden": "trouvent",
            "vragen": "demandent",
            "antwoorden": "répondent",
            "reizen": "voyagent",
            "blijven": "restent",
            "rijden": "conduisent",
            "wandelen": "marchent",
            "openen": "ouvrent",
            "koken": "cuisinent",
            "rekenen": "comptent",
            "vallen": "tombent",
            
            # Verbes - Imparfait réguliers
            "werkte": "travaillait",
            "leerde": "apprenait",
            "maakte": "faisait",
            "praatte": "parlait",
            "woonde": "habitait",
            "telde": "comptait",
            "hield": "aimait",
            "at": "mangeait",
            "dronk": "buvait",
            "gaf": "donnait",
            "nam": "prenait",
            "las": "lisait",
            "schreef": "écrivait",
            "kocht": "achetait",
            "bezocht": "visitait",
            "zette": "mettait",
            "haalde": "cherchait",
            
            "werkten": "travaillaient",
            "leerden": "apprenaient",
            "maakten": "faisaient",
            "praatten": "parlaient",
            "woondens": "habitaient",
            "telden": "comptaient",
            "hielden": "aimaient",
            "aten": "mangeaient",
            "dronken": "buvaient",
            "gaven": "donnaient",
            "namen": "prenaient",
            "lazen": "lisaient",
            "schreven": "écrivaient",
            "kochten": "achetaient",
            "bezochten": "visitaient",
            "zetten": "mettaient",
            "haalde": "cherchaient",
            
            # Verbes - Imparfait irréguliers
            "ging": "allais",
            "kwam": "venais",
            "zag": "voyais",
            "was": "était",
            "had": "avais",
            "wilde": "voulais",
            "kon": "pouvais",
            "zei": "disais",
            "hield": "aimais",
            "dacht": "pensais",
            "vond": "trouvais",
            "vroeg": "demandais",
            "antwoordde": "répondais",
            "reisde": "voyageais",
            "bleef": "restais",
            "reed": "conduisais",
            "wandelde": "marchais",
            "opende": "ouvrais",
            "kookte": "cuisinais",
            "rekende": "comptais",
            
            "gingen": "allaient",
            "kwamen": "venaient",
            "zagen": "voyaient",
            "waren": "étaient",
            "hadden": "avaient",
            "wilden": "voulaient",
            "konden": "pouvaient",
            "zeiden": "disaient",
            "hielden": "aimaient",
            "dachten": "pensaient",
            "vonden": "trouvaient",
            "vroegen": "demandaient",
            "antwoordden": "répondaient",
            "reisden": "voyageaient",
            "bleven": "restaient",
            "reden": "conduisaient",
            "wandelden": "marchaient",
            "openden": "ouvraient",
            "kookten": "cuisinaient",
            "rekenden": "comptaient",
            
            # Compléments d'objet
            "de hond": "le chien",
            "de kat": "le chat",
            "het boek": "le livre",
            "de tabel": "la table",
            "de auto": "la voiture",
            "het huis": "la maison",
            "de brief": "la lettre",
            "het eten": "la nourriture",
            "het café": "le café",
            "de winkel": "le magasin",
            "het museum": "le musée",
            "de vrienden": "les amis",
            "de kinderen": "les enfants",
            "het artikel": "l'article",
            "de bloemen": "les fleurs",
            "de pen": "le stylo",
            "het water": "l'eau",
            "de chocolade": "le chocolat",
            "de appel": "la pomme",
            "het brood": "le pain",
            "de rugzak": "le sac à dos",
            "de jas": "la veste",
            "het geschenk": "le cadeau",
            "de kaas": "le fromage",
            "het vlees": "la viande",
            "de soep": "la soupe",
            "het bier": "la bière",
            "de koffie": "le café",
            "de thee": "le thé",
            "de melk": "le lait",
            "het sap": "le jus",
            "de vis": "le poisson",
            "de maaltijd": "le repas",
            "het verhaal": "l'histoire",
            "het gedicht": "le poème",
            "de gitaar": "la guitare",
            "het instrument": "l'instrument",
            "het piano": "le piano",
            "de bal": "le ballon",
            "het voetbal": "le football",
            "het spel": "le jeu",
            "het portret": "le portrait",
            "de fiets": "le vélo",
            "het paard": "le cheval",
            "de kleding": "les vêtements",
            "het geld": "l'argent",
            "de dingen": "les choses",
            "de dagen": "les jours",
            "het raam": "la fenêtre",
            "de deur": "la porte",
            "de naam": "le nom",
            "het bureau": "le bureau",
            
            # Lieux
            "in Amsterdam": "à Amsterdam",
            "in Nederland": "aux Pays-Bas",
            "in Spanje": "en Espagne",
            "in het café": "au café",
            "in de winkel": "au magasin",
            "op straat": "dans la rue",
            "naar Ierland": "vers l'Irlande",
            "naar Luik": "vers Liège",
            "naar het museum": "vers le musée",
            "op school": "à l'école",
            "in het park": "au parc",
            "naar het station": "vers la gare",
            "in de bibliotheek": "à la bibliothèque",
            "op het plein": "sur la place",
            "in de stad": "en ville",
            "naar Brussel": "vers Bruxelles",
            "in het restaurant": "au restaurant",
            "op het terras": "sur la terrasse",
            "in het bureau": "au bureau",
            "in de fabriek": "à l'usine",
            "in de fabiek": "à l'usine",
            "naar het buitenland": "vers l'étranger",
            
            # Temps
            "vandaag": "aujourd'hui",
            "morgen": "demain",
            "gisterdag": "hier",
            "maandag": "lundi",
            "dinsdag": "mardi",
            "woensdag": "mercredi",
            "donderdag": "jeudi",
            "vrijdag": "vendredi",
            "zaterdag": "samedi",
            "zondag": "dimanche",
            "volgende week": "la semaine prochaine",
            "volgende maand": "le mois prochain",
            "volgende jaar": "l'année prochaine",
            "om 8 uur": "à 8 heures",
            "om 14 uur": "à 14 heures",
            "'s ochtends": "le matin",
            "'s middags": "l'après-midi",
            "'s avonds": "le soir",
            "na het werk": "après le travail",
            "voor het eten": "avant le repas",
            "in de nacht": "la nuit",
            "van 9 tot 5": "de 9 à 17 heures",
            "op zondag": "le dimanche",
            
            # Autres
            "niet": "pas",
            "van de hond": "du chien",
            "van de kat": "du chat",
            "van het eten": "de la nourriture",
            "van de muziek": "de la musique",
            "van de vrienden": "des amis",
            "van Nederland": "des Pays-Bas",
            "naar het werk": "vers le travail",
            "naar school": "vers l'école",
            "naar huis": "vers la maison",
            "Nederlands": "néerlandais",
            "Frans": "français",
            "Engels": "anglais",
        }
    
    def translate_phrase(self, phrase: str) -> str:
        """Traduit une phrase néerlandaise en français"""
        words = phrase.split()
        translated_words = []
        
        i = 0
        while i < len(words):
            # Vérifier les expressions de 2+ mots d'abord
            for length in [3, 2]:
                if i + length <= len(words):
                    candidate = " ".join(words[i:i+length])
                    if candidate in self.translations:
                        translated_words.append(self.translations[candidate])
                        i += length
                        break
            else:
                # Mot simple
                word = words[i]
                if word in self.translations:
                    translated_words.append(self.translations[word])
                else:
                    # Si le mot n'est pas trouvé, le garder tel quel
                    translated_words.append(word)
                i += 1
        
        return " ".join(translated_words)
    
    def process_corpus(self):
        """Charge le corpus et ajoute les traductions"""
        try:
            with open('corpus.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"Chargement du corpus: {len(data['corpus'])} phrases")
            
            # Ajouter la traduction à chaque phrase
            for entry in data['corpus']:
                phrase_nl = entry['phrase']
                phrase_fr = self.translate_phrase(phrase_nl)
                entry['phrase_francais'] = phrase_fr
            
            # Sauvegarder le fichier modifié
            with open('corpus.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"✓ Traductions ajoutées avec succès!")
            print(f"✓ Fichier corpus.json mis à jour")
            
            # Afficher quelques exemples
            print("\nExemples de traductions:")
            for i, entry in enumerate(data['corpus'][:5]):
                print(f"  NL: {entry['phrase']}")
                print(f"  FR: {entry['phrase_francais']}\n")
            
            return True
        
        except Exception as e:
            print(f"✗ Erreur: {e}")
            return False

def main():
    print("╔════════════════════════════════════════════════════╗")
    print("║  Ajout des traductions au corpus                   ║")
    print("╚════════════════════════════════════════════════════╝\n")
    
    adder = TranslationAdder()
    adder.process_corpus()

if __name__ == "__main__":
    main()
