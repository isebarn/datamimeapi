from flask import Blueprint
from flask_restx import Api, fields
# Subpaths
from .word import api as word_api
from .phrase import api as phrase_api

blueprint = Blueprint('', __name__)
api = Api(blueprint, doc='/doc/')

# Add imported subpaths to api
api.add_namespace(word_api)
api.add_namespace(phrase_api)
