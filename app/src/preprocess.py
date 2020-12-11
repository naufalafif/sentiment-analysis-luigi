from toolz import pipe
from app.src.utils.preprocess import PreprocessUtil

def preprocessing(text: str) -> str:
    """
        preprocess text by remove symbol, stopword & stemming (ID)
        :parameter text: str
        :return: str, preprocessed text
    """
    return pipe(text,
                PreprocessUtil.symbol_remover,
                PreprocessUtil.stopword_remover,
                PreprocessUtil.stemmer
                )