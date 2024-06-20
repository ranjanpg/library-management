#!/bin/bash

set -e

# Length of the generated password
PASSWORD_LENGTH=16

# File to save the generated password
PASSWORD_FILE="db_password.txt"

# Generate a random password
PASSWORD=$(LC_ALL=C tr -dc 'A-Za-z0-9!@#$%^&*()_+{}|:<>?' < /dev/urandom | head -c $PASSWORD_LENGTH)

# Save the password to a file
echo $PASSWORD > $PASSWORD_FILE

# Set the correct permissions to the file
chmod 600 $PASSWORD_FILE

# Create database and user in PostgreSQL
psql postgres -c "CREATE DATABASE librarydb;"
psql postgres -c "CREATE USER library WITH PASSWORD '$PASSWORD';"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE librarydb TO library;"

echo "Database 'librarydb' and user 'library' with the generated password have been created."
