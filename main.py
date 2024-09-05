from PySide6.QtWidgets import QApplication
import sys
from ui.battery_alert import Battery_alert 


app = QApplication(sys.argv);

mainWindow = Battery_alert();

mainWindow.show();


app.exec()
