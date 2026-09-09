# AWS VPC Projects

A collection of hands-on AWS networking projects completed to strengthen my practical understanding of Amazon Virtual Private Cloud (VPC). The projects progress from building a basic VPC to connecting and monitoring multiple VPCs and enabling private access to Amazon S3.

Each project includes PDF documentation explaining the architecture, configuration steps, testing process and key lessons learnt.

## Projects

| Part | Project                       | What I implemented                                                                                                                                          | Documentation                                                         |
| ---- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1    | Build a Virtual Private Cloud | Created a custom VPC, configured a public subnet, route table and internet gateway, and explored CIDR addressing.                                           | [View PDF](part1_documentation/legendary-aws-networks-vpc.pdf)        |
| 2    | VPC Peering                   | Built two VPCs with non-overlapping CIDR blocks, established a peering connection and updated route tables and security groups to enable connectivity.      | [View PDF](part2_documentation/legendary-aws-networks-peering.pdf)    |
| 3    | VPC Monitoring with Flow Logs | Generated traffic between EC2 instances in peered VPCs, captured network metadata with VPC Flow Logs and analysed it using Amazon CloudWatch Logs Insights. | [View PDF](part3_documentation/legendary-aws-networks-monitoring.pdf) |
| 4    | Access Amazon S3 from a VPC   | Launched an EC2 instance in a public subnet and used the AWS CLI to list, access and upload objects to an S3 bucket.                                        | [View PDF](part4_documentation/legendary-aws-networks-s3.pdf)         |
| 5    | VPC Endpoints                 | Created an S3 Gateway Endpoint, associated it with a route table and used bucket and endpoint policies to test and restrict private access to S3.           | [View PDF](part5_documentation/legendary-aws-networks-endpoints.pdf)  |

## Architecture Progression

The repository follows a practical learning path:

1. Build an isolated AWS network and connect a public subnet to the internet.
2. Connect two VPCs privately using VPC Peering.
3. Monitor traffic between the VPCs using Flow Logs and CloudWatch.
4. Access and manage S3 objects from an EC2 instance using the AWS CLI.
5. Route S3 traffic privately through a Gateway Endpoint and restrict access with policies.

## AWS Services and Concepts

* Amazon VPC
* Public subnets
* CIDR blocks
* Route tables
* Internet gateways
* Security groups
* Amazon EC2 and EC2 Instance Connect
* VPC Peering
* VPC Flow Logs
* Amazon CloudWatch Logs and Logs Insights
* Amazon S3
* AWS CLI
* IAM permissions
* Gateway VPC Endpoints
* S3 bucket policies and endpoint policies

## Key Lessons

* VPCs use CIDR blocks to define their IP address ranges, and peered VPCs must use non-overlapping ranges.
* A peering connection alone is not enough: route tables and security rules must also permit the required traffic.
* VPC Flow Logs capture network traffic metadata that can help investigate connectivity and security issues.
* IAM roles are preferable to long-term access keys for granting AWS resources permissions.
* An S3 Gateway Endpoint allows traffic to reach S3 without travelling through the public internet.
* Bucket policies and endpoint policies provide separate layers of access control and can be tested using explicit allow and deny rules.

## Security Note

These projects were created for learning in a personal AWS environment. Credentials and other sensitive values are not stored in this repository. In a production environment, EC2 instances should use IAM roles with least-privilege permissions instead of long-term access keys.

## About Me

I am a Computer Science student developing practical skills in cloud computing and DevOps through hands-on projects involving AWS, Docker, Kubernetes and CI/CD.

[Connect with me on LinkedIn](https://www.linkedin.com/in/nabil-ahmed-712b65278)

## Acknowledgements

These projects were completed through the NextWork AWS networking learning series.
