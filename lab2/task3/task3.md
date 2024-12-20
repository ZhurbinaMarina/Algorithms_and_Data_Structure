# Задание №3 по варианту: `Число инверсий`
Журбина Марина Андреевна | K3139 | ID: 465906

## Вариант 8

## Задание 
Инверсией в последовательности чисел A называется такая ситуация, когда i < j, а Ai > Aj . Количество инверсий в последовательности в некотором роде определяет, насколько близка данная последовательность к отсортированной. Например, в сортированном массиве число инверсий равно 0, а в массиве, сортированном наоборот - каждые два элемента будут составлять инверсию (всего n(n − 1)/2). Дан массив целых чисел. Ваша задача — подсчитать число инверсий в нем. Подсказка: чтобы сделать это быстрее, можно воспользоваться модификацией сортировки слиянием.
• **Формат входного файла (input.txt).** В первой строке входного файла содержится число n (1 ≤ n ≤ 10 ** 5) — число элементов в массиве. Во второй строке находятся n различных целых чисел, по модулю не превосходящих 10 ** 9.
• **Формат выходного файла (output.txt).** В выходной файл надо вывести число инверсий в массиве.

## Input / Output 

| Input    | Output |
|----------|----------|
| 10    | 17   |
| 1 8 2 1 4 7 3 2 3 6    |    |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


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
   python -m lab2.task3.src.task_3
   ```

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover -s lab2/task3 -p "*_tests.py"
```