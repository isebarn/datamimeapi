from utils import Operations
from time import sleep
def get_list(aggregate, filters):
  return Operations.QueryWordTranslations()

def post_word(data):
  for item in data:
    Operations.SaveWordTranslations(item)