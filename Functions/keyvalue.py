# Receive keys value arguments
def listterms(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


listterms(IDE='Integrated Development Environment', PK='Primary Key')
listterms(DBMS='Database Management System')


# variable Args

def displayNames(names):
    for name in names:
        print(names)


names = ["John", "Henry", "William"]
displayNames(names)
displayNames("Charles")
displayNames([10, 11])
