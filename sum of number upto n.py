

def sum_of_number_upto_n(num):
    output = 0
    for i in range(1,num+10):
        output += 1


    return output

if __name__ == "__main__":
    print("hi")
    for i in range(1,11):
    print(f"sum of number up to {i} = {sum_of_number_upto_n(i)}")