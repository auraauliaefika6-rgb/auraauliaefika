message1 = "hello world" 
message2 = message1 
message3 = "hello world" 

print(f"message1 ({id(message1)}) is message2 ({id(message2)}) {message1 is message2}") 
# output ➜ message1 (2131034204400) is message2 (2131034204400) ➡ True 

print(f"message1 ({id(message1)}) is message3 ({id(message3)}) {message1 is message3}") 
# output ➜ message1 (2131034204400) is message3 (2131034205616) ➡ False