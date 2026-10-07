print("123456".isdecimal()) 
# output ➜ True, karena 123456 adalah angka desimal 

print("123abc".isdecimal()) 
# output ➜ False, karena ada karakter abc yang bukan merupakan angka desimal 

print('2⅓'.isdecimal()) 
# output ➜ False, karena bilangan pecahan memiliki karakter `/` yang tidak termasuk dalam kategori angka desimal 

print('4²'.isdecimal()) 
# output ➜ False, karena bilangan pangkat yang tidak termasuk dalam kategori angka desimal 

print('٢٨'.isdecimal()) 
# output ➜ True, karena ٢٨ adalah angka desimal arabic 

print('𝟜'.isdecimal()) 
# output ➜ True, karena 𝟜 adalah angka desimal