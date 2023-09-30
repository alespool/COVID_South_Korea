import glob
import os
from typing import Dict, List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport


def read_csv_files(csv_files: List[str]) -> Dict[str, pd.DataFrame]:
    """
    Reads a list of csv files and returns a dictionary of dataframes.

    Args:
        csv_files (List[str]): A list of csv file paths contained in the data_folder.

    Returns:
        Dict[str, pd.DataFrame]: A dictionary where the keys are the filenames without extension
        and the values are the corresponding dataframes.
    """
    dataframes = {}

    for f in csv_files:
        df = pd.read_csv(f)
        filename = os.path.basename(f).split(".")[0].lower()+'_df'
        df.attrs['name'] = filename

        dataframes[filename] = df

        print('File acquired:')
        print(f.split("/")[-1])
        print()

    return dataframes


def check_dataframes(dataframes: Dict[str, pd.DataFrame]) -> None:
    """
    Check dataframes for duplicates and NaNs.

    Args:
        dataframes (Dict[str, pd.DataFrame]): A dictionary containing the dataframes to be checked.

    Returns:
        None
    """
    for name, df in dataframes.items():

        print(f"Checking dataframe: {name}")
        duplicated_count = df.duplicated().sum()
        if duplicated_count > 0:
            print(f"Duplicates:\n")
            print(duplicated_count)
            print()
        else:
            print(f'0 duplicate values detected for {name}')

        if df.isna().values.any():
            print(f"NAs:\n")
            print(df.isna().sum())
            print()
        else:
            print(f'0 NA values detected for {name}')

        print()
        
    print("Summary:")
    for name, df in dataframes.items():
        duplicated_count = df.duplicated().sum()
        nas_count = df.isna().sum().sum() 

        print(f"{name}:")
        print("Duplicates:", duplicated_count)
        print("NAs:", nas_count)
        print()

def trim_dataframes(dataframes: Dict[str, pd.DataFrame]) -> None:
    """
    Trim dataframes to remove trailing and leading white spaces.

    Args:
        dataframes (Dict[str, pd.DataFrame]): A dictionary containing the dataframes to be trimmed.

    Returns:
        None
    """
    for name, df in dataframes.items():
        string_columns = df.select_dtypes(include='object').columns
        df[string_columns] = df[string_columns].apply(lambda x: x.str.strip())
        dataframes[name] = df.rename(columns=lambda x: x.strip())

def create_reports(dataframes: Dict[str, pd.DataFrame], data_folder: str) -> None:
    """
    Create ydata_profiling reports for each dataframe.

    Args:
        dataframes (Dict[str, pd.DataFrame]): A dictionary containing the dataframes to be created.
        data_folder: str: The path to the data folder where the reports should be saved. 

    Returns:
        None
    """
    output_folder = os.path.join(data_folder, "ydata_profiling_reports")

    for name, df in dataframes.items():
        # Create a pandas-profiling profile report
        profile = ProfileReport(df, title=f"{name} Profiling Report", explorative=True)
        output_file = os.path.join(output_folder, f"{name}_report.html")
        profile.to_file(output_file)


def get_pivot_confirmed_deceased(data: pd.DataFrame, column_pivot: str) -> pd.DataFrame:
    """
    Generate a pivot table with the sum of confirmed and deceased cases
    for each date and the specified pivot column.
    This is a function specific to the COVID-19 dataset and is not generalizable to other datasets.

    Args:
        data (pd.DataFrame): The input data containing the cases.
        column_pivot (str): The column to use as the pivot.

    Returns:
        pd.DataFrame: The pivot table with the sum of confirmed and deceased cases
        for each date and the specified pivot column.
    """
    pivot_table = data.pivot_table(
        columns=column_pivot,
        index='date',
        values=['confirmed', 'deceased'],
        aggfunc='sum'
    )
    return pivot_table

def plot_confirmed_deceased(pivot_df: pd.DataFrame, palette=None) -> None:
    """
    Plots the COVID-19 confirmed and deceased cases by gender and age group. 
    The plot contains 2 different adjacent graphs, one for the confirmed and one for the deceased.
    This is a function specific to the COVID-19 dataset and is not generalizable to other datasets.

    Args:
        pivot_df (pd.DataFrame): DataFrame with columns 'confirmed' and 'deceased' representing the data.

    Returns:
        None
    """

    fig, axes = plt.subplots(1, 2, figsize=(15, 7))

    # Get the 'confirmed' and 'deceased' data
    confirmed_data = pivot_df['confirmed']
    deceased_data = pivot_df['deceased']

    # Define color palettes for the plots
    qualitative_colors = sns.color_palette("tab10", len(confirmed_data.columns))
    color_palette = sns.color_palette("tab10", len(confirmed_data.columns))

    for i, column in enumerate(confirmed_data.columns):
        # # Determine whether the plot is for gender or age dataframe 
        if column != 'male' and column != '10s':
            palette = qualitative_colors[i]
        else:
            palette = color_palette[i]

        # Plot the 'confirmed' and 'deceased' data for the column
        axes[0].plot(confirmed_data[column], linestyle='-', color=palette, linewidth=2)
        axes[1].plot(deceased_data[column], linestyle='-', color=palette, linewidth=2)

    # Set titles and labels for the plots
    axes[0].set_title(f"COVID-19 Confirmed Cases by {confirmed_data.columns.name.title()}")
    axes[0].set_ylabel('Number of Confirmed')
    axes[0].set_xticks(ticks=(5, 25, 50, 75, 100))
    axes[0].legend(list(confirmed_data.columns), loc='upper left', fontsize='small')

    axes[1].set_title(f"COVID-19 Deceased Cases by {confirmed_data.columns.name.title()}")
    axes[1].set_ylabel('Number of Deceased')
    axes[1].set_xticks(ticks=(5, 25, 50, 75, 100))
    axes[1].legend(list(deceased_data.columns), loc='upper left',fontsize='small')

    # Display the plots
    plt.show()

def create_duration_boxplot(x: str, y: str, order, hue=None, hue_order=None, data = pd.DataFrame) -> None:
    """
    Create a boxplot to visualize the time from confirmation to release or death. This is a function
    specific to the COVID-19 dataset and is not generalizable to other datasets.

    Args:
        x: str, name of the variable to be plotted on the x-axis
        y: str, name of the variable to be plotted on the y-axis
        order: list, order of the x-axis categories
        hue: str, name of the variable to be used for grouping the data points
        hue_order: list, order of the hue categories

    Returns:
        None
    """
    # Set the figure size
    plt.figure(figsize=(12, 8))
    sns.boxplot(x=x, y=y, order=order, hue=hue, hue_order=hue_order, data=data)

    if x == 'age_numeric':
        x = 'age'

    title = f"Time from confirmation to release or death by {x}\n (excluding post mortem confirmations) (n={len(data)})"
    plt.title(title, fontsize=16)

    plt.xlabel(x.capitalize(), fontsize=16)
    plt.ylabel("Days", fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()
