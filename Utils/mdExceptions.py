'''
Created on Oct 5, 2011

@author: evaldo
'''

class TipoLoteriaException(Exception):
    '''
    classdocs
    '''
    def __init__(self, value):
        self.value = value
    
    
    def __str__(self):
        return repr(self.value)    
        