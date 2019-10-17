def installPackage(packageName):
    shFile = open('package.sh', 'w')
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
