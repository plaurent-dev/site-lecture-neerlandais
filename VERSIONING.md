# Système de Versioning Automatique 🚀

## Comment ça fonctionne ?

Votre site utilise maintenant un **système de versioning automatique** qui incrémente la version à chaque commit Git.

### � Protection anti-boucle

Le hook est intelligent : il **n'incrémente pas** si seul `version.js` est dans le commit. 
Cela évite les boucles infinies où le hook se réexécuterait sans cesse.

### �📋 Workflow

```bash
# 1. Vous modifiez vos fichiers normalement
# 2. Vous faites votre commit habituel :
git add .
git commit -m "Votre message de commit"

# 🤖 Automatiquement :
#   - La version s'incrémente (ex: 1.0.13 → 1.0.14)
#   - version.js est mis à jour
#   - Le fichier est ajouté au commit

# 3. Vous poussez en ligne :
git push
```

### 📁 Fichiers du système

- **`version.js`** : Contient la version actuelle (ex: 1.0.13)
  - Utilisé par toutes vos pages HTML
  - Ajoute automatiquement `?v=1.0.13` aux fichiers CSS
  - Force le navigateur à recharger les fichiers CSS modifiés

- **`increment_version.py`** : Script Python qui incrémente la version
  - Lit la version actuelle
  - Incrémente le patch (+1)
  - Sauvegarde dans version.js

- **`.git/hooks/pre-commit`** : Hook Git qui s'exécute automatiquement
  - Lance le script Python avant chaque commit
  - Ajoute version.js au commit

### ✅ Avantages

- ✨ **Zéro effort** : Vous n'avez plus à penser à la version
- 🎯 **Aucun oubli** : Incrémentation à chaque commit
- 🔄 **Cache busting efficace** : Les utilisateurs voient toujours la dernière version
- 📅 **Traçabilité** : Chaque version correspond à un commit Git

### 🔧 Commandes utiles

```bash
# Voir la version actuelle
cat version.js

# Tester le script manuellement
python increment_version.py

# Désactiver temporairement le hook (si besoin)
git commit --no-verify -m "Message"
```

### 📝 Format de version

Le système utilise le format **Semantic Versioning** simplifié :
- `MAJOR.MINOR.PATCH` (ex: 1.0.13)
- Seul le **PATCH** s'incrémente automatiquement
- Pour changer MAJOR ou MINOR, éditez manuellement `version.js`

### ⚙️ Maintenance

**Le système fonctionne tout seul !** Aucune maintenance nécessaire.

Si vous clonez le dépôt sur une autre machine, le hook `.git/hooks/pre-commit` sera automatiquement présent et fonctionnel.

---

*Mis en place le 14 février 2026*
