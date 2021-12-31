"""
author(s): A. Tabulog
date: 12/30/21
email: austin.tabulog@gmail.com

=========================================================
This file is subject to the MIT license copyright notice.
=========================================================
"""

#imports
import speedtest
from datetime import datetime

#formatted data class
class simpledataStruct:
    def __init__(self, serverName, download, upload, ping):
        self._server = serverName
        self._download:str = str(download/1e6)[0:5]
        self._upload:str = str(upload/1e6)[0:5]
        self._ping:str = str(ping)
        self._updownUnit = "Mb/s"
        self._pingUnit = "ms"
    
    def print_cliPacket(self):
        print ("connection speed")
        print("============================")
        print(f"timestamp: {datetime.now()}")
        print(f"server: {self._server}")
        print(f"download: {self._download} {self._updownUnit}")
        print(f"upload: {self._upload} {self._updownUnit}")
        print(f"ping: {self._ping} {self._pingUnit}")
        print("============================\n\n")
        


#main
if __name__ == "__main__":    
    #if proper connection made
    try:
        #create speed test connection
        st = speedtest.Speedtest()
        
        #perform internet speed test with closest available server
        print("fetching internet speed data, please wait.")
        st.get_servers(); st.get_best_server()
        st.download(); st.upload()
        
        #load data into formatting object
        results = simpledataStruct(st.results.server["name"], st.results.download, st.results.upload, st.results.ping)
        #present data to CLI
        results.print_cliPacket()
        
    #else no connection made
    except speedtest.ConfigRetrievalError:
        print("ConnectionError:could not connect to server.")
    