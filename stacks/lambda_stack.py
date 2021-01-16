##############################################################
#
# lambda_stack.py
#
# Resources:
#  1 lambda functions (code in /lambda folder (from_asset))
#
##############################################################

from aws_cdk import (
  aws_iam as iam,
  aws_lambda as lambda_,
  core
)

class LambdaStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, env, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # get acct id for policies
    acct_id=env['account']

    # create the Lambda function
    self._iam_event_checker_func=lambda_.Function(self,"Lambda Func",
      code=lambda_.Code.from_asset("lambda/"),
      handler="test.lambda_handler",
      runtime=lambda_.Runtime.PYTHON_3_8,
      role=IRole",
    )


