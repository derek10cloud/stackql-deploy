import click, os
from . import __version__ as deploy_version
from dotenv import load_dotenv, dotenv_values
from .lib.bootstrap import logger, stackql
from .cmd.build import StackQLProvisioner
from .cmd.test import StackQLTestRunner
from .cmd.teardown import StackQLDeProvisioner

def common_args(f):
    f = click.argument('stack_dir', type=str)(f)
    f = click.argument('stack_env', type=str)(f)
    return f

def common_options(f):
    f = click.option('--log-level', default='INFO', help='Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')(f)
    f = click.option('--env-file', default='.env', help='Environment variables file.')(f)
    f = click.option('-e', multiple=True, type=(str, str), help='Additional environment variables.')(f)
    f = click.option('--dry-run', is_flag=True, help='Perform a dry run of the stack operation.')(f)
    f = click.option('--on-failure', type=click.Choice(['rollback', 'ignore', 'error']), default='error',
                     help='Action on failure: rollback, ignore or error.')(f)
    return f

def setup_logger(command, args_dict):
    log_level = args_dict.get('log_level', 'INFO')
    logger.setLevel(log_level)
    logger.debug(f"'{command}' command called with args: {str(args_dict)}")

def load_env_vars(env_file, overrides):
    """Load environment variables from a file and apply overrides."""
    # Load environment variables from the specified file into a new dict
    dotenv_path = os.path.join(os.getcwd(), env_file)
    if os.path.exists(dotenv_path):
        env_vars = dict(dotenv_values(dotenv_path))
    else:
        env_vars = {}
    # Apply overrides from the `-e` option
    for key, value in overrides:
        env_vars[key] = value
    return env_vars

@click.command()
@common_args
@common_options
def build(stack_env, stack_dir, log_level, env_file, e, dry_run, on_failure):
    setup_logger("build", locals())
    vars = load_env_vars(env_file, e)
    provisioner = StackQLProvisioner(stackql, vars, logger, stack_dir, stack_env)
    provisioner.run(dry_run, on_failure)

@click.command()
@common_args
@common_options
def teardown(stack_env, stack_dir, log_level, env_file, e, dry_run, on_failure):
    setup_logger("teardown", locals())
    vars = load_env_vars(env_file, e)
    deprovisioner = StackQLDeProvisioner(stackql, vars, logger, stack_dir, stack_env)
    deprovisioner.run(dry_run, on_failure)

@click.command()
@common_args
@common_options
def test(stack_env, stack_dir, log_level, env_file, e, dry_run, on_failure):
    setup_logger("test", locals())
    vars = load_env_vars(env_file, e)
    test_runner = StackQLTestRunner(stackql, vars, logger, stack_dir, stack_env)
    test_runner.run(dry_run, on_failure)

@click.command()
def info():
    """Display the version information of stackql-deploy and stackql library."""
    max_label_length = max(len(label) for label, _ in [
        ("stackql-deploy version", ""),
        ("pystackql version", ""),
        ("stackql version", ""),
        ("stackql binary path", ""),
        ("platform", "")
    ])
    info_items = [
        ("stackql-deploy version", deploy_version),
        ("pystackql version", stackql.package_version),
        ("stackql version", stackql.version),
        ("stackql binary path", stackql.bin_path),
        ("platform", stackql.platform)
    ]
    for label, value in info_items:
        click.echo(f"{label.ljust(max_label_length)}: {value}")

@click.group()
def cli():
    pass

cli.add_command(build)
cli.add_command(test)
cli.add_command(teardown)
cli.add_command(info)

if __name__ == '__main__':
    cli()
