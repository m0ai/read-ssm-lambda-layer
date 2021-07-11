import os

from ssm import load_parameter_store_with_envs


load_parameter_store_with_envs(prefix='AWS_SSM_')

def main(event, context):
    print(os.environ)
    pass
