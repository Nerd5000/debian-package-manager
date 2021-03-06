def uninstallPackage(packageName):
    shFile = open('package.sh', 'w')
    shFile.write(
        """
    #!/bin/sh
    echo " "
    echo "======================="
    echo " "
    echo "Unistalling Started"
    echo " "
    echo "======================="
    echo " "
    sudo apt-get install {0}
    echo " "
    echo "======================="
    echo " "
    echo "Unistalling Finished"
    echo " "
    echo "======================="
    echo " "
    echo "Update started"
    echo " "
    echo "======================="
    echo " "
    sudo apt-get update
    echo " "
    echo "======================="
    echo " "
    echo "Update Finished"
    echo " "
    echo "======================="
    echo " "  
        """.format(packageName))
    shFile.close()
