from sys import argv,path
from os import getcwd
path.insert(0,'{0}/clases'.format(getcwd()))
from operation import operation

if len(argv) > 1:
    if len(argv) > 2:
        if argv[1] == '-i' and argv[2] != None:
            import install
            install.installPackage(argv[2])
            operation()
        elif argv[1] == '-u' and argv[2] != None:
            import unistall
            unistall.uninstallPackage(argv[2])
            operation()
    else:
        print("""
            (Linux Package Manager)
            ==============================
            (-i) for installing a package 
            (-u) for unistalling a package
            ------------------------------
            then write the package name
            """)

else:
    print("""
    (Linux Package Manager)
    (1) for installing a package
    (2) for unistalling a package
    """)
    operationNumber = int(input('input operation number : '))
    packageName = str(input('Enter Package Name : '))
    if operationNumber == 1:
        import install
        install.installPackage(packageName)
    elif operationNumber == 2:
        import unistall
        unistall.uninstallPackage(packageName)
    else:
        print('Wrong Number')
    operation()
