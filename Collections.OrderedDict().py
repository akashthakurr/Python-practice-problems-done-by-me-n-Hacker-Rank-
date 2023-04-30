from collections import OrderedDict

ordered_dictionary=OrderedDict()
n=int(input())
for i in range(n):
    dictionary_details=input()
    item_name,net_price=' '.join(dictionary_details.split()[:-1]),int(dictionary_details.split()[-1])
    
    if item_name not in ordered_dictionary:
        ordered_dictionary[item_name]=net_price
    else:
        ordered_dictionary[item_name]+=net_price
        
for item,price in ordered_dictionary.items():
    print(item, price)