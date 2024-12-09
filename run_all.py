import subprocess


def run_lab(lab_number, lab_tasks_numbers):
    for task_number in lab_tasks_numbers:
        print(f"RUNNING: lab{lab_number} task_{task_number}")

        input_f = open(f'lab{lab_number}/task{task_number}/txtf/input.txt')
        input_data = '\n\t'.join([x.strip() for x in input_f.readlines()])
        print(f'INPUT.TXT:\n\t{input_data}')

        subprocess.run(f'python lab{lab_number}/task{task_number}/src/task_{task_number}.py', shell=True, check=False)

        output_f = open(f'lab{lab_number}/task{task_number}/txtf/output.txt')
        output_data = '\n\t'.join([x.strip() for x in output_f.readlines()])
        print(f'OUTPUT.TXT:\n\t{output_data}')
        print('------------------------------------------')


if __name__ == '__main__':
    run_lab(1, [1, 2, 3, 5, 8, 10])
    run_lab(2, [1, 2, 3, 4, 5])
    run_lab(3, [1, 3, 4, 7, 8])
    run_lab(4, [1, 2, 3, 4, 5, 8, 9, '13_1', '13_4'])
    run_lab(5, [2, 4, 6, 7])
