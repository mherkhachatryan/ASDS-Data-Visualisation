from pathlib import Path
import os

_package_path = Path(os.path.dirname(os.path.abspath(__file__)))
_data_folder = Path(_package_path.parents[0], "data")
data_path = str(list(_data_folder.glob("*csv"))[0])
