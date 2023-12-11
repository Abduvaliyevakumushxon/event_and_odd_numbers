#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=1271
#Create a variable "sum_odd" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
x1=(var_int//1000)
a=x1%2
x2=(var_int//100%10)
b=x2%2
x3=(var_int//10%10)
c=x3%2
x4=(var_int%10)
d=x4%2
sum_odd=(a*x1+b*x2+c*x3+d*x4)
print(sum_odd)
