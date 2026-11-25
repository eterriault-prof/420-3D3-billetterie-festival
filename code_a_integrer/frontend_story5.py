# ============================================================
# CODE FRONTEND — Story 5
# Fourni par l'équipe frontend
# ============================================================
# Page de traitement (délai simulé) + confirmation + erreur de paiement.
# ============================================================

ROUTES = """
@app.route("/traitement")
def traitement():
    # Paramètres transmis depuis reserver_post()
    nom        = request.args.get("nom")
    type_billet = request.args.get("type_billet")
    cible      = request.args.get("cible")
    return render_template("traitement.html",
                           nom=nom,
                           type_billet=type_billet,
                           cible=cible)


@app.route("/confirmation")
def confirmation():
    nom         = request.args.get("nom")
    type_billet = request.args.get("type_billet")
    cible       = request.args.get("cible")
    prix        = request.args.get("prix")
    return render_template("confirmation.html",
                           nom=nom,
                           type_billet=type_billet,
                           cible=cible,
                           prix=prix)


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

# Note : la simulation d'échec doit se faire dans votre route reserver_post(),
# AVANT d'appeler Registre().ajouter() :
#
#   import random
#   if random.random() < 0.1:
#       return redirect(url_for("erreur_paiement"))
#
# Ainsi, en cas d'échec, aucune réservation n'est enregistrée.
