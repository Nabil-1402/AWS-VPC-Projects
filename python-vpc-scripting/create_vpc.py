import boto3
from botocore.exceptions import ClientError

#inital ec2 to connect boto3 to AWS
ec2 = boto3.client(
    "ec2",
    region_name="eu-west-2"
)

#VPC creation
response = ec2.create_vpc(
    CidrBlock="10.0.0.0/16",
    TagSpecifications=[
        {
            "ResourceType": "vpc",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Python VPC",
                }
            ],
        }
    ],
)

vpc_id = response["Vpc"]["VpcId"]

print(f"Created VPC: {vpc_id}")


#Subnet creation
subnet_response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock="10.0.0.0/24",
    AvailabilityZone="eu-west-2a",
)

subnet_id = subnet_response["Subnet"]["SubnetId"]

ec2.create_tags(
    Resources=[subnet_id],
    Tags=[
        {
            "Key": "Name",
            "Value": "Public 1",
        }
    ],
)

print(f"Created Subnet: {subnet_id}")

# Automatically assign a public IPv4 address to instances launched in this subnet
ec2.modify_subnet_attribute(
    SubnetId=subnet_id,
    MapPublicIpOnLaunch={
        "Value": True,
    },
)

#Internet gateway creation
igw_response = ec2.create_internet_gateway()
igw_id = igw_response["InternetGateway"]["InternetGatewayId"]

ec2.create_tags(
    Resources=[igw_id],
    Tags=[
        {
            "Key": "Name",
            "Value": "Python IG",
        },
    ],
)

print(f"Created Internet Gateway: {igw_id}")

#Attach VPC to internet gateway
ec2.attach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id,
)

#Route table creation
route_table_response = ec2.create_route_table(
    VpcId=vpc_id,
)

route_table_id = route_table_response["RouteTable"]["RouteTableId"]

ec2.create_tags(
    Resources=[route_table_id],
    Tags=[
        {
            "Key": "Name",
            "Value": "Python Public Route Table",
        },
    ],
)

print(f"Created Route Table: {route_table_id}")

#Add a route to route table
ec2.create_route(
    RouteTableId=route_table_id,
    DestinationCidrBlock="0.0.0.0/0",
    GatewayId=igw_id,
)

#Associate route table with the subnet
ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)





