# 5 ki table banane ke liye variable define kiya
table_of = 5

# range() function se 5 se start karte hue 100 tak numbers ka sequence banaya,
# jo har 5 ke gap ke saath chalega (5, 10, 15, ...100)

# x=range(start, stop, step)
x = range(table_of, 100, table_of)

# Counter shuru kiya 1 se, or lopp sy hm 1  2  3  ak ak + krwygy
counter = 1

# Loop x ke har number ke liye chalega
# or n me current number store hota jayga 5  10 
for n in x:
    # Agar counter 10 se zyada ho gaya, loop ko todh do (break)
    # or x bhi khoood 50 pr rok jayga
    if counter > 10: 
        break

    # Current number aur counter ko formatted output ke saath print karte hain
    # Example: "5 x 1 = 5"
    print(f'{table_of} x {counter} = {n}')

    # Har baar counter ko 1 se badhate hain
    counter += 1
