import mysql.connector
from heinrich import heinrichString
from heinrich import heinrichBool
from heinrich import heinrichInteger
from heinrich import heinrichDouble
from heinrich import heinrichDate
import pandas as pd
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="user12",
    database="zahnklinik"
)



#mycursor = mydb.cursor()

for j in range(0,25):
    patientQuery = "SELECT * FROM patient"
    anonymQuery = "SELECT * FROM char"+str(j)+"weg"
    #anonymQuery = "SELECT * FROM lastcharweg"
    sigma = 10
    patient = pd.read_sql(patientQuery, con=mydb)
    anonym =  pd.read_sql(anonymQuery, con=mydb)

    starttime = datetime.datetime.now()
    tableTotal = 0
    for i in range(patient.__len__()):
        rowTotal = 0
        '''
        for j in range(len(patient.columns)):
    
            singlePatient = patient.iloc[i][j]
            singleAnonym = anonym.iloc[i][j]
            if not isinstance(singleAnonym, type(singlePatient)):
                break
            if isinstance(singleAnonym, str):
                rowTotal += heinrichString.compareString(singlePatient, singleAnonym)
            elif isinstance(singleAnonym, bool):
                # TODO: zur zeit wird kein bool erkannt, da nur werte zwischen 0 und 1 -> wird als int behandelt
                print("found bool")
                rowTotal += heinrichBool.compareBool(singleAnonym, singlePatient)
            elif isinstance(singleAnonym, int):
                rowTotal += heinrichInteger.compare(singleAnonym, singlePatient)
            elif isinstance(singleAnonym, float):
                rowTotal += heinrichDouble.compare(singleAnonym, singlePatient)
            elif isinstance(singleAnonym, datetime.datetime):
                rowTotal += heinrichDate.compare(singleAnonym, singlePatient)
            #rowTotal += hamming.hammingDistance(patient[i][j], anonym[i][j])
        tableTotal += abs(rowTotal)/len(patient.columns)
        '''

        tableTotal += (heinrichString.compareString(patient.iloc[i][2], anonym.iloc[i][2], sigma))/10
    print("total for all is: " + str(j) + " "+ str(tableTotal/patient.__len__()))
#print("total time: ", datetime.datetime.now()-starttime)
# hier muss for schleife hin, die die einzelnen zeilen miteinader vergleicht
