# imports
import sys, getopt

argumentList = sys.argv[1:]
options = "hen:"
long_options = ["help", "extension", "name"]

def main():
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)

        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--help", " "):
                print("Example usage:")
                print("python3 main.py [-e EXTENSION or -extension EXTENSION] [-n OUTPUT_FILE]")

            elif currentArgument in ("-e", "--extension"):
                print("File extension asked is: ", sys.argv[0])

            elif currentArgument in ("-n", "--name"):
                print (("File name is: % s") % (currentValue))

    except getopt.error as err:
        print(str(err))





if __name__ == '__main__':
    main()



