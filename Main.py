'''
Created on 04/10/2011

@author: Evaldo
'''

from PyQt4 import QtGui
from UI.QfrmPrincipalIMP import QfrmPrincipalIMP


if __name__ == '__main__':
    print 'iniciou'
    app = QtGui.QApplication([])
    frm = QfrmPrincipalIMP()
    frm.show()

    app.exec_()
    print 'fim'
