import os

from aws_cdk import core as cdk
from aws_cdk import (
    aws_lambda as lambda_,
    aws_s3 as s3_,
    aws_iam as iam_,
)

class ReadSsmCdkStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = s3_.Bucket(self, "MyFirstbucketAsCDK",
                            versioned=False)

        role = iam_.Role(self, "ParameterStoreRole",
                    assumed_by=iam_.ServicePrincipal("sns.amazonaws.com"),
                    )

        layer_source_path = os.path.join(os.getcwd(), 'layer')
        layer = lambda_.LayerVersion(self, 'ssm_layer',
                                     code=lambda_.Code.from_asset(layer_source_path),
                                     compatible_runtimes=[lambda_.Runtime.PYTHON_3_8, lambda_.Runtime.PYTHON_3_7],
                                     license='Apache-2.0',
                                     description='A Layer to test the L2 construct',
                                     )

        layer.add_permission("remote-account-grant", account_id='*')
        lambda_.Function(self, "TestLambda",
                         code=lambda_.Code.from_asset(os.path.join(os.getcwd(), 'lambda')),
                         handler="index.main",
                         layers=[layer],
                         runtime=lambda_.RuntimeFamily.PYTHON,
                         )
