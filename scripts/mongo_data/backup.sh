docker exec mongo sh -c 'mongodump -u root -p"my-secret" --db greeting --authenticationDatabase admin --out ./scripts/mongo_data'