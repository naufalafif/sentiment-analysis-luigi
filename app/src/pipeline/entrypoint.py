import luigi
import datetime
from app.src.pipeline.train_classifier import TrainClassifier

CURRENT_DATE = datetime.date.today()


class Entrypoint(luigi.WrapperTask):
    """
        Entrypoint of pipeline
    """

    def run(self):
        print(f"Running Pipeline {CURRENT_DATE}")

    def requires(self):
        yield TrainClassifier(CURRENT_DATE)


if __name__ == "__main__":
    luigi.run()
