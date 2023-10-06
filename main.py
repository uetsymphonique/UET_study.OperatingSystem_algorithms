from CPU_scheduling.CPU_scheduling import cpu_scheduling
from Semaphore.Semaphore import semaphore_examples
if __name__ == "__main__":
    choices = ['CPU scheduling algorithms', 'Semaphore examples']
    for i, choice in enumerate(choices):
        print(f'[{i+1}] {choice}')
    choice_index = -1
    while not 0 <= choice_index < len(choices):
        choice_index = int(input('Enter your choice: ')) - 1
    if choice_index == 0:
        cpu_scheduling()
    elif choice_index == 1:
        semaphore_examples()

