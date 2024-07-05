import os
import csv

def collect_algo_outputs(directory):
    # Initialize a list to hold all data rows
    all_data = []

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if "out_alg_" in filename:
            filepath = os.path.join(directory, filename)
            testcase_num = filename.split('_')[0]
            alg_name = filename.split("_")[-2]

            # Read the content from the file
            with open(filepath, 'r') as file:
                algo_result = file.readline().strip()
                time_taken = file.readline().strip()

                # Append to all_data as a tuple
                all_data.append((testcase_num, alg_name, algo_result, time_taken))

    return all_data

def write_to_csv(data, csv_filename):
    # Write collected data to a CSV file
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Testcase Number', 'Algorithm Name', 'Algorithm Result', 'Time Taken'])

        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    directory_path = "./tests_exp"
    csv_filename = "all_algo_outputs.csv"

    # Collect all algorithm outputs
    all_data = collect_algo_outputs(directory_path)

    # Write to CSV
    write_to_csv(all_data, csv_filename)
    print(f"CSV file '{csv_filename}' has been created with all algorithm outputs.")