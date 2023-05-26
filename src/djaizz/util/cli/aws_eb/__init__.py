"""Djaizz AWS Elastic Beanstalk CLI."""


from contextlib import AbstractContextManager
import os
from pathlib import Path
from pprint import pprint
from shutil import copyfile, copytree, ignore_patterns
from typing import Optional

import click
from ruamel import yaml

from ..run_cmd import run_cmd


_DJAI_AWS_EB_CLI_UTIL_DIR_PATH: Path = Path(__file__).parent


_EC2_INSTANCE_TYPES_FILE_NAME: str = 'EC2-Instance-Types.yml'

with open(file=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / _EC2_INSTANCE_TYPES_FILE_NAME,
          mode='rt',
          buffering=-1,
          encoding='utf-8',
          errors='raise',
          newline=None,
          closefd=True,
          opener=None) as f:
    _EC2_INSTANCE_TYPES: dict = yaml.safe_load(stream=f, version=None)


_EB_EXTENSIONS_DIR_NAME: str = '.ebextensions'
_PLATFORM_DIR_NAME: str = '.platform'
_INSTALL_CUDA_SCRIPT_NAME: str = '.Install-CUDA'


class ConfigFilesHandling(AbstractContextManager):
    """Handle config/extension files, e.g., `.ebextensions`/`.platform`."""

    def __init__(self, config_dir_name: str, /, *, gpu: Optional[bool] = False):  # noqa: E501
        """Initialize context manager."""
        self.config_dir_name: str = config_dir_name
        self.config_dir_path: Path = _DJAI_AWS_EB_CLI_UTIL_DIR_PATH / config_dir_name  # noqa: E501
        self.gpu: bool = gpu

    def __enter__(self):
        """Add config/extension files."""
        copytree(
            src=self.config_dir_path,
            dst=self.config_dir_name,
            symlinks=False,
            ignore=(None
                    if self.gpu
                    else ignore_patterns(_INSTALL_CUDA_SCRIPT_NAME)),
            ignore_dangling_symlinks=False,
            dirs_exist_ok=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove config/extension files."""
        paths: list[Path] = list(self.config_dir_path.rglob(pattern='*'))

        for path in paths:
            if path.is_file() and (True
                                   if self.gpu
                                   else (path.name != _INSTALL_CUDA_SCRIPT_NAME)):  # noqa: E501
                os.remove(path=path.relative_to(_DJAI_AWS_EB_CLI_UTIL_DIR_PATH))  # noqa: E501

        # remove empty directories
        for path in (paths + [self.config_dir_path]):
            if path.is_dir() and \
                    (not any((dir_path :=
                              path.relative_to(_DJAI_AWS_EB_CLI_UTIL_DIR_PATH))
                             .iterdir())):
                dir_path.rmdir()


class EBIgnoreHandling(AbstractContextManager):
    """Handle `.ebignore` file."""

    EB_IGNORE_FILE_NAME: str = '.ebignore'

    def __init__(self):
        """Initialize context manager."""
        self.eb_ignore_exists: bool = Path(self.EB_IGNORE_FILE_NAME).exists()

        if self.eb_ignore_exists:
            with open(self.EB_IGNORE_FILE_NAME,
                      mode='rt',
                      buffering=-1,
                      encoding='utf-8',
                      errors='strict',
                      newline=None,
                      closefd=True,
                      opener=None) as eb_ignore_file:
                self.eb_ignore_content: list[str] = eb_ignore_file.readlines()

    def __enter__(self):
        """Add `.ebignore` file, if applicable."""
        if self.eb_ignore_exists:
            with (open(self.EB_IGNORE_FILE_NAME,
                       mode='at',
                       buffering=-1,
                       encoding='utf-8',
                       errors='strict',
                       newline=None,
                       closefd=True,
                       opener=None) as dst,
                  open(_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / self.EB_IGNORE_FILE_NAME,  # noqa: E501
                       mode='rt',
                       buffering=-1,
                       encoding='utf-8',
                       errors='strict',
                       newline=None,
                       closefd=True,
                       opener=None) as src):
                dst.writelines(src.readlines())

        else:
            copyfile(
                src=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / self.EB_IGNORE_FILE_NAME,
                dst=self.EB_IGNORE_FILE_NAME)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove `.ebignore` file, if applicable."""
        if self.eb_ignore_exists:
            with open(self.EB_IGNORE_FILE_NAME,
                      mode='wt',
                      buffering=-1,
                      encoding='utf-8',
                      errors='strict',
                      newline=None,
                      closefd=True,
                      opener=None) as eb_ignore_file:
                eb_ignore_file.writelines(self.eb_ignore_content)

        else:
            os.remove(path=self.EB_IGNORE_FILE_NAME)


@click.command(name='init',
               cls=click.Command,
               context_settings=None,
               help=('Djaizz AWS Elastic Beanstalk CLI: '
                     'Initialize Configuration >>>'),
               epilog=('^^^ Djaizz AWS Elastic Beanstalk CLI: '
                       'Initialize Configuration'),
               short_help='Djaizz AWS-EB Init',
               options_metavar='',
               add_help_option=True,
               hidden=False,
               deprecated=False)
def init():
    """Initialize Djaizz AWS Elastic Beanstalk Configuration."""
    os.system(command='eb init')


@click.command(name='deploy',
               cls=click.Command,
               context_settings=None,
               help='Djaizz AWS Elastic Beanstalk CLI: Deploy >>>',
               epilog='^^^ Djaizz AWS Elastic Beanstalk CLI: Deploy',
               short_help='Djaizz AWS-EB Deploy',
               options_metavar='[OPTIONS]',
               add_help_option=True,
               hidden=False,
               deprecated=False)
@click.argument('aws_eb_env_name',
                cls=click.Argument,
                required=False,
                type=str,
                default=None,
                callback=None,
                nargs=None,
                metavar='AWS_EB_ENV_NAME',
                expose_value=True,
                is_eager=False,
                envvar=None)
@click.option('--asgi',
              cls=click.Option,
              show_default=True,
              prompt=False,
              confirmation_prompt=False,
              hide_input=False,
              is_flag=False,
              # flag_value=...,
              multiple=False,
              count=False,
              allow_from_autoenv=False,
              type=str,
              help=('ASGI Server (daphne, hypercorn, uvicorn) to use '
                    '[default: None]'),
              show_choices=True,
              default=None,
              required=False,
              callback=None,
              nargs=None,
              metavar='ASGI',
              expose_value=True,
              is_eager=False,
              envvar=None)
@click.option('--gpu',
              cls=click.Option,
              show_default=True,
              prompt=False,
              confirmation_prompt=False,
              hide_input=False,
              is_flag=True,
              flag_value=True,
              multiple=False,
              count=False,
              allow_from_autoenv=False,
              type=bool,
              help='Whether to use GPU',
              show_choices=True,
              default=False,
              required=False,
              callback=None,
              nargs=None,
              metavar='GPU',
              expose_value=True,
              is_eager=False,
              envvar=None)
def deploy(aws_eb_env_name: Optional[str] = None,
           asgi: Optional[str] = None,
           gpu: Optional[bool] = False):
    """Deploy Djaizz onto AWS Elastic Beanstalk."""
    profile = input('AWS CLI Profile (if not default) = ')
    if not profile.strip():
        profile = 'default'

    with (ConfigFilesHandling(_EB_EXTENSIONS_DIR_NAME),
          ConfigFilesHandling(_PLATFORM_DIR_NAME, gpu=gpu),
          EBIgnoreHandling()):
        if aws_eb_env_name:
            run_cmd(command=f'eb deploy --profile {profile} {aws_eb_env_name}',
                    asgi=asgi)

        else:
            region = input('AWS Region = ')
            vpc = input('AWS VPC = ')
            subnets = input('AWS Subnets = ')
            assert region and vpc and subnets

            # AWS EC2 Instance Type: by default, pick a
            # Compute-optimized instance type
            # with good Networking performance and sufficient Memory
            # (note: Graviton (g) instances not compatible with Djaizz deps)
            if gpu:
                pprint(object=_EC2_INSTANCE_TYPES['gpu'],
                       stream=None,
                       indent=2,
                       width=80,
                       depth=None,
                       compact=True,
                       sort_dicts=False,
                       underscore_numbers=False)
                instance_type = input('AWS EC2 Instance Type '
                                      '(default: g4dn.xlarge; min: g4dn.xlarge) = ')  # noqa: E501
                if not instance_type.strip():
                    instance_type = 'g4dn.xlarge'

            else:
                pprint(object=_EC2_INSTANCE_TYPES['cpu'],
                       stream=None,
                       indent=2,
                       width=80,
                       depth=None,
                       compact=True,
                       sort_dicts=False,
                       underscore_numbers=False)
                instance_type = input('AWS EC2 Instance Type '
                                      '(default: c6i.xlarge; min: c6i.large) = ')  # noqa: E501
                if not instance_type.strip():
                    instance_type = 'c6i.xlarge'

            run_cmd(command=(f'eb create --profile {profile}'
                             f' --region {region}'
                             f' --vpc.id {vpc} --vpc.publicip'
                             f' --vpc.dbsubnets {subnets}'
                             f' --vpc.ec2subnets {subnets}'
                             f' --vpc.elbsubnets {subnets} --vpc.elbpublic'
                             f' --instance_type {instance_type}'
                             f' --timeout 30'),
                    asgi=asgi)


@click.group(name='aws-eb',
             cls=click.Group,
             commands={'init': init, 'deploy': deploy},
             invoke_without_command=False,
             no_args_is_help=True,
             subcommand_metavar='DJAI_AWS_EB_SUB_COMMAND',
             chain=False,
             help='Djaizz AWS Elastic Beanstalk CLI >>>',
             epilog='^^^ Djaizz AWS Elastic Beanstalk CLI',
             short_help='Djaizz AWS-EB CLI',
             options_metavar='[OPTIONS]',
             add_help_option=True,
             hidden=False,
             deprecated=False)
def djaizz_aws_eb():
    """Trigger Djaizz AWS Elastic Beanstalk from CLI."""
