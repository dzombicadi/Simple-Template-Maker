# imports
import argparse

c_ext = "c"
cpp_ext = "cpp"

c_write = '''#include <stdio.h>

// This is automatically generated template

int main() {

}
'''

def import_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--extension', type=str, required=True, help="Available extensions: C, C++", metavar="[c, cpp]")
    parser.add_argument('-o', '--output', type=str, required=False, help="Name of the file you want.", metavar="[template.c/template.cpp]")
    arguments = parser.parse_args()

    print(arguments)

    which_ext(arguments.extension, arguments.output)


def which_ext(extension, output):
    tmp_name = "template"

    if(output == None):
        print("File name not given, default is: template")
    else:
        tmp_name = output

    if(extension == c_ext):
        make_c_file(tmp_name)
    else:
        print("a")

        
        
def make_c_file(tmpn):
    file = open("{}.c".format(tmpn), "a+")
    file.writelines(c_write)
    file.close()



if __name__ == '__main__':
    import_args()
    tmp_name = "template"



