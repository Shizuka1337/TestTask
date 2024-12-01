def main(input_str):
    try:
        try:
            num1, operator, num2 = input_str.split()
        except ValueError:
            raise ValueError("Неправильный формат строки: должно быть 'число оператор число'")
        
        try:
            num1, num2 = int(num1), int(num2)
        except ValueError:
            raise ValueError("Одно из введённых значений не является числом")
        
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
            raise ValueError("Неверный оператор: используйте '+', '-', '*', '/'")
    except ValueError as e:
        return f"throws Exception: {e}"
