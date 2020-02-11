# bandaid

command line interface tool to track bands you want to see.

## Server

The server is made up of the following components:

1. Roadie
    - Sync all bands data to the extent possible to database
2. SolidGold
    - Store all the things
3. WillCall
    - Queue Management / Orchestration

## Client

1. CLI to provide all interactive functionality
    - Use case is "Show me Aerosmith" and it will mark as watching and also whether on tour or now
2. Modules to integrate into other code (`from hands-in-town import blah`)

3. Agent (Watchlist manager and band tour status query)
    - Mark bands that you want to watch for and know when on tour and if coming to town
    - Use SQLite database to track and update

## Install

1. Via pip is the preferred method, must be python 3+ `pip install bandaid`

2. Direct download
