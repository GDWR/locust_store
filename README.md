# Test Store Locust

Install [pdm](https://pdm.fming.dev/latest/#installation)

```bash
pdm run dev # Start api, runs on localhost:8000 by default

pdm run test # Start locust, do magic
```

## Test with postgresql

start postgres, you can use docker compose for ease.
```bash
docker compose up
```

and change locust_store/database.py to uncomment the postgresql connection and comment sqlite3.
