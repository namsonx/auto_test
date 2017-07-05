#This module defines the libs for parking place 
#Author: Son Mai

import sys
import os
import logging
import requests

class parking_place(object):
    '''
    This is base class for parking place
    '''
    
    def __init__(self, place_id, **kwargs):
        self.id = place_id
        self.name = ''
        self.unicode = ''
        self.passrulename = ''
        self.createby = ''
        self.long = 0
        self.lat = 0
        self.parktype = 0
        
    def create_parkingplace(self):
        