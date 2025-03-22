import luigi
from dotenv import load_dotenv

from src.data.data_services import DataTasks
from src.evaluation.evaluation_services import EvaluationTasks
from src.features.feature_services import FeatureTasks
from src.models.model_services import ModelTasks

load_dotenv(dotenv_path="src/.env.example")

if __name__ == "__main__":
    luigi.build(DataTasks(), local_scheduler=True, workers=1)
    luigi.build(FeatureTasks(), local_scheduler=True, workers=1)
    luigi.build(ModelTasks(), local_scheduler=True, workers=1)
    
    luigi.build(EvaluationTasks(), local_scheduler=True, workers=1)
