def luhn_algorithm():
    processed_numbers=[]
    number=list(input().strip())
    check_digit=number.pop()
    number.reverse()
    for index,digit in enumerate(number):
        if index%2==0:
            doubledigit=int(digit)*2
            if doubledigit > 9:
                doubledigit=doubledigit-9
            processed_numbers.append(doubledigit)
        else:
            processed_numbers.append(int(digit))
    total=(int(check_digit)+sum(processed_numbers))%10==0

    return total

print(luhn_algorithm())