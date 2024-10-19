This project automates the setup of a PostgreSQL primary-read-replica architecture. It utilizes Terraform to provision the infrastructure and Ansible to configure the PostgreSQL servers, including setting up replication between the primary and replicas.

--------------------------------------------------------------------------------------------------------------------------------------------------------<br>

Run the application : uvicorn app.main:app --reload

--------------------------------------------------------------------------------------------------------------------------------------------------------<br>

Features:<br>

    1. Dynamic Infrastructure Provisioning: Uses Terraform to provision EC2 instances, security groups, and networking resources.<br>
    2. PostgreSQL Configuration: Ansible playbooks are dynamically generated to configure PostgreSQL on the primary and replica servers.<br>
    3. Replication Setup: Configures streaming replication between the primary and read-replica servers.<br>
    4. Customizable Parameters: Specify PostgreSQL version, instance type, number of replicas, and key configuration settings via the API.<br>
    5. End-to-End Automation: From infrastructure provisioning to PostgreSQL setup, everything is automated.<br>
    6. Error Handling: Proper error handling and success messages at each step to ensure smooth execution.<br>

API Endpoints<br>
    
    1. Generate Terraform and Ansible Configurations<br>
        Method: POST<br>
        Endpoint: /generate-terraform-code<br>
        Description: Accepts configurable parameters like PostgreSQL version, instance type, number of replicas, max_connections, and shared_buffers. 
        Generates Terraform and Ansible configuration files dynamically.<br>

    2. Run Terraform Plan, APPPLY<br>
        Method: POST<br>
        Endpoint: terraform-plan-and-apply<br>
        Description: Runs terraform plan to display the infrastructure changes Terraform will make based on the provided configuration.<br>

    3. Run Ansible Playbooks<br>
        Method: POST<br>
        Endpoint: /configure-postgresql<br>
        Description: Executes Ansible playbooks to install PostgreSQL and configure the primary and replica servers.<br>

--------------------------------------------------------------------------------------------------------------------------------------------------------<br>

Configuration Parameters<br>

    1. PostgreSQL Version (postgres_version): Specifies the version of PostgreSQL to be installed (e.g., 13, 14).<br>
    2. Instance Type (instance_type): Defines the EC2 instance type for the PostgreSQL servers (e.g., t3.medium).<br>
    3. Number of Replicas (num_replicas): Sets the number of read-replica servers.<br>
    4. Max Connections (max_connections): Sets the maximum number of allowed PostgreSQL connections.<br>
    5. Shared Buffers (shared_buffers): Configures the PostgreSQL shared_buffers setting for memory management.<br>

--------------------------------------------------------------------------------------------------------------------------------------------------------<br>

Future Use Cases<br>

    1. Multi-cloud Support: Extend the Terraform configuration to provision PostgreSQL on other cloud platforms (e.g., GCP, Azure).<br>
    2. Backup and Restore: Add functionality for automated backups and restore of PostgreSQL data.<br>
    3. Monitoring and Alerting: Integrate with monitoring tools to track the performance and availability of PostgreSQL instances.<br>

--------------------------------------------------------------------------------------------------------------------------------------------------------<br>

Assumptions<br>

    1. AWS credentials are configured using IAM roles.<br>
    2. Terraform and Ansible are installed on the host running this API.<br>
