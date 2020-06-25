import os, pathlib
import pytest

os.chdir( pathlib.Path.cwd() /FLASK/application )

pytest.main()
