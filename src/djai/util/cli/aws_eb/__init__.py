"""DjAI AWS Elastic Beanstalk CLI."""


import os
from pathlib import Path
import shutil
from typing import Optional

import click

from ..run_cmd import run_cmd


_DJAI_AWS_EB_CLI_UTIL_DIR_PATH = Path(__file__).parent
_EB_EXTENSIONS_DIR_NAME = '.ebextensions'
_EB_IGNORE_FILE_NAME = '.ebignore'
_PLATFORM_DIR_NAME = '.platform'


@click.command(name='init',
               cls=click.Command,
               context_settings=None,
               help=('DjAI AWS Elastic Beanstalk CLI: '
                     'Initialize Configuration >>>'),
               epilog=('^^^ DjAI AWS Elastic Beanstalk CLI: '
                       'Initialize Configuration'),
               short_help='DjAI AWS-EB Init',
               options_metavar='',
               add_help_option=True,
               hidden=False,
               deprecated=False)
def init():
    """Initialize DjAI AWS Elastic Beanstalk Configuration."""
    os.system(command='eb init')


@click.command(name='deploy',
               cls=click.Command,
               context_settings=None,
               help='DjAI AWS Elastic Beanstalk CLI: Deploy >>>',
               epilog='^^^ DjAI AWS Elastic Beanstalk CLI: Deploy',
               short_help='DjAI AWS-EB Deploy',
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
                envvar=None,
                autocompletion=None)
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
@click.option('--create',
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
              help='whether to create a new AWS Elastic Beanstalk environment',
              show_choices=True,
              default=False,
              required=False,
              callback=None,
              nargs=None,
              metavar='CREATE',
              expose_value=True,
              is_eager=False,
              envvar=None)
def deploy(aws_eb_env_name: Optional[str] = None,
           asgi: Optional[str] = None,
           create: bool = False):
    """Deploy DjAI onto AWS Elastic Beanstalk."""
    assert not os.path.exists(path=_EB_EXTENSIONS_DIR_NAME)
    shutil.copytree(
        src=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / _EB_EXTENSIONS_DIR_NAME,
        dst=_EB_EXTENSIONS_DIR_NAME,
        symlinks=False,
        ignore=None,
        ignore_dangling_symlinks=False,
        dirs_exist_ok=False)
    assert os.path.isdir(_EB_EXTENSIONS_DIR_NAME)

    _eb_ignore_exists = os.path.exists(path=_EB_IGNORE_FILE_NAME)

    if _eb_ignore_exists:
        assert os.path.isfile(_EB_IGNORE_FILE_NAME)

    else:
        shutil.copyfile(
            src=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / _EB_IGNORE_FILE_NAME,
            dst=_EB_IGNORE_FILE_NAME)
        assert os.path.isfile(_EB_IGNORE_FILE_NAME)

    assert not os.path.exists(path=_PLATFORM_DIR_NAME)
    shutil.copytree(
        src=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / _PLATFORM_DIR_NAME,
        dst=_PLATFORM_DIR_NAME,
        symlinks=False,
        ignore=None,
        ignore_dangling_symlinks=False,
        dirs_exist_ok=False)
    assert os.path.isdir(_PLATFORM_DIR_NAME)

    profile = input('AWS CLI Profile (if not default) = ')
    if not profile.strip():
        profile = 'default'

    if create:
        region = input('AWS Region = ')
        vpc = input('AWS VPC = ')
        subnets = input('AWS Subnets = ')
        assert region and vpc and subnets

        instance_type = input('AWS EC2 Instance Type (default: c5.xlarge) = ')
        if not instance_type.strip():
            instance_type = 'c5.xlarge'   # c5.large sometimes memory-insuff

        run_cmd(command=(f'eb create --profile {profile}'
                         f' --region {region}'
                         f' --vpc.id {vpc} --vpc.publicip'
                         f' --vpc.dbsubnets {subnets}'
                         f' --vpc.ec2subnets {subnets}'
                         f' --vpc.elbsubnets {subnets} --vpc.elbpublic'
                         f' --instance_type {instance_type}'
                         f" {aws_eb_env_name if aws_eb_env_name else ''}"),
                copy_standard_files=True,
                asgi=asgi)

    else:
        run_cmd(command=(f'eb deploy --profile {profile}'
                         f" {aws_eb_env_name if aws_eb_env_name else ''}"),
                copy_standard_files=True,
                asgi=asgi)

    shutil.rmtree(
        path=_EB_EXTENSIONS_DIR_NAME,
        ignore_errors=False,
        onerror=None)
    assert not os.path.exists(path=_EB_EXTENSIONS_DIR_NAME)

    if not _eb_ignore_exists:
        os.remove(_EB_IGNORE_FILE_NAME)
        assert not os.path.exists(path=_EB_IGNORE_FILE_NAME)

    shutil.rmtree(
        path=_PLATFORM_DIR_NAME,
        ignore_errors=False,
        onerror=None)
    assert not os.path.exists(path=_PLATFORM_DIR_NAME)


@click.group(name='aws-eb',
             cls=click.Group,
             commands={'init': init, 'deploy': deploy},
             invoke_without_command=False,
             no_args_is_help=True,
             subcommand_metavar='DJAI_AWS_EB_SUB_COMMAND',
             chain=False,
             help='DjAI AWS Elastic Beanstalk CLI >>>',
             epilog='^^^ DjAI AWS Elastic Beanstalk CLI',
             short_help='DjAI AWS-EB CLI',
             options_metavar='[OPTIONS]',
             add_help_option=True,
             hidden=False,
             deprecated=False)
def djai_aws_eb():
    """Trigger DjAI AWS Elastic Beanstalk from CLI."""
