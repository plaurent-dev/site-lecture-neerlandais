#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de corpus de phrases néerlandaises A1
Basé sur les règles d'ordre des mots étudiées en cours
"""
import json
import random
from typing import List, Dict, Tuple

class CorpusGenerator:
    def __init__(self):
        self.verbes_present_reguliers = []
        self.verbes_present_irreguliers = []
        self.verbes_imparfait_reguliers = []
        self.verbes_imparfait_irreguliers = []
        self.corpus = []
        self.used_phrases = set()
        
        # Sujets prédéfinis
        self.subjects = {
            "ik": ("Ik", "present_ik", "imparfait_singulier"),
            "jij": ("Jij", "present_jij_hij_ze", "imparfait_singulier"),
            "hij": ("Hij", "present_jij_hij_ze", "imparfait_singulier"),
            "zij_sg": ("Zij", "present_jij_hij_ze", "imparfait_singulier"),
            "de_man": ("De man", "present_jij_hij_ze", "imparfait_singulier"),
            "de_vrouw": ("De vrouw", "present_jij_hij_ze", "imparfait_singulier"),
            "het_kind": ("Het kind", "present_jij_hij_ze", "imparfait_singulier"),
            "de_jongen": ("De jongen", "present_jij_hij_ze", "imparfait_singulier"),
            "wij": ("Wij", "present_wij_jullie_ze", "imparfait_pluriel"),
            "jullie": ("Jullie", "present_wij_jullie_ze", "imparfait_pluriel"),
            "zij_pl": ("Zij", "present_wij_jullie_ze", "imparfait_pluriel"),
        }
        
        # Listes d'éléments pour la génération
        self.objects = [
            "de hond", "de kat", "het boek", "de tabel", "de auto", "het huis",
            "de brief", "het eten", "het café", "de winkel", "het museum",
            "de vrienden", "de kinderen", "het artikel", "de bloemen", "de pen",
            "het water", "de chocolade", "de appel", "het brood"
        ]
        
        self.locations = [
            "in Amsterdam", "in Nederland", "in Spanje", "in het café",
            "in de winkel", "op straat", "naar Ierland", "naar Luik",
            "naar het museum", "op school", "in het park", "naar het station",
            "in de bibliotheek", "op het plein", "in de stad", "naar Brussel",
            "in het restaurant", "op het terras"
        ]
        
        self.times = [
            "vandaag", "morgen", "gisterdag", "maandag", "dinsdag", "woensdag",
            "donderdag", "vrijdag", "zaterdag", "zondag", "volgende week",
            "volgende maand", "volgende jaar", "om 8 uur", "om 14 uur", 
            "'s ochtends", "'s middags", "'s avonds", "na het werk", "voor het eten",
            "in de nacht", "van 9 tot 5"
        ]
        
        self.adjectives = [
            "mooi", "groot", "klein", "rood", "oud", "jong", "druk", "rustig",
            "interessant", "aardig", "duur", "goedkoop", "slim", "sneller", 
            "langzaam", "grijs", "wit", "zwart", "geel", "groen", "blauw", "fijn",
            "leuk", "lelijk", "vrolijk", "verdrietig", "sterk", "zwak"
        ]
        
        # Associations cohérentes verbe-COD pour éviter les phrases absurdes
        self.verb_objects = {
            # Verbes de perception/connaissance
            "zien": ["de hond", "de kat", "de vrienden", "het boek", "het museum", "het kind", "de auto", "de vogels", "de film"],
            "kennen": ["de hond", "de kat", "de vrienden", "de man", "de vrouw", "het kind", "Amsterdam", "Nederland"],
            "horen": ["de muziek", "het geluid", "de stem", "het nieuws"],
            
            # Verbes d'action/activité
            "dragen": ["het boek", "de auto", "de brief", "het geschenk", "de rugzak", "de jas"],
            "brengen": ["het cadeau", "de brief", "het boek", "de tabel", "het geschenk", "de kinderen"],
            "nemen": ["het boek", "de kat", "het eten", "de pen", "het geld", "de auto"],
            "geven": ["het cadeau", "het geschenk", "de bloemen", "het geld", "de brief", "het eten"],
            
            # Verbes d'consommation/nourriture
            "eten": ["het eten", "het brood", "de appel", "de chocolade", "de kaas", "het vlees", "de soep"],
            "drinken": ["het water", "het bier", "de koffie", "de thee", "de melk", "het sap"],
            "koken": ["het eten", "de soep", "het vlees", "de vis", "de maaltijd"],
            
            # Verbes d'activités créatives/intellectuelles
            "lezen": ["het boek", "de brief", "het artikel", "de krant", "het verhaal", "het gedicht"],
            "schrijven": ["de brief", "het artikel", "het boek", "de naam", "het gedicht"],
            "tekenen": ["het huis", "de kat", "de auto", "het portret"],
            "spelen": ["het spel", "de gitaar", "het instrument", "het piano", "de bal", "het voetbal"],
            
            # Verbes intransitifs - PAS de COD
            "lopen": [],
            "gaan": [],
            "reizen": [],
            "rijden": ["de auto", "de fiets", "het paard"],
            "wandelen": [],
            
            # Verbes d'achat/commerce
            "kopen": ["het boek", "de auto", "de bloemen", "het eten", "het geschenk", "de kleding", "de pen"],
            "verkopen": ["het boek", "de auto", "het huis", "het eten"],
            
            # Verbes de visite
            "bezoeken": ["het museum", "het café", "het restaurant", "de school", "de bibliotheek", "de stad", "de vrienden"],
            
            # Verbes de travail/apprentissage - OBLIGATOIREMENT COD
            "werken": ["het project", "het plan", "de taak"],
            "leren": ["Nederlands", "Frans", "Engels", "het boek", "de les"],
            "tellen": ["het geld", "de dingen", "de kinderen", "de dagen"],
            "rekenen": ["het geld", "de getallen", "de taken", "de nummers"],
            "openen": ["de deur", "het raam", "het boek", "het geschenk", "de winkel"],
            
            # Verbes de sentiment/pensée
            "houden": ["van de hond", "van de kat", "van het eten", "van de muziek", "van de vrienden", "van Nederland"],
            "denken": ["aan de vrienden", "aan het werk", "aan de vakantie"],
            "vinden": ["het boek", "de film", "het museum", "het restaurant", "het huis"],
        }
    
    def load_data(self) -> bool:
        """Charge tous les fichiers JSON"""
        try:
            with open('present_regulier.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.verbes_present_reguliers = data.get('verbes_reguliers_present', [])
            
            with open('present_irregulier.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.verbes_present_irreguliers = data.get('verbes_irreguliers_present', [])
            
            with open('imparfait_regulier.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.verbes_imparfait_reguliers = data.get('verbes_reguliers', [])
            
            with open('imparfait_irregulier.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.verbes_imparfait_irreguliers = data.get('verbes_irreguliers', [])
                
            print("✓ Données chargées avec succès")
            print(f"  - Verbes présent réguliers: {len(self.verbes_present_reguliers)}")
            print(f"  - Verbes présent irréguliers: {len(self.verbes_present_irreguliers)}")
            print(f"  - Verbes imparfait réguliers: {len(self.verbes_imparfait_reguliers)}")
            print(f"  - Verbes imparfait irréguliers: {len(self.verbes_imparfait_irreguliers)}")
            
        except Exception as e:
            print(f"✗ Erreur: {e}")
            return False
        return True
    
    def add_phrase(self, phrase: str, rule: str, example: str) -> bool:
        """Ajoute une phrase unique au corpus"""
        if phrase not in self.used_phrases and len(phrase.strip()) > 5:
            self.corpus.append({
                "phrase": phrase.strip(),
                "regle": rule,
                "exemple": example
            })
            self.used_phrases.add(phrase)
            return True
        return False
    
    def get_subject(self, subject_key: str) -> str:
        """Retourne le sujet"""
        return self.subjects[subject_key][0]
    
    def get_verb_form(self, subject_key: str, verbs: List[Dict]) -> Tuple[str, str]:
        """Retourne un verbe conjugué et son infinitif"""
        if not verbs:
            return "", ""
        
        verb = random.choice(verbs)
        infinitive = verb.get('infinitif', '')
        subject, conj_key, _ = self.subjects[subject_key]
        form = verb.get(conj_key, '')
        return infinitive, form
    
    def get_verb_imparfait(self, subject_key: str, verbs: List[Dict]) -> Tuple[str, str]:
        """Retourne un verbe à l'imparfait et son infinitif"""
        if not verbs:
            return "", ""
        
        verb = random.choice(verbs)
        infinitive = verb.get('infinitif', '')
        subject, _, imparfait_key = self.subjects[subject_key]
        form = verb.get(imparfait_key, '')
        return infinitive, form
    
    def get_appropriate_object(self, verb_infinitive: str) -> str:
        """Retourne un COD approprié au verbe, ou None si le verbe n'en prend pas"""
        if verb_infinitive in self.verb_objects:
            objects = self.verb_objects[verb_infinitive]
            # Si la liste est vide (verbes intransitifs), retourner None
            if not objects:
                return None
            return random.choice(objects)
        
        # Verbes intransitifs ou modaux - retourner None
        intransitive_verbs = ["komen", "gaan", "zitten", "staan", "wonen", "blijven", 
                             "worden", "kunnen", "willen", "moeten", "mogen", "hoeven",
                             "lopen", "rennen", "vallen", "starten", "eindigen", "reizen",
                             "rijden", "wandelen"]
        if verb_infinitive in intransitive_verbs:
            return None
        
        # Fallback : aucun COD
        return None
    
    def requires_cod(self, verb_infinitive: str) -> bool:
        """Vérifie si un verbe exige obligatoirement un COD"""
        required_cod_verbs = ["tellen", "rekenen", "werken", "leren", "openen"]
        return verb_infinitive in required_cod_verbs
    
    def rule_1_basic_construction(self):
        """Règle 1: GNS + Verbe + Compléments + Éléments fin de phrase"""
        print("  Génération Règle 1 (Constructions de base)...")
        count = 0
        
        for _ in range(80):
            subject_key = random.choice(list(self.subjects.keys()))
            subject = self.get_subject(subject_key)
            infinitive, verb_form = self.get_verb_form(subject_key, 
                                           random.choice([self.verbes_present_reguliers, 
                                                         self.verbes_present_irreguliers]))
            
            if not verb_form:
                continue
            
            # Skip verbs that require COD for Rule 1
            if self.requires_cod(infinitive):
                continue
            
            choice = random.randint(1, 4)
            
            # GNS + Verbe + Temps
            if choice == 1:
                time = random.choice(self.times)
                phrase = f"{subject} {verb_form} {time}"
                if self.add_phrase(phrase, "Règle 1.1: GNS + Verbe + Temps", "Bert komt vandaag"):
                    count += 1
            
            # GNS + Verbe + Temps + Négation
            elif choice == 2:
                time = random.choice(self.times)
                phrase = f"{subject} {verb_form} {time} niet"
                if self.add_phrase(phrase, "Règle 1.2: GNS + Verbe + Temps + Négation", "Bert komt vandaag niet"):
                    count += 1
            
            # GNS + Verbe + Lieu
            elif choice == 3:
                loc = random.choice(self.locations)
                phrase = f"{subject} {verb_form} {loc}"
                if self.add_phrase(phrase, "Règle 1.3: GNS + Verbe + Lieu", "Zij gaan naar Amsterdam"):
                    count += 1
            
            # GNS + Verbe + Lieu + Négation
            else:
                loc = random.choice(self.locations)
                phrase = f"{subject} {verb_form} {loc} niet"
                if self.add_phrase(phrase, "Règle 1.4: GNS + Verbe + Lieu + Négation", "Peter gaat naar het museum niet"):
                    count += 1
        
        print(f"    → {count} phrases générées")
    
    def rule_2_complement_order(self):
        """Règle 2: Ordre des compléments"""
        print("  Génération Règle 2 (Ordre des compléments)...")
        count = 0
        
        for _ in range(150):
            subject_key = random.choice(list(self.subjects.keys()))
            subject = self.get_subject(subject_key)
            infinitive, verb_form = self.get_verb_form(subject_key,
                                           random.choice([self.verbes_present_reguliers,
                                                         self.verbes_present_irreguliers]))
            
            if not verb_form:
                continue
            
            choice = random.randint(1, 5)
            
            # GNS + Verbe + COD (avec verbe cohérent)
            if choice == 1:
                obj = self.get_appropriate_object(infinitive)
                if obj:  # Seulement si le verbe accepte un COD
                    phrase = f"{subject} {verb_form} {obj}"
                    if self.add_phrase(phrase, "Règle 2.1: GNS + Verbe + COD", "Hij kent de hond"):
                        count += 1
            
            # GNS + Verbe + Temps + COD
            elif choice == 2:
                obj = self.get_appropriate_object(infinitive)
                if obj:  # Seulement si le verbe accepte un COD
                    time = random.choice(self.times)
                    phrase = f"{subject} {verb_form} {time} {obj}"
                    if self.add_phrase(phrase, "Règle 2.2: GNS + Verbe + Temps + COD", "Ik eet morgen het eten"):
                        count += 1
            
            # GNS + Verbe + COD + Lieu
            elif choice == 3:
                obj = self.get_appropriate_object(infinitive)
                if obj:  # Seulement si le verbe accepte un COD
                    loc = random.choice(self.locations)
                    phrase = f"{subject} {verb_form} {obj} {loc}"
                    if self.add_phrase(phrase, "Règle 2.3: GNS + Verbe + COD + Lieu", "Ik wil een reis naar Spanje maken"):
                        count += 1
            
            # GNS + Verbe + Temps + Lieu
            elif choice == 4:
                time = random.choice(self.times)
                loc = random.choice(self.locations)
                phrase = f"{subject} {verb_form} {time} {loc}"
                if self.add_phrase(phrase, "Règle 2.4: GNS + Verbe + Temps + Lieu", "Zij is op zondag naar het museum gegaan"):
                    count += 1
            
            # GNS + Verbe + COD + Temps
            else:
                obj = self.get_appropriate_object(infinitive)
                if obj:  # Seulement si le verbe accepte un COD
                    time = random.choice(self.times)
                    phrase = f"{subject} {verb_form} {obj} {time}"
                    if self.add_phrase(phrase, "Règle 2.5: GNS + Verbe + COD + Temps", "Hij ziet de vrienden morgen"):
                        count += 1
        
        print(f"    → {count} phrases générées")
    
    def rule_3_imparfait(self):
        """Règle 3: Mêmes structures à l'imparfait"""
        print("  Génération Règle 3 (Structures à l'imparfait)...")
        count = 0
        
        for _ in range(130):
            subject_key = random.choice(list(self.subjects.keys()))
            subject = self.get_subject(subject_key)
            infinitive, verb_form = self.get_verb_imparfait(subject_key,
                                                random.choice([self.verbes_imparfait_reguliers,
                                                              self.verbes_imparfait_irreguliers]))
            
            if not verb_form:
                continue
            
            choice = random.randint(1, 4)
            
            # GNS + Verbe imparfait + COD
            if choice == 1:
                obj = self.get_appropriate_object(infinitive)
                if obj:  # Seulement si le verbe accepte un COD
                    phrase = f"{subject} {verb_form} {obj}"
                    if self.add_phrase(phrase, "Règle 3.1: Imparfait - GNS + Verbe + COD", "Zij zagen de hond"):
                        count += 1
            
            # GNS + Verbe imparfait + Temps (skip if verb requires COD)
            elif choice == 2:
                if not self.requires_cod(infinitive):
                    time = random.choice(self.times)
                    phrase = f"{subject} {verb_form} {time}"
                    if self.add_phrase(phrase, "Règle 3.2: Imparfait - GNS + Verbe + Temps", "Zij kwamen gisterdag"):
                        count += 1
            
            # GNS + Verbe imparfait + Lieu (skip if verb requires COD)
            elif choice == 3:
                if not self.requires_cod(infinitive):
                    loc = random.choice(self.locations)
                    phrase = f"{subject} {verb_form} {loc}"
                    if self.add_phrase(phrase, "Règle 3.3: Imparfait - GNS + Verbe + Lieu", "Wij waren in het park"):
                        count += 1
            
            # GNS + Verbe imparfait + Temps + Lieu (skip if verb requires COD)
            else:
                if not self.requires_cod(infinitive):
                    time = random.choice(self.times)
                    loc = random.choice(self.locations)
                    phrase = f"{subject} {verb_form} {time} {loc}"
                    if self.add_phrase(phrase, "Règle 3.4: Imparfait - GNS + Verbe + Temps + Lieu", "Zij gingen gisterdag naar Amsterdam"):
                        count += 1
        
        print(f"    → {count} phrases générées")
    
    def rule_4_complex(self):
        """Règle 4: Structures complexes"""
        print("  Génération Règle 4 (Structures complexes)...")
        count = 0
        
        for _ in range(100):
            subject_key = random.choice(list(self.subjects.keys()))
            subject = self.get_subject(subject_key)
            infinitive, verb_form = self.get_verb_form(subject_key,
                                           random.choice([self.verbes_present_reguliers,
                                                         self.verbes_present_irreguliers]))
            
            if not verb_form:
                continue
            
            choice = random.randint(1, 3)
            
            # GNS + Verbe + Temps + COD + Lieu
            if choice == 1:
                obj = self.get_appropriate_object(infinitive)
                if obj:  # Seulement si le verbe accepte un COD
                    time = random.choice(self.times)
                    loc = random.choice(self.locations)
                    phrase = f"{subject} {verb_form} {time} {obj} {loc}"
                    if self.add_phrase(phrase, "Règle 4.1: GNS + Verbe + Temps + COD + Lieu", 
                                      "Wij brengen het cadeau morgen naar Amsterdam"):
                        count += 1
            
            # GNS + Verbe + Temps + Lieu + Négation (skip if verb requires COD)
            elif choice == 2:
                if not self.requires_cod(infinitive):
                    time = random.choice(self.times)
                    loc = random.choice(self.locations)
                    phrase = f"{subject} {verb_form} {time} {loc} niet"
                    if self.add_phrase(phrase, "Règle 4.2: GNS + Verbe + Temps + Lieu + Négation",
                                      "Zij eten vandaag in het restaurant niet"):
                        count += 1
            
            # GNS + Verbe + COD + Temps + Lieu
            else:
                obj = self.get_appropriate_object(infinitive)
                if obj:  # Seulement si le verbe accepte un COD
                    time = random.choice(self.times)
                    loc = random.choice(self.locations)
                    phrase = f"{subject} {verb_form} {obj} {time} {loc}"
                    if self.add_phrase(phrase, "Règle 4.3: GNS + Verbe + COD + Temps + Lieu",
                                      "Ik breng het boek morgen naar het museum"):
                        count += 1
        
        print(f"    → {count} phrases générées")
    
    def generate(self):
        """Génère le corpus complet"""
        print("\n=== Génération du corpus de phrases ===\n")
        
        self.rule_1_basic_construction()
        self.rule_2_complement_order()
        self.rule_3_imparfait()
        self.rule_4_complex()
        
        # Mélanger le corpus
        random.shuffle(self.corpus)
        
        print(f"\n✓ Total généré: {len(self.corpus)} phrases uniques\n")
    
    def save(self) -> bool:
        """Sauvegarde le corpus dans corpus.json"""
        output = {
            "metadata": {
                "description": "Corpus de phrases néerlandaises A1 suivant les règles d'ordre des mots",
                "date": "2026-01-27",
                "total_phrases": len(self.corpus),
                "notes": "Corpus généré pour la pratique de la syntaxe néerlandaise A1"
            },
            "regles_principales": {
                "regle_1": "Constructions de base: GNS + Verbe + Temps/Lieu ± Négation",
                "regle_2": "Ordre des compléments: GNS + Verbe + COD/Temps + Lieu",
                "regle_3": "Mêmes structures à l'imparfait",
                "regle_4": "Structures complexes avec plusieurs compléments"
            },
            "details_regles": {
                "Règle 1": "GNS + Verbe + Éléments fin de phrase (négation, temps, lieu)",
                "Règle 2": "GNS + Verbe + COD et/ou Compléments (temps, lieu) dans l'ordre : temps, COD, lieu",
                "Règle 3": "Mêmes structures avec verbes à l'imparfait",
                "Règle 4": "Structures complexes avec plusieurs compléments combinés"
            },
            "corpus": self.corpus
        }
        
        try:
            with open('corpus.json', 'w', encoding='utf-8') as f:
                json.dump(output, f, ensure_ascii=False, indent=2)
            
            print(f"✓ Corpus sauvegardé dans corpus.json")
            
            # Statistiques
            rules = {}
            for phrase in self.corpus:
                rule_prefix = phrase['regle'].split(':')[0]
                rules[rule_prefix] = rules.get(rule_prefix, 0) + 1
            
            print("\nStatistiques par catégorie:")
            for rule, count in sorted(rules.items()):
                percentage = (count / len(self.corpus)) * 100
                print(f"  {rule}: {count} phrases ({percentage:.1f}%)")
            
            return True
        
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde: {e}")
            return False

def main():
    print("╔════════════════════════════════════════════════════╗")
    print("║  Générateur de Corpus Néerlandais A1               ║")
    print("║  Règles d'ordre des mots                           ║")
    print("╚════════════════════════════════════════════════════╝\n")
    
    generator = CorpusGenerator()
    
    if generator.load_data():
        generator.generate()
        if generator.save():
            print("\n✓ Processus terminé avec succès!\n")
        else:
            print("\n✗ Erreur lors de la sauvegarde\n")
    else:
        print("\n✗ Impossible de charger les données\n")

if __name__ == "__main__":
    main()
