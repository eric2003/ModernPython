import argparse

parser = argparse.ArgumentParser()

parser.add_argument('greeting',help='The greeting message displayed')

args = parser.parse_args()

print(args)

print(args.greeting)