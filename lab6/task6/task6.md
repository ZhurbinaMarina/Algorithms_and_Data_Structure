# Задание №6 по выбору: `Фибоначчи возвращается`
Журбина Марина Андреевна | K3139 | ID: 465906

## Вариант 11

## Задание 
Вам дается последовательность чисел. Для каждого числа определите, является ли оно числом Фибоначчи. Напомним, что числа Фибоначчи определяются, например, так:
```
F0 = F1 = 1
Fi = Fi−1 + Fi−2 для i ≥ 2
```
• **Формат ввода / входного файла (input.txt).** Первая строка содержит одно число N (1 ≤ N ≤ 10 ** 6) - количество запросов. Следующие N строк содержат по одному целому числу. При этом соблюдаются следующие ограничения при проверке:
1. Размер каждого числа не превосходит 5000 цифр в десятичном представлении.
2. Размер входа не превышает 1 Мб.
• **Формат вывода / выходного файла (output.txt).** Для каждого числа, данного во входном файле, выведите «Yes», если оно является числом Фибоначчи, и «No» в противном случае.


## Input / Output 

| Input    | Output |
|----------|----------|
| 8    | Yes   |
| 1    | Yes   |
| 2    | Yes   |
| 3    | No   |
| 4    | Yes   |
| 5    | No   |
| 6    | No   |
| 7    | Yes   |
| 8    |    |

## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
- Ограничение по памяти. 128 мб.

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
   python -m lab6.task6.src.task_6
   ```

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover -s lab6/task6 -p "*_tests.py"
```