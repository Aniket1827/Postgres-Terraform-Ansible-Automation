"""
This module will handle the ansible playbook execution to configure the postgres db on the provisioned EC2 instances
"""
import subprocess

def run_ansible_playbook():
    """
    This function will run the ansible playbook to configure the postgres db on the provisioned EC2 instances
    """
    ansible_command = ['ansible-playbook', 'postgres-setup.yml']
    subprocess.check_call(ansible_command)
