import random
import mysql.connector

db_host = 'localhost'
db_user = 'root'
db_password = 'Devil@123'
db_name = 'study'

table_name = 'general_knowledge'

# random number generation and sorting:::
random_list = list()

while (len(random_list)<5):
    random_number = random.randint(1,25)
    if random_number in random_list:
        continue
    else:
        random_list.append(random_number)

random_list = sorted(random_list)
print(random_list)

try:
    connection = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_name
    )

    cursor = connection.cursor()

    new_list = random_list
    for i in range(0,len(new_list)):
        sql_query = f'SELECT * FROM {table_name} WHERE id = {new_list[i]}'
        cursor.execute(sql_query)

        data = cursor.fetchall()

        for row in data:
            print(row)

except mysql.connector.Error as err:
    print("Error connceting to database: ",err)

finally:
    if connection:
        connection.cursor().close()
        connection.close()

print(f"Data fetched successfully!!.")
