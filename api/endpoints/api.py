"""
Contains implementation for all the apis being used to automate postgres db setup using terraform and ansible
"""
# pylint: disable=import-error, no-name-in-module
import subprocess
from fastapi import status, FastAPI, HTTPException
from terraform.tf_handler import generate_terraform_code
from ansible.ansible_handler import run_ansible_playbook
from config.postgres_and_server_config import PostgresAndServerConfig

app = FastAPI()

@app.post("/generate-terraform-code", status_code=status.HTTP_201_CREATED)
def generate_code(postgress_and_server_config: PostgresAndServerConfig):
    """
    This API method will genrated the terraform code, which will hold all the Postgres related configuration
    and the EC2 server setup configuration.
    """
    try:
        generate_terraform_code(postgress_and_server_config)
        return {"message": "Terraform and Ansible code generated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@app.post("/terraform-plan-and-apply", status_code=status.HTTP_200_OK)
def plan_and_apply():
    """
    This API method will call the terraform associated commands to provision the infrastructure on the cloud
        1. terraform init: initializes a working directory and downloads the necessary provider plugins and modules 
           and setting up the backend for storing your infrastructure's state.
        2. terraform plan: show the blueprint or summarise the resources that will be spawned on the cloud.
        3. terraform apply -auto-approve: Will initiate the resource spawning on the cloud. The -auto-approve flag ensures
           that the user is not prompted to confirm the resource.
    """
    try:
        subprocess.check_call(['terraform', 'init'])
        subprocess.check_call(['terraform', 'plan'])
        subprocess.check_call(['terraform', 'apply', '-auto-approve'])
        return {"message": "Infrastructure provisioned successfully"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Terraform error: {str(e)}")  from e

@app.post("/configure-postgresql", status_code=status.HTTP_201_CREATED)
def configure_postgresql():
    """
    This API method will call the ansible playbook to configure the PostgreSQL on the provisioned EC2 instances.
    """
    try:
        run_ansible_playbook()
        return {"message": "PostgreSQL configured successfully"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Ansible error: {str(e)}") from e
