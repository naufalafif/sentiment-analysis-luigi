# PREPROCESS

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string

class PreprocessUtil:
    """
        collection of preprocessing utility
    """
    __remover = StopWordRemoverFactory().create_stop_word_remover()
    __stemmer = StemmerFactory().create_stemmer()
    
    @staticmethod
    def symbol_remover(text: str) -> str:
        """
            remove symbol from text
            :parameter text: str
            :return: str
            
            example:
                >>> PreprocessUtil.symbol_remover("naufal, afif")
                naufal afif
        """
        
        return text.translate(str.maketrans('','',string.punctuation)).lower()
    
    @classmethod
    def stopword_remover(cls, text: str) -> str:
        """
            remove stopword from text
            :parameter text: str
            :return: str
            
            example:
                >>> PreprocessUtil.stopword_remover("naufal dan afif")
                naufal afif
        """
        
        return cls.__remover.remove(text)
    
    @classmethod
    def stemmer(cls, text: str) -> str:
        """
            replace word with it's root
            :parameter text: str
            :return: str
            
            example:
                >>> PreprocessUtil.stemmer("naufal berlari")
                naufal lari
        """

        return cls.__stemmer.stem(text)