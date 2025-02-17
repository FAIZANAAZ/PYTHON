def main():
    fib=0
    sum=1
    while fib < 10000:
       print(fib)
       total_sum = fib + sum #  1 + 0 = 1 ,1+1=2
       fib=sum # 0 = 1 ,1=1
       sum=total_sum # 1 = 1, 2=2
if __name__ == '__main__':
    main()