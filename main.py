import sys
from PyQt5.QtWidgets import QApplication
from jetstream_plotter.view import JetStreamView
from jetstream_plotter.controller import JetStreamController
from jetstream_plotter.model import xrds_week, pressure_levels

def main():
    app = QApplication(sys.argv)
    view = JetStreamView(xrds_week, pressure_levels)
    controller = JetStreamController(view)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
