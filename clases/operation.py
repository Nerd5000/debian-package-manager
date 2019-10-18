from os import remove
from subprocess import call
from os import chmod
def operation():
    chmod('./package.sh', 0o775)
    call('./package.sh', shell=True)
    remove('./package.sh')