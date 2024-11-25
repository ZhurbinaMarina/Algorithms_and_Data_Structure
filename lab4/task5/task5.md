# Задание №5 по варианту: `Стек с максимумом`
Журбина Марина Андреевна | K3139 | ID: 465906

## Вариант 8

## Задание 
Стек - это абстрактный тип данных, поддерживающий операции Push() и Pop(). Нетрудно реализовать его таким образом, чтобы обе эти операции работали за константное время. В этой задаче ваша цель - реализовать стек, который также поддерживает поиск максимального значения и гарантирует, что все операции по-прежнему работают за константное время.
Реализуйте стек, поддерживающий операции Push(), Pop() и Max().
• **Формат входного файла (input.txt).** В первой строке входного файла содержится n (1 ≤ n ≤ 400000) – число команд. Последющие n строк исходного файла содержит ровно одну команду: push V, pop или max. 0 ≤ V ≤ 10 ** 5.
• **Формат выходного файла (output.txt).** Для каждого запроса max выведите (в отдельной строке) максимальное значение стека.


## Input / Output 

| Input    | Output |
|----------|----------|
| 5    | 2   |
| push 2    | 2   |
| push 1    |    |
| max    |    |
| pop     |    |
| max    |    |


## Ограничения по времени и памяти

- Ограничение по времени. 5 сек.
- Ограничение по памяти. 512 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ZhurbinaMarina/Algorithms_and_Data_Structure.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Algorithms_and_Data_Structure
   ```
3. Запустите программу:
   ```bash
   python -m lab4.task5.src.task_5
   ```

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover -s lab4/task5 -p "*_tests.py"
```