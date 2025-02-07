# Mixing *args with Regular Parameters

def greet(name, *messages):
  print(f"hello,{name}!")
  for msg in messages: # Loop through each item in messages its equivalent to for i in messages:
                      # print(i)
    print(msg)
greet("Alice","Good moening!", "How are you ?", "How can i help you?")    