import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('num',help="The fibonacci number that you want to calculate.", type=int)
    parser.add_argument('-o', '--output', help='Output result to file',\
                        action='store_true')
    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print(f'The {args.num} fibonacci number is {result}.')
    elif args.quiet:
        print(result)
    else:
        print(f'fib({str(args.num)}) = {str(result)}')

    if args.output:
        f = open('fibonacci.txt', 'a')
        f.write(str(result)+'\n')

if __name__ == '__main__':
    main()
