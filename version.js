// Configuration de version centralisée
const APP_VERSION = '1.0.10';

// Remplacer automatiquement la version dans les liens CSS au chargement
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('link[rel="stylesheet"]');
    links.forEach(link => {
        const href = link.href;
        // Si le lien contient ?v=, remplacer par la version actuelle
        if (href.includes('?v=')) {
            link.href = href.replace(/\?v=[0-9.]+/, '?v=' + APP_VERSION);
        } else if (href.includes('styles.css') || href.includes('/styles.css')) {
            // Ajouter la version si elle n'existe pas
            link.href = href.includes('?') ? href + '&v=' + APP_VERSION : href + '?v=' + APP_VERSION;
        }
    });
});
