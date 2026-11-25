# ============================================================
# CODE FRONTEND — Story 8
# Fourni par l'équipe frontend
# ============================================================
# Page d'administration — statistiques et historique des ventes.
# ============================================================

ROUTE_ADMIN = """
@app.route("/admin")
def admin():
    registre = Registre()
    stats    = StatistiquesVentes()   # votre observateur de statistiques
    spectacles_complets = [
        s for j in mon_festival.journees
        for s in j.spectacles
        if s.statut == "complet"
    ]
    return render_template("admin.html",
                           reservations=registre.liste(),
                           stats=stats,
                           spectacles_complets=spectacles_complets)
"""

TEMPLATE_ADMIN = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Administration</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: sans-serif; background: #0d0d0d; color: #f0f0f0; padding: 24px 20px; max-width: 860px; margin: 0 auto; }
        nav { display: flex; gap: 20px; margin-bottom: 32px; }
        nav a { color: #f5a623; text-decoration: none; font-size: 0.95em; }
        h1 { color: #f5a623; margin-bottom: 28px; }
        h2 { color: #f5a623; margin: 28px 0 12px; font-size: 1.1em; text-transform: uppercase; letter-spacing: 1px; }
        .stats-grille { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 8px; }
        .stat-carte { background: #1a1a1a; border-radius: 6px; padding: 16px; text-align: center; }
        .stat-carte .valeur { font-size: 1.8em; font-weight: bold; color: #f5a623; }
        .stat-carte .label { color: #aaa; font-size: 0.85em; margin-top: 4px; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; padding: 8px 12px; border-bottom: 2px solid #f5a623; color: #f5a623; font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.5px; }
        td { padding: 8px 12px; border-bottom: 1px solid #1a1a1a; font-size: 0.95em; }
        tr:hover td { background: #111; }
        .badge { padding: 2px 8px; border-radius: 10px; font-size: 0.8em; font-weight: bold; background: #333; color: #aaa; }
        .vide { color: #555; font-style: italic; padding: 12px; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Accueil</a>
        <a href="/reserver">Réserver</a>
        <a href="/admin">Admin</a>
    </nav>

    <h1>⚙️ Administration</h1>

    <h2>Statistiques</h2>
    <div class="stats-grille">
        <div class="stat-carte">
            <div class="valeur">{{ stats.total_billets() }}</div>
            <div class="label">Billets vendus</div>
        </div>
        <div class="stat-carte">
            <div class="valeur">{{ stats.billets_par_type().get("spectacle", 0) }}</div>
            <div class="label">Billets spectacle</div>
        </div>
        <div class="stat-carte">
            <div class="valeur">{{ stats.billets_par_type().get("journee", 0) }}</div>
            <div class="label">Billets journée</div>
        </div>
        <div class="stat-carte">
            <div class="valeur">{{ stats.billets_par_type().get("festival", 0) }}</div>
            <div class="label">Billets festival</div>
        </div>
        <div class="stat-carte">
            <div class="valeur">{{ stats.revenu_total() }} $</div>
            <div class="label">Revenu total</div>
        </div>
    </div>

    <h2>Revenus par journée</h2>
    <table>
        <tr><th>Journée</th><th>Revenu</th></tr>
        {% for journee, revenu in stats.revenus_par_journee().items() %}
        <tr><td>{{ journee }}</td><td>{{ revenu }} $</td></tr>
        {% else %}
        <tr><td colspan="2" class="vide">Aucune vente enregistrée.</td></tr>
        {% endfor %}
    </table>

    <h2>Spectacles complets</h2>
    {% if spectacles_complets %}
    <table>
        <tr><th>Spectacle</th><th>Scène</th><th>Heure</th></tr>
        {% for s in spectacles_complets %}
        <tr><td>{{ s.nom }}</td><td>{{ s.scene }}</td><td>{{ s.heure }}</td></tr>
        {% endfor %}
    </table>
    {% else %}
    <p class="vide">Aucun spectacle complet pour l'instant.</p>
    {% endif %}

    <h2>Historique des réservations</h2>
    {% if reservations %}
    <table>
        <tr><th>Client</th><th>Type</th><th>Billet</th><th>Prix</th><th>Heure</th></tr>
        {% for r in reservations %}
        <tr>
            <td>{{ r.nom_client }}</td>
            <td><span class="badge">{{ r.type_billet }}</span></td>
            <td>{{ r.description }}</td>
            <td>{{ r.prix }} $</td>
            <td>{{ r.heure }}</td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p class="vide">Aucune réservation enregistrée.</p>
    {% endif %}
</body>
</html>
"""
