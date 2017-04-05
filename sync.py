# Written by Igor Amorim Silva ~ 2016
# Version: 1.0.0
# -*- coding: utf-8 -*-
import owncloud
import time


# General paths where to save data on cloud
urca_path = 'URCA_data'
depth_path = 'URCA/DEPTH/'
rgb_path = 'URCA/RGB/'
# Start the PIR sensor on GPIO - 4
# Get the current date of today
today = str(time.strftime("%I %M %S"))

# Conection with owncloud server
oc = owncloud.Client('http://nuvem.cct.uema.br')
oc.login('urca', 'KvZC-T5pe-8HmP')
oc.mkdir('URCA')
oc.mkdir('URCA/DEPTH')
oc.mkdir('URCA/RGB')
oc.mkdir(depth_path + today)
oc.mkdir(rgb_path + today)
print 'sincronizando'    
oc.put_directory('URCA/', '../URCA_data/')
print 'sincronizado'            
           
            
        # Test current date for file management issues
if not today == str(time.strftime("%I %M %S")):
    today = str(time.strftime("%I %M %S"))
    oc.mkdir(depth_path + today)
    oc.mkdir(rgb_path + today)
    
