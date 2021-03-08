from flask_restx import Resource
from flask_restx import fields
from utils.Models import SuccessNamespace
# Query methods
from queries.translation import post_translation

api = SuccessNamespace("translation", description="translations")

@api.route("/add")
class Add(Resource):
  def post(self):
    return post_translation(api.payload)