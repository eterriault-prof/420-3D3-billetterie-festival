# ============================================================
# CODE FRONTEND — Story 4
# Fourni par l'équipe frontend
# ============================================================
# Remplace le template reservation.html pour inclure le choix du type de billet.
# ============================================================

TEMPLATE_RESERVATION_V2 = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Réserver</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: sans-serif; background: #0d0d0d; color: #f0f0f0; padding: 24px 20px; max-width: 560px; margin: 0 auto; }
        nav { display: flex; gap: 20px; margin-bottom: 32px; }
        nav a { color: #f5a623; text-decoration: none; font-size: 0.95em; }
        h1 { color: #f5a623; margin-bottom: 24px; }
        label { display: block; margin-top: 16px; color: #aaa; font-size: 0.9em; margin-bottom: 6px; }
        input[type=text], select { width: 100%; padding: 10px; background: #1a1a1a; border: 1px solid #333; color: #f0f0f0; border-radius: 4px; font-size: 1em; }
        .type-options { display: flex; flex-direction: column; gap: 8px; margin-top: 6px; }
        .type-option { background: #1a1a1a; border: 1px solid #333; border-radius: 4px; padding: 12px 14px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
        .type-option:has(input:checked) { border-color: #f5a623; }
        .type-option input { margin-right: 10px; accent-color: #f5a623; }
        .type-option .label { font-weight: bold; }
        .type-option .desc { color: #aaa; font-size: 0.85em; margin-top: 2px; }
        .type-option .prix-info { color: #f5a623; font-size: 0.85em; white-space: nowrap; }
        .cible-section { margin-top: 8px; }
        .btn { margin-top: 24px; width: 100%; background: #f5a623; color: #000; border: none; padding: 12px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 1em; }
        .erreur { background: #3a1a1a; border-left: 4px solid #e55; padding: 10px 14px; margin-bottom: 16px; border-radius: 4px; }
    </style>
    <script>
        function majCible() {
            const type = document.querySelector('input[name=type_billet]:checked').value;
            document.getElementById('cible-spectacle').hidden = type !== 'spectacle';
            document.getElementById('cible-journee').hidden   = type !== 'journee';
        }
        document.addEventListener('DOMContentLoaded', () => {
            document.querySelectorAll('input[name=type_billet]').forEach(r => r.addEventListener('change', majCible));
            majCible();
        });
    </script>
</head>
<body>
    <nav><a href="/">Accueil</a></nav>
    <h1>🎟 Réserver un billet</h1>
    {% if erreur %}<div class="erreur">{{ erreur }}</div>{% endif %}
    <form method="POST">
        <label>Votre nom</label>
        <input type="text" name="nom_client" required placeholder="ex. : Marie Tremblay">

        <label>Type de billet</label>
        <div class="type-options">
            <label class="type-option">
                <input type="radio" name="type_billet" value="spectacle" checked>
                <div>
                    <div class="label">Billet spectacle</div>
                    <div class="desc">Accès à un spectacle précis</div>
                </div>
                <span class="prix-info">Prix de base</span>
            </label>
            <label class="type-option">
                <input type="radio" name="type_billet" value="journee">
                <div>
                    <div class="label">Billet journée</div>
                    <div class="desc">Tous les spectacles d'une journée</div>
                </div>
                <span class="prix-info">−15 %</span>
            </label>
            <label class="type-option">
                <input type="radio" name="type_billet" value="festival">
                <div>
                    <div class="label">Billet festival</div>
                    <div class="desc">Les 3 jours complets</div>
                </div>
                <span class="prix-info">−25 %</span>
            </label>
        </div>

        <div class="cible-section" id="cible-spectacle">
            <label>Spectacle</label>
            <select name="spectacle">
                {% for s in spectacles %}
                <option value="{{ s.nom }}">{{ s.nom }} — {{ s.heure }} ({{ s.places }} places · {{ s.prix_base }} $)</option>
                {% endfor %}
            </select>
        </div>

        <div class="cible-section" id="cible-journee">
            <label>Journée</label>
            <select name="journee">
                {% for j in journees %}
                <option value="{{ j.nom }}">{{ j.nom }}</option>
                {% endfor %}
            </select>
        </div>

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
        <p>Billet : <strong>{{ cible }}</strong></p>
        <p>Type : <strong>{{ type_billet }}</strong></p>
        <p class="prix">{{ prix }} $</p>
    </div>
    <a href="/reserver" class="btn">Faire une autre réservation</a>
</body>
</html>
"""


ROUTE_RESERVER_V2 = """
@app.route("/reserver", methods=["GET"])
def reserver():
    disponibles = [s for j in mon_festival.journees for s in j.spectacles if s.statut != "complet"]
    return render_template("reservation.html",
                           spectacles=disponibles,
                           journees=mon_festival.journees)


@app.route("/reserver", methods=["POST"])
def reserver_post():
    nom_client  = request.form["nom_client"]
    type_billet = request.form["type_billet"]   # "spectacle", "journee" ou "festival"

    # Déterminer la cible selon le type
    if type_billet == "spectacle":
        cible_nom = request.form["spectacle"]
        cible = next((s for j in mon_festival.journees for s in j.spectacles if s.nom == cible_nom), None)
    elif type_billet == "journee":
        cible_nom = request.form["journee"]
        cible = next((j for j in mon_festival.journees if j.nom == cible_nom), None)
    else:
        cible = mon_festival

    if cible is None:
        return render_template("reservation.html",
                               spectacles=[s for j in mon_festival.journees for s in j.spectacles if s.statut != "complet"],
                               journees=mon_festival.journees,
                               erreur="Sélection introuvable.")

    # Créer le billet via votre Fabrique et enregistrer
    billet = get_billet(type_billet, cible)      # votre fabrique
    Registre().ajouter(nom_client, billet)       # votre registre

    cible_label = cible_nom if type_billet != "festival" else "Festival complet"
    return redirect(url_for("confirmation",
                            nom=nom_client,
                            type_billet=billet.type_billet(),
                            cible=cible_label,
                            prix=billet.prix()))


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html",
                           nom=request.args.get("nom"),
                           type_billet=request.args.get("type_billet"),
                           cible=request.args.get("cible"),
                           prix=request.args.get("prix"))
"""