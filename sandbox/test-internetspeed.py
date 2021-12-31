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


#main
if __name__ == "__main__":
    print("fetching internet speed data, please wait.")
    st = speedtest.Speedtest()
    st.get_servers(); st.get_best_server()
    st.download(); st.upload()
    results = st.results.dict()
    
    print("Speed data collected. \n\n")
    print ("connection speed")
    print("============================")
    print(f"server: {st.results.server['name']}")
    print(f"download: {str(results['download']/1e6)[0:5]} Mb/s")
    print(f"upload: {str(results['upload']/1e6)[0:5]} Mb/s")
    print(f"ping: {results['ping']} ms")
    print("============================\n\n")