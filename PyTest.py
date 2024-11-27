def main(input_str):
    try:
        num1, operator, num2 = input_str.split()
        num1, num2 = int(num1), int(num2)
        if not (1 <= num1 <= 10 and 1 <= num2 <= 10):
            raise ValueError("Числа должны быть от 1 до 10")

        if operator == '+':
            return str(num1 + num2)
        elif operator == '-':
            return str(num1 - num2)
        elif operator == '*':
            return str(num1 * num2)
        elif operator == '/':
            return str(num1 // num2)
        else:
            raise ValueError("Неверный оператор")
    except:
        return "throws Exception"

