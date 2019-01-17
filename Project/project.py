import argparse

parser = argparse.ArgumentParser()
parser.add_argument('c', default=[], nargs='*')
args = parser.parse_args()
a = []
try:
    for x in args.c:
        d = int(x)
        a.append(d)
    if len(args.c) == 0:
        print('NO PARAMS')
    elif len(args.c) == 1:
        print('TOO FEW PARAMS')
    elif len(args.c) > 2:
        print('TOO MUCH PARAMS')
    else:
        print(sum(a))
except BaseException as err:
    print(err.__class__.__name__)