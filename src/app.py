from PyQt6 import QtWidgets
import sys
sys.path.append('D:/учеба/бд/курсач/brewery/front/authorisation')
from authorisation_window import AuthorisationWindow
            
app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(500)
widget.setFixedHeight(450)
window = AuthorisationWindow(app_widget=widget)
widget.addWidget(window)
widget.show()
app.exec()
