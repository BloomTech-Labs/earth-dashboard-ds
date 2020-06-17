import os, pathlib
import pytest

os.chdir( pathlib.Path.cwd() / 'FLASK_RC1/application/test.py' )

pytest.main()
