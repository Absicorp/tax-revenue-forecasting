# Tax revenue forecasting

The materials in this repository are companion pieces to an article describing the predictive models for tax revenue forecasting based on official tax data from kgd.gov.kz. 

 
## Table of contents
- [Authors](#authors)
- [Requirements](#Requirements)
- [Documentation](#documentation)
- [Research results](#results)
  
## Authors
[**Vladimir Kolesnikov** — Senior Data Scientist at Sber](https://www.linkedin.com/in/kolesnikovvladimir/) 

[**Abylaykhan Yergesh** — Junior Data Scientist at Sber](https://www.linkedin.com/in/yergeshabylaykhan/) 

[**Valeriya Rudikova** — Junior Data Scientist at Sber](https://www.linkedin.com/in/valeriya-rudikova-49874b158/) 


## Requirements
Python 3.8 version or above

silverkyte==0.2.0

fbprophet==0.1.0

Other installation options are described in the [documentation](https://pystan2.readthedocs.io/en/latest/windows.html).

## Documentation
The full documentation for silverkite available at **[https://github.com/linkedin/greykite](https://github.com/linkedin/greykite)**.


The full documentation for fbprophet available at **[https://github.com/facebook/prophet](https://github.com/facebook/prophet)**.


## results

![results](https://github.com/Absicorp/tax-revenue-forecasting/blob/main/images/result.png)

| model name  | MAPE | R2 | q_test(a=0.05) | q_test_pvalue |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| arima  | 7,859  | 0,934  | 0,007  | 0,93  |
| fbprophet  | 5,668  | 0,953  | 1,21  | 0,269  |
| silverkite  | 3,958  | 0,984  | 0,095  | 0,756  |

