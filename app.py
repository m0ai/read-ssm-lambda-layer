#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from lambda_cdk.lambda_cdk_stack import LambdaCdkStack


app = cdk.App()
account = os.getenv('CDK_DEFAULT_ACCOUNT')
region = os.getenv('CDK_DEFAULT_REGION')

LambdaCdkStack(app, "LambdaCdkStack",
               env=cdk.Environment(account=account, region=region))

app.synth()
