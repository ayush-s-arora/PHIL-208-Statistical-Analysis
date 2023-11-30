import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import table

largeLanguageModel = 'Bard'

# Import raw data from Large Language Model as a dataframe
df = pd.read_csv('dataBard.csv')

# Separate df into two dataframes - one for good credit report prompts, one for bad credit report prompts
dfGood = df[df['Prompt'] == 'promptgood']
dfBad = df[df['Prompt'] == 'promptbad']

# Further separate those dfs into Score-only dfs
dfGoodScores = dfGood.iloc[:,4]
dfBadScores = dfBad.iloc[:,4]

# Descriptive Statistics for Scores from Good & Bad Credit Report Prompts
goodDescriptiveStats = dfGoodScores.describe()
badDescriptiveStats = dfBadScores.describe()

# Save good descriptive stats as table PNG
statsView = plt.subplot(111, frame_on=False)
statsView.xaxis.set_visible(False) 
statsView.yaxis.set_visible(False) 
table(statsView, goodDescriptiveStats, loc='upper right')
plt.savefig(largeLanguageModel + ' goodDescriptiveStats.png')

# Save bad descriptive stats as table PNG
statsView = plt.subplot(111, frame_on=False)
statsView.xaxis.set_visible(False) 
statsView.yaxis.set_visible(False) 
table(statsView, badDescriptiveStats, loc='upper right')
plt.savefig(largeLanguageModel + ' badDescriptiveStats.png')

# Inferential Statistics for Good Credit Report Scores
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
fig, good18BarChart = plt.subplots()

barsBlack = good18BarChart.bar(x-2*width, df18GoodBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = good18BarChart.bar(x-width, df18GoodAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = good18BarChart.bar(x, df18GoodHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = good18BarChart.bar(x+width, df18GoodMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = good18BarChart.bar(x+2*width, df18GoodWhite['Score'].values.tolist(), width, label = 'White')
good18BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
good18BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 18 y/o Applicants with Good Credit Reports')
good18BarChart.set_xticks(x, ['Male', 'Female'])
good18BarChart.set_ylim(0, 100)
good18BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        good18BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Grouped Bar Chart Comparison between Good Credit Report Scores for 20 y/o Applicants

# Create dataframe for Good 20 y/o applicants
df20Good = dfGood[dfGood['Age'] == 'B']
# Create dataframes for Good 20 y/o applicants based on ethnicity
x = np.arange(2)
df20GoodBlack = df20Good[df20Good['Ethnicity'] == 'A']
df20GoodAsian = df20Good[df20Good['Ethnicity'] == 'B']
df20GoodHLx = df20Good[df20Good['Ethnicity'] == 'C']
df20GoodMENA = df20Good[df20Good['Ethnicity'] == 'D']
df20GoodWhite = df20Good[df20Good['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, good20BarChart = plt.subplots()

barsBlack = good20BarChart.bar(x-2*width, df20GoodBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = good20BarChart.bar(x-width, df20GoodAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = good20BarChart.bar(x, df20GoodHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = good20BarChart.bar(x+width, df20GoodMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = good20BarChart.bar(x+2*width, df20GoodWhite['Score'].values.tolist(), width, label = 'White')
good20BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
good20BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 20 y/o Applicants with Good Credit Reports')
good20BarChart.set_xticks(x, ['Male', 'Female'])
good20BarChart.set_ylim(0, 100)
good20BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        good20BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Grouped Bar Chart Comparison between Good Credit Report Scores for 30 y/o Applicants

# Create dataframe for Good 30 y/o applicants
df30Good = dfGood[dfGood['Age'] == 'C']
# Create dataframes for Good 20 y/o applicants based on ethnicity
x = np.arange(2)
df30GoodBlack = df30Good[df30Good['Ethnicity'] == 'A']
df30GoodAsian = df30Good[df30Good['Ethnicity'] == 'B']
df30GoodHLx = df30Good[df30Good['Ethnicity'] == 'C']
df30GoodMENA = df30Good[df30Good['Ethnicity'] == 'D']
df30GoodWhite = df30Good[df30Good['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, good30BarChart = plt.subplots()

barsBlack = good30BarChart.bar(x-2*width, df30GoodBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = good30BarChart.bar(x-width, df30GoodAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = good30BarChart.bar(x, df30GoodHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = good30BarChart.bar(x+width, df30GoodMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = good30BarChart.bar(x+2*width, df30GoodWhite['Score'].values.tolist(), width, label = 'White')
good30BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
good30BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 30 y/o Applicants with Good Credit Reports')
good30BarChart.set_xticks(x, ['Male', 'Female'])
good30BarChart.set_ylim(0, 100)
good30BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        good30BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Grouped Bar Chart Comparison between Good Credit Report Scores for 40 y/o Applicants

# Create dataframe for Good 40 y/o applicants
df40Good = dfGood[dfGood['Age'] == 'D']
# Create dataframes for Good 20 y/o applicants based on ethnicity
x = np.arange(2)
df40GoodBlack = df40Good[df40Good['Ethnicity'] == 'A']
df40GoodAsian = df40Good[df40Good['Ethnicity'] == 'B']
df40GoodHLx = df40Good[df40Good['Ethnicity'] == 'C']
df40GoodMENA = df40Good[df40Good['Ethnicity'] == 'D']
df40GoodWhite = df40Good[df40Good['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, good40BarChart = plt.subplots()

barsBlack = good40BarChart.bar(x-2*width, df40GoodBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = good40BarChart.bar(x-width, df40GoodAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = good40BarChart.bar(x, df40GoodHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = good40BarChart.bar(x+width, df40GoodMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = good40BarChart.bar(x+2*width, df40GoodWhite['Score'].values.tolist(), width, label = 'White')
good40BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
good40BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 40 y/o Applicants with Good Credit Reports')
good40BarChart.set_xticks(x, ['Male', 'Female'])
good40BarChart.set_ylim(0, 100)
good40BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        good40BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Grouped Bar Chart Comparison between Good Credit Report Scores for 50 y/o Applicants

# Create dataframe for Good 50 y/o applicants
df50Good = dfGood[dfGood['Age'] == 'E']
# Create dataframes for Good 20 y/o applicants based on ethnicity
x = np.arange(2)
df50GoodBlack = df50Good[df50Good['Ethnicity'] == 'A']
df50GoodAsian = df50Good[df50Good['Ethnicity'] == 'B']
df50GoodHLx = df50Good[df50Good['Ethnicity'] == 'C']
df50GoodMENA = df50Good[df50Good['Ethnicity'] == 'D']
df50GoodWhite = df50Good[df50Good['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, good50BarChart = plt.subplots()

barsBlack = good50BarChart.bar(x-2*width, df50GoodBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = good50BarChart.bar(x-width, df50GoodAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = good50BarChart.bar(x, df50GoodHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = good50BarChart.bar(x+width, df50GoodMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = good50BarChart.bar(x+2*width, df50GoodWhite['Score'].values.tolist(), width, label = 'White')
good50BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
good50BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 50 y/o Applicants with Good Credit Reports')
good50BarChart.set_xticks(x, ['Male', 'Female'])
good50BarChart.set_ylim(0, 100)
good50BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        good50BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()






# Inferential Statistics for Bad Credit Report Scores
# Grouped Bar Chart Comparison between Bad Credit Report Scores for 18 y/o Applicants

# Create dataframe for Bad 18 y/o applicants
df18Bad = dfBad[dfBad['Age'] == 'A']

# Create dataframes for Bad 18 y/o applicants based on ethnicity
x = np.arange(2)
df18BadBlack = df18Bad[df18Bad['Ethnicity'] == 'A']
df18BadAsian = df18Bad[df18Bad['Ethnicity'] == 'B']
df18BadHLx = df18Bad[df18Bad['Ethnicity'] == 'C']
df18BadMENA = df18Bad[df18Bad['Ethnicity'] == 'D']
df18BadWhite = df18Bad[df18Bad['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, bad18BarChart = plt.subplots()

barsBlack = bad18BarChart.bar(x-2*width, df18BadBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = bad18BarChart.bar(x-width, df18BadAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = bad18BarChart.bar(x, df18BadHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = bad18BarChart.bar(x+width, df18BadMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = bad18BarChart.bar(x+2*width, df18BadWhite['Score'].values.tolist(), width, label = 'White')
bad18BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
bad18BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 18 y/o Applicants with Bad Credit Reports')
bad18BarChart.set_xticks(x, ['Male', 'Female'])
bad18BarChart.set_ylim(0, 100)
bad18BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        bad18BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Create dataframe for Bad 20 y/o applicants
df20Bad = dfBad[dfBad['Age'] == 'B']

# Create dataframes for Bad 20 y/o applicants based on ethnicity
x = np.arange(2)
df20BadBlack = df20Bad[df20Bad['Ethnicity'] == 'A']
df20BadAsian = df20Bad[df20Bad['Ethnicity'] == 'B']
df20BadHLx = df20Bad[df20Bad['Ethnicity'] == 'C']
df20BadMENA = df20Bad[df20Bad['Ethnicity'] == 'D']
df20BadWhite = df20Bad[df20Bad['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, bad20BarChart = plt.subplots()

barsBlack = bad20BarChart.bar(x-2*width, df20BadBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = bad20BarChart.bar(x-width, df20BadAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = bad20BarChart.bar(x, df20BadHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = bad20BarChart.bar(x+width, df20BadMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = bad20BarChart.bar(x+2*width, df20BadWhite['Score'].values.tolist(), width, label = 'White')
bad20BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
bad20BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 20 y/o Applicants with Bad Credit Reports')
bad20BarChart.set_xticks(x, ['Male', 'Female'])
bad20BarChart.set_ylim(0, 100)
bad20BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        bad20BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Create dataframe for Bad 30 y/o applicants
df30Bad = dfBad[dfBad['Age'] == 'C']

# Create dataframes for Bad 30 y/o applicants based on ethnicity
x = np.arange(2)
df30BadBlack = df30Bad[df30Bad['Ethnicity'] == 'A']
df30BadAsian = df30Bad[df30Bad['Ethnicity'] == 'B']
df30BadHLx = df30Bad[df30Bad['Ethnicity'] == 'C']
df30BadMENA = df30Bad[df30Bad['Ethnicity'] == 'D']
df30BadWhite = df30Bad[df30Bad['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, bad30BarChart = plt.subplots()

barsBlack = bad30BarChart.bar(x-2*width, df30BadBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = bad30BarChart.bar(x-width, df30BadAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = bad30BarChart.bar(x, df30BadHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = bad30BarChart.bar(x+width, df30BadMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = bad30BarChart.bar(x+2*width, df30BadWhite['Score'].values.tolist(), width, label = 'White')
bad30BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
bad30BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 30 y/o Applicants with Bad Credit Reports')
bad30BarChart.set_xticks(x, ['Male', 'Female'])
bad30BarChart.set_ylim(0, 100)
bad30BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        bad30BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Create dataframe for Bad 40 y/o applicants
df40Bad = dfBad[dfBad['Age'] == 'D']

# Create dataframes for Bad 40 y/o applicants based on ethnicity
x = np.arange(2)
df40BadBlack = df40Bad[df40Bad['Ethnicity'] == 'A']
df40BadAsian = df40Bad[df40Bad['Ethnicity'] == 'B']
df40BadHLx = df40Bad[df40Bad['Ethnicity'] == 'C']
df40BadMENA = df40Bad[df40Bad['Ethnicity'] == 'D']
df40BadWhite = df40Bad[df40Bad['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, bad40BarChart = plt.subplots()

barsBlack = bad40BarChart.bar(x-2*width, df40BadBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = bad40BarChart.bar(x-width, df40BadAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = bad40BarChart.bar(x, df40BadHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = bad40BarChart.bar(x+width, df40BadMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = bad40BarChart.bar(x+2*width, df40BadWhite['Score'].values.tolist(), width, label = 'White')
bad40BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
bad40BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 40 y/o Applicants with Bad Credit Reports')
bad40BarChart.set_xticks(x, ['Male', 'Female'])
bad40BarChart.set_ylim(0, 100)
bad40BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        bad40BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()


# Create dataframe for Bad 40 y/o applicants
df50Bad = dfBad[dfBad['Age'] == 'E']

# Create dataframes for Bad 50 y/o applicants based on ethnicity
x = np.arange(2)
df50BadBlack = df50Bad[df50Bad['Ethnicity'] == 'A']
df50BadAsian = df50Bad[df50Bad['Ethnicity'] == 'B']
df50BadHLx = df50Bad[df50Bad['Ethnicity'] == 'C']
df50BadMENA = df50Bad[df50Bad['Ethnicity'] == 'D']
df50BadWhite = df50Bad[df50Bad['Ethnicity'] == 'E']
width = 0.1

# Create plot with ethnicity dataframes
sns.set_theme()
fig, bad50BarChart = plt.subplots()

barsBlack = bad50BarChart.bar(x-2*width, df50BadBlack['Score'].values.tolist(), width, label = 'Black')
barsAsian = bad50BarChart.bar(x-width, df50BadAsian['Score'].values.tolist(), width, label = 'Asian')
barsHLx = bad50BarChart.bar(x, df50BadHLx['Score'].values.tolist(), width, label = 'Hispanic/Latinx')
barsMENA = bad50BarChart.bar(x+width, df50BadMENA['Score'].values.tolist(), width, label = 'Middle Eastern and/or North African')
barsWhite = bad50BarChart.bar(x+2*width, df50BadWhite['Score'].values.tolist(), width, label = 'White')
bad50BarChart.set_ylabel('Assigned "Job Trustworthiness" Score')
bad50BarChart.set_title(largeLanguageModel + '\nAssigned "Job Trustworthiness" Scores for 50 y/o Applicants with Bad Credit Reports')
bad50BarChart.set_xticks(x, ['Male', 'Female'])
bad50BarChart.set_ylim(0, 100)
bad50BarChart.legend(loc = 8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        bad50BarChart.annotate('{}'.format(height),
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')

add_labels(barsBlack)
add_labels(barsAsian)
add_labels(barsHLx)
add_labels(barsMENA)
add_labels(barsWhite)

plt.tight_layout()
plt.show()