from time import time, sleep

default_msg_wait = 1

def output(string, wait=default_msg_wait):
    print(string)
    sleep(wait)


def ensure_choice(number):
    while True:
        try:
            choice = int(input("?"))
        except:
            continue
        if choice in range(1, number+1):
            break
    return choice

def question(question, options):
    output(question)
    for idx, option in enumerate(options):
        output(f"{idx+1}: {option}", wait=0)
    choice = ensure_choice(len(options))
    return choice