from http.client import responses

import requests

def main():
    try:
        #Делаю GET-запрос для получения первой страницы фактов
        response = requests.get("https://catfact.ninja/facts")
        response.raise_for_status()

        data = response.json()
        #Извлекаю общее количество фактов и количество на странице
        total_facts = data["total"]
        count_per_page = data["per_page"]

        #Вычисляю номер последней страницы
        last_page = (total_facts + count_per_page - 1) // count_per_page

        #Делаю второй запрос на последнюю страницу
        last_page_response = requests.get(f"https://catfact.ninja/facts?page={last_page}")
        last_page_response.raise_for_status()

        last_page_data = last_page_response.json()

        #Нахожу самый короткий факт
        shortest_fact = min(last_page_data["data"], key = lambda x: len(x["fact"]))

        #Вывожу результаты
        print(f"Самый короткий факт(по количеству символов) с последней страницы ({last_page}):")
        print(f"Длина: {len(shortest_fact["fact"])} символов.")
        print(f"Факт: {shortest_fact["fact"]}.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except KeyError as e:
        print(f"Ошибка в структуре ответа API: отсутствует ключ {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()