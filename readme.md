# Google Play Store apps and reviews

## Overview

In this project, we will do a comprehensive analysis of the android maker by comparing over ten thousand apps 
in Google play across diferent categories

It consist of two data sets: 
1. **apps.csv**: contains all the detail of the applications on Google Play.
2. **user_reviews.csv**: contains 100 reviews for each app, most helpful first.

we will be using different techniques and plotting libraries.

## Prerequisites

1. Pandas
```
$ pip3 install pandas
```
2. matplotlib.pyplot
```
$ pip3 install matplotlib
```
3. Seaborn
```
$ pip3 install seaborn
```
Reference: [Seaborn](https://seaborn.pydata.org/index.html)

4. plotly
```
$ pip3 install plotly
```
Reference: [Plotly](https://plotly.com/python/box-plots/)

## Section 1: Check the data

This section, duplicated values are deleted, and print the total number of apps. 
We import the data. 

## Section 2: Data Cleaning

We start cleaning the data, we remove different characters from different sections 
of the database, make sure all data is clean. 

## Section 3: Correcting Data Types

We make sure "Installs" & "Price" are identified as float. If we apply numerical 
operations we need to make sure they are the right type. 

[Figure 1](/pictures/figure1.png)

## Section 4: Exploring App Categories

With more than 1 billion active users in 190 countries, Google separates apps and groups
them into categories. This bring us the following questions

1. which category has the higher share of (active) apps in the market?
2. is any specific category dominating the market?
3. Which categories have the fewest number of apps?

[Figure 2](pictures/figure2.png)

**Conclusion:** There are 33 unique apps present in our dataset. Family and Game apps
have the highest market prevalence. Tools, Business, and Medical apps are on the top.

## Section 5: Distribution of app ratings

After looking the market share for each category of apps, let's see how all apps perform
on average.

[Figure 3](pictures/figure3.png)

**Conclusion:** from our reserch, we found that the average volume of ratings across all
app categories is 4.17. The histogram plot is skewed to the left indicating that the majority
of the apps are highly rated with only few exceptions in the low-rated apps. 

## Section 6: Size and price an app

Let's now examine app size and app price. For size, if the mobile app is too large, it may too
large, it may be difficult and/or inexpensive for users to download. 
This bring us to the following questions.

1. Does the size of an app effect its rating? 
2. Do users really care about system-heave apps or do they prefer light-weighted apps?
3. Does the price of an app affect its rating?
4. Do users always prefer free apps over paid apps?

[Figure 4](pictures/figure4.png)

**Conclusion:** We find most of the top rated apps(rating over 4) range from 4MB to 20MB. We
also find that the vast majority of apps price themselves under $10.

## Section 7: Relationship between app category and app price

This is the hard part. How are the companies and developers supposed to make ends meet?
what monetization strategies can companies use to maximize profit? The cost of apps are largerly
based on features, complexity and platform. 

It is important to consider the willingness of your costumer to pay for your app. A wrong price 
could break the deal. 

[Figure 5](pictures/figure5.png)

**Conclusion:** We see that Medical and Family apps are the most expensive. Some medical apps extend
even up to $80, All game apps are reasonably priced below $20. 

Resources:
1. [Estimate my app](https://estimatemyapp.com/)
2. [How much to make an app](http://howmuchtomakeanapp.com/)

## Section 8: Filter out "junk" apps

In this section, I filtered out the junk apps and re-do our visualization. 

[Figure 6](pictures/figure6.png)

## Section 9: Popularity of paid apps vs free apps

There are five types of pricing strategies:

1. free
2. freemium
3. paid
4. paymium
5. subscription

Some characteristics of free apps are: 

- Free to download
- Main source of income often comes from advertisement
- Often created by companies that have other products and the app serves as an extension of those products
- Can serve as a tool for customer retention, communication, and consumer service.

Some characteristics of paid apps are:
- Users are asked to pay once for the app to download and use it.
- The user can't really get a feel for the app before buying it.

[Figure 7](pictures/figure7.png)

**Conclusion:** Are paid apps installed as much as free apps? It turns out that paid apps have relatively
lower number of install than free apps, though the difference is not as stark as I would have expected.

Resources: 
1. [Understand and interpreting box plots](https://www.wellbeingatschool.org.nz/information-sheet/understanding-and-interpreting-box-plots)

## Section 10: Sentimental analysis of reviews

Mining user review data to determine how people feel about your product, brand, or service can be done
using a technique called sentiment analysis.

[Figure 8](pictures/figure8.png)

**Conclusion:** By plotting sentiment polarity scores of user reviews for paid and free apps, we observe
that free apps receive a lot of harsh comments, reviews for paid apps appear never to be extremely negative. 
This may indicate something about app quality, paid apps being of higher quality than free apps on average. 

Resources: 
1. [boxplot()](https://seaborn.pydata.org/generated/seaborn.boxplot.html)
