# this is a small project that estimates the integration, derivative, and determinant like a terminal game
import math

class Calculus_Operation:
    def __init__(self, function):
        self.function = function
        self.funcs = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'ln': math.log,
            'log': math.log10,
            'sqrt': math.sqrt,
            'arctan': math.atan,
            'arccos': math.acos,
            'arcsin': math.asin,
            '!': math.factorial
        }
    def create_function(self):
        # create a function for math expression
        self.f = self.function.replace('^', '**')
    
        for self.func in self.funcs:
            self.f = self.f.replace(self.func, f"self.funcs['{self.func}']")
    
        return lambda x: eval(self.f)



    def print_result(self, result):
        self.result = result
        print(f"\nThe result of the calculation is {self.result}\n")

class Integral_Calculator(Calculus_Operation):
    # Using Riemann's Sum Method
    def riemann_sum(self, a, b, n):
        dx = (b - a) / n
        x = a
        self.result = 0
        for i in range(n):
            x += dx
            self.result += self.create_function()(x) * dx

class Derivative_Calculator(Calculus_Operation):
    def limit(self, x):
        # step size
        # for better accuracy, step size could be reduced
        h = 0.0001
        self.result = (self.create_function()(x + h) - self.create_function()(x)) / h


def determinant(A):
    # recursive funtion to return determinant value
    n = len(A)
    det = 0
    if n == 1:
        return A[0][0]
    elif n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        for i in range(n):
            matrix = [[A[j][k] for k in range(n) if k != i] for j in range(1, n)]
            det += ((-1)**i) * A[0][i] * determinant(matrix)
        return det



def form_matrix():
    size = int(input("To create a matix with n x n size, Please supply the value of n: "))
    credibility = True
    matrix = []
    for i in range(size):
        row = []
        temp_str_row = input(f"\nPlease enter the values of row {i+1} in format(e.g. 1,2,3,4,...): ")

        for i in temp_str_row.split(","):
            i = i.strip()
            if i:
                row.append(int(i))
        if(len(row) != size):
            credibility = False
        
        if credibility:
            matrix.append(row)
        else:
            print("\nYou did not supply right amount of values")
            break
    if credibility:
        return matrix
    


def main():
    print("\nHello there, we can help you with your integral and single variable differentiation problems. In addition, if there is matrix that you want its determinant to be determined, you are at the right place\n")
    print("Also, please take 1-2% of error into account\n")
    flag = True
    while(flag):
        choice = input("Please tell, which operation you would like to get help. For integral help enter \"a\", for derivative help enter \"b\", and for determinant calculation enter \"c\" : ")
        
        if choice == 'a' or choice == 'A':
            f = input("\nPlease enter the function: ")
            integral = Integral_Calculator(f)
            
            a = int(input("\nPlease enter the starting boundary of the integral: "))
            b = int(input("\nPlease enter the ending boundary of the integral: "))
            # n could be increased for better accuracy
            integral.riemann_sum(a, b, 10000)
            integral.print_result(integral.result)
            
        elif choice == 'b' or choice == 'B':
            f = input("\nPlease enter the function: ")
            diff = Derivative_Calculator(f)
            x = int(input("\nPlease enter at what value would you like to see the estimated value of the derivative of the function: "))
            diff.limit(x)
            diff.print_result(diff.result)

        elif choice == 'c' or choice == 'C':
            matrix = form_matrix()
            if matrix is not None:
                print(determinant(matrix))
        else:
            print("\nYou did not enter any valid options\n")

     
        con = input("\nDo you want to use it again(Please answer y or n): ")
        if con[0] == 'n' or con[0] == "N":
            flag = False
            print("\nThanks for choosing us!\n") 




main()





