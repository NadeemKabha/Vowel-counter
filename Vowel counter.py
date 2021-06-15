'''import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--task')
parser.add_argument('--arg')
args = parser.parse_args()
task = args.task
arg = args.arg'''

arg = input("Input: ")
task="vowels"
def vowels(arg):
    arg = arg.lower()
    count = 0
    for i in range(0, len(arg)):
        if arg[i] in ['a', 'e', 'u', 'y', 'i', 'o']:
            count += 1

    return count


def perfect(arg):
    prfct = [0, 1]
    for i in range(2, 81):
        for j in range(2, 14):
            if (i ** j) < 6401:
                prfct.append(i ** j)
    sorted(prfct)
    fprf = []
    for i in sorted(prfct):
        if i not in fprf:
            fprf.append(i)
    arg=int(arg)
    return fprf[arg]


def lazy(arg):
    arg = int(arg)
    x = int(((arg ** 2) - arg + 2) / 2)
    return x


if task == 'vowels':
    print(vowels(arg))
elif task == 'lazy':
    print(lazy(arg))
elif task == 'perfect':
    print(perfect(arg))
