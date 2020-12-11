from sklearn.naive_bayes import MultinomialNB
from app.src.utils.wrapper import wrapper_factory
        
NaivebayesClassifierWrapper = wrapper_factory(MultinomialNB)