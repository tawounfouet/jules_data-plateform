#!/bin/bash
set -e

echo "Starting backup of metastore database..."
docker exec platform-postgres pg_dump -U admin metastore > /tmp/metastore_backup.sql

echo "Backing up MinIO metadata..."
# Assuming mc is configured locally
mc cp -r myminio/bronze /tmp/backup/bronze

echo "Backup complete."\n