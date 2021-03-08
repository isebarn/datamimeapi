from flask_restx import Resource
from flask_restx import fields
from utils.Models import SuccessNamespace
# Query methods
from queries.word import post_word
from queries.word import get_list

api = SuccessNamespace("word", description="wordpath")

@api.route("/list")
class List(Resource):
  def get(self):
    return get_list({}, api.payload)

@api.route("/add")
class Add(Resource):
  def post(self):
    return post_word(api.payload)