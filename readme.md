# MY Patrick Visual IVR Integration

## Dependancys

* Python 2.6+
* pip
* Pyst2
* nohup (For running SocketServer off of the command line)
* Port 8020

## Installation

1. Use pip to install Pyst2 -> `pip install pyst2` 
2. Run `chmod 777` on containing directory (for sqlite) and on the file `agi-reroute.py`
    * `chmod 777 /path/to/mypatrickAGI`
    * `chmod 777 /path/to/mypatrickAGI/agi-rerote.py`
        * Please note that the AGI script is a __*prototype*__ and relies on other files in the folder such as `sqlite3test.py` and `test.db`

### How To Start MyPatrick Python SimpleSocket Server *Detached* From Terminal Instance

     nohup python pyServer.py >> /dev/null 2>&1 &


## Setup

1. Add the following to your asterisk DialPlan (generally found at `/etc/asterisk/extensions.conf` on FreePBX it is located at `etc/asterisk/extensions_custom.conf`)
    
        [my-patrick-proto]
        exten => 66,1,AGI(/path/to/mypatrickAGI/agi-rerote.py)
        exten => 66,n,Goto(namespace,extension,position)

2. Replace namespace,extension,position with the failover for if the CallerID is not in the database.
    * For some reason the integrated FreePBX failover is not working. TODO Fix

3. Direct the trunk you want to test to `my-patrick-proto,66,1` (generally with `Goto()`)


