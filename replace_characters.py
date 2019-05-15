
import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="user12",
    database="zahnklinik"
)


patientQuery = "SELECT * FROM patient"
df = pd.read_sql(patientQuery, con=mydb)
emailColumn = df["email"]
print(emailColumn)

letterToBeRemoved = 0 #counting starts at 0 ;)
newMailColumn = []
for row in range(emailColumn.__len__()):
    oldstring = emailColumn[row]
    df.at[row, "email"] = oldstring[:letterToBeRemoved] + oldstring[letterToBeRemoved +1:]

print("email new: ", df["email"])


name = "char" + str(letterToBeRemoved) + "weg"
path = '/home/user/Desktop/'+name+".csv"
df.to_csv(path_or_buf=path)






