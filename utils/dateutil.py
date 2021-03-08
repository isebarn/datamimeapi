from datetime import datetime

def get_date(string_date):
  return datetime.fromisoformat(string_date)