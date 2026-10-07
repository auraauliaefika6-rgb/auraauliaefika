print("123456".isdigit()) 
# output ➜ True, karena 123456 adalah digit 

print("123abc".isdigit()) 
# output ➜ False, karena ada karakter abc yang bukan merupakan digit 

print('2⅓'.isdigit()) 
# output ➜ False, karena bilangan pecahan memiliki karakter `/` yang tidak termasuk dalam kategori digit 

print('4²'.isdigit()) 
# output ➜ True, karena 4² adalah bilangan pangkat 

print('٢٨'.isdigit()) 
# output ➜ True, karena ٢٨ adalah digit arabic 

print('𝟜'.isdigit()) 
# output ➜ True, karena 𝟜 adalah digit