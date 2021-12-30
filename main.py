import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data\\autos.csv", encoding="ISO-8859-1")
# print(df.info())
# print(df.columns)
df.rename({"dateCrawled": "date_crawled", "offerType": "offer_type", "vehicleType": "vehicle_type",
           "powerPS": "power_ps", "yearOfRegistration": "registration_year",
           "monthOfRegistration": "registration_month", "fuelType": "fuel_type",
           "notRepairedDamage": "unrepaired_damage", "dateCreated": "date_created",
           "nrOfPictures": "number_of_pictures", "postalCode": "postal_code", "lastSeen": "last_seen",
           "kilometer": "odometer_km"},
          axis=1, inplace=True)
df.drop(df[df['price'] == 0].index, inplace=True)
df.drop("number_of_pictures", axis=1, inplace=True)
df.drop(df[(df["registration_year"] < 1900) | (df["registration_year"] > 2016)].index, inplace=True)
print(df["registration_year"].unique())


print(df.columns)
print(df.describe())
selected_columns = df[["price", "odometer_km"]]
print(selected_columns.describe())

sns.heatmap(df.corr(), vmax=.8, square=True)
plt.show()

plt.scatter(df['price'], df['odometer_km'])
plt.show()
plt.scatter(df['registration_year'], df['odometer_km'])
plt.show()
quantitative = [f for f in df.columns if df.dtypes[f] != 'object']

facet = pd.melt(df, value_vars=quantitative)
z = sns.FacetGrid(facet, col="variable", col_wrap=2, sharex=False, sharey="False")
z = z.map(sns.distplot, "value")
plt.show()

for q in quantitative:
    for q2 in quantitative:
        value = df[q].corr(df[q2])
        if q != q2 and (value > 0.1 or value < -0.1):
            print("{q} correlates to {q2} with a value of {v:.2f}".format(q=q, q2=q2, v=value))
# print(df["registration_year"].unique())
# print(df['date_created'].unique())
# print(df['date_crawled'].value_counts(dropna=False))

