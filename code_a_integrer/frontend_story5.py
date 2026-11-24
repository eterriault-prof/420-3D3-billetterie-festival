# ============================================================
# CODE FRONTEND — Story 5
# Fourni par l'équipe frontend
# ============================================================
# Instructions :
#   1. Ajoutez les routes ci-dessous dans votre app.py
#   2. Créez les templates reservation.html et confirmation.html
#   3. Adaptez les imports pour utiliser votre Registre et votre Festival
# ============================================================

ROUTES_A_AJOUTER = """
from flask import Flask, render_template, request, redirect, url_for
from registre import Registre       # ← votre import
from festival import mon_festival   # ← votre import

@app.route("/reserver", methods=["GET"])
def reserver():
    # Construire la liste des spectacles disponibles pour le formulaire
    spectacles = []
    for scene in mon_festival.scenes:
        for s in scene.spectacles:
            spectacles.append(s)
    return render_template("reservation.html", spectacles=spectacles)

@app.route("/reserver", methods=["POST"])
def reserver_post():
    nom_client   = request.form["nom_client"]
    nom_spectacle = request.form["spectacle"]

    # Trouver le spectacle correspondant
    spectacle_choisi = None
    for scene in mon_festival.scenes:
        for s in scene.spectacles:
            if s.nom == nom_spectacle:
                spectacle_choisi = s
                break

    if spectacle_choisi is None or spectacle_choisi.places_disponibles() <= 0:
        return render_template("reservation.html",
                               spectacles=[s for sc in mon_festival.scenes for s in sc.spectacles],
                               erreur="Ce spectacle est complet ou introuvable.")

    # Enregistrer la réservation — c'est votre Registre qui gère ça
    Registre().ajouter(nom_client, spectacle_choisi)
    spectacle_choisi.reserver()   # ← méthode à implémenter sur Spectacle

    return redirect(url_for("confirmation", nom=nom_client, spectacle=spectacle_choisi.nom))

@app.route("/confirmation")
def confirmation():
    nom = request.args.get("nom")
    spectacle = request.args.get("spectacle")
    return render_template("confirmation.html", nom=nom, spectacle=spectacle)
"""

TEMPLATE_RESERVATION = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Réserver un billet</title>
    <style>
        body { font-family: sans-serif; max-width: 500px; margin: 40px auto; padding: 0 20px; background: #0d0d0d; color: #f0f0f0; }
        h1 { color: #f5a623; }
        label { display: block; margin-top: 16px; color: #aaa; }
        input, select { width: 100%; padding: 10px; margin-top: 6px; background: #1a1a1a; border: 1px solid #333; color: #f0f0f0; border-radius: 4px; box-sizing: border-box; }
        .btn { margin-top: 24px; background: #f5a623; color: #000; border: none; padding: 12px 24px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 1em; width: 100%; }
        .erreur { background: #3a1a1a; border-left: 4px solid #e55; padding: 10px 14px; margin-bottom: 16px; border-radius: 4px; }
        nav a { color: #f5a623; margin-right: 16px; text-decoration: none; }
    </style>
</head>
<body>
    <nav><a href="/">Accueil</a></nav>
    <h1>🎟 Réserver un billet</h1>
    {% if erreur %}
    <div class="erreur">{{ erreur }}</div>
    {% endif %}
    <form method="POST">
        <label>Votre nom</label>
        <input type="text" name="nom_client" required placeholder="ex. : Marie Tremblay">
        <label>Spectacle</label>
        <select name="spectacle">
            {% for s in spectacles %}
            {% if s.places_disponibles() > 0 %}
            <option value="{{ s.nom }}">{{ s.nom }} — {{ s.heure }} ({{ s.places_disponibles() }} places)</option>
            {% endif %}
            {% endfor %}
        </select>
        <button type="submit" class="btn">Réserver</button>
    </form>
</body>
</html>
"""

TEMPLATE_CONFIRMATION = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Confirmation</title>
    <style>
        body { font-family: sans-serif; max-width: 500px; margin: 40px auto; padding: 0 20px; background: #0d0d0d; color: #f0f0f0; text-align: center; }
        h1 { color: #f5a623; }
        .carte { background: #1a1a1a; border: 2px solid #f5a623; border-radius: 8px; padding: 32px; margin-top: 24px; }
        .btn { display: inline-block; margin-top: 24px; background: #f5a623; color: #000; padding: 12px 24px; border-radius: 4px; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="carte">
        <div style="font-size: 2em;">🎵</div>
        <h1>Réservation confirmée !</h1>
        <p>Merci, <strong>{{ nom }}</strong> !</p>
        <p>Votre billet pour <strong>{{ spectacle }}</strong> est réservé.</p>
    </div>
    <a href="/" class="btn">Retour à l'accueil</a>
</body>
</html>
"""
# Note : copiez le contenu de chaque TEMPLATE dans le fichier .html correspondant
