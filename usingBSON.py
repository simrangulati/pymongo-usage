# Install  pymongo which has support for bson. Do not use `pip install bson` as it installs unofficial package which might lack support for latest pymongo features
# Import MongoDB BSON types for ObjectId and high-precision Decimal
from bson import ObjectId, Decimal128

# Import JSON utility from bson to handle serialization/deserialization of special Mongo types
from bson.json_util import dumps, loads, CANONICAL_JSON_OPTIONS, RELAXED_JSON_OPTIONS

# Import datetime to store current timestamp
import datetime

# Define a Python dictionary with MongoDB-specific types
data = {
    "_id": ObjectId("507f1f77bcf86cd799439011"),  # MongoDB's unique object ID
    "createdAt": datetime.datetime.utcnow(),       # Current timestamp
    "price": Decimal128("19.99")                   # High-precision decimal, good for money
}

# 🔴 Try converting to standard JSON — this will FAIL
# Because the regular json module doesn’t understand ObjectId or Decimal128
import json
try:
    print(json.dumps(data))
except Exception as e:
    print("❌ Regular JSON failed:", e)

# ✅ Convert to Extended JSON using Relaxed Mode
# This looks more like normal JSON — human-readable and readable by MongoDB
relaxed_json = dumps(data, json_options=RELAXED_JSON_OPTIONS)
print("✅ Relaxed EJSON:\n", relaxed_json)

# ✅ Convert to Extended JSON using Canonical Mode
# This keeps type information very precise — useful for exact round-tripping
canonical_json = dumps(data, json_options=CANONICAL_JSON_OPTIONS)
print("✅ Canonical EJSON:\n", canonical_json)

# 🔁 Convert back from Extended JSON to native Python objects
# This proves that EJSON supports round-trip conversion
parsed_data = loads(relaxed_json)
print("🔄 Back to Python:\n", parsed_data)
