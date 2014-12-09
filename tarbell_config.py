import tarbell
import os

from flask import Blueprint

blueprint = Blueprint('tarbell_readme', __name__)

NAME = "tarbell-readme"

TITLE = "Tarbell"

# SPREADSHEET_KEY = ""

S3_BUCKETS = {
    "production": "s3://tarbell.tribapps.com",
    "staging": "s3://tarbell.beta.tribapps.com",
}

# Repository this project is based on (used for updates)
TEMPLATE_REPO_URL = "https://github.com/newsapps/tarbell-template"

DEFAULT_CONTEXT = {
    'name': 'tarbell-site',
    'title': 'Tarbell',
    'intro': 'Craft and publish beautiful websites',
}

def get_tutorial():
    path = os.path.join(os.path.dirname(tarbell.__file__), "docs/tutorial.rst")
    try:
        return open(path, 'r').read()
    except IOError:
        return None

@blueprint.app_context_processor
def context_processor():
    return {
        'tutorial': get_tutorial(),
    }
