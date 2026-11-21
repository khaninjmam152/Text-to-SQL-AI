import sqlite3
 ## connect to sqlite

connection = sqlite3.connect("student.db")

 ## create a cursr object to insert record, create table, retrieve 

cursor=connection.cursor()

 ## create the table
# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    STUDENTNAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

## insert some more records
cursor.execute('''Insert Into STUDENT values('mohammed','Data Science','A', 90)''')
cursor.execute('''Insert Into STUDENT values('sudhansu','Data Science','B', 100)''')
cursor.execute('''Insert Into STUDENT values('Rahul','Data Science','A', 85)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A', 50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A', 35)''')

## Display all the records

print("The inserted records are")

data=cursor.execute('''select * FROM STUDENT''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()