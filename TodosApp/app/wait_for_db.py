#!/usr/bin/env python3
"""
Wait for database to be ready before starting the application.
"""
import time
import psycopg2
from psycopg2 import OperationalError
import os

def wait_for_db(host, port, dbname, user, password, max_retries=30):
    """Wait for database to be ready."""
    retries = 0
    while retries < max_retries:
        try:
            connection = psycopg2.connect(
                host=host,
                port=port,
                database=dbname,
                user=user,
                password=password
            )
            connection.close()
            print("Database is ready!")
            return True
        except OperationalError:
            retries += 1
            print(f"Database not ready, waiting... ({retries}/{max_retries})")
            time.sleep(1)
    
    print("Database failed to become ready in time")
    return False

if __name__ == "__main__":
    # Get database connection details from environment variables
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "todos")
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("POSTGRES_PASSWORD", "password")
    
    success = wait_for_db(db_host, db_port, db_name, db_user, db_password)
    if not success:
        exit(1)
