// Version Manager - Charge la version depuis version.json
class VersionManager {
    constructor() {
        this.version = null;
    }

    async init() {
        try {
            // Charger la version depuis le fichier centralisé
            const response = await fetch('version.json?t=' + Date.now());
            if (response.ok) {
                const data = await response.json();
                this.version = data.version;
                this.updateAllLinks();
            }
        } catch (error) {
            console.warn('Impossible de charger version.json, utilisation de la valeur par défaut');
            this.version = '1.0.0';
        }
    }

    updateAllLinks() {
        const links = document.querySelectorAll('link[rel="stylesheet"]');
        links.forEach(link => {
            let href = link.href;
            // Remplacer ou ajouter le paramètre de version
            if (href.includes('?v=')) {
                href = href.replace(/\?v=[0-9.]+/, '?v=' + this.version);
            } else if (href.includes('styles.css')) {
                href = href.includes('?') ? href + '&v=' + this.version : href + '?v=' + this.version;
            }
            link.href = href;
        });
    }

    getVersion() {
        return this.version || '1.0.0';
    }
}

// Initialiser au chargement
const versionManager = new VersionManager();
document.addEventListener('DOMContentLoaded', () => {
    versionManager.init();
});
