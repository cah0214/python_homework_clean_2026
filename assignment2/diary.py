from email import message
import traceback

# Task 1
try:
    with open("diary.txt", "a") as diary_file:
        first_entry = True

        while True:
            if first_entry:
                entry = input("What happened today? ")
                first_entry = False
            else:
                entry = input("What else? ")

            diary_file.write(entry + "\n")

            if entry =="done for now":
                break
except Exception as e:
    print("An exception occured.")
    print(f"Exception type: {type(e).__name__}")

    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]}, Func.Name : {trace[2]}, Line No : {trace[1]}, Message : {trace[3]}')

    message = str(e)        
    if message:
        print(f"Exception message : {message}")

        print(f"Stack trace: {stack_trace}")