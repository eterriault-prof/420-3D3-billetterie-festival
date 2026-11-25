from flask import Flask, render_template, request

app = Flask(__name__)

# --- Données de départ ---
# Vous remplacerez ces structures par vos propres classes au fil des stories.

FESTIVAL = {
    "nom": "Festival Montréal en Fête",
    "journees": [
        {
            "nom": "Vendredi",
            "spectacles": [
                {"nom": "Les Étoiles du Nord",  "scene": "Grande Scène",   "heure": "19h00", "categorie": "pop",      "places": 5, "prix_base": 45.0, "statut": "disponible"},
                {"nom": "DJ Soleil",             "scene": "Grande Scène",   "heure": "22h00", "categorie": "électro",  "places": 5, "prix_base": 40.0, "statut": "disponible"},
                {"nom": "Trio Harmonie",         "scene": "Scène Jazz",     "heure": "18h00", "categorie": "jazz",     "places": 3, "prix_base": 35.0, "statut": "disponible"},
            ]
        },
        {
            "nom": "Samedi",
            "spectacles": [
                {"nom": "Voix du Fleuve",        "scene": "Grande Scène",   "heure": "20h00", "categorie": "folk",     "places": 5, "prix_base": 50.0, "statut": "disponible"},
                {"nom": "Quatuor Montréal",      "scene": "Scène Classique","heure": "17h00", "categorie": "classique","places": 4, "prix_base": 55.0, "statut": "disponible"},
                {"nom": "Rythmes du Monde",      "scene": "Scène Jazz",     "heure": "21h00", "categorie": "world",    "places": 3, "prix_base": 38.0, "statut": "disponible"},
            ]
        },
        {
            "nom": "Dimanche",
            "spectacles": [
                {"nom": "Grand Finale",          "scene": "Grande Scène",   "heure": "21h00", "categorie": "pop",      "places": 5, "prix_base": 60.0, "statut": "disponible"},
                {"nom": "Jazz Fusion Session",   "scene": "Scène Jazz",     "heure": "16h00", "categorie": "jazz",     "places": 3, "prix_base": 35.0, "statut": "disponible"},
                {"nom": "Acoustic Corner",       "scene": "Scène Émergence","heure": "14h00", "categorie": "folk",     "places": 2, "prix_base": 25.0, "statut": "disponible"},
            ]
        },
    ]
}


@app.route("/")
def accueil():
    tri = request.args.get("tri", "jour")
    # Construction du programme par jour (par défaut, avant la story 2)
    programme = {j["nom"]: j["spectacles"] for j in FESTIVAL["journees"]}
    return render_template("accueil.html", festival=FESTIVAL, programme=programme, tri=tri)


if __name__ == "__main__":
    app.run(debug=True)