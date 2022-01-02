"""
author(s): A. Tabulog
date: 12/30/21
email: austin.tabulog@gmail.com

=========================================================
This file is subject to the MIT license copyright notice.
=========================================================

Custom object wrapping on mysql based custom 'networkData' table.
"""

#imports
import mysql.connector as mysql
from sys import platform
#generic MySQL db object
class MysqlDb(object):
    def __init__(self, host, db_name, user, password, port=3306):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.port = port
        self.linuxSocket = "/var/run/mysqld/mysqld.sock"
        self.conn = None
        self.cursor = None
    
    
    """Connect object to server.
    Args:
        None.
    Returns:
        status (bool): True if connected established, false if not.
    """
    def connect(self):    
        #create connection to supplied database
        try:
            #connect using different methods depending on the system making the call
            if platform == "win32":
                self.conn = mysql.connect(host=self.host, database=self.db_name, user=self.user, password=self.password, port=self.port)
                self.cursor = self.conn.cursor()
                return True
            elif platform == "linux":
                self.conn = mysql.connect(host=self.host, database=self.db_name, user=self.user, password=self.password, unix_socket=self.linuxSocket)
                self.cursor = self.conn.cursor()
                return True
            else:
                return False
        #tie to null values if connection fails
        except:
            self.conn = None
            self.cursor = None
            return False
        
        
    """Disconnect object from server.
    Args:
        None.
    Returns:
        None.
    """
    def disconnect(self):
        try:
            self.conn.close()
            self.conn = None
            self.cursor = None
        except:
            self.conn = None
            self.cursor = None
    
    
    """Creates table in current db.
    Args:
        tableName (str): name of table to create.
        desc (str): MySQL command description of table to create.
    """
    def create_table(self, tableName, desc):
        query = f"CREATE TABLE {tableName}({desc});"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except:
            raise mysql.Error(f"Could not execute command:\n{query}")

    
    """Checks if table with given name exists in db.
    Args:
        tableName (str): name of table to look for in db.
    Returns:
        status (bool): true if table exists, false if it doesn't.
    """
    def tableExists(self, tableName):
        self.cursor.execute(f"SHOW TABLES LIKE '{tableName}';")
        #if returned data is empty return false
        if self.cursor.fetchall() == []:
            return False
        #else return true
        else:
            return True
            
            

#object for network data table
class networkDataTable(MysqlDb):
    def __init__(self):
        #init parent object
        super().__init__(host="localhost", 
                         db_name="rpi_dashboard", 
                         user="user", 
                         password="", 
                         port=3306)
        
        #init other attributes
        self.results = None
        self._tableName = "networkData"
        self._tableDesc = "uid INT NOT NULL AUTO_INCREMENT, "+\
                          "timestamp TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, "+\
                          "server VARCHAR(30), "+\
                          "ping FLOAT, "+\
                          "download FLOAT, "+\
                          "upload FLOAT, "+\
                          "PRIMARY KEY (uid)"
         
        #connect to host server, and raise error if connection failed
        if(not self.connect()):
            raise ConnectionError(f"can't connect ot MySQL server on {self.host}:{self.port}")

        #create table if one does not exist
        self.create_tableIfMissing()
        
    
    """Create networkData table in current database if one does not exist.
    Args:
        None.
    Returns:
        None.
    """
    def create_tableIfMissing(self):
        if not self.tableExists(tableName=self._tableName):
            self.create_table(tableName=self._tableName, desc=self._tableDesc)
    
    
    """Adds new network speed data entry to database.
    Args:
        server (str): location of test server.
        ping (float): server ping time in ms.
        upload (float): upload time in Mb/s.
        download (float): download time in Mb/s.
    Returns:
        None.
    """
    def record_newEntry(self, server, ping, upload, download):
        query = f"INSERT INTO {self._tableName} \
                (server, ping, download, upload) \
                VALUES (%s, %s, %s, %s);"
        self.cursor.execute(query, (str(server), float(ping), float(download), float(upload)))
        self.conn.commit()
