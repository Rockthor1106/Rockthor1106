#we can use
# try: (code)
# except: 
# (code)
# to manage exceptions in our programs

#A function to find the smallest value
def smallest():
    smallest_so_far = None
    print("Before", )
    for the_num in [9, 41, 12, 3, 74, 15]:
        if smallest_so_far is None: #It takes the first position within the array and use it to compare
            smallest_so_far = the_num
        elif the_num < smallest_so_far :
            smallest_so_far = the_num
    print("After", smallest_so_far)

def exerciseFive():
    #Read a number while the variable entry is not equal tod "done" if is not received a number then it prints an error
    sum = 0
    count = 0
    while True:
        entry = input("Enter a number ")
        if entry == "done":
            break
        try: 
            sum = sum + int(entry)
            count = count + 1
        except: 
            print("Invalid Input")

    print(sum, count, sum/count)
    
