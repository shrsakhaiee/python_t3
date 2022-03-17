n = int(input("Enter n:"))
for i in range (n):

    if n % 2 == 0:
        print("🟩" , end="")

    else:
        print("🟨" , end="")
        
    n = n - 1