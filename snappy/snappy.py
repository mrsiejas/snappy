import boto3
import click

# define which profile from ~/.aws/credentials should be used to create the session
session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

#@decorator - wrap functions
@click.command()

def list_instances():
    "Lists EC2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))

    return



if __name__ == "__main__":
#    print(sys.argv)
    list_instances()