resource "aws_iam_user" "security_consultant" {
  name = "security-consultant"
  path = "/external/"

  tags = {
    application = "infosec"
  }
}

resource "aws_iam_access_key" "security_consultant" {
  user = aws_iam_user.security_consultant.name
}

resource "aws_iam_user_policy" "security-read-only" {
  name = "security_consultant"
  user = aws_iam_user.security_consultant.name

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:Describe*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}