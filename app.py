

## from flask import Flask
# import requests
# from bs4 import BeautifulSoup
#
# app = Flask(__name__)
#
# text_name = ''
#
#
# @app.route('/')
# def index():
#     global text_name
#     return text_name
#
#
# def paging_func(paging):
#     global text_name
#     for a in paging:
#         url = f"http://dgu.ru/AllNews?pageNumber={a}&nt=1"
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")  # html.parser
#
#         data = soup.find("table", class_='table').find_all('h5', class_="card-title font-news text-darkblue text-uppercase")
#
#         for i in data:
#             text_name += (i.text + '\n\n')
#         print(f"работаю над {a} страницей")
#
#
# paging_list = []
# url = "http://dgu.ru/AllNews?pageNumber=1&nt=1"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")  # html.parser
# data_paging = soup.find('ul', class_="pagination").find_all("li", class_="page-item")
# for i in data_paging:
#     paging_list.append(i.text)
#
# paging_func(paging_list)
#
# print(text_name)
#
# if __name__ == "__main__":
#     app.run(debug=True)  # показывать все ошибки на странице конечному пользователю