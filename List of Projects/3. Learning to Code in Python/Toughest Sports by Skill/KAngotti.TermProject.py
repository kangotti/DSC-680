# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:55:46 2020

@author: kevin

"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excdf = pd.read_excel (r'C:\Users\kevin\OneDrive\Bellevue University\DSC 530\Final Project')
DF = pd.DataFrame(df)
print(DF.sum())  
print(DF.mean())  
print(DF.std())
print(DF.mode()[DF.columns[0:6]])
print(DF.median())
print(DF.describe())
print(DF.describe(include='all'))
print(DF.head()[DF.columns[0:6]])
print(np.var(DF))
print(DF.head()[DF.columns[0:8]])

df.Strength.tail()
df.Popularity_Total.tail()

variance= np.var(df)
print(variance)

# Pearsons Correlation & Covariance
np.corrcoef(df['Strength'], df['Total'])[0, 1]
np.cov(df['Strength'], df['Total'])[0, 1]

np.corrcoef(df['Agility'], df['Popularity_Total'])[0, 1]
np.cov(df['Agility'], df['Popularity_Total'])[0, 1]

np.corrcoef(df['Durability'], df['Popularity_Total'])[0, 1]
np.cov(df['Durability'], df['Popularity_Total'])[0, 1]

np.corrcoef(df['Analytical Aptitude'], df['Popularity_Total'])[0, 1]
np.cov(df['Analytical Aptitude'], df['Popularity_Total'])[0, 1]

np.corrcoef(df['Flexibility'], df['Popularity_Total'])[0, 1]
np.cov(df['Flexibility'], df['Popularity_Total'])[0, 1]

np.corrcoef(df['Endurance'], df['Popularity_Total'])[0, 1]
np.cov(df['Endurance'], df['Popularity_Total'])[0, 1]


df.Strength.tail()
df.Endurance.tail()
df.Agility.tail()
df['Analytical Aptitude'].tail()
df.Flexibility.tail()
df.Durability.tail()
df.Popularity_Total.tail()


df.plot(kind='scatter',x='Strength',y='Total',color='Blue')
plt.show()
df.plot(kind='scatter',x='Endurance',y='Popularity_Total',color='Red')
plt.show()
df.plot(kind='scatter',x='Agility',y='Popularity_Total',color='Green')
plt.show()
df.plot(kind='scatter',x='Analytical Aptitude',y='Popularity_Total',color='Purple')
plt.show()
df.plot(kind='scatter',x='Flexibility',y='Total',color='Red')
plt.show()
df.plot(kind='scatter',x='Durability',y='Popularity_Total',color='Teal')
plt.show()
df.plot(kind='scatter',x='Rank',y='Popularity_Total',color='Red')
plt.show()
df.plot(kind='scatter',x='Sport',y='Popularity_Total',color='Red') 
plt.show() # hard to read but provides outlies 
df.groupby(['Strength','Speed']).size().unstack().plot(kind='bar',stacked=True)
plt.show() # hard to read 


df[['Strength']].plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9,10],rwidth=.8)
plt.show()
df[['Endurance']].plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9,10],rwidth=.8)
plt.show()
df[['Agility']].plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9,10],rwidth=.8)
plt.show()
df[['Durability']].plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9,10],rwidth=.8)
plt.show()
df[['Analytical Aptitude']].plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9,10],rwidth=.8)
plt.show()
df[['Flexibility']].plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9,10],rwidth=.8)
plt.show()
df[['Nerve']].plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9,10],rwidth=.8)
plt.show()
df[['Popularity_Total']].plot(kind='hist',bins=[5,10,15,20,25,30,40,50,55,60],rwidth=.9)
plt.show()
df[['Popularity']].plot(kind='hist',bins=[5,10,15,20,25,30,35,40,45,50,55,60],rwidth=.9)
plt.show()


df['Popularity_Total'].value_counts().sort_index().plot.barh() # hard to read
df.groupby("Sport").Popularity.mean().sort_values(ascending=False)[:5].plot.bar()
df.groupby("Sport").Popularity_Total.mean().sort_values(ascending=False)[:6].plot.bar() # good visual



## Computing p-value between two variables
# H0 :- means difference between two sample is 0
# H1:- mean difference between two sample is not 0
df[['Strength','Total']].describe()
ttest,pval = stats.ttest_rel(df['Strength'], df['Total'])
print(pval)
if pval <= 0.05:
    print("reject null hypothesis")
    print("accept alternate hypothesis")
else:
    print("accept null hypothesis")


## z-test
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
ztest,pval = stests.ztest(df['Agility'], x2=None, value=60)
print(float(pval))
if pval <= 0.05:
    print("reject null hypothesis")
    print("accept alternate hypothesis")
else:
    print("accept null hypothesis")
    
    
## Multiple Regression 
import statsmodels.formula.api as smf
formula = 'Strength ~ Total + Power + Popularity_Total'   # Analytical Aptitude as a 
model = smf.ols(formula, data=df)                  # function of Popularity Total
results = model.fit()
results.summary()
inter = results.params['Intercept']
slope = results.params['Popularity_Total']
inter, slope
slope_pvalue = results.pvalues['Popularity_Total'] # p-value of the slope estimate
slope_pvalue
results.rsquared # coefficient of determination


## Logistic Regression, can't run since no target column had values between 0 & 1.
formula = 'Popularity ~ Strength + Endurance'
model = smf.logit(formula, data=df)
results = model.fit()
endog = pd.DataFrame(model.endog, columns=[model.endog_names])
exog = pd.DataFrame(model.exog, columns=model.exog_names)
results.summary()
actual = endog['Popularity']
baseline = actual.mean()
baseline


## PMF's
probabilities = df['Strength'].value_counts(normalize=True, bins=range(1, 8))    
sns.barplot(probabilities.index, probabilities.values)
_ = plt.xlabel('Srength')
_ = plt.ylabel('PMF')
plt.show()

probabilities = df['Analytical Aptitude'].value_counts(normalize=True, bins=range(1, 8))    
sns.barplot(probabilities.index, probabilities.values)
_ = plt.xlabel('Analytical Aptitude')
_ = plt.ylabel('PMF')
plt.show()


# PMF's Two Variables 
bins = np.arange(0, max(df['Strength']) + 1.5) - 0.5
_ = plt.hist(df['Strength'], normed=True, bins=bins)
_ = plt.hist(df['Popularity_Total'], normed=True, bins=bins)
_ = plt.xlabel('Attribute')
_ = plt.ylabel('PMF')
plt.show()



#PMF's single variable 
bins = np.arange(0, max(df['Strength']) + 1.5) - 0.5
_ = plt.hist(df['Strength'], normed=True, bins=bins)
_ = plt.xlabel('Strength')
_ = plt.ylabel('PMF')
plt.show()

bins = np.arange(0, max(df['Endurance']) + 1.5) - 0.5
_ = plt.hist(df['Endurance'], normed=True, bins=bins)
_ = plt.xlabel('Endurance')
_ = plt.ylabel('PMF')
plt.show()

## CDF's
num_bins = 25
counts, bin_edges = np.histogram (df['Strength'], bins=num_bins, normed=True)
cdf = np.cumsum (counts)
plt.plot (bin_edges[1:], cdf/cdf[-1])
_ = plt.xlabel('Strength')
_ = plt.ylabel('CDF')
## Shows the median and tail statistic for the variable
for q in [50, 90, 95, 100]:
  print ("{}%% percentile: {}".format (q, np.percentile(df['Strength'], q)))


num_bins = 25
counts, bin_edges = np.histogram (df['Endurance'], bins=num_bins, normed=True)
cdf = np.cumsum (counts)
plt.plot (bin_edges[1:], cdf/cdf[-1])
_ = plt.xlabel('Endurance')
_ = plt.ylabel('CDF')
## Shows the median and tail statistic for the variable
for q in [50, 90, 95, 100]:
  print ("{}%% percentile: {}".format (q, np.percentile(df['Strength'], q)))
  

## Analytical Distribution  probabilty Plot's
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
data = df['Strength'] * np.random.randn(60) + 0.5
counts, start, dx, _ = scipy.stats.cumfreq(data, numbins=25)
x = np.arange(counts.size) * dx + start
plt.plot(x, counts, 'ro')
plt.xlabel('Strength')
plt.ylabel('Cumulative Frequency')
plt.title('Probability Plot')
plt.show()


## Hypothesis test's
from scipy.stats import chi2_contingency
data = df['Endurance']
stat, p, dof, expected = chi2_contingency(data)
print('stat=%.3f, p=%.1f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')
    
# ANOVA Hypothesis test    
from scipy.stats import f_oneway                  # For use in project
data1 = df['Strength']
data2 = df['Total']
#data3 = df['Rank']
stat, p = f_oneway(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p <= 0.05:
	print('Accept null hypothesis they are Probably the same distribution')
else:
	print('Reject the null hypothesis, they are Probably different distributions')