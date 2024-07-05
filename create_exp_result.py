import os
import csv
import argparse

def collect_algo_outputs(directory):
    # Initialize a list to hold all data rows
    all_data = []

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if '.out' in filename and filename.split('_')[0].isdigit():
            filepath = os.path.join(directory, filename)
            test_case_name = filename.split('.')[0]
            alg_name = filename.split("_")[-2]

            # Read the content from the file
            with open(filepath, 'r') as file:
                algo_result = file.readline().strip()
                time_taken = file.readline().strip()

            # Append to all_data as a tuple
            all_data.append((test_case_name, alg_name, algo_result, time_taken))

    return all_data

def write_to_csv(data, csv_filename):
    # Write collected data to a CSV file
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Testcase Name', 'Algorithm Name', 'Algorithm Result', 'Time Taken'])
        # Sory by testcase name and then by algorithm name
        data.sort(key=lambda x: (int(x[0].split('_')[0]), x[1]))
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--test_folder", help="The test folder name", default="./tests_exp/")
    arg = argparser.parse_args()
    TEST_FOLDER = arg.test_folder

    directory_path = arg.test_folder
    csv_filename = os.path.join(directory_path, "all_algo_outputs.csv")

    # Collect all algorithm outputs
    all_data = collect_algo_outputs(directory_path)

    # Write to CSV
    write_to_csv(all_data, csv_filename)
    print(f"CSV file '{csv_filename}' has been created with all algorithm outputs.")