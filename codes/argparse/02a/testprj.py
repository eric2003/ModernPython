import argparse

parser = argparse.ArgumentParser()

parser.add_argument('greeting',help='The greeting message displayed')
parser.add_argument('-n','--numbers',type=float,nargs=2,help='The numbers to be added')

args = parser.parse_args()

print(args)
print(args.greeting)
print(args.numbers)

if args.numbers is not None:
  print(args.numbers[0]+args.numbers[1])