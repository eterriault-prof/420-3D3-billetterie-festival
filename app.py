from flask import Flask, render_template

app = Flask(__name__)

# --- Données de départ ---
# Vous remplacerez ces données par vos propres objets au fil des stories.

NOM_FESTIVAL = "Festival Montréal en Fête"

PROGRAMME = [
    {
        "scene": "Grande Scène",
        "spectacles": [
            {"nom": "Les Étoiles du Nord", "heure": "19h00", "places": 200},
            {"nom": "DJ Soleil",           "heure": "21h30", "places": 200},
        ]
    },
    {
        "scene": "Scène Émergence",
        "spectacles": [
            {"nom": "Trio Harmonie",  "heure": "18h00", "places": 80},
            {"nom": "Voix du Fleuve", "heure": "20h00", "places": 80},
        ]
    },
]


@app.route("/")
def accueil():
    return render_template("accueil.html",
                           nom_festival=NOM_FESTIVAL,
                           programme=PROGRAMME)


if __name__ == "__main__":
    app.run(debug=True)
