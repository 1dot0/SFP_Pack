"""
Toxicity is a program which can be controlled by SFP_Queen.
It scans the networks nearby and save all of the data of those in the SFP_Mercury Database.
"""

import subprocess
import sqlite3
import geo
import socket
import re

data = {
    'HostMac' : '',
    'HostName' : '',
    'HostIP' : '',
    'HostNetMask' : '',
    'HostsLatitude' : '',
    'HostsLongitude' : '',
    'CountriesID' : '',
    'CountriesName' : '',
    'CountriesContinent' : '',
    'RegionsName' : '',
    'TimezonesName' : '',
}

def getHostNetmask():
    pass

def getHostMac(ipAdd):
    try:
        result = subprocess.check_output(['nmap', '-sP', ipAdd])
        mac_address = re.search(r'MAC Address: (.*?)\n', result.decode())[1]
        return mac_address
    except subprocess.CalledProcessError:
        return '?'

def NetworkScan():
    pass

def populateDatabase():
    pass

def getHostInfo():
    data['HostName'] = socket.gethostname()
    data['HostIP'] = geo.getIP()
    #data['HostMac'] = getHostMac()
    
    data['HostMac'] = getHostMac(data['HostIP'])
    #data['HostNetMask'] = getHostNetmask()
    geodata = geo.getGeoData(data['HostIP'])
    data['HostsLatitude'] = geodata['latitude']
    data['HostsLongitude'] = geodata['longitude']
    data['CountriesID'] = geodata['country_code']
    data['CountriesName'] = geodata['country']
    data['CountriesContinent'] = geodata['continent_code']
    #data['RegionsName'] = geodata['region']
    data['TimezonesName'] = geodata['timezone']
    print(data)

getHostInfo()