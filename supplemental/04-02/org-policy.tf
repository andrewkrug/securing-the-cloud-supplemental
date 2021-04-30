
# ---------------------------------------- # 
# Service Control Policies for all accounts
# ---------------------------------------- #

# ---------------------------- #
# REGION RESTRICTION 
# ---------------------------- #

data "aws_iam_policy_document" "restrict_regions" {
  statement {
    sid       = "RegionRestriction"
    effect    = "Deny"
    actions   = ["*"]
    resources = ["*"]

    condition {
      test     = "StringNotEquals"
      variable = "aws:RequestedRegion"

      values = [
        "us-east-1",
        "us-west-2"
      ]
    }
  }
}

resource "aws_organizations_policy" "restrict_regions" {
  name        = "restrict_regions"
  description = "Deny all regions except US East 1 and us-west-2."
  content     = data.aws_iam_policy_document.restrict_regions.json
}

# resource "aws_organizations_policy_attachment" "restrict_regions_on_root" {
#   policy_id = aws_organizations_policy.restrict_regions.id
#   target_id = var.organization_root
# }

# ---------------------------- #
# EC2 INSTANCE TYPE RESTRICTION 
# ---------------------------- #

data "aws_iam_policy_document" "restrict_ec2_types" {
  statement {
    sid       = "RestrictEc2Types"
    effect    = "Deny"
    actions   = ["ec2:RunInstances"]
    resources = ["arn:aws:ec2:*:*:instance/*"]

    condition {
      test     = "StringNotEquals"
      variable = "ec2:InstanceType"

      values = [
        "t2*",
        "t3*",
      ]
    }
  }
}

resource "aws_organizations_policy" "restrict_ec2_types" {
  name        = "restrict_ec2_types"
  description = "Allow certain EC2 instance types only."
  content     = data.aws_iam_policy_document.restrict_ec2_types.json
}

resource "aws_organizations_policy_attachment" "restrict_ec2_types_on_root" {
  policy_id = aws_organizations_policy.restrict_ec2_types.id
  target_id = var.organization_root
}

# ---------------------------- #
# REQUIRE EC2 TAGS 
# ---------------------------- #

data "aws_iam_policy_document" "require_ec2_tags" {
  statement {
    sid    = "RequireTag"
    effect = "Deny"
    actions = [
      "ec2:RunInstances",
      "ec2:CreateVolume"
    ]
    resources = [
      "arn:aws:ec2:*:*:instance/*",
      "arn:aws:ec2:*:*:volume/*"
    ]

    condition {
      test     = "Null"
      variable = "aws:RequestTag/Name"

      values = ["true"]
    }
  }
}

resource "aws_organizations_policy" "require_ec2_tags" {
  name        = "require_ec2_tags"
  description = "Name tag is required for EC2 instances and volumes."
  content     = data.aws_iam_policy_document.require_ec2_tags.json
}

# ---------------------------- #
# ATTACH POLICY 
# ---------------------------- #

resource "aws_organizations_policy_attachment" "restrict_regions_on_list" {
  count = length(var.attach_restrict_region_ous)
  policy_id = aws_organizations_policy.restrict_regions.id
  target_id = var.attach_restrict_region_ous[count.index]
}