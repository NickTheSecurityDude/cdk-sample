#!/usr/bin/env python3

from aws_cdk import core

import boto3
import sys

client = boto3.client('sts')

region=client.meta.region_name

#if region != 'us-east-1':
#  print("This app may only be run from us-east-1")
#  sys.exit()

account_id = client.get_caller_identity()["Account"]

my_env = {'region': region, 'account': account_id}

from stacks.lambda_stack import LambdaStack

proj_name="proj-name-"

app = core.App()

lambda_stack=LambdaStack(app, proj_name+"lambda",env=my_env)

app.synth()
