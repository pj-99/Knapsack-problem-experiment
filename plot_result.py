import pandas as pd
import matplotlib.pyplot as plt

def plot_by_epsilon(df, y_axis):
    plt.figure(figsize=(10, 6))

    # Filter data for algorithms starting with 'rounding'
    rounding_algos = df[df['Algorithm Name'].str.startswith('rounding')]

    # Sort the data by epsilon to ensure correct line connection
    epsilons = []
    y_values = []

    for alg_name, data in rounding_algos.groupby('Algorithm Name'):
        # Extract epsilon from algo name
        epsilon = float(alg_name.split('rounding')[-1])
        epsilons.append(epsilon)
        y_values.append(data[y_axis].values[0])

    # Sort the data points by epsilon
    sorted_data = sorted(zip(epsilons, y_values))
    epsilons, y_values = zip(*sorted_data)

    # Plot the line
    plt.plot(epsilons, y_values, marker='o', linestyle='-', label=f"{y_axis} vs Epsilon")

    plt.xlabel('Epsilon')
    plt.ylabel(y_axis)
    plt.title(f'{y_axis} vs. Epsilon for Rounding Algorithms')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load CSV into a DataFrame
    csv_filename = "all_algo_outputs.csv"
    df = pd.read_csv(csv_filename)
    # Filter one testcase
    df = df[df['Testcase Number'] == "1.out"]
    print(df)

    # Plotting
    plot_by_epsilon(df, 'Time Taken')
    plot_by_epsilon(df, 'Algorithm Result')