def time_range_doc():
  return {
    "start_time": "filter w.r.t start_time by ONLY setting start time",
    "end_time": "filter w.r.t end_time by ONLY setting end_time",
    "start_time AND end_time": "filter w.r.t start_time AND end_time by setting both",
    "start_time OR end_time": "filter w.r.t start_time OR end_time by setting both and setting time_property_in_range_combine_as_or=True",
  }

def time_property_in_range_doc(time_property_in_range, time_range):
  return {
    'INSTRUCTIONS:': time_range_doc(),
    **{
        k:
        {
          kk: "ISO DateTime" for kk in time_range.keys()
        } for k in time_property_in_range.keys()
      }
    }