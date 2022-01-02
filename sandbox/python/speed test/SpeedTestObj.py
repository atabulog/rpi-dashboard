"""
author(s): A. Tabulog
date: 01/01/22
email: austin.tabulog@gmail.com

=========================================================
This file is subject to the MIT license copyright notice.
=========================================================

Custom speed test object to capture speed test data in desired format.
"""

#imports
import speedtest
from datetime import datetime

#class defining speed test data object
class SpeedTestData:
    def __init__(self):
        self.timestamp = "NULL"
        self.server = "NULL"
        self.upload = 0.0
        self.download = 0.0
        self.ping = 0.0
        self.rateUnit = "Mb/s"
        self.pingUnit = "ms"
    
    """Convert object data to dictionary and return to caller.
    Args:
        None.
    Returns:
        Dictionary of SpeedTestData object attributes.
    """
    def toDict(self):
        tempDict = {"timestamp": self.timestamp,
                    "server": self.server,
                    "download":self.download,
                    "upload": self.upload,
                    "ping": self.ping,
                    "rateUnit":self.rateUnit,
                    "pingUnit": self.pingUnit,}
        return tempDict

    """Print speed test results to CLI.
    Args:
        None.
    Returns:
        None.
    """
    def print_results(self):
            print ("connection speed")
            print("============================")
            print(f"timestamp: {self.timestamp}")
            print(f"server: {self.server}")
            print(f"ping: {self.ping} {self.pingUnit}")
            print(f"download: {self.download} {self.rateUnit}")
            print(f"upload: {self.upload} {self.rateUnit}")
            print("============================\n\n")
        
        

#class defining speed test object
class SpeedTest:
    def __init__(self, printFlag=True):
        self._printFlag = printFlag
        self._testData = SpeedTestData()
        
        #try to connect to speedtest broker
        try:
            self._st = speedtest.Speedtest()
        #raise custom error if could not connect
        except speedtest.ConfigRetrievalError:
            self._st = None
            raise("ConnectionError: could not establish connection to server.")
                
            
    
    """Run speed test to the 'best' server.
    Args:
        None.
    Returns:
        None. 
    """
    def run_bestTest(self):
        #optional print header
        if self._printFlag:
            print("fetching internet speed data, please wait.")
            
        #perform internet speed test with closest available server
        self._st.get_servers()
        self._st.get_best_server()
        self._st.download()
        self._st.upload()
        
        #format speedtest data to object data fields
        self._testData.timestamp = datetime.now()
        self._testData.server = self._st.results.server["name"]
        self._testData.download = float(str(self._st.results.download/1e6)[0:5])
        self._testData.upload = float(str(self._st.results.upload/1e6)[0:5])
        self._testData.ping = float(str(self._st.results.ping)[0:5])
        
        if self._printFlag:
            self._testData.print_results()
        
        
    """Returns test data dictionary to caller.
    Args:
        None.
    Returns: 
        Test data dictionary.
    """
    def get_testData(self):
        return self._testData.toDict()