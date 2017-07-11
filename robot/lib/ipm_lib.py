'''
This module is define libs for ipm
author: Son Mai
'''

import os
import sys
#import lib.objects
import requests
import json


def get_place_info(place_id = None, place_name = ''):
    print 'Starting get place infog'
    
def create_parking_place(place_name = "autotest", unicode = "uni012", parktype = 0, **kwargs):
    if kwargs.get('passRuleName'):
        passrule = kwargs.passRuleName
    else:
        passrule = "24hr"
    
    if kwargs.get('createBy'):
        createby = kwargs.createBy
    else:
        createby = "Admin"
    
    if kwargs.get('longitude') and kwargs.get('latitude'):
        long = kwargs.longtitude
        lat = kwargs.latitude
    else:
        long = 77.61259979044553
        lat = 12.935567399778256
        
    if kwargs.get('autoExit'):
        autoexit = kwargs.autoExit
    else:
        autoexit = "Yes"
        
    if kwargs.get('availability'):
        avai = kwargs.availability 
    else:
        avai = 0
              
    headers = {"content-type": "application/json"}
    data = {"placeName": place_name, "unicode": unicode, "autoExit": autoexit, "availability": avai, "createdBy": createby, "lang": long, "lat": lat, "park_type": parktype, "passRuleName": passrule} 
    r = requests.post('http://localhost:50201/admin/createParkingPlace', data=json.dumps(data), headers=headers)
    
    
    if r.status_code == 200:
        return r
    else:
        print (r.status_code, r.reason)
        return r.status_code
    