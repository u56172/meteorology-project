from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QSlider
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class JetStreamView(QWidget):
    def __init__(self, xrds_week, pressure_levels):
        super().__init__()

        self.xrds_week = xrds_week
        self.pressure_levels = pressure_levels

        self.setWindowTitle('Jetstream App')
        self.setGeometry(225, 225, 300, 225)

        main_layout = QHBoxLayout()
        control_layout = QVBoxLayout()
        plot_layout = QVBoxLayout()

        main_layout.addLayout(control_layout, 1)
        main_layout.addLayout(plot_layout, 3)

        # Elementy GUI
        control_layout.addWidget(QLabel("Select day:"))
        self.day_box = QComboBox()
        self.day_box.addItems(xrds_week.keys())
        control_layout.addWidget(self.day_box)

        control_layout.addWidget(QLabel("Pressure level (100–400 hPa):"))
        self.level_slider = QSlider(Qt.Horizontal)
        self.level_slider.setMinimum(0)
        self.level_slider.setMaximum(6)
        self.level_slider.setValue(3)
        self.level_slider.setTickInterval(1)
        self.level_slider.setTickPosition(QSlider.TicksBelow)
        control_layout.addWidget(self.level_slider)

        self.level_label = QLabel(f"Current level: {pressure_levels[3]} hPa")
        control_layout.addWidget(self.level_label)

        control_layout.addWidget(QLabel('Colormap:'))
        self.cmap_box = QComboBox()
        self.cmap_box.addItems([
            'viridis', 'plasma', 'inferno', 'magma', 'coolwarm', 'jet', 'twilight', 'turbo'
        ])
        control_layout.addWidget(self.cmap_box)

        self.btn_generate = QPushButton("Generate Jetstream")
        self.btn_pdf = QPushButton("Save as PDF")
        self.btn_tif = QPushButton("Save as TIFF")
        self.btn_clear = QPushButton("Clear")
        self.btn_exit = QPushButton("Exit")

        for btn in [self.btn_generate, self.btn_pdf, self.btn_tif, self.btn_clear, self.btn_exit]:
            control_layout.addWidget(btn)

        control_layout.addStretch()

        self.canvas = FigureCanvas(Figure(figsize=(8, 5)))
        plot_layout.addWidget(self.canvas)
        self.ax = None

        self.setLayout(main_layout)
