from flask_restx import Resource
from flask_restx import fields
from utils.Models import SuccessNamespace
# Query methods
from queries.phrase import get_list

api = SuccessNamespace("phrase", description="phraseapi")

@api.route("/list")
class List(Resource):
  def get(self):
    return get_list({}, api.payload)