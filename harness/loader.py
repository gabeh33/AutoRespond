"""
Loads the JSON logs from various sources (aws, Okta, etc.) and flattens them into a dict
"""

import json
import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent 
AWS_LOGS = (ROOT / "logs" / "aws" / "cloudtrail_logs" / "start_logging.json")

def flatten_file(folder: Path) -> dict:
    """ Given a Path object to a Json file, returns a flattened dict containing the data """
    with folder.open(mode='r', encoding="utf-8") as file:
        raw_jason = json.load(file)
    tmp_frame = pd.json_normalize(raw_jason, sep="_")

    dictionary = tmp_frame.to_dict(orient='records')[0]
 
    return dictionary

my_dict = flatten_file(AWS_LOGS)
print(len(my_dict.keys()))