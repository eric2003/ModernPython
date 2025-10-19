import argparse

parser = argparse.ArgumentParser()

parser.add_argument('greeting',help='The greeting message displayed')
parser.add_argument('-n','--numbers',type=float,nargs='*',help='The numbers to be added')
parser.add_argument('-v','--verbosity',type=int,choices=[0,1,2],help='Determin how much')

args = parser.parse_args()

print(args)

if args.verbosity is None:
  print(args.greeting)
  if args.numbers is not None:
    print(sum(args.numbers))
else:
  if args.verbosity == 0:
    print(args.greeting)
    if args.numbers is not None:
      print(sum(args.numbers))
  elif args.verbosity == 1:
    print(args.numbers)
  elif args.verbosity == 2:
    print('Extra info')
  