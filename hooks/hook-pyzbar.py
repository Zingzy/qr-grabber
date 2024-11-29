from PyInstaller.utils.hooks import collect_data_files

# Collect data files for pyzbar (e.g., DLLs like libiconv.dll)
datas = collect_data_files("pyzbar")
