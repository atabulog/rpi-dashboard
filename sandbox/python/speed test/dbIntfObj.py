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


class MysqlDb(object):
    def __init__(self, host, db_name, user, password, port=3306):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.port = port
        
        #create connection to supplied database
        try:
            self.conn = mysql.conn(host=self.host, port=self.port, database=self.db_name, user=self.user, password=self.password)
            self.cursor = self.conn.cursor()
        #tie to null values if connection fails
        except:
            self.conn = None
            self.cursor = None
