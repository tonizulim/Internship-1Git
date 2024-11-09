def split_to_str_len(str_len, txt):
    row=txt[0]
    return_str=[]
    for word in txt[1:]:
        if len(row) + len(word) <= str_len:
            row = row + " " + word
        else:
            return_str.append(row)
            row=word
    return_str.append(row)

    return return_str

def print_space(num):
    for i in range(num):
        print(' ', end="")

def print_center(page_len, txt):
    for row in txt:
        print_space(int(page_len/2)-int(len(row)/2))
        print(row)

str_len=int(input("Unesi duljinu reda: "))
page_len=int(input("Unesi duljinu stranice: "))

txt=[]
print("Unesi tekst:")

while True:
    str_temp=input()
    if(str_temp==""):
        break
    
    txt=txt+str_temp.split()


txt=split_to_str_len(str_len, txt)

print_center(page_len, txt)