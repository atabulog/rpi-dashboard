"""
author(s): A. Tabulog
date: 12/30/21
email: austin.tabulog@gmail.com

=========================================================
This file is subject to the MIT license copyright notice.
=========================================================

Script to test speedtest related objects.
"""

#imports
import pdb
from mysql.connector.errors import DataError
import dbIntfObj
import SpeedTestObj

if __name__ == "__main__":
    #create connection to database
    dbTable = dbIntfObj.networkDataTable()
    
    #run a speed test
    test = SpeedTestObj.SpeedTest()
    test.run_bestTest()
    
    #get data as formatted dictionary, sanitize, and insert into db
    results = test.get_testData()
    try:
        dbTable.record_newEntry(server=results['server'],
                                ping=results['ping'],
                                upload=results['upload'],
                                download=results['download'])
    except:
        raise DataError("Could not record new entry.")