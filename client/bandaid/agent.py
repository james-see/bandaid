"""Gets latest band data for a particular band and adds to user watchlist."""
from bs4 import BeautifulSoup as bs
import requests 
import argparse

__version__ = "1.0.3"


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
        exit()
    else:
        exit(1)


def prepper():
    """
    Process all runtime arguments.
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
    printlogo()
    getBand(" ".join(args.bandname))


if __name__ == "__main__":
    main()
