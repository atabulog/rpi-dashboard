# rpi-dashboard
QT based web app for basic rpi-hosted dashboard.

## Overview
The rpi-dashboard is a web app hosted on a simple raspberry pi home server. The purpose of this application is to display basic home network data in a clean and clear UI. 

## Features
For the first iteration, the rpi-dashboard will only display network connection speeds. The dashboard will keep a log of the sample timestamp, the host server, ping time, and upload and download rates. This log will contain a week's worth of data that's polled every 5 minutes. The log will hold data for the past week's connectivity, then start dumping data to maintain a reasonable size.

### LEFT OFF
1. mysql is running on rpi and collecting network speed data every 5 minutes using crontab
2. no interface has bee built for this yet

### TODO
1. Need to setup a way for the db to act as a rolling buffer, getting rid of old data
2. build qt web app hosted on pi to display network data as a tab on the dashboard
3. write test to get closest available server, not 'best' server.
