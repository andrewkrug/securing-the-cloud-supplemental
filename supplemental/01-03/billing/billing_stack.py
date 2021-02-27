from aws_cdk import (
    aws_budgets,
    core
)


class BillingStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Email parameter passed to the subsequent form of Cloudformation
        # pass this with --parameters EmailDistributor=
        email = core.CfnParameter(
            self,
            id="EmailDistributor",
            description="An email address.  This should be a list because there is a 10 email limit.",
            type="String",
            default="YOUR@EMAIL.COM",
        )

        emails_list = [email.value_as_string]

        thresholds_list = [
            100,
            250,
            500
        ]

        subscribers_list = []

        for emails in emails_list:
            subscribers_list.append(
                aws_budgets.CfnBudget.SubscriberProperty(
                    address=emails, subscription_type="EMAIL"
                )
            )

        for thresholds in thresholds_list:
            property = aws_budgets.CfnBudget.BudgetDataProperty(
                budget_type="COST",
                budget_limit=aws_budgets.CfnBudget.SpendProperty(
                    amount=thresholds, unit="USD"
                ),
                time_unit="MONTHLY",
            )
            budgets = aws_budgets.CfnBudget(
                self,
                id="Auto-Budget-{}".format(thresholds),
                budget=property,
                notifications_with_subscribers=[
                    aws_budgets.CfnBudget.NotificationWithSubscribersProperty(
                        notification=aws_budgets.CfnBudget.NotificationProperty(
                            comparison_operator="GREATER_THAN",
                            notification_type="ACTUAL",
                            threshold=80,
                            threshold_type="PERCENTAGE",
                        ),
                        subscribers=subscribers_list,
                    )
                ],
            )