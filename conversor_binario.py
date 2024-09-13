# variable to store the binary number
number_binary = []
# variable for store the user number
number_decimal = number = int(input("type any number: "))
# loop to divide "number_decimal"
while number_decimal > 0:
    # to add the rest of the division inside the list "number_binary"
    number_binary.append(number_decimal % 2)
    number_decimal = number_decimal // 2
print(f"The number {number} transformed is: ")
# Loop for show numbers inside "number_binary" in sequence
for index, value in enumerate(number_binary):
    print(value, end=" ")
