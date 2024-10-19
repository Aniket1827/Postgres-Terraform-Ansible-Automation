"""
This module holds the Postgres associated configurations
"""
# pylint: disable=no-name-in-module
from pydantic import BaseModel

class PostgresAndServerConfig(BaseModel):
    """
    Class to hold the configuration to setup the DB & infrastructure
    """
    postgres_version: str
    instance_type: str
    num_replicas: int
    max_connections: int
    shared_buffers: str
