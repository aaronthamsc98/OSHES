from mysqlaccessors import connectTo, readQuery, executeQuery
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

connection = connectTo("localhost", "root", "password", "oshes")

'''
query = "SELECT * FROM Purchase"
res = readQuery(connection, query)
print(res)

query = "SELECT warranty FROM Product"
res = readQuery(connection, query)
print(res)

query = "SELECT * FROM Item"
res = readQuery(connection, query)
print(res)

query = "SELECT adminID, COUNT(adminID) FROM Administrator LEFT JOIN Request USING(adminID) GROUP BY adminID"
res = readQuery(connection, query)
print(res)

query = "SELECT * FROM Request"
res = readQuery(connection, query)
print(res)

query = "SELECT * FROM Purchase"
res = readQuery(connection, query)
print(res)

query = "SELECT * FROM Item"
res = readQuery(connection, query)
print(res)'''


query = "SELECT DATE_ADD(requestDate, INTERVAL 10 DAY) > '2021-10-20' AS DATEADD FROM Request "
res = readQuery(connection, query)
print(res)