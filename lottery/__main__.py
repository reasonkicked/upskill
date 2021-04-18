import lottery.lottery
import sys


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")



# if __name__ == '__main__':
  #  main()
lottery.lottery_menu()

lottery.cli()
# print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
    print("File one executed when ran directly")
else:
    print("File one executed when imported")
