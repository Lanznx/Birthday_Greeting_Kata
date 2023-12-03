# Birthday_Greeting_Kata
Pre-assignment from LINE interview.

## How to run
```bash
docker compose up -d
```

## How to test
```bash
bash scripts/mongo_data/restore.sh # restore test data of mongodb
                                   # data of mysql has already been restored when starting up
docker exec -i backend sh -c "sh scripts/run_test.sh"
```

## API Document

http://localhost:7070/docs