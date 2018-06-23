import json
import os

from utils import parse_calendar

"""
START SETTINGS
"""
# Settings to manually adjust/pass in as args
folder_path = './in'
# A lazy way of getting the filename without the extension
num_months = 13
start_month = 6
start_year = 2018
num_columns = 3
"""
END SETTINGS
"""

for filename in os.listdir(folder_path):
    select = parse_calendar(
        filename=f"{folder_path}/{filename}",
        start_year=start_year,
        start_month=start_month,
        num_months=num_months,
        num_columns=num_columns,
    )

    # Write the output to a file
    title = filename.split(".")[0]
    output_name = f"out/{title}.json"
    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_name), exist_ok=True)
    # Write JSON to file
    with open(output_name, "w") as out:
        json.dump(select, out)
