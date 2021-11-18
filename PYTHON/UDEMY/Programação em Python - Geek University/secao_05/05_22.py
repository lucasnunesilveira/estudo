age = int(input("how old are you"))
service_time = float(input("service time"))
if age > 65:
    print("Ok , can retire")
if service_time > 30:
    print("Ok , can retire")
if service_time > 30 and age > 65:
    print("Ok, can retire")
else:
    print("Can’t get used to it")
