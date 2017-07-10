'''
This module is define libs for ipm
author: Son Mai
'''

import os
import sys
import lib.objects


def get_place_info(place_id = None, place_name = ''):
    print 'Starting get place infog'
    
def create_parking_place(place_name, unicode, parktype = 0, **kwargs):
    if kwargs.get('passrule'):
        passrule = kwargs.passrule
    else:
        passrule = '24hr'
    
    if kwargs.get('createby'):
        createby = kwargs.createby
    else:
        createby = 'Admin'
    
    if kwargs.get('longitude') and kwargs.get('latitude'):
        long = kwargs.longtitude
        lat = kwargs.latitude
    else:
        long = 77.61259979044553
        lat = 12.935567399778256
        
    