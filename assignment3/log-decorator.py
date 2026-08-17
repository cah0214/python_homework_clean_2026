import logging 

# Task 1 

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        logger.log(logging.INFO, f"function: {func.__name__}")
        
        if args:
            logger.log(logging.INFO, f"positional parameters: {list(args)}")
        else:
            logger.log(logging.INFO, "positional parameters: none")

        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        else:
            logger.log(logging.INFO, "keyword parameters: none")
        logger.log(logging.INFO, f"return: {result}")

        return result
    return wrapper

@logger_decorator
def hello():
    print("Hello, World!")

@logger_decorator
def positional_function(*args):
    return True
@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator

hello()
positional_function(1, 2, 3)
keyword_function(name="Crystal", course="Python")


