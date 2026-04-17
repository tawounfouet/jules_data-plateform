#!/bin/bash
set -e

echo "Restoring metastore database..."
cat /tmp/metastore_backup.sql | docker exec -i platform-postgres psql -U admin metastore

echo "Restore complete."\n