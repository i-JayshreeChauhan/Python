from typing import List , Tuple , Dict , Union

#list of integer

#without type hints
num = [1,2,3,4]    #list

#with type hints
number : List[int] = [1,3,5,83,4]         #'typing' class allows list hint to be of one type only (in our case only int) 
number1 : List[Union[str,int]] = [1,20,"jjj","kkk",2,5,6,4,"A",3]  #to define list with multiple types of data , u use union (meaning value can be either str or int)


#tuple
t : Tuple[str,int] = (1,3,4,"AA",2,0,23,"AB","CC",1)

#Dictionary
d : Dict[str,int] = {"ABC" : 1 , "XYZ": 10 , "WXY" : 4}