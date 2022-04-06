import requests
from bs4 import BeautifulSoup

def get_page_content(fact_num):
    url = f'https://www.snapple.com/real-facts/{fact_num}'
    html_text = requests.get(url).text
    return BeautifulSoup(html_text, 'html.parser')


def get_fact(fact_num):
    
    text = get_page_content(fact_num)
    try:
        return text.find(class_ ='fact pt-3').get_text()
    except AttributeError:
        return f"ERROR! Fact number does not exist ({fact_num})"

def main():
    fact_list = []
    false_facts = 0

    for x in range(1600):
        current_fact = get_fact(x)

        if current_fact[0:5] == "ERROR":
            false_facts += 1
        else:
            false_facts = 0
        print(current_fact)
        fact_list.append(f"{current_fact}\n")

    f = open("snapple_facts.txt", "a")
    f.writelines(fact_list)
    f.close()
        

main()




