# Задание №2 по варианту: `Высота дерева`
Журбина Марина Андреевна | K3139 | ID: 465906

## Вариант 8

## Задание 
В этой задаче ваша цель - привыкнуть к деревьям. Вам нужно будет прочитать описание дерева из входных данных, реализовать структуру данных, сохранить дерево и вычислить его высоту.
• Вам дается корневое дерево. Ваша задача - вычислить и вывести его высоту. Напомним, что высота (корневого) дерева - это максимальная глубина узла или максимальное расстояние от листа до корня. Вам дано произвольное дерево, не обязательно бинарное дерево.
• **Формат ввода или входного файла (input.txt).** Первая строка содержит число узлов n (1 ≤ n ≤ 10 ** 5). Вторая строка содержит n целых чисел от−1 до n − 1 – указание на родительский узел. Если i-ое значение равно −1, значит, что узел i - корневой, иначе это число является обозначением индекса родительского узла этого i-го узла (0 ≤ i ≤ n − 1). Индексы считать с 0. Гарантируется, что дан только один корневой узел, и что входные данные предстваляют дерево.
• **Формат вывода или выходного файла (output.txt).** Выведите целое число – высоту данного дерева.

## Input / Output 

| Input    | Output |
|----------|----------|
| 5    | 3   |
| 4 -1 4 1 1    |    |

## Ограничения по времени и памяти

- Ограничение по времени. 3 сек.
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
   python -m lab5.task2.src.task_2
   ```

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover -s lab5/task2 -p "*_tests.py"
```