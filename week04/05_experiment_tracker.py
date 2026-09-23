import json
from pathlib import Path
from experiment import Experiment


lab_folder = Path(__file__).resolve().parent

json_path = lab_folder / "data" / "experiments.json"

report_path = (lab_folder/ "reports"/ "experiment_summary.txt")


def add_experiment(experiments,experiment_id,model_name,dataset_name,accuracy):
    try:
        accuracy = float(accuracy)
    except ValueError:
        raise ValueError("Accuracy must be a number between 0 and 1.")

    experiment = Experiment(experiment_id,model_name,dataset_name,accuracy)

    experiments.append(experiment)

    return experiment


def display_experiments(experiments):
    if not experiments:
        print("No experiments are available")
        return

    for experiment in experiments:
        print(f"{experiment.experiment_id} | "f"{experiment.model_name} | "
            f"{experiment.dataset_name} | "f"Accuracy: {experiment.accuracy}")


def search_experiment(experiments,experiment_id):
    for experiment in experiments:
        if experiment.experiment_id == experiment_id:
            return experiment

    return None


def find_best_experiment(experiments):
    if not experiments:
        return None

    return max(experiments,key=lambda experiment: experiment.accuracy)


def save_experiments(experiments,file_path):
    file_path = Path(file_path)

    file_path.parent.mkdir(parents=True,exist_ok=True)

    records = [experiment.to_dictionary()for experiment in experiments]

    try:
        with file_path.open("w",encoding="utf-8") as file:
            json.dump(
                records,
                file,
                indent=4
            )

    except PermissionError:
        print(f"The location {file_path} is not writable.")


def load_experiments(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        return []

    try:
        with file_path.open("r",encoding="utf-8") as file:
            records = json.load(file)

        experiments = []

        for record in records:
            experiments.append(
                Experiment(record["experiment_id"],record["model_name"],
                    record["dataset_name"],record["accuracy"]))

        return experiments

    except json.JSONDecodeError:
        print("The JSON data is invalid.")
        return []


def write_summary(experiments,file_path):
    file_path = Path(file_path)

    file_path.parent.mkdir(parents=True,exist_ok=True)

    best = find_best_experiment(experiments)

    lines = []

    lines.append("AI Experiment Summary")
    lines.append("======================")
    lines.append("")

    for experiment in experiments:
        lines.append(f"{experiment.experiment_id} | "f"{experiment.model_name} | "
            f"Accuracy: {experiment.accuracy}")

    lines.append("")

    if best is not None:
        lines.append("Best Experiment")
        lines.append("----------------")
        lines.append(f"ID: {best.experiment_id}")
        lines.append(f"Model: {best.model_name}")
        lines.append(f"Accuracy: {best.accuracy}")

    try:
        with file_path.open("w",encoding="utf-8") as file:
            file.write(
                "\n".join(lines))

    except PermissionError:
        print(f"The location {file_path} is not writable.")


def run_assertions():
    experiments = []

    experiment = add_experiment( experiments,"TEST-001","Test Model","Test Dataset","0.75")

    assert experiment.accuracy == 0.75

    dictionary = experiment.to_dictionary()

    assert isinstance(dictionary, dict)
    assert dictionary["accuracy"] == 0.75

    found = search_experiment(experiments,"TEST-001")

    assert found is experiment

    not_found = search_experiment(experiments,"UNKNOWN")

    assert not_found is None

    best = find_best_experiment(experiments)

    assert best is experiment

    try:
        Experiment("BAD-001","Bad Model","Bad Dataset",1.5)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid accuracy should raise ValueError.")

    print("All assertions passed.")


def main():
    run_assertions()

    experiments = load_experiments(json_path)

    print(f"Loaded {len(experiments)} experiment(s) at startup.")

    if not experiments:
        add_experiment(experiments,"EXP-001","Logistic Regression","Student Performance",0.84)

        add_experiment(experiments,"EXP-002","Decision Tree","Student Performance",0.88)

        add_experiment(experiments,"EXP-003","kNN","Student Performance",0.91)

    print()
    print("All experiments:")
    display_experiments(experiments)

    print()
    print("Search result for EXP-002:")

    found = search_experiment(experiments,"EXP-002")

    if found is not None:
        print(found.to_dictionary())
    else:
        print("Experiment was not found.")

    print()
    print("Best experiment:")

    best = find_best_experiment(experiments)

    if best is not None:
        print(best.to_dictionary())

    save_experiments(experiments,json_path)

    write_summary(experiments,report_path)

    reloaded_experiments = load_experiments( json_path)

    print()
    print(f"Successfully reloaded "f"{len(reloaded_experiments)} experiment(s).")

    assert (len(reloaded_experiments) == len(experiments))

    print("Reload assertion passed.")


if __name__ == "__main__":
    main()