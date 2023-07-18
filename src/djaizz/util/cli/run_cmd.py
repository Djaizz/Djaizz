"""Djaizz Run-Command Utilities."""


from contextlib import AbstractContextManager
import os
from pathlib import Path
import shutil
from typing import Optional


from ..git import _GIT_HASH_FILE_NAME, get_git_repo_head_commit_hash


_SERVER_FILES_DIR_PATH: Path = Path(__file__).parent / '_server_files'


class ManagePyHandling(AbstractContextManager):
    """Handle `manage.py` file."""

    MANAGE_PY_FILE_NAME: str = 'manage.py'
    MANAGE_PY_FILE_SRC_PATH: Path = _SERVER_FILES_DIR_PATH / MANAGE_PY_FILE_NAME   # noqa: E501

    def __init__(self):
        """Initialize context manager."""
        self.manage_py_missing: bool = not Path(self.MANAGE_PY_FILE_NAME).exists()   # noqa: E501

    def __enter__(self):
        """Add `manage.py` file, if applicable."""
        if self.manage_py_missing:
            shutil.copyfile(src=self.MANAGE_PY_FILE_SRC_PATH,
                            dst=self.MANAGE_PY_FILE_NAME,
                            follow_symlinks=False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove `manage.py` file, if applicable."""
        if self.manage_py_missing:
            os.remove(path=self.MANAGE_PY_FILE_NAME)


class SGIFilesHandling(AbstractContextManager):
    """Handle `asgi.py`/`wsgi.py` file & Procfile."""

    ASGI_PY_FILE_NAME: str = 'asgi.py'
    ASGI_PY_FILE_SRC_PATH: Path = _SERVER_FILES_DIR_PATH / ASGI_PY_FILE_NAME

    WSGI_PY_FILE_NAME: str = 'wsgi.py'
    WSGI_PY_FILE_SRC_PATH: Path = _SERVER_FILES_DIR_PATH / WSGI_PY_FILE_NAME

    PROCFILE_NAME: str = 'Procfile'

    def __init__(self, asgi: Optional[str] = None):
        """Initialize context manager."""
        self.asgi: Optional[str] = asgi

        if self.asgi:
            self.asgi_py_missing: bool = not Path(self.ASGI_PY_FILE_NAME).exists()   # noqa: E501
            self.procfile_missing: bool = not Path(self.PROCFILE_NAME).exists()

        else:
            self.wsgi_py_missing: bool = not Path(self.WSGI_PY_FILE_NAME).exists()   # noqa: E501

    def __enter__(self):
        """Add `asgi.py`/`wsgi.py` file & Procfile, if applicable."""
        if self.asgi:
            if self.asgi_py_missing:
                shutil.copyfile(src=self.ASGI_PY_FILE_SRC_PATH,
                                dst=self.ASGI_PY_FILE_NAME,
                                follow_symlinks=False)

            if self.procfile_missing:
                shutil.copyfile(
                    src=(_SERVER_FILES_DIR_PATH /
                         f'{self.PROCFILE_NAME}.{self.asgi.capitalize()}'),
                    dst=self.PROCFILE_NAME,
                    follow_symlinks=False)

        elif self.wsgi_py_missing:
            shutil.copyfile(src=self.WSGI_PY_FILE_SRC_PATH,
                            dst=self.WSGI_PY_FILE_NAME,
                            follow_symlinks=False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove `asgi.py`/`wsgi.py` file & Procfile, if applicable."""
        if self.asgi:
            if self.asgi_py_missing:
                os.remove(path=self.ASGI_PY_FILE_NAME)

            if self.procfile_missing:
                os.remove(path=self.PROCFILE_NAME)

        elif self.wsgi_py_missing:
            os.remove(path=self.WSGI_PY_FILE_NAME)


class GitHashHandling(AbstractContextManager):
    """Handle `Procfile` file."""

    def __init__(self):
        """Initialize context manager."""
        self.git_hash: Optional[str] = get_git_repo_head_commit_hash()

    def __enter__(self):
        """Add `.git-hash` file if applicable."""
        if self.git_hash:
            assert not Path(_GIT_HASH_FILE_NAME).exists()

            with open(file=_GIT_HASH_FILE_NAME,
                      mode='wt',
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


def run_cmd(command: str,
            asgi: Optional[str] = None):
    """Run a CLI command."""
    with ManagePyHandling(), SGIFilesHandling(asgi=asgi), GitHashHandling():
        os.system(command=command)
