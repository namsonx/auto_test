#This module defines the objects for parking place 
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
        
    def create_parkingplace(self, server_ip, port):
        ser_ip = server_ip
        ser_port = port
        
class parking_lot(object):
    '''
    This is base class for parking lot
    '''
    def __init__(self, lot_id, place_id, **kwargs):
        self.id = lot_id
        self.place = place_id
        self.name = ''
        self.unicode = ''
        self.createby = ''
        self.availability = 0
        
class parking_block(object):
    '''
    This is base class for parking block
    '''
    def __init__(self, block_id, place_id, lot_id = None, **kwargs):
        self.id = block_id
        self.place = place_id