# PHIL 208 Statistical Analysis
 Statistical Analysis of LLM "Job Trustworthiness" Scoring Data for PHIL 208 Data Science Ethics Project

## About the Project
Credit scores, despite being a metric originally developed to quantify a person’s ability to pay back their debts, have turned into a measure of a person’s trustworthiness. Credit scores now impact a person’s ability to rent a home, seek employment, and more. However, these scores do not directly demonstrate the degree to which an individual can be considered a trustworthy homeowner or job applicant.

Unfortunately, in the hiring process, recruiters may react differently to the same piece of credit history from diverse job candidates, creating unethical human bias in the hiring process.

I, alongside classmates Matthew Chan, Abhilasha Jain, Hamilton Wang, and Jabez Williams, brought awareness to artificial intelligence’s biases in the contexts of credit reports and hiring, proving that the challenge of bias stems beyond humans and AI is currently not an ethical tool for evaluating job candidates.

## About This Repository
This repository is for my statistical analysis within our project. Using data from GPT-3.5, Google Bard, and Bing Chat, I created bar graphs (see PNG files in repo) to compare each LLM's "Job Trustworthiness Score" across different races and sexes for each tested age (18 y.o., 20 y.o., 30 y.o., 40 y.o., 50 y.o.). I also conducted ANOVA tests to test whether there was a statistically significant difference between the LLM “Job Trustworthiness” Scores for all applicants with good mock credit reports and bad mock credit reports. This test ultimately determined if the decision making of AI is uniform enough across LLMs for humans to comfortably rely on it.

### ANOVA Results (see ANOVA files for source p-values):

There was a statistically significant difference between the Job Trustworthiness scores for applicants with good credit reports among the 3 tested models but there was no difference for applicants with bad credit reports at the 95% confidence level.
