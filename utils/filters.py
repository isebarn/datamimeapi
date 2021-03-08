from functools import wraps
from datetime import datetime
from bson.objectid import ObjectId
from utils.dateutil import get_date
from utils.DbConnection import get_collection
from app_constants import filter_maps


def aggregate_by_property_match(fn):
  @wraps(fn)
  def wrapped(aggregate, filters):
    if filters is not None and "property_match" in filters:
      aggregate.insert(0, {"$match": {
        key: ObjectId(value) if ObjectId.is_valid(value) else value
        for key, value in filters.get("property_match").items()
      }})

    return fn(aggregate, filters)

  return wrapped


def aggregate_time_property_in_range(fn):
  @wraps(fn)
  def wrapped(aggregate, filters):
    if filters is not None:
      for key, value in filters.get('time_property_in_range', {}).items():

        aggregate.insert(0, { "$match": {key: {
          "$gte": get_date(value['from']),
          "$lte": get_date(value['to'])
        }}})


    return fn(aggregate, filters)
  return wrapped


def aggregate_property_in_list_of_items(fn):
  @wraps(fn)
  def wrapped(aggregate, filters):
    for key, value in filters.get('property_in_list_of_items', {}).items():

      # if all in list are valid object_id objects, convert to ObjectId objects
      if all(map(lambda x: ObjectId.is_valid(x), value)):
        value = [ObjectId(x) for x in value]

      aggregate.insert(0, {"$match":  { key : { "$in": value }}})
    return fn(aggregate, filters)
  return wrapped

def find_by_property_match(fn):
  @wraps(fn)
  def wrapped(find, filters):
    for key, value in filters.get('property_match', {}).items():

      # convert to ObjectId objects if value is a valid ObjectId string
      if ObjectId.is_valid(value):
        find[key] = ObjectId(value)

      else:
        find[key] = value

    return fn(find, filters)
  return wrapped


def find_property_in_list_of_items(fn):
  @wraps(fn)
  def wrapped(find, filters):
    for key, value in filters.get('property_in_list_of_items', {}).items():

      # convert to ObjectId objects if values is a list of valid ObjectId strings
      if all(map(lambda x: ObjectId.is_valid(x), value)):
        find[key] = { "$in": [ObjectId(x) for x in value] }

      else:
        find[key] = { "$in": value }

    return fn(find, filters)
  return wrapped


def find_time_property_in_range(fn):
  @wraps(fn)
  def wrapped(find, filters):
    for key, value in filters.get('time_property_in_range', {}).items():
      find[key] = {
        "$gte": get_date(value["from"]),
        "$lte": get_date(value["to"])
      }

    if filters.get('time_property_in_range_combine_as_or', False):
      find["$or"] = [{key: find.pop(key) for key in
        filters['time_property_in_range'].keys()}]

    return fn(find, filters)
  return wrapped

def name_hash_to_id(fn):
  @wraps(fn)
  def wrapped(search_type, filters):
    items = filters.get('property_in_list_of_items', {})
    for key in list(items.keys()):
      if "_name_hash" in key:
        collection = key.replace('_name_hash', '')
        collection_name, property_name = filter_maps[collection].values()

        items[property_name] = [x['_id'] for x in get_collection(
          collection_name).find({"name": {"$in": items[key]}}, {"_id": 1})]

        items.pop(key)

    return fn(search_type, filters)
  return wrapped
