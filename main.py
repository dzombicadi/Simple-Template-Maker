# imports
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--extension', type=str, required=True, help="Available extensions: C, C++", metavar="[c, cpp]")
    parser.add_argument('-o', '--output', type=str, required=False, help="Name of the file you want.", metavar="[template.c/template.cpp]")
    args = parser.parse_args()

    

   

if __name__ == '__main__':
    main()



