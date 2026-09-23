import json
from pathlib import Path


class Experiment:
    def __init__(self,experiment_id,model_name,dataset_name,accuracy):
        if not 0 <= accuracy <= 1:
            raise ValueError("Accuracy must be between 0 and 1.")

        self.experiment_id = experiment_id
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.accuracy = accuracy

    def to_dictionary(self):
        return {"experiment_id": self.experiment_id,"model_name": self.model_name,
                "dataset_name": self.dataset_name,"accuracy": self.accuracy}


def main():
    experiments = [Experiment("EXP-001","Logistic Regression","Student Performance", 0.84),
        Experiment("EXP-002","Decision Tree","Student Performance",0.88),
        Experiment("EXP-003","kNN","Student Performance",0.91)]

    file_path = Path("week04/data/experiments.json")

    file_path.parent.mkdir(parents=True,exist_ok=True)

    records = [experiment.to_dictionary()for experiment in experiments]

    with file_path.open("w",encoding="utf-8") as file:
        json.dump(records,file,indent=4)

    with file_path.open("r",encoding="utf-8") as file:
        loaded_records = json.load(file)

    best_experiment = max(loaded_records,key=lambda experiment: experiment["accuracy"])

    print("Experiments:")
    for experiment in loaded_records:
        print(experiment)

    print()
    print("Best experiment:")
    print(best_experiment)


if __name__ == "__main__":
    main()