from os import remove
from subprocess import call
from os import chmod
packageName=str(input('Enter Package Name : '))
shFile=open('package.sh','w')
shFile.write(
    """
#!/bin/sh
echo "Starting Update"
sudo apt-get update
echo "Finishing Update"
echo "Starting Downloading"
sudo apt-get install {0}
echo "Finishing Downloading"
    """.format(packageName))
shFile.close()
chmod('./package.sh', 0o775)
call('./package.sh',shell=True)
remove('./package.sh')
