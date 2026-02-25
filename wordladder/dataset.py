import pandas as pd

def load_dataset():
    splits = {'train': 'data/train-00000-of-00001.parquet', 'validation': 'data/validation-00000-of-00001.parquet',
              'test': 'data/test-00000-of-00001.parquet'}
    df = pd.concat(
        [pd.read_parquet("hf://datasets/magus4450/english-words-small-letter-count/" + splits["train"]),
        pd.read_parquet("hf://datasets/magus4450/english-words-small-letter-count/" + splits["validation"]),
        pd.read_parquet("hf://datasets/magus4450/english-words-small-letter-count/" + splits["test"])]
    )
    return df['text'].tolist()

def prune(size, words):
    return [word.lower() for word in words if isinstance(word, str) and len(word) == size]