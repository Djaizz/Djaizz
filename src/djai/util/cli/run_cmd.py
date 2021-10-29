"""DjAI Run-Command Utilities."""


import os
from pathlib import Path
import shutil
from typing import Optional


from ..git import _GIT_HASH_FILE_NAME, get_git_repo_head_commit_hash


_SERVER_FILES_DIR_PATH = Path(__file__).parent / '_server_files'

_ASGI_PY_FILE_NAME = 'asgi.py'
_ASGI_PY_FILE_SRC_PATH = _SERVER_FILES_DIR_PATH / _ASGI_PY_FILE_NAME

_WSGI_PY_FILE_NAME = 'wsgi.py'
_WSGI_PY_FILE_SRC_PATH = _SERVER_FILES_DIR_PATH / _WSGI_PY_FILE_NAME

_PROCFILE_NAME = 'Procfile'


def run_cmd(command: str,
            copy_standard_files: bool = False,
            asgi: Optional[str] = None):
    """Run a certain CLI command."""
    if copy_standard_files:
        if asgi:
            assert not os.path.exists(path=_ASGI_PY_FILE_NAME)
            shutil.copyfile(
                src=_ASGI_PY_FILE_SRC_PATH,
                dst=_ASGI_PY_FILE_NAME)
            assert not os.path.exists(path=_PROCFILE_NAME)
            shutil.copyfile(
                src=(_SERVER_FILES_DIR_PATH /
                     f'{_PROCFILE_NAME}.{asgi.capitalize()}'),
                dst=_PROCFILE_NAME)
        else:
            assert not os.path.exists(path=_WSGI_PY_FILE_NAME)
            shutil.copyfile(
                src=_WSGI_PY_FILE_SRC_PATH,
                dst=_WSGI_PY_FILE_NAME)

        assert not os.path.exists(path=_GIT_HASH_FILE_NAME)
        git_hash = get_git_repo_head_commit_hash()
        if git_hash:
            with open(_GIT_HASH_FILE_NAME, 'w') as f:
                f.write(git_hash)

    os.system(command=command)

    if copy_standard_files:
        if asgi:
            os.remove(_ASGI_PY_FILE_NAME)
            assert not os.path.exists(path=_ASGI_PY_FILE_NAME)
            os.remove(_PROCFILE_NAME)
            assert not os.path.exists(path=_PROCFILE_NAME)
        else:
            os.remove(_WSGI_PY_FILE_NAME)
            assert not os.path.exists(path=_WSGI_PY_FILE_NAME)

        if git_hash:
            os.remove(_GIT_HASH_FILE_NAME)
            assert not os.path.exists(path=_GIT_HASH_FILE_NAME)
