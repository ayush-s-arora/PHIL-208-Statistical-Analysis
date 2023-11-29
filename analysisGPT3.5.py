import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Import raw data from ChatGPT 3.5 as a dataframe
df = pd.read_csv('dataGPT3.5.csv')

# Separate df into two dataframes - one for good credit report prompts, one for bad credit report prompts
dfGood = df[df['Prompt'] == 'promptgood']
dfBad = df[df['Prompt'] == 'promptbad']

# Further separate those dfs into Score-only dfs
dfGoodScores = dfGood.iloc[:,4]
dfBadScores = dfBad.iloc[:,4]

# Descriptive Statistics for Scores from Good Credit Report Prompts
goodDescriptiveStats = dfGoodScores.describe()
# Descriptive Statistics for Scores (only numeric data in df) from Bad Credit Report Prompts
badDescriptiveStats = dfBadScores.describe()

# Round Descriptive Statistics to 2 decimal places (for readability & analytical relevance)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Inferential Statistics
# Grouped Bar Chart Comparison between Good Credit Report Scores for 18 y/o Applicants

# Create dataframe for Good 18 y/o applicants
df18Good = dfGood[dfGood['Age'] == 'A']

# Create dataframes for Good 18 y/o applicants based on ethnicity
x = np.arange(2)
df18GoodBlack = df18Good[df18Good['Ethnicity'] == 'A']
df18GoodAsian = df18Good[df18Good['Ethnicity'] == 'B']
df18GoodHLx = df18Good[df18Good['Ethnicity'] == 'C']
df18GoodMENA = df18Good[df18Good['Ethnicity'] == 'D']
df18GoodWhite = df18Good[df18Good['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, goodYoungBarChart = plt.subplots()

goodYoungBarChart.bar(x-0.2, df18GoodBlack['Score'].values.tolist(), width, label = 'Black')
goodYoungBarChart.bar(x, df18GoodAsian['Score'].values.tolist(), width, label = 'Asian')
goodYoungBarChart.bar(x+0.2, df18GoodHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
goodYoungBarChart.bar(x+0.4, df18GoodMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
goodYoungBarChart.bar(x+0.6, df18GoodWhite['Score'].values.tolist(), width, label = 'White')
goodYoungBarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
goodYoungBarChart.set_title('Assigned "Job Trustworthiness" Scores for Young (18 y/o) Applicants')
goodYoungBarChart.set_xticks(x, ['Male', 'Female'])
goodYoungBarChart.set_ylim(0, 100)
goodYoungBarChart.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()