def convert(msg):
    msg = msg.replace(':)', '🙂')
    msg = msg.replace(':(', '🙁')
    print(msg)

def main():
    text = input()
    convert(text)

main()
