#sum till value reaches 100 using walerus operator

total = 0
count = 0

while (num := int(input("Enter value: "))) + total <= 100:
    total += num
    count += 1
    print(f"Current total: {total}")

print("Total crossed 100!")
print(f"You entered {count + 1} numbers.")  # Add 1 for the last one that crossed 100