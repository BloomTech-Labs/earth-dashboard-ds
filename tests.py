import os, pathlib
import pytest

os.chdir( pathlib.Path.cwd() / 'application' )

pytest.main()
