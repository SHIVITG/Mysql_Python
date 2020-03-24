
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "root"
)

print(db) # it will print a connection object if everything is fine


# In[32]:


import os


# In[24]:


## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'Basic_Info'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'Basic_Info' database
cursor.execute("CREATE DATABASE Basic_Info")


# In[23]:


for database in databases:
    print(database)


# In[ ]:


### Working in the database created: Basic_Info --> Creating Table Information


# In[25]:


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "Basic_Info"
)
cursor = db.cursor()


# In[28]:


cursor.execute("CREATE TABLE information(customer_id VARCHAR(255) PRIMARY KEY,customer_name VARCHAR(255),customer_email VARCHAR(255), customer_address VARCHAR(255), customer_number INT(10), feedback VARCHAR(255), time_of_feedback VARCHAR(255), loaction VARCHAR(255))")


# In[29]:


cursor.execute("SHOW TABLES")

tables = cursor.fetchall() ## it returns list of tables present in the database

## showing all the tables one by one
for table in tables:
    print(table)


# In[30]:


cursor.execute("DESC information")

## it will print all the columns as 'tuples' in a list
print(cursor.fetchall())


# In[35]:


# Export database file / store the file
os.system('mysqldump -u root -p%s Basic_Info > Basic_Info.sql' % 'root')


# In[ ]:




