"""DjAI Run-Command Utilities."""


from contextlib import AbstractContextManager
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


class HandleManagePy(AbstractContextManager):
    """Handle `manage.py` file."""

    def __enter__(self):
        """Add `manage.py` file, if applicable."""
        # pylint: disable=attribute-defined-outside-init
        self._manage_py_missing = not Path(_MANAGE_PY_FILE_NAME).exists()

        if self._manage_py_missing:
            shutil.copyfile(src=_MANAGE_PY_FILE_SRC_PATH,
                            dst=_MANAGE_PY_FILE_NAME,
                            follow_symlinks=False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove `manage.py` file, if applicable."""
        if self._manage_py_missing:
            os.remove(path=_MANAGE_PY_FILE_NAME)
            assert not Path(_MANAGE_PY_FILE_NAME).exists()


class HandleServerFiles(AbstractContextManager):
    """Handle `asgi.py`/`wsgi.py` file & Procfile."""

    def __init__(self, asgi: Optional[str] = None):
        """Initialize context manager."""
        self.asgi = asgi

    def __enter__(self):
        """Add `asgi.py`/`wsgi.py` file & Procfile, if applicable."""
        if self.asgi:
            assert not Path(_ASGI_PY_FILE_NAME).exists()
            shutil.copyfile(src=_ASGI_PY_FILE_SRC_PATH,
                            dst=_ASGI_PY_FILE_NAME,
                            follow_symlinks=False)

            assert not Path(_PROCFILE_NAME).exists()
            shutil.copyfile(src=(_SERVER_FILES_DIR_PATH /
                                 f'{_PROCFILE_NAME}.{self.asgi.capitalize()}'),
                            dst=_PROCFILE_NAME,
                            follow_symlinks=False)

        else:
            assert not Path(_WSGI_PY_FILE_NAME).exists()
            shutil.copyfile(src=_WSGI_PY_FILE_SRC_PATH,
                            dst=_WSGI_PY_FILE_NAME,
                            follow_symlinks=False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove `asgi.py`/`wsgi.py` file & Procfile, if applicable."""
        if self.asgi:
            os.remove(path=_ASGI_PY_FILE_NAME)
            assert not Path(_ASGI_PY_FILE_NAME).exists()
            os.remove(path=_PROCFILE_NAME)
            assert not Path(_PROCFILE_NAME).exists()

        else:
            os.remove(path=_WSGI_PY_FILE_NAME)
            assert not Path(_WSGI_PY_FILE_NAME).exists()


class HandleGitHash(AbstractContextManager):
    """Handle `Procfile` file."""

    def __enter__(self):
        """Add `.git-hash` file if applicable."""
        assert not Path(_GIT_HASH_FILE_NAME).exists()

        # pylint: disable=attribute-defined-outside-init
        self.git_hash = get_git_repo_head_commit_hash()

        if self.git_hash:
            with open(file=_GIT_HASH_FILE_NAME,
                      mode='w',
                      buffering=-1,
                      encoding='utf-8',
                      errors='strict',
                      newline=None,
                      closefd=True,
                      opener=None) as opened_file:
                opened_file.write(self.git_hash)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove `.git-hash` file, if applicable."""
        if self.git_hash:
            os.remove(path=_GIT_HASH_FILE_NAME)
            assert not Path(_GIT_HASH_FILE_NAME).exists()


def run_cmd(command: str,
            asgi: Optional[str] = None):
    """Run a certain CLI command."""
    with HandleManagePy(), HandleServerFiles(asgi=asgi), HandleGitHash():
        os.system(command=command)
