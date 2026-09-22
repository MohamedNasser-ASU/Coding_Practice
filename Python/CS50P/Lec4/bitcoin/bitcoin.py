import sys
import requests
def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoin = float(sys.argv[1])
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c207c5bb06604f937d7fd018265cf5e609a95eacc549814a0fd31de895a30219")
        js = response.json()
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        pass
    else:
        data = js["data"]
        priceUsd = data["priceUsd"]
        price = float(priceUsd)
        amount = price * bitcoin
        print(f"${amount:,.4f}")
main()
