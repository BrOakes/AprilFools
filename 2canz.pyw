import ctypes
import os
cwd = os.getcwd()
image = "328365.jpg"
image_path = os.path.join(cwd, image)
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
