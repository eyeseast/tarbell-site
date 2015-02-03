import datetime
import os
import tarbell

from dateutil.parser import parse as date_parse
from flask import Blueprint

from metalsmyth import Stack
from metalsmyth.plugins.dates import Dates
from metalsmyth.plugins.markup import Markdown


blueprint = Blueprint('tarbell_readme', __name__)

NAME = "tarbell-readme"

TITLE = "Tarbell"

# SPREADSHEET_KEY = ""

S3_BUCKETS = {
    "production": "s3://www.tarbell.io",
    "staging": "s3://www.tarbell.io/preview",
}

# Repository this project is based on (used for updates)
TEMPLATE_REPO_URL = "https://github.com/newsapps/tarbell-template"

DEFAULT_CONTEXT = {
    'name': 'tarbell-site',
    'title': 'Tarbell',
    'intro': 'Craft and publish beautiful websites',
}

# stack setup
stack = Stack('_showcase',
    Dates('date'), 
    Markdown(output_mode='html5')
)


def get_tutorial():
    path = os.path.join(os.path.dirname(tarbell.__file__), "docs/tutorial.rst")
    try:
        return open(path, 'r').read()
    except IOError:
        return None


@blueprint.app_context_processor
def add_stack():
    """
    Add showcase posts to context, sorted by filename.
    For better sorting, use `sort` filter.
    """
    return {'showcase_posts': stack.iter()}


@blueprint.app_context_processor
def context_processor():
    return {
        'tutorial': get_tutorial(),
    }


@blueprint.app_template_filter('date')
def date_format(s, format=None):
    "Parse and format date string or Excel serial date"

    # handle Excel serial dates
    if isinstance(s, (int, float)):
        tt = xlrd.xldate_as_tuple(s, 0) # 1900-based
        date = datetime.datetime(*tt)

    # handle strings of various kinds
    elif isinstance(s, basestring):
        date = date_parse(s)

    # if it's already a date, just move on
    elif isinstance(s, (datetime.datetime, datetime.date)):
        date = s
    
    # format if we have a format
    if format is not None:
        return date.strftime(format)
    
    return date

