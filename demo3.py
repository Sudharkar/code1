print("hellp")
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

def fun(str):
  return str
print(f"this is a function {fun("string value will store")}")

print(f"comma with thousand seperated {43535:+}")

a=90
b=30
c=45
txt="value of a is {1} and b {1} is and c is{2}"
print(txt.format(a,b,c))  
print(txt.format(34,54,64))
str="my name is  {name} and recently i am in {place} and i am doing very hard word"
print(str.format(name="sudhakar",place="indore"))
print(str.format(place='indore',name="sudhakar"))  import logging

logging.basicConfig(level=logging.INFO)logging.info("Program started")def main():
    print("Hello")

    def convert_feet_to_meters(feet):
        return feet * 0.3048

    altitude_in_feet = 30000
    txt = f"The plane is flying at a {convert_feet_to_meters(altitude_in_feet):.2f} meter altitude"
    print(txt)

    def get_string(input_str):
        return input_str

    print(f"this is a function {get_string('string value will store')}")

    print(f"comma with thousand separated {43535:,}")

    a = 90
    b = 30
    c = 45
    txt = "value of a is {0} and b {1} is and c is {2}"
    print(txt.format(a, b, c))  
    print(txt.format(34, 54, 64))
    input_str = "my name is  {name} and recently i am in {place} and i am doing very hard word"
    print(input_str.format(name="sudhakar", place="indore"))
    print(input_str.format(place='indore', name="sudhakar"))

    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("Program started")

if __name__ == "__main__":
    main()

print("hellp")
logging.info("Program started")

def myconverter(x):
  logging.info("Converting feet to meters")
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
logging.info("Altitude calculated")
print(txt)

def fun(str):
  logging.info("Processing string")
  return str
print(f"this is a function {fun("string value will store")}")

print(f"comma with thousand seperated {43535:+}")

a=90
b=30
c=45
txt="value of a is {1} and b {1} is and c is{2}"
logging.info("Formatting string")
print(txt.format(a,b,c))  
print(txt.format(34,54,64))
str="my name is  {name} and recently i am in {place} and i am doing very hard word"
logging.info("Formatting string with variables")
print(str.format(name="sudhakar",place="indore"))
print(str.format(place='indore',name="sudhakar"))print("hello")
def convert_feet_to_meters(feet):
  return feet * 0.3048

altitude_in_feet = 30000
txt = f"The plane is flying at a {convert_feet_to_meters(altitude_in_feet):.2f} meter altitude"
print(txt)

def get_string(str):
  return str
print(f"this is a function {get_string('string value will store')}")

print(f"comma with thousand separated {43535:,}")

a = 90
b = 30
c = 45
txt = "value of a is {0} and b {1} is and c is {2}"
print(txt.format(a, b, c))  
print(txt.format(34, 54, 64))
str = "my name is  {name} and recently i am in {place} and i am doing very hard word"
print(str.format(name="sudhakar", place="indore"))
print(str.format(place='indore', name="sudhakar"))logging.basicConfig(level=logging.INFO)
logging.info("Program started")  