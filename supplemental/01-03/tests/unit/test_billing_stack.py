import json
import pytest

from aws_cdk import core
from billing.billing_stack import BillingStack


def get_template():
    app = core.App()

    # Maybe some day in a future course learn to write tests for this