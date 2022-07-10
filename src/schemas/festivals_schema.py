festivals_schema = {

  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "type": "array",
  "items": {
    "type": "object",
    "required": ["name", "bands"],
    "properties": {
      "name": {"type": "string"},
      "bands": {
        "type": "array",
        "items": {"$ref": "#/defs/band" }
      }
    }
  },


  "defs": {
    "band": {
      "type": "object",
      "required": ["name", "recordLable"],
      "properties": {
        "name": {"type": "string"},
        "recordLabel": {"type": "string"}
      }
    }
  }

}



