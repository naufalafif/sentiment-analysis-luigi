import os

DATASET_FILENAME = "dataset.csv"
DATASET_DIR = os.path.join(os.curdir, 'dataset')
DATASET_FILE_PATH = os.path.join(DATASET_DIR, DATASET_FILENAME)

PREPROCESSED_FILENAME = "preprocessed_dataset-{version}.csv"
PREPROCESSED_DATASET_DIR = os.path.join(os.curdir, 'preprocessed_dataset')

MODEL_DIR = os.path.join(os.curdir, 'app', 'src', 'model')
VECTORIZER_FILENAME = "vectorizer-{version}.bin"
VECTORIZER_VECTOR_FILENAME = "weighter_vector-{version}.bin"
CLASSIFIER_FILENAME = "classfier-{version}.bin"