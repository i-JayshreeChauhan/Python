
####---- NOTE : these are just type hints (doesnt mean varible or function argument or return type are bound to that datatype)
####---------------Example : def sum(a:int,b:int) -> int: --- i can pass float value as arguments and return float type (ie. python will not stop u if you pass any other type of value )



# type --> explicitely(clearly/strongly) defining the datatype (so as we can use its methods)
 
n : int = 5          # ': <datatype>' ---defining datatype explicitely
s : str = "jayshree"

# hence we will be able to use various integer methods example n.bit_count , n.bit_length , etc.


#--------------------- type in functions ---------------------

"""
Syntax -->  def <function_name>(arg1 : <datatype> , arg2 : <datatype>) -> <return_datatype>:
"""

def sum(a:int,b:int) -> int:        # variable a will be of int type and b will be of int type --return type will be int
    return a+b