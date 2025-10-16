import subprocess
import shutil

project_path = "/Users/francescapanteli/Desktop/CodingNomads-python-SQL-and-Databases-MySQL"

if shutil.which("charm") is None:
    print("Error: PyCharm command-line launcher 'charm' not found. Enable it via PyCharm → Tools → Create Command-line Launcher.")
else:
    subprocess.run(["charm", project_path])