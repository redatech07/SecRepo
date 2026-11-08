# SecRepo
### 🇫🇷 Documentation
---
SecRepo est un outil d'audit de sécurité local de dépôts de code, développé en Python. Il aide les développeurs à identifier les secrets potentiellement exposés et les fichiers sensibles avant de publier ou de partager leurs projets.

SecRepo analyse un répertoire, détecte des mots-clés associés aux identifiants et aux secrets, et identifie le statut Git des fichiers.

---

## Fonctionnalités

### 1. Analyse du dépôt
- Analyse récursive des fichiers d'un répertoire.
- Exclusion de répertoires inutiles tels que `.git`, `node_modules` et `__pycache__`.
- Ignorance de fichiers système courants tels que `.DS_Store` et `Thumbs.db`.
- Exclusion des fichiers dépassant 5 Mo.

### 2. Détection de secrets

Détecte des mots-clés associés à différents types d'informations sensibles :

- Mots de passe
- Clés API
- Jetons d'accès
- Clés privées
- Identifiants de bases de données
- Identifiants Cloud
- Identifiants SSH
- Identifiants de paiement
- Secrets liés à l'infrastructure

La détection est insensible à la casse. Pour chaque correspondance, SecRepo indique le fichier, le numéro de ligne, la catégorie et le mot-clé détecté.

**Les valeurs réelles des secrets ne sont ni affichées ni enregistrées dans les résultats.**

### 3. Analyse Git

Identifie le statut Git des fichiers analysés :

| Statut | Description |
|---|---|
| `TRACKED` | Fichier suivi par Git. |
| `UNTRACKED` | Fichier non suivi et non ignoré par Git. |
| `IGNORED` | Fichier exclu par les règles d'ignorance de Git. |
| `OUTSIDE_GIT` | Fichier situé en dehors du dépôt Git. |
| `UNKNOWN` | Statut Git impossible à déterminer. |

### 4. Export des rapports

Génère un rapport structuré au format JSON contenant les résultats de l'analyse.

## Structure du projet

```text
SecRepo/
│
├── main.py
│
├── modules/
│   ├── scanner.py
│   ├── file_checker.py
│   ├── secret_checker.py
│   ├── git_checker.py
│   ├── reporter.py
│   └── exporter.py
│
├── reports/
│ 
└── README.md
```

## Prérequis

- Python 3.9 ou version ultérieure.
- Git installé et accessible depuis le terminal pour l'analyse Git.

SecRepo utilise actuellement uniquement des modules de la bibliothèque standard de Python. Aucune dépendance externe n'est nécessaire.

## Installation

Clonez le dépôt :

```bash
git clone https://github.com/redatech07/SecRepo.git
cd SecRepo
```

## Utilisation

Pour analyser un dépôt :

```bash
python3 main.py --directory /path/to/repository
```

Vous pouvez également utiliser l'option courte :

```bash
python3 main.py -d /path/to/repository
```

Pour analyser le répertoire courant :

```bash
python3 main.py -d .
```

## Exemple de sortie

```text
=======================================================
                       SECREPO
             Local Repository Security Auditor
=======================================================

[1] SCAN SUMMARY
-------------------------------------------------------
Target directory : ./repository
Files discovered : 42
Files readable   : 38
Secrets detected : 1

[2] SECRET DETECTION
-------------------------------------------------------
[!] config/settings.py | Line: 12 | Type: API_KEY | Keyword: api_key

[3] GIT ANALYSIS
-------------------------------------------------------
Git repository : /path/to/repository

Tracked files   : 30
Untracked files : 7
Ignored files   : 5

[4] FILE STATUS
-------------------------------------------------------
config/settings.py                       | TRACKED
.env                                     | IGNORED

[5] REPORT
-------------------------------------------------------
JSON report generated successfully.
Report location : reports/secrepo_report.json

=======================================================
                    SCAN COMPLETED
=======================================================
```

## Limites et sécurité

SecRepo est un projet étudiant développé à des fins éducatives et de sécurité défensive. Il est fourni « en l'état », sans garantie d'exactitude ou d'exhaustivité.

Sa version actuelle présente certaines limites :
- La détection par mots-clés peut générer des faux positifs.
- Certains secrets peuvent ne pas être détectés s'ils ne contiennent aucun mot-clé reconnu.
- Les fichiers binaires et ceux qui ne peuvent pas être décodés avec les encodages pris en charge sont ignorés.
- Les fichiers dépassant 5 Mo ne sont pas analysés.
- Un scan réussi ne garantit pas qu'un dépôt est exempt de secrets exposés.

L'utilisateur est responsable de disposer des autorisations nécessaires avant d'analyser un dépôt ou des fichiers.

L'auteur décline toute responsabilité concernant les dommages, pertes de données ou incidents résultant de l'utilisation du logiciel.


---

# 🇬🇧 English 

## Features

### 1. Repository scanning

- Recursively scans files inside a target directory.
- Skips unnecessary directories such as `.git`, `node_modules` and `__pycache__`.
- Ignores common system files such as `.DS_Store` and `Thumbs.db`.
- Skips files larger than 5 MB.

### 2. Secret detection

Detects keywords associated with different types of sensitive information:

- Passwords
- API keys
- Access tokens
- Private keys
- Database credentials
- Cloud credentials
- SSH credentials
- Payment credentials
- Infrastructure secrets

Detection is case-insensitive. For each match, SecRepo reports the file, line number, category and detected keyword.

**Actual secret values are neither displayed nor stored in the results.**

### 3. Git analysis

Identifies the Git status of scanned files:

| Status | Description |
|---|---|
| `TRACKED` | File tracked by Git. |
| `UNTRACKED` | File not tracked and not ignored by Git. |
| `IGNORED` | File excluded by Git ignore rules. |
| `OUTSIDE_GIT` | File located outside the Git repository. |
| `UNKNOWN` | Git status could not be determined. |

### 4. JSON report export

Generates a structured JSON report containing the scan results.

## Project structure

```text
SecRepo/
│
├── main.py
│
├── modules/
│   ├── scanner.py
│   ├── file_checker.py
│   ├── secret_checker.py
│   ├── git_checker.py
│   ├── reporter.py
│   └── exporter.py
│
├── reports/
│
└── README.md
```

## Requirements

- Python 3.9 or later.
- Git installed and available in the system PATH for Git analysis.

SecRepo currently uses only Python standard-library modules. No external dependencies are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/redatech07/SecRepo.git
cd SecRepo
```

## Usage

To scan a repository:

```bash
python3 main.py --directory /path/to/repository
```

You can also use the short option:

```bash
python3 main.py -d /path/to/repository
```

To scan the current directory:

```bash
python3 main.py -d .
```

## Example output

```text
F=======================================================
                       SECREPO
             Local Repository Security Auditor
=======================================================

[1] SCAN SUMMARY
-------------------------------------------------------
Target directory : ./repository
Files discovered : 42
Files readable   : 38
Secrets detected : 1

[2] SECRET DETECTION
-------------------------------------------------------
[!] config/settings.py | Line: 12 | Type: API_KEY | Keyword: api_key

[3] GIT ANALYSIS
-------------------------------------------------------
Git repository : /path/to/repository

Tracked files   : 30
Untracked files : 7
Ignored files   : 5

[4] FILE STATUS
-------------------------------------------------------
config/settings.py                       | TRACKED
.env                                     | IGNORED

[5] REPORT
-------------------------------------------------------
JSON report generated successfully.
Report location : reports/secrepo_report.json

=======================================================
                    SCAN COMPLETED
=======================================================
```

*Illustrative example.*

## Limitations and Security

SecRepo is a student project developed for educational and defensive security purposes. It is provided "as is", without any guarantee of accuracy or completeness.

The current version has several limitations:
- Keyword-based detection may generate false positives.
- Some secrets may go undetected if they do not contain any recognized keywords.
- Binary files and files that cannot be decoded using the supported encodings are ignored.
- Files larger than 5 MB are not scanned.
- A successful scan does not guarantee that a repository is free of exposed secrets.

Users are responsible for ensuring they have the necessary authorization before scanning any repository or files.

The author accepts no liability for any damage, data loss, or security incidents resulting from the use of this software.