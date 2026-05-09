iimport math
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        quantity = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    if not math.isfinite(quantity):
        sys.exit("Command-line argument is not a finite number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            params={"apiKey": "FFFF"}
        )
    except requests.RequestException:
        sys.exit("Could not reach Bitcoin API")

    try:
        price = float(response.json()["data"]["priceUsd"])
    except (KeyError, ValueError):
        sys.exit("Unexpected API response")

    print(f"${price * quantity:,.4f}")


if __name__ == "__main__":
    main()

## First iteration had both API calling and CLI input taking withing same try loop but it made sense to separate them so that any code later on can be added peacefully without much problems.
'''
else:
        try:
            quantity = float(sys.argv[1])
            bitcoin_data = requests.get("rest.coincap.io/v3/assets/bitcoin", params ={"apiKey":"FFFF"})

        except ValueError:
            sys.exit("Input is not a number")
        except requests.RequestException:
            sys.exit("Could not reach Bitcoin API")
        parsed_data = bitcoin_data.json()
        price = float(parsed_data["data"]["priceUsd"])
        print(f"${price*quantity:,.4f}")

'''