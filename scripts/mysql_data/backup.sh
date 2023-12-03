docker exec mysql sh -c 'exec mysqldump -uroot -p"my-secret" --databases greeting' > ./scripts/mysql_data/backup.sql
