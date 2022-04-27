#!/usr/bin/env python


# for Sans else
def main01():
    l = [10,20,30,40]

    to_find = 80
    is_found = False    
    for i in l:
        if i == to_find:
            is_found=True
            break
        print(i)

    if is_found:
        print(f"la valeur {to_find} est dans la liste")
    else:
        print(f"la valeur {to_find} n'est pas dans la liste")

# for avec else
def main():
    l = [10,20,30,40]

    to_find = 80
    is_found = False    
    for i in l:
        if i == to_find:
            is_found=True
            break
        print(i)
    else:
        print(f"la valeur {to_find} n'est pas dans la liste")


    if is_found:
        print('ok')
    
if __name__ == '__main__':
    main()