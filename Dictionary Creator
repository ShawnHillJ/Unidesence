file_pad = open(str(raw_input("enter filename in this directory:")),'r')
dictionary_blocks = {}
name_list = []
number_list = []
number_of_stuff = int(raw_input("enter number of indexes:")
for x in range(number_of_stuff):
    prewrite = file_pad.readline()[0:3]
    print(prewrite)
    number_list.append(prewrite)
print(name_list)
for y in range(number_of_stuff):
    rp = file_pad.readline()
    name_list.append(rp.rstrip())
for z in range(number_of_stuff):
    dictionary_blocks[number_list[z]] = name_list[z]
file_pad.close()
new_file = open("New Dictionary.txt","w")
new_file.write(str(dictionary_blocks))
new_file.close()
