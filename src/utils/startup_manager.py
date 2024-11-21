import os
import sys
import winreg
import logging

logger = logging.getLogger(__name__)


def get_app_path() -> str:
    """Get the path to the executable or script"""
    if getattr(sys, "frozen", False):
        return sys.executable
    return os.path.abspath(sys.argv[0])


def set_startup_registry(enable: bool) -> bool:
    """Set or remove the application from Windows startup registry"""
    try:
        app_path = get_app_path()
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE | winreg.KEY_QUERY_VALUE,
        )

        if enable:
            escaped_path = app_path.strip('"')  # Remove existing quotes if present
            winreg.SetValueEx(key, "QRGrabber", 0, winreg.REG_SZ, f'"{escaped_path}"')
        else:
            try:
                winreg.DeleteValue(key, "QRGrabber")
            except FileNotFoundError:
                pass

        winreg.CloseKey(key)
        return True
    except Exception as e:
        logger.error(f"Failed to modify startup registry: {e}")
        return False


def is_startup_enabled() -> bool:
    """Check if the application is set to run at startup"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_READ,
        )
        try:
            winreg.QueryValueEx(key, "QRGrabber")
            return True
        except FileNotFoundError:
            return False
        finally:
            winreg.CloseKey(key)
    except Exception:
        return False
