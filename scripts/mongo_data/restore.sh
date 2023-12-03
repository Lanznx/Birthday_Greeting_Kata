docker exec -i mongo sh -c "mongorestore -u root -p"my-secret" --authenticationDatabase admin ./scripts/mongo_data"
