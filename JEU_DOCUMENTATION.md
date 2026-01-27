# 🎮 Jeu des Mots Mélangés - Documentation

## Vue d'ensemble
Le **Jeu des Mots Mélangés** est un exercice interactif qui permet aux étudiants de réorganiser des mots néerlandais dans le bon ordre en utilisant leur souris (drag & drop).

## Fichiers
- **jeu_mots_melanges.html** : Le jeu complet avec interface et logique
- **corpus.json** : Source de données contenant toutes les phrases et leurs métadonnées

## Fonctionnalités principales

### 1. **Système de Jeu**
- Les phrases du corpus sont présentées une par une
- Les mots de chaque phrase sont mélangés aléatoirement
- L'étudiant doit cliquer sur les mots dans le bon ordre pour reconstituer la phrase
- Les mots sélectionnés apparaissent dans une zone dédiée

### 2. **Système d'Aide Progressive**
Quatre niveaux d'aide disponibles :

1. **📋 Voir la règle** - Affiche la règle grammaticale associée
   - Exemple: "Règle 1.4: GNS + Verbe + Lieu + Négation"

2. **💡 Voir l'exemple** - Affiche un exemple fourni par le professeur
   - Aide à comprendre le pattern grammatical

3. **🇫🇷 Voir traduction** - Affiche la traduction française
   - Permet de vérifier la compréhension du sens

4. **✅ Voir la réponse** - Affiche directement la bonne réponse
   - Dernier recours si l'étudiant ne trouve pas

### 3. **Système de Vérification**
- Bouton **Vérifier** : Valide la réponse de l'étudiant
- Comparaison exacte avec la phrase du corpus
- Messages de feedback instantanés :
  - ✅ "Excellent! C'est correct!" (en vert)
  - ❌ "Ce n'est pas correct. Réessayez ou demandez de l'aide." (en rouge)

### 4. **Système de Scoring**
Le score est basé sur le nombre de phrases testées :
- **Points** : Nombre de phrases correctement réorganisées
- **Phrases testées** : Nombre total de phrases abordées
- **Pourcentage** : Calculé automatiquement (Points / Testées * 100)
- **Statistiques finales** :
  - Réussies : Nombre de bonnes réponses
  - Échouées : Nombre de mauvaises réponses
  - Score : Pourcentage final

### 5. **Navigation**
- **Commencer** : Démarrer le jeu avec la première phrase
- **Suivant →** : Passer à la phrase suivante (après validation)
- **Recommencer** : Réinitialiser le jeu complet
- **← Retour** : Revenir à la page d'accueil

## Interface Utiliselle

### Zone 1: Score et comptage
```
Points: X | Phrases testées: Y
```
Affichage en temps réel du progression

### Zone 2: Affichage de la phrase
Affiche "🎯 Reorganisez les mots" en attente de réponse

### Zone 3: Zone d'aide
S'affiche dynamiquement quand l'étudiant clique sur un bouton d'aide
- Fond bleu clair
- Texte explicatif
- Apparition en douceur (animation)

### Zone 4: Mots mélangés (Jaune/Orange)
- Les mots sont affichés individuellement
- Chaque mot est cliquable
- Survol : surlignage et effet de profondeur
- Sélection : changement de couleur et agrandissement

### Zone 5: Réponse (Vert)
- Zone de construction progressive de la réponse
- Les mots sélectionnés apparaissent dans l'ordre
- Clic sur un mot pour le retirer (annulation)

### Zone 6: Contrôles
Boutons d'action contextuels qui s'affichent/masquent selon l'état du jeu

### Zone 7: Statistiques
Résumé final avec 3 métriques clés :
- Réussies
- Échouées  
- Score (%)

## Flux du Jeu

```
1. Clic "Commencer"
   ↓
2. Affichage phrase #1
   ├─ Mots mélangés (jaune)
   ├─ Boutons d'aide disponibles
   ├─ Zone de réponse vide (vert)
   ↓
3. Étudiant clique sur mots pour les ajouter
   ├─ Mots deviennent sélectionnés
   ├─ Apparaissent dans zone de réponse
   ├─ Peut cliquer sur aide si besoin
   ↓
4. Clique "Vérifier"
   ├─ Comparaison avec corpus
   ├─ Message de feedback
   ├─ Incrémentation des compteurs
   ↓
5. Clique "Suivant"
   ├─ Charge phrase suivante
   ├─ Réinitialise zones
   ├─ Retour à l'étape 2
   ↓
6. Après dernière phrase
   ├─ Affichage "Jeu terminé!"
   ├─ Résumé des résultats
   ├─ Affichage statistiques
   └─ Bouton "Recommencer"
```

## Données du Corpus

Chaque phrase dans corpus.json contient :

```json
{
  "phrase": "Ik ga naar de bibliotheek niet",
  "regle": "Règle 1.4: GNS + Verbe + Lieu + Négation",
  "exemple": "Peter gaat naar het museum niet",
  "phrase_francais": "Je ne vais pas à la bibliothèque"
}
```

Le jeu utilise :
- **phrase** : Phrase source à réorganiser (après suppression du "niet")
- **regle** : Affichée via le bouton "Voir la règle"
- **exemple** : Affichée via le bouton "Voir l'exemple"
- **phrase_francais** : Affichée via le bouton "Voir traduction"

## Améliorations Techniques

### Responsive Design
- Desktop : Grille de mots optimale
- Tablette : Adaptation des espacements
- Mobile : Boutons en colonne, mots en deux colonnes

### Accessibilité
- Navigation au clavier (onclick)
- Messages clairs et colorés
- Contraste de couleurs adéquat

### Performance
- Chargement JSON asynchrone
- Pas de rechargement page
- État persistant pendant la session

## Personnalisation Possible

### Ajouter des phrases
1. Modifier corpus.json
2. Ajouter une nouvelle entrée avec les 4 champs
3. Rafraîchir le jeu

### Modifier les règles de validation
Éditer la fonction `validateAnswer()` dans le JavaScript

### Changer les couleurs
Modifier les variables CSS (sections `.word-box`, `.word-in-answer`, etc.)

### Ajouter des niveaux de difficulté
Implémenter un sélecteur et filtrer le corpus par niveau

## Intégration au Site

Le jeu est accessible via :
1. **Menu principal** → Exercices → 🎮 Jeu des Mots Mélangés
2. **URL directe** : `jeu_mots_melanges.html`

## Messages Pédagogiques

Tous les messages utilisent des emojis pour l'engagement :
- ✅ Succès
- ❌ Erreur
- 💡 Conseil
- 📖 Information
- 🎯 Objectif
- 🎊 Fin/Célébration

## Limitations et Améliorations Futures

### Actuellement
- Une seule forme de la phrase (pas d'variations)
- Pas de limite de temps
- Pas de système de compte utilisateur

### Possibilités d'amélioration
- Ajouter un timer pour plus de challenge
- Implémenter un classement
- Ajouter des phrases avec variations
- Système de badges
- Export de résultats
- Mode multijoueur
- Difficultés progressives
