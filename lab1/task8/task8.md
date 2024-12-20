# Задание №8 по выбору: `Секретарь Своп`
Журбина Марина Андреевна | K3139 | ID: 465906

## Вариант 8

## Задание 
Дан массив, состоящий из n целых чисел. Вам необходимо его отсортировать по неубыванию. Но делать это нужно так же, как это делает мистер Своп — то есть, каждое действие должно быть взаимной перестановкой пары элементов. Вам также придется записать все, что Вы делали, в файл, чтобы мистер Своп смог проверить Вашу работу.
• **Формат входного файла (input.txt).** В первой строке входного файла содержится число n (3 ≤ n ≤ 5000) — число элементов в массиве. Во второй строке находятся n целых чисел, по модулю не превосходящих 10 ** 9. Числа могут совпадать друг с другом.
• **Формат выходного файла (output.txt).** В первых нескольких строках выведите осуществленные Вами операции перестановки элементов. Каждая строка должна иметь следующий формат:
Swap elements at indices X and Y.
Здесь X и Y — различные индексы массива, элементы на которых нужно переставить (1 ≤ X, Y ≤ n). Мистер Своп любит порядок, поэтому сделайте так, чтобы X < Y.
После того, как все нужные перестановки выведены, выведите следующую фразу:
No more swaps needed.

## Input / Output 

| Input    | Output |
|----------|----------|
| 5    | Swap elements at indices 1 and 2.   |
| 3 1 4 2 2    | Swap elements at indices 2 and 4.   |
|     | Swap elements at indices 3 and 5.   |
|     | No more swaps needed.   |

## Ограничения по времени и памяти

- Ограничение по времени. 1сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ZhurbinaMarina/Algorithms_and_Data_Structure.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Algorithms_and_Data_Structure/lab1
   ```
3. Запустите программу:
   ```bash
   python -m lab1.task8.src.task_8
   ```

## Тестирование
Для запуска тестов выполните:
```bash
 python -m unittest discover -s lab1/task8 -p "*_tests.py"
```