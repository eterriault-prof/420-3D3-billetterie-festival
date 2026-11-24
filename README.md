# Billetterie Festival — Code de départ

Application web Flask minimaliste pour l'exercice de révision sur les patrons de conception.

## Prérequis

- Python 3.10 ou plus récent
- pip

## Installation

### 1. Créer un environnement virtuel

```bash
python -m venv venv
```

Activer l'environnement :

- **macOS / Linux :**
  ```bash
  source venv/bin/activate
  ```
- **Windows (PowerShell) :**
  ```powershell
  venv\Scripts\Activate.ps1
  ```

### 2. Installer Flask

```bash
pip install flask
```

Optionnel — sauvegarder les dépendances :

```bash
pip freeze > requirements.txt
git add requirements.txt
```

## Lancer l'application

```bash
python app.py
```

Ouvrez ensuite votre navigateur à l'adresse : **http://127.0.0.1:5000**

Vous devriez voir la page d'accueil du festival avec le programme initial.