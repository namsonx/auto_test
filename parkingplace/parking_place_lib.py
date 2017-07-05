#This module defines the libs for parking place 
#Author: Son Mai

import sys
import os
import logging

class parking_place(object):
    '''
    This is base class for parking place
    '''
    
    def __init__(self, place_id, **kwargs):
        self.id = place_id
        