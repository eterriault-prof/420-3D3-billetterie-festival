# ============================================================
# CODE FRONTEND — Story 3
# Fourni par l'équipe frontend
# ============================================================
# Ajoutez les routes ci-dessous dans votre app.py.
# Adaptez les imports selon vos propres classes.
# ============================================================

ROUTES = """
@app.route("/reserver", methods=["GET"])
def reserver():
    # Récupérer tous les spectacles disponibles (toutes journées confondues)
    disponibles = [
        s for j in mon_festival.journees
        for s in j.spectacles
        if s.statut != "complet"
    ]
    return render_template("reservation.html", spectacles=disponibles)


@app.route("/reserver", methods=["POST"])
def reserver_post():
    nom_client    = request.form["nom_client"]
    nom_spectacle = request.form["spectacle"]

    spectacle_choisi = None
    for journee in mon_festival.journees:
        for s in journee.spectacles:
            if s.nom == nom_spectacle:
                spectacle_choisi = s
                break

    if spectacle_choisi is None or spectacle_choisi.statut == "complet":
        disponibles = [s for j in mon_festival.journees for s in j.spectacles if s.statut != "complet"]
        return render_template("reservation.html",
                               spectacles=disponibles,
                               erreur="Ce spectacle est complet ou introuvable.")

    # Créer le billet et enregistrer la réservation — à vous d'implémenter
    billet = get_billet("spectacle", spectacle_choisi)   # votre fabrique
    Registre().ajouter(nom_client, billet)               # votre registre

    return redirect(url_for("confirmation",
                            nom=nom_client,
                            type_billet="spectacle",
                            cible=spectacle_choisi.nom,
                            prix=billet.prix()))


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html",
                           nom=request.args.get("nom"),
                           type_billet=request.args.get("type_billet"),
                           cible=request.args.get("cible"),
                           prix=request.args.get("prix"))
"""

TEMPLATE_RESERVATION = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Réserver</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: sans-serif; background: #0d0d0d; color: #f0f0f0; padding: 24px 20px; max-width: 500px; margin: 0 auto; }
        nav { display: flex; gap: 20px; margin-bottom: 32px; }
        nav a { color: #f5a623; text-decoration: none; font-size: 0.95em; }
        h1 { color: #f5a623; margin-bottom: 24px; }
        label { display: block; margin-top: 16px; color: #aaa; font-size: 0.9em; margin-bottom: 6px; }
        input, select { width: 100%; padding: 10px; background: #1a1a1a; border: 1px solid #333; color: #f0f0f0; border-radius: 4px; font-size: 1em; }
        .btn { margin-top: 24px; width: 100%; background: #f5a623; color: #000; border: none; padding: 12px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 1em; }
        .erreur { background: #3a1a1a; border-left: 4px solid #e55; padding: 10px 14px; margin-bottom: 16px; border-radius: 4px; }
    </style>
</head>
<body>
    <nav><a href="/">Accueil</a></nav>
    <h1>🎟 Réserver un billet</h1>
    {% if erreur %}<div class="erreur">{{ erreur }}</div>{% endif %}
    <form method="POST">
        <label>Votre nom</label>
        <input type="text" name="nom_client" required placeholder="ex. : Marie Tremblay">

        <label>Spectacle</label>
        <select name="spectacle">
            {% for s in spectacles %}
            <option value="{{ s.nom }}">{{ s.nom }} — {{ s.heure }} ({{ s.places }} places · {{ s.prix_base }} $)</option>
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
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: sans-serif; background: #0d0d0d; color: #f0f0f0; padding: 24px 20px; max-width: 500px; margin: 0 auto; }
        nav { display: flex; gap: 20px; margin-bottom: 32px; }
        nav a { color: #f5a623; text-decoration: none; font-size: 0.95em; }
        h1 { color: #f5a623; margin-bottom: 24px; }
        .carte { background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 8px; padding: 24px; }
        .carte p { margin-bottom: 12px; color: #aaa; font-size: 0.95em; }
        .carte strong { color: #f0f0f0; }
        .prix { font-size: 1.4em; color: #f5a623; font-weight: bold; margin-top: 8px; }
        .btn { display: inline-block; margin-top: 24px; background: #f5a623; color: #000; padding: 10px 20px; border-radius: 4px; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <nav><a href="/">Accueil</a></nav>
    <h1>✅ Réservation confirmée</h1>
    <div class="carte">
        <p>Client : <strong>{{ nom }}</strong></p>
        <p>Spectacle : <strong>{{ cible }}</strong></p>
        <p>Type de billet : <strong>{{ type_billet }}</strong></p>
        <p class="prix">{{ prix }} $</p>
    </div>
    <a href="/reserver" class="btn">Faire une autre réservation</a>
</body>
</html>
"""
