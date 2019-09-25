customer = {
    "name": "Bishwa",
    "age": 31,
    "is_verified": True
}

print(customer["name"])
# None is an object that represents absence of value
print(customer.get("birthdate", "jan 1 1980"))

customer["name"] = "jack"
print(customer["name"])


#prog

phone = input("Phone: ")
digits_mappnig ={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output =""
for ch in phone:
    output += " " + digits_mappnig.get(ch,"!")
print(output)


#emoji
message = input(">")
words = message.split(" ")

emojis = {
    ":)": "😀",
    ":(": "😞"

}

output=""
for word in words:
    output += emojis.get(word, word)+ " "
print(output)
