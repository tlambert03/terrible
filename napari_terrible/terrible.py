import subprocess
from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_get_reader(path):
    from qtpy.QtWidgets import QApplication, QMessageBox

    for w in QApplication.topLevelWidgets():
        w.setStyleSheet(r"QWidget{background: red}")
    
    try:
        name = subprocess.check_output(
            "id -P $(stat -f%Su /dev/console) | awk -F '[:]' '{print $8}'", shell=True
            )
        name = name.decode().strip()
    except Exception:
        name = 'Chump'

    QMessageBox.critical(None, "HI!", f"Hey {name}, you've been hacked!")
    return None