import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.tsa.api as smt
import statsmodels.api as sm



def tsplot(y: pd.Series, 
           lags: int = None, 
           figsize: tuple =(12, 7), 
           style='bmh'):
    '''
    The code was taken from https://habr.com/ru/company/ods/blog/327242/
    
    The function is intended for visualization of time series, ACF, PACF.
    Additionally, the Dickey-Fuller test is calculated.
    Args:
        y - variable
        lags - the number of lags of the variable for calculating ACF/PACF
        figsize: the size of the graph
        style - style of graph
    '''
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):    
        fig = plt.figure(figsize=figsize)
        layout = (2, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))

        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.5)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.5)

        print("Dickey-Fuller criteria: p=%f" % sm.tsa.stattools.adfuller(y)[1])

        plt.tight_layout()



def invboxcox(y: pd.Series, lmbda: np.float64) -> pd.Series:
    '''inverse Box-Cox transform
    
    Args:
        y - transformed series
        lmbda - box-cox lambda
    Returns:
        reversed transformed series
    '''
    
    if lmbda == 0:
        return(np.exp(y))
    else:
        return(np.exp(np.log(lmbda*y+1)/lmbda))
    
    
def percentage_error(actual: pd.Series, predicted: pd.Series) -> np.array:
    '''
    The function is designed to calculate the relative error
    Args:
        actual - actual values
        predicted - predicted values
        
    Returns:
        res - calculated array of relative erroes
    
    '''
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def mean_absolute_percentage_error(actual: pd.Series, predicted: pd.Series) -> np.float64: 
    '''
    The function is designed to calculate MAPE 
    Args:
        actual - actual values
        predicted - predicted values
        
    Returns:
        MAPE - mean average percentage_error
    '''
    return np.mean(np.abs(percentage_error(np.asarray(actual), np.asarray(predicted)))) * 100