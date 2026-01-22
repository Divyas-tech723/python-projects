import requests

def convert_currency(from_currency, to_currency, amount):
    url = "https://api.frankfurter.app/latest"
    params = {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount
    }
    headers={
        "apikey":"your_API_key_here"  
    }

    response = requests.get(url, params=params,headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("full api response:",data)
        if "result" in data:
           converted = data['result']
           print(f"💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            print("error")
    else:
        print("Error fetching exchange rates.")

#Example usage
convert_currency("USD", "INR", 10)