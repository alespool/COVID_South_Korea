# **COVID-19 crisis**

## Project objective:
------------

<div><img width="400px" height="auto" src="https://images.unsplash.com/photo-1574515944794-d6dedc7150de?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1532&q=80" /></div>

The world is still struggling with one of the most rapidly spreading pandemics.
There are a lot of people who say that data is the best weapon we can use in this "Corona Fight."

Imagine that we are one of the best data scientists in the country.
The president of our country asked us to analyze the COVID-19 patient-level data of South Korea and prepare our homeland for the next wave of the pandemic.
We, as the lead data scientists of the country **have to create and prove a plan of fighting the pandemics in our country** by analyzing the provided data.
We must get the most critical insights using learned data science techniques and present them to the lead of our country.

The link to the [Kaggle dataset is here](https://www.kaggle.com/kimjihoo/coronavirusdataset/) and fortunately we have a great dataset on our hands that doesn't need us to overly modify it, as it is quite clean already at present.

There are many datasets present, and we will need most of them. But we can disregard the 'weather', 'searchtrend' and 'seoulfloating' ones.

## Project outline
------------

The data we have at disposition is extensive, and covers a great amount of interesting variables, such as times, dates, patients information and even so far as having weather data. We need to use all of this to come up with a plan to tackle the issue at hands.

First of all, although this data seems great, we need to make sure that we are working with clean data. This is important because it hinders us from doing our job well first, but also can give rise to a different perception of the data compared to reality. When the data is cleaned, we can proceed with visualizing in the entirety what it is trying to *tell us*. We should let the data speak for itself, not the other way around. From the information at hands, we will extrapolate insights to present to the leads.

Thus, the project outline will be as follows:

- Data cleaning
- Data visualization
- Conclusions

## Requirements
------------

To run the analysis, we will need:

-   Python 3.x
-   Jupyter Notebook or any compatible environment
-   A series of Python libraries (you can install them by compiling+ `pip install -r requirements.txt` in your terminal)

## Folder Structure
-----------------

The project includes the following files and directories:

-   `data`: A folder containing all the CSV files we will work with.
-   `ydata_profiling_reports`: A folder containing the data profiling reports created with ydata_profiling.
-   `py_functions`: A folder containing the Python modules that will help us with the project.
    -   `correlation_utilities`: Python file for calculating the correlation between variables.
    -   `pandas_utilities`: Python file to help us read the CSV files, check for inconsistencies, and clean the strings.
-   `data_cleaning.ipynb`: Jupyter Notebook containing the data cleaning and preprocessing code.
-   `data_visualization.ipynb`: Jupyter Notebook containing the data visualization code.
-   `dataframes.pickle`: Pickle file containing the cleaned data.
-   `README.md`: Documentation file explaining the project and its requirements.

## Getting Started
---------------

We are top notch data scientists, and I don't expect you to be told how to do this. However, the country's leadership needs our guidance and we need to make sure that they can reproduce this analysis, and as such we need to list the steps that should be taken to ensure a proper usage of these documents. The analysis is divided into 3 different files, and the order is important for understanding the context. Here is the suggested sequence of steps:

1.  Download the dataset from Kaggle: [[NeurIPS 2020] Data Science for COVID-19 (DS4C)](https://www.kaggle.com/kimjihoo/coronavirusdataset/).
2.  Place the downloaded CSV file in the `data` directory.
3.  Open the Jupyter Notebook `data_cleaning.ipynb` and run each cell to execute the code step-by-step.
4.  Open the Jupyter Notebook `data_visualization.ipynb` and run each cell to execute the code step-by-step.

## Data Analysis
-------------

The data analysis covers the following aspects:

1.  ### Data cleaning:

    -   Handling missing values.
    -   Removing duplicate samples and features.
    -   Adding useful columns.
    -   Creating reports on each dataset for better understanding.
    
2.  ### Data Visualization:

    -   Visualizing the features to understand the data.
    -   These features include times, dates, patients information, and so on.
    -   The visualization focuses heavily on the geographical and time distribution of the infection.

3.  ### Explanation and interpretation:

    -   All the analysis steps are accompanied by an explanation of the objectives, results, and their meanings.

## Suggestions for improvement:
-------------
The scope of this project could be too big, as the analysis is quite extensive and focusing on many aspects of the infection. It would be better if the project could be broken down into smaller parts, as well as a more detailed explanation of the steps, so that each of the sides can be taken care of extensively. 

However, I believe that the approach taken here is the most advisable for requests such as this, as it can give a good general idea of where the efforts might need to be focussed. 

There is also the possibility to undergo a modelling procedure, to try to predict the future cases starting from the present information we have on patients. Unfortunately, due to time constraints this was not feasible, but it is something worth considering.

## Conclusion
----------
The COVID-19 Crisis project provides critical insights into the patient-level data of South Korea during the pandemic. The analysis involves data cleaning, visualization, and modeling to understand the current situation and prepare for future waves of the pandemic. To make clear what where the main findings of the analysis, we will post them here as well.

At the end of this analysis, the major recommendations that we can give are:

- Avoid gatherings and meetings of more than 10 people;
- Wear masks to prevent the spread of the virus;
- Lookout for tourism or international traffic flow;
- Increase the security of hospitals and nursing homes;
- More attention should be given to elderly people who are more susceptible to the virus;
- Use the best measures to control the spread of the virus such as increasing testing facilities, and contact tracing.
- Deploy help precisely and rapidly, so that the infection has less probabilities to spread.

We hope that this analysis has been helpful and interesting, and that our recommendations can help prevent the spread of the virus in the country. By understanding the analysis and following the recommendations, I'm sure the country can develop a comprehensive plan to fight the pandemic effectively.

For any questions or feedback, please contact me at [alessionespoli.97@gmail.com].