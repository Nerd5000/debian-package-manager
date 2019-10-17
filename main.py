from os import remove
from subprocess import call
from os import chmod
print("""
(Linux Package Manager)
(1) for installing a package
(2) for unistalling a package
""")
operation=int(input('input operation number : '))
packageName = str(input('Enter Package Name : '))
if operation==1:
    import install
    install.installPackage(packageName)
elif operation==2:
    import unistall
    unistall.uninstallPackage(packageName)
chmod('./package.sh', 0o775)
call('./package.sh', shell=True)
remove('./package.sh')
