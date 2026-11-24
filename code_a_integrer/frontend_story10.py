# ============================================================
# CODE FRONTEND — Story 10
# Fourni par l'équipe frontend
# ============================================================
# Page d'administration : liste des réservations + changement de statut.
# ============================================================

ROUTE_ADMIN = """
@app.route("/admin")
def admin():
    registre = Registre()
    reservations = registre.liste()
    spectacles = [s for sc in mon_festival.scenes for s in sc.spectacles]
    return render_template("admin.html",
                           reservations=reservations,
                           spectacles=spectacles,
                           total=registre.total())

@app.route("/admin/statut", methods=["POST"])
def changer_statut():
    nom_spectacle  = request.form["spectacle"]
    nouveau_statut = request.form["statut"]

    for scene in mon_festival.scenes:
        for s in scene.spectacles:
            if s.nom == nom_spectacle:
                s.changer_statut(nouveau_statut)   # ← déclenche les notifications
                break

    return redirect(url_for("admin"))
"""

TEMPLATE_ADMIN = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Administration</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; background: #0d0d0d; color: #f0f0f0; }
        h1, h2 { color: #f5a623; }
        table { width: 100%; border-collapse: collapse; margin-top: 16px; }
        th { text-align: left; border-bottom: 2px solid #f5a623; padding: 8px; color: #f5a623; }
        td { padding: 8px; border-bottom: 1px solid #222; }
        tr:hover { background: #1a1a1a; }
        .total { background: #1a1a1a; padding: 16px; border-radius: 4px; margin-bottom: 24px; font-size: 1.1em; }
        select, input[type=text] { background: #1a1a1a; border: 1px solid #333; color: #f0f0f0; padding: 8px; border-radius: 4px; }
        .btn { background: #f5a623; color: #000; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; font-weight: bold; }
        nav a { color: #f5a623; margin-right: 16px; text-decoration: none; }
        .section { margin-top: 40px; }
    </style>
</head>
<body>
    <nav><a href="/">Accueil</a> <a href="/reserver">Réserver</a></nav>
    <h1>⚙️ Administration</h1>

    <div class="total">
        Total des réservations : <strong>{{ total }}</strong>
    </div>

    <h2>Réservations</h2>
    <table>
        <tr>
            <th>Client</th>
            <th>Spectacle</th>
            <th>Type</th>
            <th>Prix</th>
        </tr>
        {% for r in reservations %}
        <tr>
            <td>{{ r.nom_client }}</td>
            <td>{{ r.spectacle }}</td>
            <td>{{ r.type_billet or "—" }}</td>
            <td>{{ r.prix or "—" }}</td>
        </tr>
        {% endfor %}
    </table>

    <div class="section">
        <h2>Changer le statut d'un spectacle</h2>
        <form method="POST" action="/admin/statut" style="display: flex; gap: 12px; align-items: flex-end; flex-wrap: wrap;">
            <div>
                <label style="display:block; color:#aaa; margin-bottom:4px;">Spectacle</label>
                <select name="spectacle">
                    {% for s in spectacles %}
                    <option value="{{ s.nom }}">{{ s.nom }}</option>
                    {% endfor %}
                </select>
            </div>
            <div>
                <label style="display:block; color:#aaa; margin-bottom:4px;">Nouveau statut</label>
                <select name="statut">
                    <option value="disponible">Disponible</option>
                    <option value="complet">Complet</option>
                    <option value="annulé">Annulé</option>
                    <option value="déplacé">Déplacé</option>
                </select>
            </div>
            <button type="submit" class="btn">Mettre à jour</button>
        </form>
    </div>
</body>
</html>
"""
