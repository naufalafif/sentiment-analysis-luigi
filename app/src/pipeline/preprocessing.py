import luigi
from app.src.pipeline.dataset import Dataset
from app.config import PREPROCESSED_DATASET_DIR, PREPROCESSED_FILENAME
import pandas as pd
from os import path
from app.src.preprocess import preprocessing

class Preprocessing(luigi.Task):
    datetime = luigi.DateParameter()
    def requires(self):
        return Dataset()

    def run(self):
        dataset_file_path = self.input().path
        dataset_dataframe = pd.read_csv(dataset_file_path)
        dataset_dataframe.Sentence = dataset_dataframe.apply(lambda row: preprocessing(row.Sentence), axis=1)
        dataset_dataframe.to_csv(self.output().path)

    def output(self):
        preprocessed_filemame = PREPROCESSED_FILENAME.format(version=self.datetime)
        preprocessed_filepath = path.join(PREPROCESSED_DATASET_DIR, preprocessed_filemame)
        return luigi.LocalTarget(preprocessed_filepath)

if __name__ == "__main__":
    luigi.run()