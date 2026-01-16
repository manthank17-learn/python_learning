def eval_loop():
    last = None

    while True:
        user_input = input("what you wanna do chat?: ")

        if user_input == "done":
            return last

        result = eval(user_input)
        print(result)
        last = result

final_value = eval_loop()
print("Last value:", final_value)
