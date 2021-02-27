#!/usr/bin/env python3

from aws_cdk import core

from billing.billing_stack import BillingStack


app = core.App()
BillingStack(app, "billing", env={'region': 'us-east-1'})

app.synth()
