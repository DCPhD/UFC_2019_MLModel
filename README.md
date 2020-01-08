# UFC_2019_MLModel
Results from all fights in 2019 were scraped from http://www.ufcstats.com/statistics/events/completed

smallUFCdataset csv file contains the final cleaned dataset with 3 predictors: Strikes, Takedown attempts, Submission attempts, 
along with the target variable of win/loss (1/0)

sherdog.py file contains all code for webscraping and cleaning dataset

UFC_MLmodel.py file contains code for 3 different ML models applied to dataset

Results of ML models- best prediction performance was approximately 0.60, indicating too few datapoints or not enough predictors
