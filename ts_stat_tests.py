from scipy import stats
import numpy as np
import statsmodels.api as sm

from statsmodels.tsa.stattools import adfuller

def ks_2s_test(a: float, f: np.array, g: np.array, alt = 'two-sided'):   
    '''
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html
    
    This function performs the two-sample Kolmogorov-Smirnov test for goodness of fit. 
    This test compares the underlying continuous distributions F(x) and G(x) of two independent samples. 
    
    Args:
        a - chosen significance level 
        f - first continuous distribution 
        g - second continuous distribution
        alt - defines the null and alternative hypotheses. Default is 'two-sided', others are 'less', 'greater'
    Returns:
        D - Kolmogorov-Smirnov statistic
        p - one-tailed or two-tailed p-value
        cv - crtitical value of D for given level of significance and sample sizes
    
    '''
    res = stats.ks_2samp(f, g, alternative= alt)
    D = res[0]
    p = res[1]
    n = np.shape(f)[0]
    m = np.shape(g)[0]
    cv = np.sqrt(-0.5*np.log(a/2)*(n+m)/(n*m))
    if D > cv:
        print(f"Null hypothesis is rejected with D={D}, p={p} for a={a}")
        print(f"The distributions differ")
    else:
        print(f"Null hypothesis is not rejected with D={D}, p={p} for a={a}")
        print(f"The distributions are similar")
    return D, p, cv 


def ljungboxtest(a: float, f: np.array, lag = 1):   
    '''
    https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.acorr_ljungbox.html
    
    This function performs the Ljung-Box test of autocorrelation in residuals.  
    
    Args:
        a - chosen significance level    
        f - continuous distribution
        lag - if lags is an integer then this is taken to be the largest lag that is included, 
            the test result is reported for all smaller lag length. If lags is a list or array, 
            then all lags are included up to the largest lag in the list, 
            however only the tests for the lags in the list are reported. 
            If lags is None, then the default maxlag is currently min((nobs // 2 - 2), 40). 
            After 0.12 this will change to min(10, nobs // 5).
    Returns:
        lbvalue - The Ljung-Box test statistic
        p - The p-value based on chi-square distribution

    '''
    result = sm.stats.acorr_ljungbox(f, lags = [lag], return_df=False)
    lbvalue = float(result[0])
    p = float(result[1])
    if p < a:
        print(f"Null hypothesis is rejected with Ljung-Box test statistic = {lbvalue}, p = {p} for a = {a}") 
        print(f"There is a autocorrelation in residuals")
    else:
        print(f"Null hypothesis is not rejected with Ljung-Box test statistic = {lbvalue}, p = {p} for a = {a}")
        print(f"There is no autocorrelation in residuals")
    return lbvalue, p

