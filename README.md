# validator-python
this project is the python implementation of the project: https://github.com/edegeyer/validator

the mathematical base can be found in the following paper:
https://www.proficom.de/fileadmin/user_upload/Downloads/proficom_AEhnlichkeitsmessung_von_ausgewaehlten_Datentypen_in_Datenbanksystemen_zur_Berechnung_des_Grades_der_Anonymisierung.pdf

some information about sigma will be available soon in another paper

this implementation only works with the python3 console.

System requirements
- python3
- pandas
- mysql-connector
- MySQL database with the tables you want to compare (they both need the same strucutre)

1. Get the project from github and import it into the editor of your choice
2. Set up a MySQl Database including at minimum two tables (one with the original data, one with the anonymized data) -> working at proficom: you find some example data in the sharepoint folder in the databases.zip -> see exact steps of setting up the database further down
3. Easiest to include the data in the database: use DBeaver or MySQL workbench
4. set up the mysql connector in demo_mysql_test with the configuration details pf the database that you used in step 2
5. just run the demo_mysql_test and both the tables will be compared, the sigma value and the distance metric can be adjusted in that file (the necessary positions are marked)
6. if you want to adjust any data of a table and save it as a .csv file, use the replace_characters  script, it just requires manual import into the database after before your can use it

for further instructions on how to set up the database, please see the java project

this project is a python copy of the java project, as the type safety of java makes it more complicated to import different tables from a database