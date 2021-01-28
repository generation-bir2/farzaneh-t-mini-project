product = []

def file_to_list(entry_list, file):
    for line in file:
        stripped_line = line.strip()
        entry_list.append(stripped_line)
    return entry_list

with open("products.txt", "r") as a_file:
    products = file_to_list(product, a_file)
    
print(*products, sep = "\n")