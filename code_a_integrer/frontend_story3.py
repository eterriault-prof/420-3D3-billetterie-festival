# ============================================================
# CODE FRONTEND — Story 3
# Fourni par l'équipe frontend
# ============================================================
# Instructions :
#   1. Copiez ce code dans votre app.py (remplacez la route "/" existante)
#   2. Remplacez le template accueil.html par le nouveau ci-dessous
#   3. Adaptez les variables pour utiliser vos objets Festival/Scene/Spectacle
# ============================================================

# --- Route à intégrer dans app.py ---
#
# from flask import Flask, render_template
# from festival import Festival  # ← votre import
#
# @app.route("/")
# def accueil():
#     # Remplacez "mon_festival" par votre objet Festival
#     return render_template("accueil.html", festival=mon_festival)


# --- Nouveau template accueil.html ---
TEMPLATE_ACCUEIL = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ festival.nom }}</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; background: #0d0d0d; color: #f0f0f0; }
        h1 { color: #f5a623; letter-spacing: 2px; }
        h2 { color: #f5a623; border-bottom: 1px solid #333; padding-bottom: 8px; }
        .scene { margin-bottom: 32px; }
        .places-scene { color: #aaa; font-size: 0.9em; margin-left: 8px; }
        .spectacle { background: #1a1a1a; border-left: 4px solid #f5a623; padding: 12px 16px; margin: 8px 0; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; }
        .spectacle .nom { font-weight: bold; font-size: 1.1em; }
        .spectacle .info { color: #aaa; font-size: 0.9em; }
        .places { background: #f5a623; color: #000; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
        .complet { background: #555; color: #aaa; }
        nav a { color: #f5a623; margin-right: 16px; text-decoration: none; }
        .btn { background: #f5a623; color: #000; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; font-weight: bold; text-decoration: none; font-size: 0.9em; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Accueil</a>
        <a href="/reserver">Réserver</a>
        <a href="/admin">Admin</a>
    </nav>
    <h1>🎵 {{ festival.nom }}</h1>
    <p>{{ festival.places_disponibles() }} places disponibles au total</p>

    {% for scene in festival.scenes %}
    <div class="scene">
        <h2>{{ scene.nom }} <span class="places-scene">({{ scene.places_disponibles() }} places)</span></h2>
        {% for spectacle in scene.spectacles %}
        <div class="spectacle">
            <div>
                <div class="nom">{{ spectacle.nom }}</div>
                <div class="info">{{ spectacle.heure }} · {{ spectacle.statut }}</div>
            </div>
            {% if spectacle.places_disponibles() > 0 %}
            <span class="places">{{ spectacle.places_disponibles() }} places</span>
            {% else %}
            <span class="places complet">Complet</span>
            {% endif %}
        </div>
        {% endfor %}
    </div>
    {% endfor %}
</body>
</html>
"""

# Note : copiez le contenu de TEMPLATE_ACCUEIL dans templates/accueil.html
# (sans les guillemets Python)
