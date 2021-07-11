import os
import boto3
import logging

ssm = boto3.client('ssm')
log = logging.getLogger('ssm-layer')
log.setLevel(logging.INFO)

DEBUG = int(os.getenv('SSM_LAYER_DEBUG', 0))
if DEBUG:
    import sys
    sh = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    sh.setFormatter(formatter)
    log.addHandler(sh)
    log.setLevel(logging.DEBUG)
    log.debug("Logging as Debug mode")


def load_parameter_store_with_envs(*, prefix='AWS_SSM_'):
    log.debug(f'Read environment variable that starts with prefix "{prefix}"')
    envs = dict(filter(lambda x: x[0].startswith(prefix), os.environ.items()))

    if not len(envs):
        log.warning(f'An environment variable that satisfies the condition does not exist. (filtered prefix={prefix})')
        return

    parameters = ssm.get_parameters(
        Names=[*envs.values()],
        WithDecryption=True)

    # Create env with strip prefix
    for p in parameters.get('Parameters'):
        path = p['Name']
        value = p['Value']
        log.debug(f'Loaded {path} from parameter store')

        # Get key name from envs
        *_, (env_name, ssm_path) = filter(lambda x: x[1] == path, envs.items())
        new_env_name = env_name.strip(prefix)
        log.info(f'Create new environment variable {new_env_name} from parameter store path {path}')
        os.environ[new_env_name] = value

    for invalid_path in parameters.get('InvalidParameters'):
        log.error(f'Failed to create environment variable, invalid parameter store path {invalid_path}')
