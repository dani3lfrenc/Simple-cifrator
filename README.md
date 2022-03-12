
# Cipher

In this project you can download and modify your cipher with the key that you need

# What you need to do

After you have downloaded the file, inside it, there is both in the decryption and encryption section, the number 2. This is the encryption key. You can replace this number with any key you like, which will be used to perform the two functions in this file.



## Usage/Examples

```python

def decript():
    code_to_cifrate = input("\nEnter the text you want to decrypt: ")

    code_to_cifrate_list = list(code_to_cifrate)


    cifrate_list = list("abcdefghijklmnopqrstuvwxyz @#")
    final_code = ""

    i2 = 0 

# Insert where there is the numeber 2, the key you would use, example: 3 ==> the cifrator goes 3 position forward

    for i in code_to_cifrate_list:
        new_pos = cifrate_list.index(i)-2  #<--- Here there is the key that you can change
        final_code = final_code + cifrate_list[new_pos]
        i2 = i2 + 1
    
    sleep(2)

    print("\n"+final_code+"\n")
```

