import luigi
from app.config import DATASET_FILE_PATH

class Dataset(luigi.Task):
    def run(self):
        raise FileNotFoundError("dataset must exist in order to run task")

    def output(self):
        return luigi.LocalTarget(DATASET_FILE_PATH)

if __name__ == "__main__":
    luigi.run()