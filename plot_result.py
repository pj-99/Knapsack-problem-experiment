from itertools import cycle
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

def plot_by_epsilon(ax, dfs, y_axis, y_unit, compare_algos=[], simplified_legend=False,
                    fix_rounding_linestyle=False,
                    fix_rounding_marker=None,
                    title=None,
                    fix_y_range=False):
    norm_colors = ["red"]
    uni_colors = ["blue"]
    linestyles = {
        'dp': "solid",
        'greedy': 'solid',
        'fractional': 'solid',
        "modifiedgreedy": ":",
    }

    algo_colors = {
        "fractional": "green",
        "greedy": "cyan",
        "dp": "gold",
        "modifiedgreedy": "purple",
    }

    rounding_linestyles = ['solid', 'dotted', 'dashed', '-.', ':'] * 10
    rounding_markers = ['.', 'o', 's', 'x', 'P', 'D', 'v', '>', 'P', '*']

    handles = []
    labels = []

    for i, (file_name, df) in enumerate(dfs.items()):
        testcase_idx = int(file_name.split('_')[0]) - 1

        if file_name.endswith('norm'):
            color = norm_colors[0]
            prefix = "Norm"
        else:
            color = uni_colors[0]
            prefix = "Uniform"
        marker = rounding_markers[i] if fix_rounding_marker is None else fix_rounding_marker
        rounding_linestyle = "-" if fix_rounding_linestyle else rounding_linestyles[testcase_idx]
        rounding_algos = df[df['Algorithm Name'].str.startswith('rounding')].copy()
        rounding_algos['epsilon'] = rounding_algos['Algorithm Name'].str.extract('rounding(0\.\d*)').astype(float)
        rounding_algos = rounding_algos.sort_values('epsilon')
        line, = ax.plot(rounding_algos['epsilon'], rounding_algos[y_axis],
                        marker=marker, linestyle=rounding_linestyle, color=color, linewidth=2)

        if simplified_legend:
            print("prefix", prefix, labels)
            if f"Rounding, {prefix}" not in labels:
                handles.append(line)
                labels.append(f"Rounding, {prefix}")
        else:
            handles.append(line)
            labels.append(f"{prefix}{file_name.split('_')[0]}, rounding ")

        for alg in compare_algos:
            y_value = df[df['Algorithm Name'] == alg][y_axis].values[0]
            line = ax.axhline(y=y_value,
                              color=algo_colors[alg],
                              linestyle=linestyles[alg],
                              marker=None,
                              linewidth=2,
                              )
            if simplified_legend:
                if alg not in labels:
                    handles.append(line)
                    labels.append(alg)
            else:
                handles.append(line)
                if alg == 'dp': alg = "DP (OPT)"
                labels.append(f"{prefix}{file_name.split('_')[0]}, {alg} ")

    ax.set_xlabel('Epsilon')
    ax.set_ylabel(y_axis + f' {y_unit}')
    title = title if title is not None else f'[{y_axis}] Algorithms comparison across different tests'
    ax.set_title(title)

    # Set y range to rounding results window
    if fix_y_range:
        ax.set_ylim(fix_y_range)

    ax.legend(handles, labels)

    ax.grid(True)

def filter_tests(df, test_names):
    return df[df['Testcase Name'].isin(test_names)]

if __name__ == "__main__":
    # Load all CSV files
    csv_file = "tests_exp/all_algo_outputs.csv"
    df = pd.read_csv(csv_file)

    # Filter
    # df = filter_tests(df, ['1_norm'])

    # Convert seconds to milliseconds
    df['Time Taken'] = df['Time Taken'] * 1000

    # Create dfs dictionary
    dfs = {}

    for test_name in df['Testcase Name'].unique():
        dfs[test_name] = df[df['Testcase Name'] == test_name]
        # Convert Algorithm Result to ratio of OPTIMAL
        optimal = dfs[test_name][dfs[test_name]['Algorithm Name'] == 'dp']['Algorithm Result'].values[0]
        dfs[test_name]['Algorithm Result'] = dfs[test_name]['Algorithm Result'] / optimal

    print(dfs)
    # Create two separate figures
    fig1, ax1 = plt.subplots(figsize=(14, 8))
    fig2, ax2 = plt.subplots(figsize=(14, 8))
    fig3, ax3 = plt.subplots(figsize=(14, 8))
    fig4, ax4 = plt.subplots(figsize=(14, 8))


    # Time
    # plot_by_epsilon(ax1, dfs, 'Time Taken', "(ms)")

    # Overview time
    plot_by_epsilon(ax1, dfs, 'Time Taken', "(ms)", compare_algos=['dp', 'fractional', 'greedy', 'modifiedgreedy'],
                    title="All algorithms time comparison",
                    simplified_legend=True)


    plot_by_epsilon(ax2, dfs, 'Time Taken', "(ms)", compare_algos=['dp', 'fractional', 'greedy', 'modifiedgreedy'],
                    title="(Zoom in) All algorithms time comparison",
                    simplified_legend=True,
                    fix_y_range=[0, 100])

    # Performance
    plot_by_epsilon(ax3, dfs, 'Algorithm Result', "(ALG/OPT)", compare_algos=['dp'],
                    title="DP and rounding results for all tests")
    plot_by_epsilon(ax4, dfs, 'Algorithm Result', "(ALG/OPT)",
                    compare_algos=['dp', 'fractional', 'greedy', 'modifiedgreedy'],
                    simplified_legend=True,
                    title="All Algorithms results",)
    # Adjust layout and show plots
    fig1.tight_layout()
    fig2.tight_layout()
    plt.show()