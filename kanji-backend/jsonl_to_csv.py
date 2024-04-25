import json
import pandas as pd

def convert_to_csv(file_path,output_path):
    """
    Converts data from a JSONL file to a CSV file.

    Parameters:
    - file_path: The path to the JSONL file to read data from.
    - output_path: The path to save the resulting CSV file.

    Returns:
    This function does not return anything.
    """
    data = []
    with open(file_path) as f:
        for line in f:
            data.append(json.loads(line))

    df = pd.DataFrame(data)
    df = pd.DataFrame.from_dict(data)
    df = pd.DataFrame.from_records(data)
    df.to_csv(output_path)





