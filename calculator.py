


# take the operator input
 operator = (input('Enter operator ( either +, -, * or / ): '))

#take the operand input
 number1 = (int(input('Enter first number: ')))
 number2 = (int(input('Enter second number: ')))

let result;

# using if...else if... else
if (operator == '+') {
    result = number1 + number2;
}
else if (operator == '-') {
    result = number1 - number2;
}
else if (operator == '*') {
    result = number1 * number2;
}
else {
    result = number1 / number2;
}

# display the result
console.log(`${number1} ${operator} ${number2} = ${result}`);