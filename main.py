# imports
import argparse

c_ext = "c"
cpp_ext = "cpp"
cs_ext = "cs"

c_write = '''#include <stdio.h>

// This is automatically generated template

int main() {

}
'''
cpp_write = '''#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}'''
cs_write = '''using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hello World!");    
    }
  }
}'''



def import_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--extension', type=str, required=True, help="Available extensions: C, C++", metavar="[c, cpp, cs]")
    parser.add_argument('-o', '--output', type=str, required=False, help="Name of the file you want.", metavar="[template.c/template.cpp/template.cs]")
    arguments = parser.parse_args()

    which_ext(arguments.extension, arguments.output)


def which_ext(extension, output):
    tmp_name = "template"

    if(output != None):
        tmp_name = output 

    if(extension == c_ext):
        make_file(tmp_name, c_ext)
    elif(extension == cpp_ext):
        make_file(tmp_name, cpp_ext)
    elif(extension == cs_ext):
        make_file(tmp_name, cs_ext)
    else:
        print("Available extensions are: 'c', 'cpp', 'cs'")

        
        
def make_file(tmp_name, ext):
    file = open("{}.{}".format(tmp_name, ext), "a+")

    if(ext == c_ext):
        file.writelines(c_write)
    elif(ext == cpp_ext):
        file.writelines(cpp_write)
    elif(ext == cs_ext):
        file.writelines(cs_write)

    file.close()


if __name__ == '__main__':
    import_args()



