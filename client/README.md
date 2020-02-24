# BANDAID CLIENT

Install by `pip install bandaid` with Python 3.x only.

## Client

1. CLI to provide all interactive functionality
    - Use case is "Show me Aerosmith" and it will mark as watching and also whether on tour or now
2. Modules to integrate into other code (`from bandaid import bandaid`)

3. Agent (Watchlist manager and band tour status query)
    - Mark bands that you want to watch for and know when on tour and if coming to town
    - Use SQLite database to track and update

```bash
$ python3 agent.py -h
usage: agent.py [-h] [-b BANDNAME [BANDNAME ...]] [-w] [-f]

optional arguments:
  -h, --help            show this help message and exit
  -b BANDNAME [BANDNAME ...], --band BANDNAME [BANDNAME ...]
                        band to lookup
  -w, --watchlist       add to watchlist
  -f, --fetch           fetch a band (with -b flag) or no extra flag for all bands tracking current status
```
