from flask_restx import fields
from flask_restx import Namespace
from flask_restx import Resource

class ObjectIdString(fields.Raw):
  __schema_example__='ObjectId'

  def format(self, value):
    return str(value)

class Percentage(fields.Raw):
  __schema_example__='Percentage'

  def format(self, value):
    return 100 * value


class SuccessNamespace(Namespace):
  def success(self, name, data):
    return self.model("GET_{}_DATA".format(name), data)

  def property_in_list_of_items(self, name, property_name, property_type):
    return self.model(name + property_name, { property_name: property_type })

  def time_property_in_range(self, name, property_names):
    time_range = self.model(name + "_time_range", {
      "from": fields.DateTime,
      "to": fields.DateTime
    })
    return fields.Nested(self.model(name + "_time_property_in_range",
      { property_name: fields.Nested(time_range) for property_name in property_names } ))

  def get_property_in_list_of_items(self, name, properties):
    return fields.Nested(self.model(name + "_property_in_list_of_items",
      { item['name']: fields.List(item['type']) for item in properties}))

  def get_property_match(self, name, properties):
    return fields.Nested(self.model(name + "_property_match",
      { item['name']: item['type'] for item in properties}))

  def root_level_properties(self, items, result):
    return {key: value for key, value in items.items() if key not in result}

  # Parse passed filters
  def filters(self, name, items={}, base_filters=True):
    result = {}

    if "property_match" in items:
      result["property_match"] = self.get_property_match(name, items.get('property_match', []))

    if "time_property_in_range" in items:
      result["time_property_in_range"] = self.time_property_in_range(name, items.get('time_property_in_range'))

    if "property_in_list_of_items" in items:
      result["property_in_list_of_items"] = self.get_property_in_list_of_items(name, items.get('property_in_list_of_items', []))

    return {**result, **self.root_level_properties(items, result)}

  def phrase_base_filters(self, items):
    if "property_match" not in items:
      items['property_match'] = []

    items['property_match'].append({"name": "persona_id", "type": ObjectIdString})

  def phrase_filters(self, name, items={}, base_filters=True):
    result = {}

    if base_filters:
      self.phrase_base_filters(items)

    result = self.filters(name, items)
    return self.model("FILTER_" + name, result)

  def word_base_filters(self, items):
    if "property_match" not in items:
      items['property_match'] = []

    items['property_match'].append({"name": "persona_id", "type": ObjectIdString})

  def word_filters(self, name, items={}, base_filters=True):
    result = {}

    if base_filters:
      self.word_base_filters(items)

    result = self.filters(name, items)
    return self.model("FILTER_" + name, result)

  def phrase_base_filters(self, items):
    if "property_match" not in items:
      items['property_match'] = []

    items['property_match'].append({"name": "persona_id", "type": ObjectIdString})

  def phrase_filters(self, name, items={}, base_filters=True):
    result = {}

    if base_filters:
      self.phrase_base_filters(items)

    result = self.filters(name, items)
    return self.model("FILTER_" + name, result)

  def word_base_filters(self, items):
    if "property_match" not in items:
      items['property_match'] = []

    items['property_match'].append({"name": "persona_id", "type": ObjectIdString})

  def word_filters(self, name, items={}, base_filters=True):
    result = {}

    if base_filters:
      self.word_base_filters(items)

    result = self.filters(name, items)
    return self.model("FILTER_" + name, result)

  def translations_base_filters(self, items):
    if "property_match" not in items:
      items['property_match'] = []

    items['property_match'].append({"name": "persona_id", "type": ObjectIdString})

  def translations_filters(self, name, items={}, base_filters=True):
    result = {}

    if base_filters:
      self.translations_base_filters(items)

    result = self.filters(name, items)
    return self.model("FILTER_" + name, result)