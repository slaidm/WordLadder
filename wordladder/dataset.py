import pandas as pd
import os.path
from core import import_settings

def load_dataset(config = None):
    if config is None:
        config = import_settings().get("data")

    if os.path.isfile(config.get("file")):
        with open(config.get("file")) as csvfile:
            df = pd.read_csv(csvfile)
            return df[config.get("column")].tolist()
    else: #load from new
        splits = config.get("splits")
        ds = config.get("dataset")
        df = pd.concat(
            [pd.read_parquet("hf://" + ds + splits["train"]),
            pd.read_parquet("hf://" + ds + splits["validation"]),
            pd.read_parquet("hf://" + ds + splits["test"])]
        )
        if config.get("save_to_file"):
            df[config.get("column")].to_csv(config.get("file"), index=False)

        return df[config.get("column")].tolist()

def prune(size, words):
    return [word.lower() for word in words if isinstance(word, str) and len(word) == size]