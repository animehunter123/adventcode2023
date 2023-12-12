# with f = open('input.txt'):
with open('input2.txt') as f:

    total=0
    for line in f:
        line = line.rstrip()
        digits = list(filter(str.isdigit,line))
        if digits:
            first_digit,last_digit = digits[0], digits[len(digits)-1]
            total += int(first_digit)*10 + int(last_digit)

print(f'the total is... {total}')