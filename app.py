#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from read_ssm_cdk.read_ssm_cdk_stack import ReadSsmCdkStack

app = cdk.App()

account = os.getenv('CDK_DEFAULT_ACCOUNT')
region = os.getenv('CDK_DEFAULT_REGION')

ReadSsmCdkStack(app, "ReadSsmCdkStack",
                env=cdk.Environment(account=account, region=region))

app.synth()
