import requests

def main():
    base= input("first currency: ")
    other= input("second currency: ")
    res = requests.get("http://api.fixer.io/lastest", params={"base":base, "symbols":other})
    if res.status.code != 200:
        raise Exception("Error: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()