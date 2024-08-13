#myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
#for name, value in myDictionary.items():
 # print(f"{name} {value}")


print("🌟 Website Rating 🌟")
print()
website = {"name": "", "url": "", "description": "", "rating": ""}
for name in website:  website[name] = input(f"{name}: ")
print()
print("*********")
print()
for name, value in website.items():
  print(f"{name}: {value}")
  