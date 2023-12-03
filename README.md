# Birthday_Greeting_Kata
Pre-assignment from LINE interview.

## Clean Architecture
![Pre-assignment Clean Arcitecture](https://github.com/Lanznx/Birthday_Greeting_Kata/assets/96360357/df4f79c6-dba1-455d-b747-330ee1e0fb01)


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

![image](https://github.com/Lanznx/Birthday_Greeting_Kata/assets/96360357/e21cdaa6-1f47-4c45-9cc4-ee411186bc1a)
