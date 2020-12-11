from sklearn.feature_extraction.text import TfidfVectorizer
from app.src.utils.wrapper import wrapper_factory


TFIDFVectorizerWrapper = wrapper_factory(TfidfVectorizer)