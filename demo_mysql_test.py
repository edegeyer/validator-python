import mysql.connector
from heinrich import heinrichString
from heinrich import heinrichInteger
from heinrich import heinrichDate
from heinrich import heinrichDouble
from heinrich import heinrichBool
from commonMetrik import levenshtein
from commonMetrik import  hamming
from commonMetrik import damerau
import pandas as pd
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="user12",
    database="zahnklinik"
)



# select the data for the not manipulated data
patientQuery = "SELECT * FROM patient"
# select the data for the anonymized data
anonymQuery = "SELECT * FROM lastcharweg"

# set up sigma for all the different cases
sigmaDouble = 1.0
sigmaDay = 1.0
sigmaMonth = 1.0
sigmaStringLength = 1.0
sigmaStringContent = 1.0
sigmaStringDistribution = 1.0

''' possible for metric:
    1: Heinrich
    2: Levenshtein
    3: Damerau Levenshtein
    4: Hamming'''

metric = 1
# use pandas to read the sql table content
patient = pd.read_sql(patientQuery, con=mydb)
anonym =  pd.read_sql(anonymQuery, con=mydb)

starttime = datetime.datetime.now()
tableTotal = 0
print(patient.columns, " length: ", len(patient.columns))

# iterate over all the entities of the table
for i in range(patient.__len__()):
    rowTotal = 0
    # iterate over all the attributes of the entities
    for j in range(len(patient.columns)):
        # TODO: hier klapppt das mit dem range nicht, werte sind nur 0 oder 1
        print(j)
        # print("i, j", i, " f ", j )
        # get the individual data of the cells to compare them
        singlePatient = patient.iloc[i][j]
        singleAnonym = anonym.iloc[i][j]
        # check if the data of both cells is of the same type
        if not isinstance(singleAnonym, type(singlePatient)):
            print("error", type(singleAnonym), type(singlePatient), singleAnonym, singlePatient)
        # find the correct comparer for the datatype
        if isinstance(singleAnonym, str):
            # only differntiate between the different metrics for string, for all the oothers heinrich gets used
            if metric == 1:
                rowTotal += heinrichString.compareString(singlePatient, singleAnonym, sigmaStringLength, sigmaStringDistribution, sigmaStringContent)
            elif metric == 2:
                rowTotal += levenshtein.levenshteinDistance(singlePatient, singleAnonym)
            elif metric == 3:
                rowTotal += damerau.damerau_levenshtein_distance(singlePatient, singleAnonym)
            elif metric == 4:
                rowTotal += hamming.hammingDistance(singlePatient, singleAnonym)
            else:
                print("incorrect value for distance metric")
        elif isinstance(singleAnonym, bool):
            # TODO: zur zeit wird kein bool erkannt, da nur werte zwischen 0 und 1 -> wird als int behandelt
            rowTotal += heinrichBool.compareBool(singleAnonym, singlePatient)
        elif isinstance(singleAnonym, int):
            rowTotal += heinrichInteger.compare(singleAnonym, singlePatient)
        elif isinstance(singleAnonym, float):
            rowTotal += heinrichDouble.compare(singleAnonym, singlePatient)
        elif isinstance(singleAnonym, datetime.datetime):
            rowTotal += heinrichDate.compare(singleAnonym, singlePatient, sigmaDay, sigmaMonth)
        #rowTotal += hamming.hammingDistance(patient[i][j], anonym[i][j])
    tableTotal += abs(rowTotal)/len(patient.columns)
print("total: ", tableTotal)

'''

        tableTotal += (levenshtein.levenshteinDistance(patient.iloc[i][2], anonym.iloc[i][2]))/9
    print("total for all is: " + str(j) + " "+ str(tableTotal/patient.__len__())) '''
#print("total time: ", datetime.datetime.now()-starttime)
# hier muss for schleife hin, die die einzelnen zeilen miteinader vergleicht
