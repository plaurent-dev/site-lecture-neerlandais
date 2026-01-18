# 🔄 Gestion Centralisée de la Version

Vous avez maintenant **3 solutions** pour gérer la version de cache busting sans modifier chaque fichier HTML.

## **Solution 1 : Simple (Fichier JS uniquement)** 🟢 - Recommandée

### Mise en place
Ajoutez une ligne dans le `<head>` de chaque page HTML (après les autres `<link>`):
```html
<script src="version.js"></script>
```

### Fonctionnement
- Chaque page charge le fichier `version.js`
- La constante `APP_VERSION` définit la version
- Le script remplace automatiquement `?v=X.X.X` au chargement

### Avantages ✅
- Facile à implémenter
- Pas de requête HTTP supplémentaire (juste du JS)
- Fonctionne partout
- Aucune modification des fichiers HTML existants

### À chaque déploiement
Modifiez juste cette ligne dans `version.js`:
```javascript
const APP_VERSION = '1.0.1';  // ← Changez le numéro
```

---

## **Solution 2 : Flexible (Fichier JSON + Script JS)** 🟠

### Mise en place
Ajoutez dans le `<head>` de chaque page:
```html
<script src="version-manager.js"></script>
```

### Fonctionnement
- Charge la version depuis `version.json`
- Remplace les versions dans tous les liens CSS
- Gère les erreurs gracieusement

### Avantages ✅
- Version externalisée dans un JSON
- Facile à mettre à jour
- Peut contenir des métadonnées
- Approche plus "DevOps"

### À chaque déploiement
Modifiez juste dans `version.json`:
```json
{
  "version": "1.0.1",  // ← Changez le numéro
  "lastUpdated": "2026-01-18"
}
```

---

## **Solution 3 : Côté Serveur** 🔴 - Pour plus tard

Si vous utilisez un serveur (Node.js, PHP, etc.), vous pouvez :
- Générer la version automatiquement au déploiement
- Ajouter un hash du fichier CSS
- Cache busting intelligent

---

## 🎯 **Recommandation**

**Utilisez la Solution 1** car:
1. Aucune requête HTTP supplémentaire
2. Pas de risque d'erreur de chargement
3. Simple et efficace
4. Fonctionne sans serveur backend

---

## 📝 **Procédure de Déploiement**

### Avant le déploiement
1. Mettez à jour votre CSS/contenu
2. Modifiez **UNE SEULE LIGNE** dans `version.js`:
   ```javascript
   const APP_VERSION = '1.0.1';  // Incrémenter juste le numéro
   ```
3. Déployez tous les fichiers normalement (pas de modification HTML nécessaire)

### Comment l'utilisateur voit la mise à jour
- Navigateur visite votre site
- `version.js` se charge et vérifie la version
- Tous les CSS reçoivent le nouveau `?v=1.0.1`
- Navigateur reconnaît l'URL comme "nouvelle"
- Cache est ignoré, nouvelle version affichée ✅

---

## 📊 **Comparaison**

| Critère | Solution 1 | Solution 2 |
|---------|-----------|-----------|
| Fichiers à ajouter | 1 (version.js) | 2 (version.json + version-manager.js) |
| Modification HTML | Ajouter 1 script | Ajouter 1 script |
| Modification CSS | NON | NON |
| Requêtes HTTP | +1 (JS minuscule) | +2 (JSON + JS) |
| Complexité | Très simple | Modérée |
| Flexibilité | Bonne | Excellente |
| Maintenabilité | Facile | Facile |

---

## 🔧 **Installation Rapide (Solution 1)**

1. Vérifiez que `version.js` existe dans la racine
2. Ajoutez dans le `<head>` de chaque page:
   ```html
   <script src="version.js"></script>
   ```
3. C'est tout ! Aucune autre modification nécessaire

### Ou utilisez un préprocesseur
Si vous avez Gulp/Webpack, vous pouvez injecter ce script automatiquement dans toutes les pages.

---

## ⚡ **Bonus : Script de Mise à Jour**

Créez `update-version.sh` (pour Linux/Mac) ou `.bat` (Windows):

**Linux/Mac:**
```bash
#!/bin/bash
NEW_VERSION=$1
sed -i "s/const APP_VERSION = '[0-9.]*'/const APP_VERSION = '$NEW_VERSION'/" version.js
echo "Version mise à jour à $NEW_VERSION"
git add version.js
git commit -m "Version $NEW_VERSION"
```

**Windows (PowerShell):**
```powershell
$NewVersion = $args[0]
(Get-Content version.js) -replace "const APP_VERSION = '[0-9.]*'", "const APP_VERSION = '$NewVersion'" | Set-Content version.js
Write-Host "Version mise à jour à $NewVersion"
```

---

**Dernière mise à jour**: 18 janvier 2026
