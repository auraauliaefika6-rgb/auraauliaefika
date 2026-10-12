message1 = "hello world" 
message2 = message1 
message3 = "hello world" 

print(f"message1 ({id(message1)}) == message2 ({id(message2)})") (message1 == message2)
      # output ➜ message1 (2131034204400) == message2 (2131034204400) ➡ True
      
print(f"message1 ({id(message1)}) == message3 ({id(message3)})") (message1 == message3) 
      # output ➜ message1 (2131034204400) == message3 (2131034205616) ➡ True 

print(f"message2 ({id(message2)}) == message3 ({id(message3)})") (message2 == message3) 
      # output ➜ message2 (2131034204400) == message3 (2131034205616) ➡ True