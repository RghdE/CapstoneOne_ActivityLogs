<a name="readme-top"></a>

# :moneybag: FinTech Project
As part of the Big Data and AI Engineering Onsite Bootcamp, we are asked to deliver a solution for the Saudi market that can be solved by data science. The project has to have an impact and deliver a solution for a real-world problem using Saudi datasets. 

![logo_](https://user-images.githubusercontent.com/53378171/209428414-2b342d92-1ec1-47b8-a527-e9deb0bc1600.png)


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#project-overview">Project Overview</a></li>
    <li>
    <a href="#business-objective">Business Objective</a>
      <ul>
        <li><a href="#methods-used">Methods Used</a></li>
        <li><a href="#technologies">Technologies</a></li>
      </ul>
    </li>
    <li><a href="#dataset-overview">Dataset Overview</a></li>
    <li><a href="#preprocessing-overview">Preprocessing Overview</a></li>
    <li><a href="#visualization">Visualization</a></li>
    <li><a href="#modeling-results">Modeling Results</a></li>
    <li><a href="#contributing-members-contact">Contributing Members Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

##
## Project Overview

This is the overview of the project's structure and files for easier navigation. However, some notebooks and datasets cannot be uploaded either to ensure the company's confidentiality or due to size limits:

```
├── README.md
├── CapestoneProject_Dashboard_Desert_Ninjas.pdf
├── CapstoneProject_Presentation_Desert_Ninjas.pdf
├── Notebooks
│   ├── CapstoneProject_Pre_Preprocessing_Notebook_ComanyNameEncryption.ipynb 
|   ├── CapstoneProject_Preprocessing_Notebook_Desert_Ninjas.ipynb
│   ├── CapstoneProject_EDA_Notebook_Desert_Ninjas.ipynb
│   └── CapstoneProject_ML_Notebook_Desert_Ninjas.ipynb
└── Datasets
    ├── Encrypted_full_dataset.csv (output of the pre-preprocessing notebook) 
    ├── Encrypted_exported_raw_data.csv (output of the pre-preprocessing notebook) 
    ├── Preprocessed_full_dataset.csv (output of the preprocessing notebook) 
    └── Final_extracted_dataset.csv (used for the EDA, Dashboard, and Machine Learning models)
```

**Note: As a beginning, we were provided with two datasets that contain different schemas (Encrypted_full_dataset + Encrypted_exported_raw_data)**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Business Objective
The purpose of this project is to predict potential customers for a FinTech startup company using their visitor's activity logs. Those potential investors would then be targeted with marketing strategies.


### Methods Used
* Preprocessing raw data
* Feature Engineering
* Feature Selection
* Labeling and classifying the data
* Exploratory Data Analysis
* Data Visualization
* Machine Learning
* Oversampling

### Technologies
* Python, Jupyter
* Pandas
* Plotly
* Sklearn
* Imbalanced-learn
* Power BI

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Dataset Overview
A startup FinTech company named X is interested in knowing its customers’ behaviors and whether they’re going to invest based on their activity logs. However, the problem has challenges because we don't have the following to support our analysis:
- The number of visitors to the website
- The demographics of these visitors

The analysis will help the company create a new marketing strategy for attracting more customers, increasing its revenues, and learning the patterns of customers who reach the investment pages but do not commit to the full transaction. Lucky for the FinTech company, we say, challenge accepted! 

At the beginning of our analysis, we raised some questions that we intend to answer using our EDA, dashboard visualization, and modeling. The questions are:
1. What kind of data does their website collect from users? 
2. What is the path that gets visited by users usually? And how much time do users spend on this path?
3. Does the average time spent on a page differ based on the user type? 
4. Which path has the maximum time? Is this the path that leads to a successful transaction (investment)?
We hope to answer all of these questions in our analysis.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Preprocessing Overview 

Preprocessing is the essence of this project. In this README file, we will be listing the overview of each step. However, for a more detailed description, visit our [Medium Blog Post](https://medium.com/@RghdE/investments-analysis-dataset-predicting-customer-investment-based-on-visitors-activity-logs-using-b725ad1fa559). 

The dataset before and after the preprocessing:

![image](https://user-images.githubusercontent.com/53378171/209435148-8574304c-aa53-469b-9680-2e3aeea82cfc.png)

Preprocessing steps:

<img width="697" alt="prep1" src="https://user-images.githubusercontent.com/53378171/209435195-09483cb3-2abf-41f5-a907-dfe9f1a0e156.png">

Feature engineering steps:

<img width="671" alt="feateng" src="https://user-images.githubusercontent.com/53378171/209435395-bc77cd67-b9d4-462c-9533-fd18059200c6.png">

Features *before* removing data leakage:

<img width="414" alt="fs1" src="https://user-images.githubusercontent.com/53378171/209435463-dc8ad774-aa72-4e0d-9641-c26cbbb2a9b2.png">

Selecting the features *after* removing the data leakage:

<img width="418" alt="fs2" src="https://user-images.githubusercontent.com/53378171/209435583-ffc8e29b-fcd9-490f-be4f-718ee4f43818.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Visualization

Based on our [EDA](https://medium.com/@RghdE/investments-analysis-dataset-predicting-customer-investment-based-on-visitors-activity-logs-using-b725ad1fa559), we found that 80% of our users are regular visitors, while only 17% are investors, thus, we wanted to create two dashboards for these two user types.

Visitors dashboard:

<img width="718" alt="dash1" src="https://user-images.githubusercontent.com/53378171/209436098-559d6bbc-ae15-47ce-96ba-596542ee5aee.png">

Investors dashboard:

<img width="721" alt="dash2" src="https://user-images.githubusercontent.com/53378171/209436094-128b4d7e-085c-4dfd-aad2-255aa83dc4d7.png">

As mentioned above, you can visit [our web blog](https://medium.com/@RghdE/investments-analysis-dataset-predicting-customer-investment-based-on-visitors-activity-logs-using-b725ad1fa559) for a detailed analysis of the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Modeling Results

All of these models were evaluted in order to choose the best one of them.

![image](https://user-images.githubusercontent.com/53378171/209435933-f479b325-5cd1-4d09-afa4-370da91a68fb.png)

However, in our criteria, since our dataset is imbalanced, we will take recall as our evaluation metric. Also, we want to focus on identifying the potential customers class, so, we took the best model in identifying this class as compared to our baseline; which is XGBoost. 

XGBoost results:

![image](https://user-images.githubusercontent.com/53378171/209436015-7bbad509-17d0-4d23-b61b-2421513d9dd1.png)

Baseline Distribution:

![image](https://user-images.githubusercontent.com/53378171/209436053-2edd3534-cad2-474a-9fe9-7390062618c2.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing Members Contact

**Team Leadear: Reema Alaswad** ([Reema's LinkedIn](https://www.linkedin.com/in/reema-alaswad-2002a3188/))

#### Other Members:

|Name     |  LinkedIn   | 
|---------|-----------------|
| Raghad Aleisa | [Raghad's LinkedIn](https://www.linkedin.com/in/rghde)  |
| AlJohara Alkanhal | [AlJohara's LinkedIn](https://www.linkedin.com/in/joharaalkanhal/) |
| Maha AlHazzani | [Maha's LinkedIn](https://www.linkedin.com/in/mahazzani/)  |
| Eman Aldosari | [Eman's LinkedIn](https://www.linkedin.com/in/eman-aldosari-51215a204/)  |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments
* [Readme Template 1](https://github.com/sfbrigade/data-science-wg/blob/master/dswg_project_resources/Project-README-template.md)
* [Readme Template 2](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
