## read-ssm-lambda-layer
Lambda Layer that loads environment variable from AWS Parameter Store with predefined your env variable. (discern as env prefix; like 'AWS_SSM_')

```python
# in your lambda handler
import os

from ssm import load_parameter_store_with_envs

# Useage
load_parameter_store_with_envs(prefix='AWS_SSM_')


def main(event, context):
  pass
  
```
