import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:password@localhost:3306/coffeedb")

# Display original Table
sql_df = pd.read_sql("SELECT * FROM coffee", con=engine)
print(sql_df)

# Create new data using DataFrame
new_data_df = pd.DataFrame({
    'Description': ['TEST1', 'TEST2'],
    'ProdNum': ['99-001', '99-002'],
    'Price': [9.99, 8.88]})
print(new_data_df)

# Insert the new data into the table
new_data_df.to_sql('coffee', con=engine, if_exists='append', chunksize=1000, index=False)
sql_df2 = pd.read_sql("SELECT * FROM coffee", con=engine)
print(sql_df2)

# Delete the newly added rows
engine.execute("DELETE FROM coffee WHERE Description = 'TEST1'")
engine.execute("DELETE FROM coffee WHERE Description = 'TEST2'")
sql_df3 = pd.read_sql("SELECT * FROM coffee", con=engine)
print(sql_df3)

