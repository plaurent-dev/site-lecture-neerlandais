# 📋 Guide d'Implémentation - Version Centralisée

## ✅ Fichiers créés

```
Mon-site/
├── version.js                    ← Solution 1 (Recommandée)
├── version.json                  ← Optionnel pour Solution 2
├── version-manager.js            ← Optionnel pour Solution 2
├── VERSION_MANAGEMENT.md         ← Cette documentation
└── ... vos pages HTML
```

---

## 🎯 **À FAIRE MAINTENANT**

### Étape 1 : Choisir une solution

**Option A (Recommandée)** : Utilisez `version.js`
```html
<!-- Ajouter dans le <head> de chaque page HTML -->
<script src="version.js"></script>
```

**Option B** : Utilisez `version-manager.js` (si vous avez besoin de plus de contrôle)
```html
<!-- Ajouter dans le <head> de chaque page HTML -->
<script src="version-manager.js"></script>
```

### Étape 2 : Ajouter le script aux pages

Pour chaque fichier HTML, insérez avant la balise `</head>` fermante:

#### Exemple pour `index.html`:
```html
    <link rel="stylesheet" href="styles.css?v=1.0.0">

    <style>
        * {
            ...
        }
    </style>
    
    <script src="version.js"></script>  <!-- ← AJOUTER ICI -->
</head>
```

#### Exemple pour `admin.html`:
```html
    <link rel="stylesheet" href="styles.css?v=1.0.0">
    
    <script src="version.js"></script>  <!-- ← AJOUTER ICI -->
</head>
```

---

## 🔄 **À chaque DÉPLOIEMENT**

1. Mettez à jour votre CSS/contenu comme d'habitude
2. **Modifiez JUSTE CETTE LIGNE** dans `version.js`:
   ```javascript
   const APP_VERSION = '1.0.1';  // Changez 1.0.0 → 1.0.1
   ```
3. Déployez les fichiers (le HTML n'a pas besoin de changement!)

### Exemples de versioning:
```
v1.0.0  → v1.0.1  (patch: petit correctif)
v1.0.1  → v1.1.0  (minor: nouvelle fonctionnalité)
v1.1.0  → v2.0.0  (major: changement majeur)
```

---

## 🧪 **Vérifier que ça fonctionne**

### Test dans le navigateur:
1. Ouvrez votre site
2. Ouvrez DevTools (F12)
3. Allez à l'onglet "Network"
4. Rechargez la page (Ctrl+F5)
5. Vous devriez voir `styles.css?v=1.0.0` dans les requêtes

### Vérifier l'affichage:
1. Ouvrez la console (F12 > Console)
2. Tapez: `document.querySelector('link').href`
3. Vous devriez voir: `...styles.css?v=1.0.0`

---

## 🎓 **Comment ça marche techniquement?**

```
┌─────────────────────────────────────────┐
│ Page HTML se charge                     │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ <link> demande: styles.css?v=1.0.0      │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ <script src="version.js"> se charge     │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ version.js lit APP_VERSION = '1.0.0'    │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ version.js modifie le lien CSS si besoin│
│ (ou le laisse tel quel)                 │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ CSS appliqué avec le bon cache busting  │
└─────────────────────────────────────────┘
```

---

## 📌 **Points importants**

| Point | Explication |
|-------|-------------|
| ✅ Les fichiers HTML RESTENT inchangés | Oui, ajoutez juste `<script>` une fois |
| ✅ Juste `version.js` à modifier | Oui, une seule ligne à chaque déploiement |
| ✅ Fonctionne sans serveur backend | Oui, c'est du pur JavaScript client |
| ✅ Cache busting automatique | Oui, l'URL change à chaque version |
| ✅ Compatible avec tous les navigateurs | Oui, c'est du JS vanilla simple |

---

## 🚀 **Prochaines étapes**

### Recommandé:
- [ ] Ajouter `<script src="version.js"></script>` aux pages HTML principales
- [ ] Tester dans le navigateur
- [ ] À la prochaine mise à jour, changer juste la version dans `version.js`

### Optionnel (futur):
- [ ] Utiliser `version-manager.js` si vous voulez plus de contrôle
- [ ] Automatiser avec Git hooks
- [ ] Créer un script de déploiement

---

## 💡 **Besoin d'aide?**

**Q: Toutes les pages doivent avoir le script?**
A: Oui, mais juste une ligne `<script src="version.js"></script>` dans le `<head>`

**Q: Ça affecte les performances?**
A: Non, `version.js` est très léger (< 1KB)

**Q: Que faire si j'oublie de changer la version?**
A: Pas grave, juste que les visiteurs verront le cache. À la prochaine mise à jour, changez la version.

**Q: Puis-je utiliser un autre numéro de version?**
A: Oui! Utilisez n'importe quel format: `1.2.3`, `v2.0`, `20260118`, etc.

---

**Créé**: 18 janvier 2026
