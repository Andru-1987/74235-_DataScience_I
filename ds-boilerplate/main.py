import os

# Lista de carpetas a crear
folders = [
    "data/external",
    "data/interim",
    "data/processed",
    "data/raw",
    "docs",
    "models",
    "notebooks",
    "references",
    "reports/figures",
    "src/data",
    "src/features",
    "src/models",
    "src/visualization"
]

# Archivos vacíos para mantener carpetas
empty_files = [
    "data/external/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",
    "data/raw/.gitkeep",
    "docs/.gitkeep",
    "models/.gitkeep",
    "notebooks/.gitkeep",
    "references/.gitkeep",
    "reports/.gitkeep",
    "reports/figures/.gitkeep",
    "src/__init__.py",
    "src/data/make_dataset.py",
    "src/features/build_features.py",
    "src/models/predict_model.py",
    "src/models/train_model.py",
    "src/visualization/visualize.py"
]

# Archivos raíz típicos (algunos vacíos)
root_files = [
    "LICENSE",
    "Makefile",
    "requirements.txt",
    "setup.py",
    "tox.ini"
]

# Contenido del README.md
readme_content = """
# Este es el boiler-plate de un proyecto de data science

```bash

LICENSE             <- Makefile with commands like `make data` or `make train`.
Makefile            <- Makefile with commands like `make data` or `make train`.
README.md           <- The top-level README for developers using this project.
data/
├── external        <- Data from third party sources.
├── interim         <- Intermediate data that has been transformed.
├── processed       <- The final, canonical data sets for modeling.
├── raw             <- The original, immutable data dump.
docs/               <- A default Sphinx project; see sphinx-doc.org for details.
models/             <- Trained and serialized models, model predictions, or model summaries.
notebooks/          <- Jupyter notebooks. Naming convention is a number (for ordering),
the creator's initials, and a short `_` delimited description, e.g.
`1.0-jqp-initial-data-exploration`.
references/         <- Data dictionaries, manuals, and all other explanatory materials.
reports/
├── figures         <- Generated graphics and figures to be used in reporting.
requirements.txt    <- The requirements file for reproducing the analysis environment,
e.g. generated with `pip freeze > requirements.txt`
setup.py            <- Make this project pip installable with `pip install -e`
src/                <- Source code for use in this project.
├── **init**.py     <- Makes src a Python module.
├── data/
│   └── make\_dataset.py
├── features/
│   └── build\_features.py
├── models/
│   ├── predict\_model.py
│   └── train\_model.py
└── visualization/
└── visualize.py

```
"""

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for file in empty_files + root_files:
        with open(file, 'w') as f:
            pass

    with open("README.md", "w") as f:
        f.write(readme_content.strip())

    print("Estructura de proyecto y README.md creada con éxito.")

if __name__ == "__main__":
    create_structure()
