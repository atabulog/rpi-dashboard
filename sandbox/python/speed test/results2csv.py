"""
author(s): A. Tabulog
date: 12/30/21
email: austin.tabulog@gmail.com

=========================================================
This file is subject to the MIT license copyright notice.
=========================================================

Script to create csv file for all results in db table.
"""

#imports
from mysql.connector.errors import DataError
import dbIntfObj
import csv

if __name__ == "__main__":
    #create connection to database
    dbTable = dbIntfObj.networkDataTable()    
    dbTable.fetch_allData()
    
    with open('C:\\Users\\Austi\\Desktop\\networkData.csv', "w+") as f:
        writer = csv.writer(f)
        [writer.writerow(row) for row in dbTable.results]
    