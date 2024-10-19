"""
Holds the code to spawn the dynamic(on-demand) resource on the cloud
"""
def generate_terraform_code(postgress_and_server_config):
    """
    Accepts the postgres configuration to provision the resource, and then pass the postgres config to the 
    ansible playbook
    """
    infastructure_code = f""""
      variable 'postges_version' {{
        default = {postgress_and_server_config.pg_version}
      }}

      variable 'instance_type' {{
        default = {postgress_and_server_config.instance_type}
      }}

      variable 'num_replicas' {{
        default = {postgress_and_server_config.num_replicas}
      }}

      resource "aws_instance" "postgresql-instance" {{
        count = var.num_replicas + 1
        ami           = 'ami-0c55b159cbfafe1f0'
        instance_type = var.instance_type

        tags = {{
          Name = 'postgresql-instance-${{count.index}}'
        }}
      }}
    """

    with open('terraform/main.tf', 'w', encoding='utf-8') as f:
      f.write(infastructure_code)
