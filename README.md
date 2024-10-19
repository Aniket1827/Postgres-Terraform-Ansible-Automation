This project automates the setup of a PostgreSQL primary-read-replica architecture. It utilizes Terraform to provision the infrastructure and Ansible to configure the PostgreSQL servers, including setting up replication between the primary and replicas.

Run the application : uvicorn app.main:app --reload

Features:
    Dynamic Infrastructure Provisioning: Uses Terraform to provision EC2 instances, security groups, and networking resources.
    PostgreSQL Configuration: Ansible playbooks are dynamically generated to configure PostgreSQL on the primary and replica servers.
    Replication Setup: Configures streaming replication between the primary and read-replica servers.
    Customizable Parameters: Specify PostgreSQL version, instance type, number of replicas, and key configuration settings via the API.
    End-to-End Automation: From infrastructure provisioning to PostgreSQL setup, everything is automated.
    Error Handling: Proper error handling and success messages at each step to ensure smooth execution.

API Endpoints
    Generate Terraform and Ansible Configurations
    Method: POST
    Endpoint: /generate-terraform-code
    Description: Accepts configurable parameters like PostgreSQL version, instance type, number of replicas, max_connections, and shared_buffers. Generates Terraform and Ansible configuration files dynamically.

    Run Terraform Plan, APPPLY
    Method: POST
    Endpoint: terraform-plan-and-apply
    Description: Runs terraform plan to display the infrastructure changes Terraform will make based on the provided configuration.

    Run Ansible Playbooks
    Method: POST
    Endpoint: /configure-postgresql
    Description: Executes Ansible playbooks to install PostgreSQL and configure the primary and replica servers.

Configuration Parameters
    PostgreSQL Version (postgres_version): Specifies the version of PostgreSQL to be installed (e.g., 13, 14).
    Instance Type (instance_type): Defines the EC2 instance type for the PostgreSQL servers (e.g., t3.medium).
    Number of Replicas (num_replicas): Sets the number of read-replica servers.
    Max Connections (max_connections): Sets the maximum number of allowed PostgreSQL connections.
    Shared Buffers (shared_buffers): Configures the PostgreSQL shared_buffers setting for memory management.

Future Use Cases
    Multi-cloud Support: Extend the Terraform configuration to provision PostgreSQL on other cloud platforms (e.g., GCP, Azure).
    Backup and Restore: Add functionality for automated backups and restore of PostgreSQL data.
    Monitoring and Alerting: Integrate with monitoring tools to track the performance and availability of PostgreSQL instances.

Assumptions
    AWS credentials are configured using IAM roles.
    Terraform and Ansible are installed on the host running this API.