import requests
def get_quotes():
    url = "https://api.freeapi.app/api/v1/public/quotes"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        number_of_quotes = data["data"]["currentPageItems"]
        quote_list = data["data"]["data"]
        # for quote in quote_list:
        #     print(f"Author: {quote["author"]}\nQuote: {quote["content"]}\n\n")
        return quote_list, number_of_quotes
    
    else:
        raise Exception("Failed to fetch data!")
    
def main():
    try:
        qoute_list , number_of_quotes= get_quotes()
        print(f"number of quotes: {number_of_quotes}")
        for quote in qoute_list:
            print(f"Author: {quote["author"]}\nQuote: {quote["content"]}\n")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
    