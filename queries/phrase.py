from utils import Operations

def get_list(aggregate, filters):
  return Operations.QueryPhraseTranslations()

def post_phrase(data):
  Operations.SavePhraseTranslations(data)