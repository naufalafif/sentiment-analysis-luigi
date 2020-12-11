import luigi
from app.src.pipeline.preprocessing import Preprocessing
from app.config import MODEL_DIR, VECTORIZER_FILENAME, VECTORIZER_VECTOR_FILENAME
from os import path
import pandas as pd
from app.src.vector import TFIDFVectorizerWrapper
import pickle

class CreateWeighter(luigi.Task):
    datetime = luigi.DateParameter()
    def requires(self):
        return Preprocessing(self.datetime)

    def run(self):
        preprocessed_dataset_path = self.input().path
        dataset_dataframe = pd.read_csv(preprocessed_dataset_path)
        TFIDFVectorizerWrapper.instance.fit(dataset_dataframe.Sentence)
        with open(self.output().path, 'wb') as file_io:
            TFIDFVectorizerWrapper.to_file(file_io)

    def output(self):
        vectorizer_filename = VECTORIZER_FILENAME.format(version=self.datetime)
        vectorizer_filepath = path.join(MODEL_DIR, vectorizer_filename)
        return luigi.LocalTarget(vectorizer_filepath)

class Weighting(luigi.Task):
    datetime = luigi.DateParameter()
    def requires(self):
        return CreateWeighter(self.datetime), Preprocessing(self.datetime)

    def run(self):
        weigher_target, preprocessed_dataset_target = self.input()
        weighter = pickle.load(open(weigher_target.path, 'rb'))
        preprocessed_dataframe = pd.read_csv(preprocessed_dataset_target.path)

        x_train_weighted_vector = weighter.transform(preprocessed_dataframe.Sentence)
        with open(self.output().path, 'wb') as file_io:
            pickle.dump(x_train_weighted_vector, file_io)

    def output(self):
        vector_filename = VECTORIZER_VECTOR_FILENAME.format(version=self.datetime)
        vector_filepath = path.join(MODEL_DIR, vector_filename)
        return luigi.LocalTarget(vector_filepath)


if __name__ == "__main__":
    luigi.run()