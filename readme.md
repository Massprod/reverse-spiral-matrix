# Completed [Trainee assignment](https://github.com/avito-tech/python-trainee-assignment) ![coverage](coverage.svg)
Задачи:
- [x] Библиотека содержит функцию со следующим интерфейсом:
  ```
  async def get_matrix(url: str) -> List[int]:
        ...
  ```
- [x] Функция единственным аргументом получает URL для загрузки матрицы с сервера по протоколу HTTP(S).
- [x] Функция возвращает список, содержащий результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла.
- [x] Взаимодействие с сервером должно быть реализовано асинхронно - посредством aiohttp, httpx или другого компонента на asyncio.
- [x] Библиотека должна корректно обрабатывать ошибки сервера и сетевые ошибки (5xx, Connection Timeout, Connection Refused, ...).
- [x] В дальнейшем размерность матрицы может быть изменена с сохранением форматирования. Библиотека должна сохранить свою работоспособность на квадратных матрицах другой размерности.
- [x] Решение задачи необходимо разместить на одном из публичных git-хостингов (GitHub, GitLab, Bitbucket). Можно также выслать решение в виде архива (zip, tar). Загружать библиотеку в PyPi или другие репозитории не требуется.

Для тестов ``pytest`` из рут директории.