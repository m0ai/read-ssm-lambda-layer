## read-ssm-lambda-layer
Lambda Layer that loads environment variable from AWS Parameter Store with predefined your env variable. (discern as env prefix; like 'AWS_SSM_')

```python

import os

# before
# AWS_SSM_DB_PASSWORD=/app/db_password
# AWS_SSM_SECRET_KEY=/app/key

from ssm import load_parameter_store_with_envs
load_parameter_store_with_envs(prefix='AWS_SSM_')

# after 
# AWS_SSM_DB_PASSWORD=/app/db_password
# AWS_SSM_SECRET_KEY=/app/key
# DB_PASSWORD=p@assw0rd!
# SECRET_KEY=S2cr2t_key


def main(event, context):
  # in your lambda handler
  pass
  
```
