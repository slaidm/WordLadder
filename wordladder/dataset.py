from google.colab import drive
import pandas as pd

def load_dataset(dataset_name, type='text'):
    drive.mount('/content/gdrive')
    if type == 'text':
        with open('/content/gdrive/My Drive/' + dataset_name, 'r') as f:
            return f.read().splitlines()
    if type == 'csv':
        return pd.read_csv('/content/gdrive/My Drive/' + dataset_name)['word'].to_list()

#Prunes the dataset and puts into set for fast lookup
def prune(size, words):
    return [word for word in words if isinstance(word, str) and len(word) == size]