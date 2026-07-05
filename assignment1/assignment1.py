def hello():
    return "Hello!"


def greet(name):
    return f"Hello, {name}!"


def calc(num1, num2, operation="multiply"):
    if operation == "multiply":
        try:
            return num1 * num2
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        if num2 == 0:
            return "You can't divide by 0!"
        else:
            return num1 / num2
    elif operation == "modulo":
        return num1 % num2
    


def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    


def grade(*scores):
    try:
        average = sum(scores) / len(scores)
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
    


def repeat(string, count):
    return string * count


def student_scores(score_type, **kwargs):
    if score_type == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif score_type == "best":
        return max(kwargs, key=kwargs.get)
    else:
        return "Invalid score type."

def titleize(string):
    little_words = ["a", "an", "the", "and", "but", "or", "for", "nor", "On", "at", "to", "from", "by"]
    words = string.split()
    titleized_words = []
    for i, word in enumerate(words):
        if i == 0 or word not in little_words:
            titleized_words.append(word.capitalize())
        else:
            titleized_words.append(word)
    return " ".join(titleized_words)

def hangman(word, guesses):
    result = ""
    for letter in word:
        if letter in guesses:
            result += letter
        else:
            result += "_"
    return result
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        elif word.startswith("qu"):
            pig_latin_words.append(word[2:] + "quay")
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    if word[i-1:i+1] == "qu":
                        pig_latin_words.append(word[i+1:] + word[:i+1] + "ay")
                    else:
                        pig_latin_words.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(pig_latin_words)
