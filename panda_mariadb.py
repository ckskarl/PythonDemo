import pandas as pd
import sqlalchemy

# connect to database
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:password@localhost:3306/coffeedb")

# read table and turn it into DataFrame type
table_df = pd.read_sql_table('coffee', con=engine)

# Display a summary on the DataFrame object
table_df.info()

# Run SQL Select statement in DataFrame format
sql_df = pd.read_sql("SELECT * FROM coffee", con=engine)
# output result for query
print(sql_df)

# Create a new DataFrame with certain Column from the given DataFrame Object
df = pd.DataFrame(sql_df, columns=['Description', 'Price'])
# output result
print(df)





