import requests
# Пользовательский запрос
user_query = input("Введите название книги: ")

# Параметры запроса
params = {'q': f'"{user_query}"',
          'mode': 'everything'}

# Header -> User-Agent взят с httpbin.org
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/122.0.0.0 Safari/537.36"
  }

# Запрос с параметрами и заголовком(.json - говорит сайту использовать application/json, а не text/html)
responce = requests.get('https://openlibrary.org/search.json', params=params, headers=headers)


# Проверка на правильность запроса
if responce.status_code == 200:
    # print(responce.json())

    query = responce.json()['q']
    num_found = responce.json()['num_found']

    print(f"По запросу: {query}")
    print(f"Найдено: {num_found} результат(ов)")
    print()

    for i in range(num_found):

        # Title
        try:
            title_book = responce.json()['docs'][i]['title']
            print(f"\tНазвание: {title_book}")
        except KeyError:
            print('\tНет названия')

        # Author name
        try:
            author_name = responce.json()['docs'][i]['author_name']
            print(f"\tАвтор: {author_name[0]}")
        except KeyError:
            print('\tНет автора')

        # Publish_year
        try:
            publish_year = responce.json()['docs'][i]['publish_year']
            print(f"\tДата публикаций: {publish_year[0]}")
        except KeyError:
            print('\tДата публицации неизвестна')

        print()
