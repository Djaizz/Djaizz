"""Djaizz Git-related Utilities."""


from pathlib import Path
from sys import version_info
from typing import Optional

from git.exc import InvalidGitRepositoryError   # pylint: disable=import-error
from git.repo.base import Repo   # pylint: disable=import-error

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = ('get_git_repo_head_commit_hash',)


_GIT_HASH_FILE_NAME: str = '.git-hash'


def get_git_repo_head_commit_hash(path: Optional[str] = None) -> Optional[str]:
    """Get Git Repo Head Commit Hash."""
    try:
        repo: Repo = Repo(path=path,
                          search_parent_directories=True,
                          expand_vars=True)

        return repo.head.commit.hexsha

    except InvalidGitRepositoryError:
        if Path(_GIT_HASH_FILE_NAME).is_file():
            with open(file=_GIT_HASH_FILE_NAME,
                      mode='rt',
                      buffering=-1,
                      encoding='utf-8',
                      errors='strict',
                      newline=None,
                      closefd=True,
                      opener=None) as opened_file:
                return opened_file.read()

        else:
            return None
