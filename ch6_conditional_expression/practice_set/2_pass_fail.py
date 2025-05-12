#if student on avg have percentage > 40 and for each subject marks >=33% (HE/SHE is passed else failed)

a = int(input("Enter Physics marks /100 : "))
b = int(input("Enter Maths marks /100 : "))
c = int(input("Enter Chemistry marks /100 : "))

total_avg = ( ( (a+b+c)/3 ) * 100 )

if total_avg>40 and a>=33 and b>=33 and c>=33:
    print("passed")
else:
    print("Better Luck next time -- Failed !")