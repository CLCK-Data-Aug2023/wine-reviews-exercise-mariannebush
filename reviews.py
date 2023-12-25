#Import Pandas
import pandas as pd

#Read In Data from Existing File
df = pd.read_csv(r"C:\Users\maria\Documents\Code KY\Data Analytics\wine-reviews-exercise-mariannebush\data\winemag-data-130k-v2.csv.zip")

#Reviews_Summary data frame
reviews_summary = df.groupby('country').agg({'points': ['count', 'mean']})
reviews_summary.columns = ['count', 'points']
reviews_summary['points'] = reviews_summary['points'].round(1)

#Write to csv file
reviews_summary.to_csv(r"C:\Users\maria\Documents\Code KY\Data Analytics\wine-reviews-exercise-mariannebush\data\reviews-per-country.csv")

