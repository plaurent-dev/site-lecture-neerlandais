document.getElementById("btnImport").addEventListener("click", () => {
    const text = document.getElementById("inputText").value.trim();

    if (!text) {
        alert("Merci de coller un extrait.");
        return;
    }

    // On stocke le texte pour les autres pages
    localStorage.setItem("articleText", text);

    // On redirige vers la page d'analyse
    window.location.href = "analyse.html";
});
