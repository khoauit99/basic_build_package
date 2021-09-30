import argparse

parser = argparse.ArgumentParser(prog = "khoa_plus")
parser.add_argument('--number_1' , '-number_1' , type = int , default= 10 ,
 required= False , help="First_number_of_summation")
parser.add_argument('--number_2' , '-number_2' , type= int , default= 20,
 required= False , help="Second_number_of_summation")

def plus_2_num(a,b):
    tmp_sum = a+b
    return tmp_sum


def main():

    args = parser.parse_args()

    number_1 = args.number_1
    number_2 = args.number_2

    print(plus_2_num(number_1, number_2))