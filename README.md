Assignment for Software Development class (WiSe '23)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=IpshitaSingh_scraper-analyzer)](https://sonarcloud.io/summary/new_code?id=IpshitaSingh_scraper-analyzer)

# Data Scraper and Analyzer

This is a Python project that involves scraping data from a specific website and performing analysis on the extracted data.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Outcome](#outcome)
- [UML Diagrams](#uml-diagrams)
- [Requirements Engineering](#requirements-engineering)
- [Analysis Checklist](#analysis-checklist)
- [Domain Driven Design (DDD)](#domain-driven-design-ddd)
- [Metrics](#metrics)
- [Clean Code Development](#clean-code-development)
- [Build, CI/CD, Tests](#build-cicd-tests)
- [IDE](#ide)
- [Functional Programming](#functional-programming)

Note: Some hypothetical additions/expansions have been made, e.g, in UML diagrams, analysis checklist, etc., which assume this project is turning into a start up venture. This has been done to get familiar with the concepts mentioned above! 

## Introduction
Scraper-Analyzer aims to simplify the process of extracting and analyzing data from a particular website. It provides a convenient way to retrieve relevant information and perform insightful analysis, enabling the user to make data-driven decisions efficiently.

### Overview
The project consists of three main components:
1. Scraper: Fetches data from a specified website.
2. Analyzer: Performs data analysis and computations on the scraped data.
3. Main: Integrates the scraping and analysis functionalities to provide the final result.

### Features
- Web scraping functionality to extract data from a specified website.
- Data analysis capabilities to process, visualize, and analyze the scraped data.

## Installation
1. Step 1: Clone the repository

```
git clone https://github.com/IpshitaSingh/scraper-analyzer.git
```

2. Step 2: Navigate to the project directory
```
cd scraper-analyzer
```

3. Step 3: Install dependencies
```
pip install -r requirements.txt
```
4. Step 4: Run the application
```
python main.py
```
The console output will display both summary statistics for the dataset and four visually presented charts with data insights.

## Outcome
The following outcome is produced upon running the program:
### Data Visulizations
1. Plot 1: Top 20 Countries by Population
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/output/Figure_1.png" height="400" width="auto">
This bar chart displays the top 20 countries based on their population.

2. Plot 2: Population Distribution
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/output/Figure_2.png" height="400" width="auto">
The population distribution chart illustrates the spread of population across different countries.

3. Plot 3: Area vs. Population
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/output/Figure_3.png" height="400" width="auto">
This scatter plot visualizes the relationship between the area and population of countries, highlighting any potential correlations.

4. Plot 4: Scatter Plots to depict Correlation between Variables
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/output/Figure_4.png" height="400" width="auto">
These charts present a correlation matrix, offering insights into the relationships between different variables in the dataset.

### Summary Statistics
The console output provides a summary of the data, including shape, data types, and key statistical metrics.
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/output/console.png" height="350" width="auto">

## UML Diagrams
- Activity

<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/UML%20Diagrams/activitydiag.png" height="770" width="auto">  

- Components
  
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/UML%20Diagrams/componentsdiag.png" height="530" width="auto">

- Classes

<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/UML%20Diagrams/class_diag.png" height="440"> 

## Requirements Engineering
Requirements are mapped using:
1. [Trello](https://trello.com/b/Fu2rZBkf/scraper-analyzer) - Requirements have been mapped using the Kanban method. This board can be accessed via the link.
2. [Jira](https://ipshita.atlassian.net/jira/core/projects/SA/board?atlOrigin=eyJpIjoiYzAxZDY0NmVjODMxNDgxMmI1ZjI5MzUxZWFhMTM1ZWMiLCJwIjoiaiJ9) - Requirements have been mapped using the Kanban method. This board can only be accessed via invite! 

Both Trello and Jira has been used to manage the project's requirements and features and to keep track of pending, ongoing and completed tasks in the following manner-
- Trello 

<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/Requirements%20Engineering/Trello.png" width="740">

- Jira 

<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/Requirements%20Engineering/Jira.png" width="740">


## Analysis Checklist
- [Analysis Checklist for Scraper-Analyzer](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/Project%20Analysis/Analysis%20Checklist_Scraper-Analyzer.pdf)
- [Project Analysis](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/Project%20Analysis/project_analysis.pdf)

## Domain Driven Design (DDD)
[Event storming board](https://lucid.app/lucidchart/5dbdb898-77d6-457c-bb14-c9d824771a51/edit?invitationId=inv_9fef94fb-e800-489e-86cd-dbce4d7ab49c)
Core domains have been encircled and the domain relationships have been mapped out.
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/DDD/DDD.png" height="700">

## Metrics

The code's quality and adherence to coding standards have been evaluated using two tools: **SonarCloud** and **Pylint**.

### SonarCloud Analysis
SonarCloud has been integrated with this repository for continuous inspection of code quality. The analysis includes a range of metrics such as code smells, bugs, security vulnerabilities, and maintainability. 

The SonarCloud dashboards below provides a detailed overview of the project's health, aiding in identifying areas for improvement.

<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/metrics/sonar2.png" width="700">
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/metrics/sonar1.png" width="700">

### Pylint Analysis (Spyder IDE)

The project's codebase is further subjected to code analysis using Pylint, an in-built code analyzer in the Spyder IDE. Pylint assesses the code according Python coding conventions, identifying issues and provides a score based on it.

Note: Unresolved errors are intentional since they don't impact the code's functionality or cannot be feasibly fixed.

- Pylint's score on scraper.py
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/metrics/pylint-scraper.png" width="500">
- Pylint's score on analyzer.py
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/metrics/pylint-analyzer.png" width="500">
- Pylint's score on main.py
<img src="https://raw.githubusercontent.com/IpshitaSingh/scraper-analyzer/main/imgs/metrics/pylint-main.png" width="500">

## Clean Code Development
Points that have contributed in keeping the code clean:
1. **Modularity:**
The code is divided in two parts: Scraper and Analyzer. It is then organized into functions, with each responsible for a specific task (adhering to the "Single Responsibility" principle). This structure makes the code easy to understand, modify, and maintain.

2. **Clear Flow of Execution**
The code follows a clear and logical structure making it easier to modify and extend. It moves from scraping to analysis, starting with fundamental DataFrame operations then progressing to more detailed insights.

3. **Docstrings and Comments:**
Comments and docstrings are used to provide additional context and explanations where necessary.

4. **Descriptive Names:**
Variable and function names are clear and descriptive of their intended behavior. This makes it easy to understand the role of each component in the code.

5. **Consistent Formatting and Syntax:**
Consistent indentation, spacing, and formatting is maintained throughout the project, making the code easier to read and visually clean.  

## Build, CICD, Tests

As this project involves a console output, a seperate Flask project has been developed to implement build management, CI/CD, and testing. Additionally, Docker has been implemented in it for containerization and deployment.
This project can be accessed via this link: [IpshitaSingh/CICD](https://github.com/IpshitaSingh/CICD)
This Flask app demonstrates: 
1. Build management with setuptools(a Python library).
2. CI/CD implementation using GitHub Actions.
3. Unit tests with pytest(a Python testing framework).
3. Containerization with Docker.

All other details are available in the project's [README file](https://github.com/IpshitaSingh/CICD/blob/main/README.md)

## IDE

The integrated development environment (IDE) used for the development of this project is **Visual Studio Code**.
### Favorite Feature:
Git Integration: VSC's integration with Git, including staging, committing, and pushing changes, makes version control straightforward and extremely convenient. Also, having a visual indicator to promptly check the current branch is both helpful and time-saving.

### Favourite Shortcuts:
**General:**
1. Indent and Unindent: Tab to indent, Shift + Tab to unindent.
2. Comment Out Multiple Lines: Ctrl + /
3. Open Terminal: Ctrl + ` (Backtick)

**Git-Specific:**
1. Open the source control view: Ctrl + Shift + G
2. Stage changes: Ctrl + Enter
3. Commit staged changes: Ctrl + Alt + Enter
4. Pull or push changes: Type "Git: Pull" or "Git: Push" in terminal

## Functional Programming

The project demonstrates the use of final data structures, side-effect-free functions, the use of higher-order functions, functions as parameters and return values, and closure/anonymous function.

Here's how these requirements are met:

1. **Final Data Structures:**
   - The primary data structure used in this oroject is the Pandas DataFrame called `data_frame` (created from scraped data in the [Scraper file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/scraper.py) and later renamed `df` for use in the [Main file.](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/main.py)). `data_frame` or `df` is a final data structure containing the data for analysis and visualization.

2. **Side-Effect-Free Functions:**
   - The functions `get_soup()`, `extract_country_data()`, and `create_df()` from the [Scraper file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/scraper.py) and `check_missing_values()`, `explore_data()`, and `visualize_data()` from the [Analyzer file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/analyzer.py) do not have any side effects. They take input parameters, perform operations based on the input, and return results without modifying external state.

3. **Use of Higher-Order Functions:**
   - Each function in [Analyzer file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/analyzer.py) (i.e, `check_missing_values()`, `explore_data()`, and `visualize_data()`) takes `data_frame` as an input which is defined as:
      ```
      data_frame = create_df(url).
      ```
     in [Scraper file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/scraper.py). This reflects the higher-order function concept, where functions are either passed as arguments or returned.
    - `data_analysis()` function in the [Main file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/main.py) also takes a renamed version of `data_frame`, which is `df`,  as parameter.
      ```
      df = scraper.data_frame
      ```

5. **Functions as Parameters and Return Values:**
   - `check_missing_values()` function in [Analyzer file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/analyzer.py) takes data_frame (_defined above_) as parameter  and returns a boolean value:

            - True if there are missing values in the DataFrame along with the count of missing values.

            - False if there are no missing values in the DataFrame and it prints a message indicating this.
   - `data_analysis` function in [Main file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/main.py) takes a renamed version of data_frame as parameter, which is `df`, (_defined above_) and returns three functions (`check_missing_values()`, `explore_data()`, `visualize_data()`) with each giving an output accordingly. 

6. **Use of Closures/Anonymous Functions:**
   - `explore_data()` in [Analyzer file](https://github.com/IpshitaSingh/scraper-analyzer/blob/main/analyzer.py) uses lambda function, which is an anonymous function, to format the display of numbers. It takes a floating-point number, `x`, as input and formats it as a string with two decimal places `:.2f` -
   ```
    pd.set_option('display.float_format', lambda x: f'{x:.2f}')
   ```

