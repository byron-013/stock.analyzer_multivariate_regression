import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler, PowerTransformer

def log_transform(data, column):
    data[column] = np.log(data[column])
def sqrt_transform(data, column):
    data[column] = np.sqrt(data[column])
def cube_root_transform(data, column):
    data[column] = np.cbrt(data[column])
def polynomial_transform(data, column, degree):
    data[column] = data[column] ** degree
def standardize(data, column):
    scaler = StandardScaler()
    data[column] = scaler.fit_transform(data[[column]])
def center(data, column):
    mean = data[column].mean()
    data[column] = data[column] - mean
def box_cox_transform(data, column):
    data[column], _ = stats.boxcox(data[column])
def yeo_johnson_transform(data, column):
    pt = PowerTransformer(method='yeo-johnson')
    data[column] = pt.fit_transform(data[[column]])



    # Provide recommendations based on the summary: 
    ### F STATISTIC If the F-statistic is not significant, consider applying a logarithmic transformation to your dependent variable. This can help with non-linearity and heteroscedasticity.
    ### DURBIN WATSON: If the Durbin-Watson statistic indicates autocorrelation, consider applying a square root transformation to your independent variables. This can help stabilize variance.
    ### JB TEST: If the Jarque-Bera test indicates non-normality, consider applying a square transformation to your dependent variable. This can help achieve normality.
    ### SKEW: If the data is skewed, consider applying a cube root or Yeo-Johnson transformation. These can help reduce skewness.
    ### CONDITION NUMBER: If the condition number is high, indicating potential multicollinearity, consider centering your variables by subtracting the mean or standardizing them. This can help mitigate multicollinearity.
    ### OMNIBUS: If the Omnibus test indicates non-normality, consider applying a Box-Cox transformation. This can help achieve normality.
        