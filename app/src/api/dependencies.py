import pickle
import app.config as config
from os.path import join
from fastapi import Request

def get_model(request: Request):
    """
        dependency injection, get model based on version
    """

    version = request.app.state.version
    vectorizer_filepath = join(config.MODEL_DIR, config.VECTORIZER_FILENAME.format(version=version))
    vectorizer = pickle.load(open(vectorizer_filepath, 'rb'))

    classifier_filepath = join(config.MODEL_DIR, config.CLASSIFIER_FILENAME.format(version=version))
    classifier = pickle.load(open(classifier_filepath, 'rb'))

    return vectorizer, classifier