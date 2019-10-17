def uninstallPackage(packageName):
    shFile = open('package.sh', 'w')
    shFile.write(
        """
    #!/bin/sh
    echo "Starting Update"
    sudo apt-get update
    echo "Finishing Update"
    echo "Start unistalling"
    sudo apt-get purge {0}
    echo "Finish unistalling"
        """.format(packageName))
    shFile.close()
