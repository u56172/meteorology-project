import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from jetstream_plotter.model import xrds_week, pressure_levels, boundry_box_usa, specific_level, wind_vel

class JetStreamController:
    def __init__(self, view):
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.level_slider.valueChanged.connect(self.update_level_label)
        self.view.btn_generate.clicked.connect(self.generate_plot)
        self.view.btn_pdf.clicked.connect(self.save_pdf)
        self.view.btn_tif.clicked.connect(self.save_tif)
        self.view.btn_clear.clicked.connect(self.clear_plot)
        self.view.btn_exit.clicked.connect(self.view.close)

    def update_level_label(self, idx):
        level = pressure_levels[idx]
        self.view.level_label.setText(f"Current level: {level} hPa")

    def generate_plot(self):
        day = self.view.day_box.currentText()
        idx = self.view.level_slider.value()
        level = pressure_levels[idx]
        cmap = self.view.cmap_box.currentText()
        ds = xrds_week[day]

        usa = boundry_box_usa(ds)
        layer = specific_level(usa, level).isel(time=0)
        u = layer["ugrdprs"].load()
        v = layer["vgrdprs"].load()
        wind = wind_vel(u, v)

        self.view.canvas.figure.clf()
        ax = self.view.canvas.figure.add_subplot(111, projection=ccrs.PlateCarree())
        ax.coastlines()
        ax.set_extent([230, 300, 10, 70])

        im = ax.pcolormesh(layer["lon"], layer["lat"], wind, cmap=cmap, transform=ccrs.PlateCarree())
        self.view.canvas.figure.colorbar(im, ax =ax, label="Wind speed [m/s]")
        ax.set_title(f"JETSTREAM {level} hPa — {day}")
        self.view.canvas.draw()

    def save_pdf(self):
        self.view.canvas.figure.savefig("jetstream_output.pdf")
        print("Saved jetstream_output.pdf")

    def save_tif(self):
        self.view.canvas.figure.savefig("jetstream_output.tiff", dpi=300)
        print("Saved jetstream_output.tiff")

    def clear_plot(self):
        self.view.canvas.figure.clf()
        self.view.canvas.draw()
        print("Plot cleared.")
