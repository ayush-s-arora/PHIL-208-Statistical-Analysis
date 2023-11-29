# BEFORE starting, we will set our significance level to 0.05!
# Null Hypothesis 1: There is not a statistically significant difference between the LLM "Job Trustworthiness" Scores for all applicants with good credit reports
# Null Hypothesis 2: There is not a statistically significant difference between the LLM "Job Trustworthiness" Scores for all applicants with bad credit reports
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

# Dfs with only good credit report data
dfGPT35Good = dfGPT35[dfGPT35['Prompt'] == 'promptgood']
dfGPT4Good = dfGPT4[dfGPT4['Prompt'] == 'promptgood']
dfBardGood = dfBard[dfBard['Prompt'] == 'promptgood']
dfBingChatGood = dfBingChat[dfBingChat['Prompt'] == 'promptgood']

# Dfs with only Job Trustworthiness scores for good credit reports
dfGPT35GoodScores = dfGPT35Good.iloc[:,4]
dfGPT4GoodScores = dfGPT4Good.iloc[:,4]
dfBardGoodScores = dfBardGood.iloc[:,4]
dfBingChatGoodScores = dfBingChatGood.iloc[:,4]

# Bartlett's Test for Equal Variances - same 0.05 significance level. Results printed to text file
with open("All LLMs Good Reports - Bartlett's Test for Equal Variances.txt", "a") as f:
    print(stats.bartlett(dfGPT35GoodScores, dfGPT4GoodScores, dfBardGoodScores, dfBingChatGoodScores), file = f)

# ANOVA, results printed to text file
with open("All LLMs Good Reports - ANOVA Hypothesis Test Results.txt", "a") as f:
    print(stats.f_oneway(dfGPT35GoodScores, dfGPT4GoodScores, dfBardGoodScores, dfBingChatGoodScores), file = f)


# Dfs with only bad credit report data
dfGPT35Bad = dfGPT35[dfGPT35['Prompt'] == 'promptbad']
dfGPT4Bad = dfGPT4[dfGPT4['Prompt'] == 'promptbad']
dfBardBad = dfBard[dfBard['Prompt'] == 'promptbad']
dfBingChatBad = dfBingChat[dfBingChat['Prompt'] == 'promptbad']

# Dfs with only Job Trustworthiness scores for good credit reports
dfGPT35BadScores = dfGPT35Bad.iloc[:,4]
dfGPT4BadScores = dfGPT4Bad.iloc[:,4]
dfBardBadScores = dfBardBad.iloc[:,4]
dfBingChatBadScores = dfBingChatBad.iloc[:,4]

# Bartlett's Test for Equal Variances - same 0.05 significance level. Results printed to text file
with open("All LLMs Bad Reports - Bartlett's Test for Equal Variances.txt", "a") as f:
    print(stats.bartlett(dfGPT35BadScores, dfGPT4BadScores, dfBardBadScores, dfBingChatBadScores), file = f)

# ANOVA, results printed to text file
with open("All LLMs Bad Reports - ANOVA Hypothesis Test Results.txt", "a") as f:
    print(stats.f_oneway(dfGPT35BadScores, dfGPT4BadScores, dfBardBadScores, dfBingChatBadScores), file = f)