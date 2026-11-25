# ============================================================
# CODE FRONTEND — Story 5
# Fourni par l'équipe frontend
# ============================================================
# Modifications à apporter dans app.py :
#
# 1. Ajouter en haut du fichier :
#       import random
#
# 2. Remplacer la route reserver_post() par la version ci-dessous
#    (ajout de la vérification d'échec + redirect vers /traitement).
#
# 3. Remplacer la route confirmation() par la version ci-dessous
#    (elle existe déjà depuis la story 4, mais on la redonne pour clarté).
#
# 4. Ajouter les routes traitement() et erreur_paiement().
#
# 5. Créer les templates traitement.html et erreur_paiement.html.
# ============================================================

ROUTE_RESERVER_POST_V2 = """
@app.route("/reserver", methods=["POST"])
def reserver_post():
    nom_client  = request.form["nom_client"]
    type_billet = request.form["type_billet"]

    # Trouver la cible selon le type
    if type_billet == "spectacle":
        cible_nom = request.form["spectacle"]
        cible = next((s for j in mon_festival.journees for s in j.spectacles if s.nom == cible_nom), None)
    elif type_billet == "journee":
        cible_nom = request.form["journee"]
        cible = next((j for j in mon_festival.journees if j.nom == cible_nom), None)
    else:
        cible     = mon_festival
        cible_nom = "Festival complet"

    if cible is None:
        return render_template("reservation.html",
                               spectacles=[s for j in mon_festival.journees for s in j.spectacles if s.statut != "complet"],
                               journees=mon_festival.journees,
                               erreur="Sélection introuvable.")

    # Simulation d'échec de paiement (10 % du temps)
    # IMPORTANT : cette vérification se fait AVANT Registre().ajouter()
    # pour qu'aucune place ne soit décrémentée en cas d'échec.
    if random.random() < 0.1:
        return redirect(url_for("erreur_paiement"))

    # Fabrique + enregistrement atomique
    billet      = get_billet(type_billet, cible)
    Registre().ajouter(nom_client, billet)

    return redirect(url_for("traitement",
                            nom=nom_client,
                            type_billet=billet.type_billet(),
                            cible=cible_nom,
                            prix=billet.prix()))
"""

ROUTES_NOUVELLES = """
@app.route("/traitement")
def traitement():
    return render_template("traitement.html",
                           nom=request.args.get("nom"),
                           type_billet=request.args.get("type_billet"),
                           cible=request.args.get("cible"),
                           prix=request.args.get("prix"))


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html",
                           nom=request.args.get("nom"),
                           type_billet=request.args.get("type_billet"),
                           cible=request.args.get("cible"),
                           prix=request.args.get("prix"))


@app.route("/erreur-paiement")
def erreur_paiement():
    return render_template("erreur_paiement.html")
"""

TEMPLATE_TRAITEMENT = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Traitement en cours</title>
    <!-- Redirection automatique après 3 secondes vers /confirmation -->
    <meta http-equiv="refresh" content="3;url=/confirmation?nom={{ nom }}&type_billet={{ type_billet }}&cible={{ cible }}&prix={{ prix }}">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: sans-serif; background: #0d0d0d; color: #f0f0f0; display: flex; align-items: center; justify-content: center; min-height: 100vh; }
        .carte { text-align: center; padding: 48px 32px; }
        .spinner { width: 48px; height: 48px; border: 4px solid #333; border-top-color: #f5a623; border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 24px; }
        @keyframes spin { to { transform: rotate(360deg); } }
        h2 { color: #f5a623; margin-bottom: 8px; }
        p { color: #aaa; }
    </style>
</head>
<body>
    <div class="carte">
        <div class="spinner"></div>
        <h2>Traitement du paiement…</h2>
        <p>Merci de patienter, {{ nom }}.</p>
    </div>
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
        body { font-family: sans-serif; background: #0d0d0d; color: #f0f0f0; padding: 24px 20px; max-width: 500px; margin: 0 auto; text-align: center; }
        .carte { background: #1a1a1a; border: 2px solid #f5a623; border-radius: 8px; padding: 40px 32px; margin-top: 40px; }
        .icone { font-size: 2.5em; margin-bottom: 16px; }
        h1 { color: #f5a623; margin-bottom: 16px; }
        .detail { color: #aaa; margin: 6px 0; }
        .prix { font-size: 1.6em; color: #f5a623; font-weight: bold; margin-top: 16px; }
        .btn { display: inline-block; margin-top: 28px; background: #f5a623; color: #000; padding: 12px 28px; border-radius: 4px; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="carte">
        <div class="icone">🎵</div>
        <h1>Réservation confirmée !</h1>
        <p class="detail">Merci, <strong>{{ nom }}</strong> !</p>
        <p class="detail">Billet {{ type_billet }} — {{ cible }}</p>
        <div class="prix">{{ prix }} $</div>
    </div>
    <a href="/" class="btn">Retour à l'accueil</a>
</body>
</html>
"""

TEMPLATE_ERREUR_PAIEMENT = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Erreur de paiement</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: sans-serif; background: #0d0d0d; color: #f0f0f0; padding: 24px 20px; max-width: 500px; margin: 0 auto; text-align: center; }
        .carte { background: #1a1a1a; border: 2px solid #e55; border-radius: 8px; padding: 40px 32px; margin-top: 40px; }
        .icone { font-size: 2.5em; margin-bottom: 16px; }
        h1 { color: #e55; margin-bottom: 16px; }
        p { color: #aaa; margin: 8px 0; }
        .btn { display: inline-block; margin-top: 28px; background: #f5a623; color: #000; padding: 12px 28px; border-radius: 4px; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="carte">
        <div class="icone">❌</div>
        <h1>Échec du paiement</h1>
        <p>Une erreur est survenue lors du traitement de votre paiement.</p>
        <p>Aucune réservation n'a été enregistrée.</p>
    </div>
    <a href="/reserver" class="btn">Réessayer</a>
</body>
</html>
"""