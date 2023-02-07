
"""
Toxicity is a program which can be controlled by SFP_Queen.
It scans the networks nearby and save all of the data of those in the SFP_Mercury Database.
"""

import subprocess
import sqlite3

def get_network_list():
    output = []
    raw = subprocess.check_output(['netsh', 'wlan', 'show', 'network']).decode("ascii")
    
    # split on blank line
    raw = raw.strip().replace("\r", "").split("\n\n")[1:]

    for i in range(len(raw)):
        net = raw[i].strip().replace("\r", "").split("\n")

        output.append({
            "SSID": net[0].split(":")[1].strip(),
            "Type": net[1].split(":")[1].strip(),
            "AuthType": net[2].split(":")[1].strip(),
            "CryptType": net[3].split(":")[1].strip(),
        })

    return output

def populateDatabase(networkList):
    #Connects to SFP_Mercury Database
    conn = sqlite3.connect('SFP_Mercury.db')
    c = conn.cursor()
    
    #Insert Data into the table
    for item in networkList:
        c.execute(f'INSERT INTO mytable({", ".join(item.keys())}) VALUES({", ".join("?" * len(item))})', tuple(item.values()))

    #saves changes and closes connection
    conn.commit()
    conn.close()

networkList = get_network_list()
#populateDatabase(networkList)
#print(networkList)
#for i in range(len(networkList)):
#   print(f"Network: {wifiList[i]}")
