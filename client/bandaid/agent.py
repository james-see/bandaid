"""Gets latest band data for a particular band and adds to user watchlist."""
from bs4 import BeautifulSoup as bs
import requests
import argparse
from pathlib import Path
import sqlite3

__version__ = "1.0.5"


def printlogo():
    """
    Prints logo
    Returns nothing
    """
    print("")
    print("     ;;;;;;;;;;;;;;;;;;; ")
    print("     ;;;;;;;;;;;;;;;;;;; ")
    print("     ;                 ; ")
    print("     ;     bandaid     ; ")
    print("     ;                 ; ")
    print("     ;  +-----------+  ; ")
    print("     ;  |by JC 2020 |  ; ")
    print("     ;  +-----------+  ; ")
    print("     ;                 ; ")
    print(",;;;;;            ,;;;;; ")
    print(";;;;;;            ;;;;;; ")
    print("`;;;;'            `;;;;' ")
    print("")


def initDB(dbpath):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute('''CREATE TABLE tracker
             (date_added text, date_last_checked text, band text, ontour integer, zipcode integer)''')


def checkFirstRun():
    """
    Check if file exists for the sqlite database and if not creates it and cfg
    """
    my_cfg = Path.home() / ".bandaid.cfg"
    my_db = Path.home() / ".bandaid.db"
    if not my_cfg.exists():
        print("First run, making the donuts...")
        zipcode = input("Enter your zipcode for concerts near you: ")
        with open(Path.home() / ".bandaid.cfg") as f:
            f.write('DBPATH=~/.bandaid.db')
            f.write(f'ZIPCODE={zipcode}')
        initDB(my_db)
        print(f"Database and config file created at {my_cfg}")


def watchlist(bandname):
    """
    Add band to watchlist, initialize watchlist service and db is doesn't exist
    """
    conn = sqlite3.connect(Path.home() / ".bandaid.db")


def getBand(bandname):
    """
    Get band page and related data
    """
    baseurl = "https://www.bandsintown.com/{}"
    r = requests.get(baseurl.format(bandname))
    if r.status_code == 200:
        if "No upcoming events</div>" in r.text:
            print(f"No upcoming events for {bandname}.")
        else:
            print(f"{bandname} is on tour!")
            bandtrack = input(f"Would you like to track {bandname}? (y/n)")
            if bandtrack in ['y', 'Y']:
                print(f"Adding {bandname} to your watchlist now...")
                watchlist(bandname)
        exit()
    else:
        exit(1)


def prepper():
    """
    Process all runtime arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--band', dest='bandname',
                        help="band to lookup", type=str, nargs='+')
    parser.add_argument('-w', '--watchlist', dest='watchlist',
                        action='store_true', help="add to watchlist")
    args = parser.parse_args()
    return args


def main():
    """
    Main function that runs everything
    """
    args = prepper()
    checkFirstRun()
    printlogo()
    if args.bandname:
        getBand(" ".join(args.bandname))
    else:
        exit('Must set band name -h for help.')


if __name__ == "__main__":
    main()
