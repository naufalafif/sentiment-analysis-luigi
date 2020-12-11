import luigi
from app.src.pipeline.weighting import Weighting
from app.src.pipeline.preprocessing import Preprocessing
from app.config import MODEL_DIR, CLASSIFIER_FILENAME
from os import path
import pandas as pd
from app.src.classifier import NaivebayesClassifierWrapper
import pickle

class TrainClassifier(luigi.Task):
    datetime = luigi.DateParameter()
    def requires(self):
        return Weighting(self.datetime), Preprocessing(self.datetime)

    def run(self):
        x_train_weighted_vector_target, preprocessed_dataset_target = self.input()
        x_train_weighted_vector = pickle.load(open(x_train_weighted_vector_target.path, 'rb'))

        preprocessed_dataframe = pd.read_csv(preprocessed_dataset_target.path)
        NaivebayesClassifierWrapper.instance.fit(x_train_weighted_vector, preprocessed_dataframe.Sentiment)

        with open(self.output().path, 'wb') as file_io:
            NaivebayesClassifierWrapper.to_file(file_io)

    def output(self):
        classifier_filename = CLASSIFIER_FILENAME.format(version=self.datetime)
        classifier_filepath = path.join(MODEL_DIR, classifier_filename)
        return luigi.LocalTarget(classifier_filepath)


if __name__ == "__main__":
    luigi.run()