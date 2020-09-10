import pyodbc
import matplotlib.pyplot as plt
import sqlalchemy as db
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
engine = db.create_engine('mssql+pyodbc://THINKPAD\SQL2014/AdventureWorks2014?driver=SQL Server?Trusted_Connection=yes')
connection = engine.connect()
result = engine.execute('select * from person.address')
other_result = result.fetchall()
print(type(other_result))
print(other_result)
print(len(other_result))

query = 'select * from person.address'
data_query = pd.read_sql_query(query, engine)
print(type(data_query))
print(data_query.columns)
print(data_query.dtypes)
print(data_query.head())
print (data_query[['PostalCode', 'ModifiedDate']].max())
print (data_query[['PostalCode', 'ModifiedDate']].describe())
print (data_query[['PostalCode', 'ModifiedDate']].dropna()[:50])

x = data_query['PostalCode']
y = data_query['ModifiedDate']
colors = np.random.rand(4500)
plt.scatter(x, y, c=colors)
plt.title('show postalcodes')
plt.xlabel('PostalCode')
plt.ylabel('ModifiedDate')
print(plt.show())
