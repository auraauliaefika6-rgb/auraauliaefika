print("123abc".isalnum()) 
# output ➜ True, karena 123 adalah digit dan abc adalah alfabet 

print("12345⅓".isalnum()) 
# output ➜ True, karena 12345⅓ adalah digit 

print("abcdef".isalnum()) 
# output ➜ True, karena abcdef adalah alfabet 

print("abc 12".isalnum()) 
# output ➜ False, karena ada karakter spasi yang bukan merupakan karakter digit ataupun alfabet 

print("موز".isalnum()) 
# output ➜ True, karena موز adalah abjad arabic 

print("⯑⯑⯑".isalnum()) 
# output ➜ True, karena ⯑⯑⯑ adalah karakter jepang