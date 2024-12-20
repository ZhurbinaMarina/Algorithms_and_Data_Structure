# Задание №8 по варианту: `Постфиксная запись`
Журбина Марина Андреевна | K3139 | ID: 465906

## Вариант 8

## Задание 
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.
Дано выражение в обратной польской записи. Определите его значение.
• **Формат входного файла (input.txt).** В первой строке входного файла дано
число N (1 ≤ n ≤ 10 ** 6) – число элементов выражения. Во второй строке содержится выражение в постфиксной записи, состоящее из N элементов. В выражении могут содержаться неотрицательные однозначные числа и операции +, -, *. Каждые два соседних элемента выражения разделены ровно одним пробелом.
• **Формат выходного файла (output.txt).** Необходимо вывести значение записанного выражения. Гарантируется, что результат выражения, а также результаты всех промежуточных вычислений, по модулю будут меньше, чем 2 ** 31.


## Input / Output 

| Input    | Output |
|----------|----------|
| 7    | -102   |
| 8 9 + 1 7 - *    |    |



## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
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
   python -m lab4.task8.src.task_8
   ```

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover -s lab4/task8 -p "*_tests.py"
```