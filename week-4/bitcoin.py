
import requests
import sys
#import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of command line arguments.")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not a number.")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()

    except requests.RequestException:
        sys.exit("JSON Request Error.")

    #print(json.dumps(o, indent=2))

    rate = float(o["bpi"]["USD"]["rate_float"])
    bitcoin_value = n * rate
    print(f"${bitcoin_value:,.4f}")


if __name__ == "__main__":
    main()






