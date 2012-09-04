'''
Created on 05/10/2011

@author: Evaldo
'''

from PyQt4 import QtGui, QtCore
from QQuantidade import Ui_QQuantidade


class QNumSorteioIMP(QtGui.QDialog,Ui_QQuantidade):
    '''
    classdocs
    '''

    def __init__(self,parent):
        '''
        Constructor
        '''
        
        super(QNumSorteioIMP, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.action_ok, QtCore.SIGNAL('triggered()'),self.__sair)
        self.connect(self.pushButtonOk,QtCore.SIGNAL('clicked()'),self.action_ok, QtCore.SIGNAL('triggered()'))
        
    def __sair(self):
        print 'saindo'
        self.close()