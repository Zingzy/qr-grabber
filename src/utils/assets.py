import sys
import os


def get_asset_path(relative_path):
    """Get the absolute path to an asset, handling PyInstaller paths."""
    if getattr(sys, "frozen", False):  # If running as a PyInstaller EXE
        base_path = sys._MEIPASS
    else:  # If running in development
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


app_icon_png = get_asset_path("../../assets/icon.png")
app_icon_ico = get_asset_path("../../assets/icon.ico")
