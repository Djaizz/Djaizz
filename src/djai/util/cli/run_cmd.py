"""DjAI Run-Command Utilities."""


import os
from pathlib import Path
import shutil
from typing import Optional


from ..git import _GIT_HASH_FILE_NAME, get_git_repo_head_commit_hash


_SERVER_FILES_DIR_PATH = Path(__file__).parent / '_server_files'

_MANAGE_PY_FILE_NAME = 'manage.py'
_MANAGE_PY_FILE_SRC_PATH = _SERVER_FILES_DIR_PATH / _MANAGE_PY_FILE_NAME

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
        _manage_py_missing = not Path(_MANAGE_PY_FILE_NAME).exists()
        if _manage_py_missing:
            shutil.copyfile(src=_MANAGE_PY_FILE_SRC_PATH,
                            dst=_MANAGE_PY_FILE_NAME,
                            follow_symlinks=False)

        if asgi:
            assert not Path(_ASGI_PY_FILE_NAME).exists()
            shutil.copyfile(src=_ASGI_PY_FILE_SRC_PATH,
                            dst=_ASGI_PY_FILE_NAME,
                            follow_symlinks=False)

            assert not Path(_PROCFILE_NAME).exists()
            shutil.copyfile(src=(_SERVER_FILES_DIR_PATH /
                                 f'{_PROCFILE_NAME}.{asgi.capitalize()}'),
                            dst=_PROCFILE_NAME,
                            follow_symlinks=False)

        else:
            assert not Path(_WSGI_PY_FILE_NAME).exists()
            shutil.copyfile(src=_WSGI_PY_FILE_SRC_PATH,
                            dst=_WSGI_PY_FILE_NAME,
                            follow_symlinks=False)

        assert not Path(_GIT_HASH_FILE_NAME).exists()
        git_hash = get_git_repo_head_commit_hash()
        if git_hash:
            with open(file=_GIT_HASH_FILE_NAME,
                      mode='w',
                      buffering=-1,
                      encoding='utf-8',
                      errors='strict',
                      newline=None,
                      closefd=True,
                      opener=None) as opened_file:
                opened_file.write(git_hash)

    os.system(command=command)

    if copy_standard_files:
        if _manage_py_missing:
            os.remove(path=_MANAGE_PY_FILE_NAME)
            assert not Path(_MANAGE_PY_FILE_NAME).exists()

        if asgi:
            os.remove(path=_ASGI_PY_FILE_NAME)
            assert not Path(_ASGI_PY_FILE_NAME).exists()
            os.remove(path=_PROCFILE_NAME)
            assert not Path(_PROCFILE_NAME).exists()

        else:
            os.remove(path=_WSGI_PY_FILE_NAME)
            assert not Path(_WSGI_PY_FILE_NAME).exists()

        if git_hash:
            os.remove(path=_GIT_HASH_FILE_NAME)
            assert not Path(_GIT_HASH_FILE_NAME).exists()
