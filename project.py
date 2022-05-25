# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.graph_objects as go

# Section 1: Check the data

# Data import
apps_with_duplicates = pd.read_csv("datasets/apps.csv", index_col=0)
reviews_df = pd.read_csv("datasets/user_reviews.csv")

# Drop duplicates
apps = apps_with_duplicates.drop_duplicates(subset="App")

# Print the total number of apps
print('Total number of apps in the dataset = ', apps["App"].count())

# Section 2: Data Cleaning

chars_to_remove = ['+', ',', '$', ]

cols_to_clean = ['Installs', 'Price']

# This is how we remova character in the differents sections already stablished
for col in cols_to_clean:
    for char in chars_to_remove:
        apps[col] = apps[col].apply(lambda x: x.replace(char, ''))

# Section 3: Correcting Data types

apps['Installs'] = apps['Installs'].astype(float)

apps['Price'] = apps['Price'].astype(float)

# Section 4: Exploring App Categories

# Print the total number of unique categories

num_categories = len(apps["Category"].unique())
print('Number of categories = ', num_categories)

# Count the number of apps in each 'Category'.
num_apps_in_category = apps['Category'].value_counts()

# Sort num_apps_in_category in descending order based on the count
sorted_num_apps_in_category = num_apps_in_category.sort_values(ascending=False)

sorted_num_apps_in_category.plot(kind='bar', x=num_apps_in_category.index,
                                 y=num_apps_in_category.values)

plt.show()

# Section 5: Distribution of app ratings

avg_app_rating = apps["Rating"].mean()

print('Average App Rating = ', avg_app_rating)

apps['Rating'].hist(bins=30)

plt.plot([avg_app_rating, avg_app_rating], [0, 1000])

plt.legend(["hist", "avg"])

plt.show()

# Section 6: Size and price an app

# adjustments for Seaborn
sns.set_style("darkgrid")
warnings.filterwarnings("ignore")

# we use the apps that have a rate
apps_with_size_and_rating_present = apps[apps['Rating'].notna(
) & apps['Size'].notna()]

# We group them by category with a lenght >= 250
large_categories = apps_with_size_and_rating_present.groupby(
    'Category').filter(lambda x: len(x) >= 250)

plt1 = sns.jointplot(x=large_categories["Size"], y=large_categories["Rating"])

paid_apps = apps_with_size_and_rating_present[
    apps_with_size_and_rating_present["Type"] == 'Paid']

plt2 = sns.jointplot(x=paid_apps["Price"], y=paid_apps["Rating"])

plt.show()

# Section 7: Relationship between app category and app price

fig, ax = plt.subplots()  # this allows to plot multiple lots on a single figure
fig.set_size_inches(15, 8)

# Select a few popular app categories
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                           'MEDICAL', 'TOOLS', 'FINANCE',
                                            'LIFESTYLE', 'BUSINESS'])]

# we are using a different type of graph
ax = sns.stripplot(
    x=popular_app_cats["Price"], y=popular_app_cats["Category"], jitter=True, linewidth=1)
ax.set_title('App Pricing trend across categories')

apps_above_200 = apps[apps["Price"] > 200]
apps_above_200[['Category', 'App', 'Price']]

plt.show()

# Section 8: Filter out "junk" apps

fig, ax = plt.subplots()

fig.set_size_inches(15, 8)

# I'm filtering the apps with a price lower than 100
apps_under_100 = popular_app_cats[popular_app_cats["Price"] < 100]

ax = sns.stripplot(x="Price", y="Category",
                   data=apps_under_100, jitter=True, linewidth=1)

ax.set_title(
    'App pricing trend across categories after filtering for junk apps')

plt.show()

# Section 9: Popularity of paid apps vs free apps

fig = go.Figure()

fig.add_trace(go.Box(
    y=apps[apps['Type'] == 'Paid']['Installs'],
    name='Paid'
))

fig.add_trace(go.Box(
    y=apps[apps['Type'] == 'Free']['Installs'],
    name='Free'
))

fig.update_layout(
    title="Number of downloads of paid app vs. free apps",
    yaxis=dict(title="Log number of downloads",
               type='log',
               autorange=True)
)

fig.show()

# Sentimental analysis of reviews

merge_df = apps.merge(reviews_df)

merge_df = merge_df.dropna(subset=["Sentiment", "Review"])

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11, 8)

ax = sns.boxplot(x='Type', y='Sentiment_Polarity', data=merge_df)

ax.set_title('Sentiment Polarity Distribution')

plt.show()
