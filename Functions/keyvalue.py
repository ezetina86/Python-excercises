# Receive keys value arguments
def listterms(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


listterms(IDE='Integrated Development Environment', PK='Primary Key')
listterms(DBMS='Database Management System')
