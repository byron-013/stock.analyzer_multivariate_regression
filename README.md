# stock.analyzer_multivariate_regression

# About the Project - What it does.
This project consists of a python program that analyzes and helps interperet economic/financial data in order to indentify trends, forecast prices, etc.

Several economic indicators (risk free rates, unemployment rates, etc) are provided in economic_data.csv so that the conditions of the economy can be taken into account when looking at company financials.

The program cleans the data and formats it so that no issues arise from missing values. Outliers are taken care of, and the different financial/economic data files are made to to be covering the same (user defined) date range for a provided frequency (daily, weekly, or monthly). 

Once the data cleaning and processing is done you are left with a single csv file where all of the data is merged into once csv file while still being accurately organized by date. The process also ensures that all columns (each col corresponds to a variable) have the same number of row entries so that the regressions can be run.

The program allows the user to choose which variables to use in a multivariable linear regression. 

After that the program splits the selected variable data into two data sets: train and test.

Then, using the train data, it performs several diagnostic tests to identify if some variables need to be removed due to dependence or multicollinearity. 
It also conducts tests for heteroskedasticity and allows for the user to change error type in order to get more accurate results when working with heteroskedastic data

The program offers the option to remove variables and provides guidance on how to transform the data to use a variable with multicollinearity or heteroskedasticity. It will also test the normallity of the error terms to make sure a linear model is viable for the selected variables.


In the final step, the program performs the regression on the test data set. With your choice of variables and error type (after performing transformations if needed), it will perform the regression and print the OLS results summary. If you specify a robust error type it will also print the corresponding results summary for that error type after providing the nonrobust summary.


All test results come with explanations. Whenever an OLS summary is printed or a diagnostic test is ran, a paragraph is also generated containing the real world/statistical implications of the values are.



# Data Science Skills Used in this Project

Data gathering, preprocessing, and transformation.


# About the Author

Byron Delaney Jr - Berkeley Applied Mathematics 

Contact Information: byron13@berkeley.edu

LinkedIn: www.linkedin.com/in/byron13
