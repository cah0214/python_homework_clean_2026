def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"

def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
            return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "int":
            return int(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        
    except TypeError:
        return "Invalid data was provided."

def repeat(string, coount):
    result = ""

    for i in range(coount):
        result += string

    return result

def student_scores(option, **kwargs):
    if option == "mean":
       return sum(kwargs.values()) / len(kwargs)
    
    elif option == "best":
        best_name = ""
        best_score = -1

        for name, score in kwargs.items():
            if score > best_score:
                best_name = name
                best_score = score
        return best_name
    

def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"] 
    words = text.split()
    new_words = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            new_words.append(word.capitalize())
        elif word in little_words:
            new_words.append(word)
        else:
            new_words.append(word.capitalize())

    return " ".join(new_words)


def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

def pig_latin(test):
    vowels = "aeiou"
    words = test.split()
    pig_words = []

    for word in words:
        if word[0] in vowels:
            pig_words.append(word + "ay")
        else:
            index = 0

            while index < len(word):
                if word[index] in vowels:
                    if word[index] == "u" and index > 0 and word[index - 1] == "q":
                        index += 1
                    break
                index += 1


            pig_word = word[index:] + word[:index] + "ay"
            pig_words.append(pig_word)

    return " ".join(pig_words)



