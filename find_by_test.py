import sys
from index import load_json

manifest = load_json("data/failures/manifest")

for id in manifest["failures"]:
    failure = load_json(f"data/failures/{id}")

    if sys.argv[1] in failure["test_id"]:
        print(f"{id} {failure['test_id']}")