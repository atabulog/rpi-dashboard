"""
author(s): A. Tabulog
date: 12/30/21
email: austin.tabulog@gmail.com

=========================================================
This file is subject to the MIT license copyright notice.
=========================================================

Script to grab all results from networkData table in db.
"""

#imports
from mysql.connector.errors import DataError
import dbIntfObj
import SpeedTestObj

if __name__ == "__main__":
    #create connection to database
    dbTable = dbIntfObj.networkDataTable()    
    dbTable.fetch_allData()
    [print(x) for x in dbTable.results]