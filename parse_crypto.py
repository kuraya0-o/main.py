import requests
from bs4 import BeautifulSoup as Bs

def printArr(arr: list, count: int):
    arr.sort(key=lambda x: x[2], reverse=True)
    print(f'{"Название":>60}{"Ссылка":^70}{"Прайс":>10}')
    for i in range(min(len(arr), count)):
        print(f"{arr[i][0]:>60} {arr[i][1]:^70} {arr[i][2]:>10.2f}")



def getHtml() -> str:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }
        r = requests.get("https://etherscan.io/tokens", headers=headers)
        if r.status_code == 200:
            return r.text
        else:
            return "error"
    except Exception as e:
        return "error"   

def main():
    count = input("Введите количество записей или оставьте поле пустым ->")
    if count.isdigit():
        

if __name__ == "__main__":
    main()