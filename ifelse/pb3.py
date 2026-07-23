a = "Rajus is a good boy"
b = "buy now"
c = "subscribe"
d = "click this"

message = input("Enter your comment ;")

if(a in message or b in message or c in message or d in message):
    print("This is a Spam")
else:
    print("This is not a Spama")