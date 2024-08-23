import requests
from pystyle import Colors, Colorate

text = """
 █████  ███    ██  █████  ██      ██    ██ ███████ ███████ ██████  
██   ██ ████   ██ ██   ██ ██       ██  ██     ███  ██      ██   ██ 
███████ ██ ██  ██ ███████ ██        ████     ███   █████   ██████  
██   ██ ██  ██ ██ ██   ██ ██         ██     ███    ██      ██   ██ 
██   ██ ██   ████ ██   ██ ███████    ██    ███████ ███████ ██   ██ 
                                                                   
                                                                   
"""
print(Colorate.Horizontal(Colors.red_to_green, text, 1))
print(Colorate.Horizontal(Colors.red_to_green, "[@] Author: raccoon888"))
url = input(Colorate.Horizontal(Colors.red_to_green, "[?] Введите ссылку на API: "))

response = requests.get(url)

data = response.json()

for key, value in data.items():
    print(Colorate.Horizontal(Colors.red_to_green, f"[+] Поле: {key}, Значение: {value}"))
