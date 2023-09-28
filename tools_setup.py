import datetime

def my_brand(title):
    dateAndtime = datetime.datetime.now()
    brand = """=*=*=*= Juan Ocampo =*=*=*=

=*=*=*= Course 2023S-SSW567-WS =*=*=*= 

=*=*=*= {0} =*=*=*= 

=*=*=*= {1} =*=*=*= """.format(title, dateAndtime)
    print(brand)
    
my_brand("HW 00 - Tools Setup")
print("Hello World")