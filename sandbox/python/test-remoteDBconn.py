"""
author(s): A. Tabulog
date: 12/30/21
email: austin.tabulog@gmail.com

=========================================================
This file is subject to the MIT license copyright notice.
=========================================================

Script to test the connection to the remote mysql datbase running on the rpi 
home server.
"""

#imports
from pdb import Pdb
import mysql.connector as mysql
import speedtest 


class simpledataStruct:
    def __init__(self, serverName, download, upload, ping):
        self._server = serverName
        self._download:str = str(download/1e6)[0:5]
        self._upload:str = str(upload/1e6)[0:5]
        self._ping:str = str(ping)
        self._updownUnit = "Mb/s"
        self._pingUnit = "ms"
    
    def write2db(self, cursor, conn):
        cursor.execute("insert into networkData (sampleID, data) values (2, 1.414);")
        conn.commit()


if __name__ == "__main__":
    host_ip = "10.0.0.152"
    db_name = "demo"
    host_port = 3306
    user = "user"
    password = ""   
    
    #connect and create cursor
    conn = mysql.connect(host=host_ip, port=host_port, database=db_name, user=user, password=password)
    cursor = conn.cursor()
    cursor.execute("SELECT * from networkData")
    res = cursor.fetchall()
    [print(x) for x in res]
    """
    #create speed test connection
    st = speedtest.Speedtest()
    
    #perform internet speed test with closest available server
    print("fetching internet speed data, please wait.")
    st.get_servers(); st.get_best_server()
    st.download(); st.upload()
    #load data into formatting object
    results = simpledataStruct(st.results.server["name"], st.results.download, st.results.upload, st.results.ping)
    results.write2db(cursor, conn)
    
    cursor.execute("SELECT * from networkData")
    res = cursor.fetchall()
    [print(x) for x in res]
    """
    conn.close()