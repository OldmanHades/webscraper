
# First import pandas
# You might also need to install lxml as that is the parser it's using
import pandas as pd
# This loads the page using pandas 
scraped = pd.read_html("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")
# We need to make the data more organized so it is readable
for idx, table in enumerate(scraped):
    print("*********************")
    print(idx)
    print(table)

# The table we need is under #3
scraped[3]
# Create a loadable data frame
df = pd.DataFrame(scraped[3])
# Put that Dataframe into a .csv file so you can make use of it.
gfg_csv_data = df.to_csv('scraped.csv', index = True)