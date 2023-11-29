# BEFORE starting, we will set our significance level to 0.05!
# Null Hypothesis: There is not a statistically significant difference between the LLM "Job Trustworthiness" Scores for all applicants
# Conditions of independence and normality are met (CLT), will check equal variance with Bartlett's Test

import numpy as np
from scipy.stats import f_oneway
import pandas as pd
import scipy.stats as stats

# Import raw data from each LLM as a unique dataframe
dfGPT35 = pd.read_csv('dataGPT3.5.csv')
dfGPT4 = pd.read_csv('dataGPT4.csv')
dfBard = pd.read_csv('dataBard.csv')
dfBingChat = pd.read_csv('dataBingChat.csv')

# Dfs with only Job Trustworthiness scores
dfGPT35Scores = dfGPT35.iloc[:,4]
dfGPT4Scores = dfGPT4.iloc[:,4]
dfBardScores = dfBard.iloc[:,4]
dfBingChatScores = dfBingChat.iloc[:,4]

# Bartlett's Test for Equal Variance - same 0.05 significance level. Results printed to text file
with open("All LLMs - Bartlett's Test for Equal Variance", "a") as f:
    print(stats.bartlett(dfGPT35Scores, dfGPT4Scores, dfBardScores, dfBingChatScores), file = f)

# ANOVA, results printed to text file
with open("All LLMs - ANOVA Hypothesis Test Results.txt", "a") as f:
    print(stats.f_oneway(dfGPT35Scores, dfGPT4Scores, dfBardScores, dfBingChatScores), file = f)