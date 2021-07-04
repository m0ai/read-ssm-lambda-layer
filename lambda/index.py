from ssm import load_parameter_store_with_envs

load_parameter_store_with_envs(prefix='AWS_SSM_')

import os

def main(event, context):
    print(os.environ)
    return {
        'message' : message
    }
