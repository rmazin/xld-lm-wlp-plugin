#!/bin/bash

# for debug purposes
echo ${targetPath}
echo ${deployed.name}

#move ear
mkdir ${targetPath}/${deployed.name}
mv ${targetPath}/${deployed.name}.ear ${targetPath}/${deployed.name}

# Validate EAR was move
moveCheck=`ls ${targetPath}/${deployed.name} | grep ${deployed.name}.ear | wc -l`
if [[ $moveCheck == 0 ]]; then
	echo "ERROR: ${deployed.name}.ear does not exist in ${targetPath}/${deployed.name} after move"
	echo "   Exiting... "
	exit 3
else
	echo "Info: Move of ${deployed.name}.ear completed successfully"
fi

cd ${targetPath}/${deployed.name}
unzip -q ${targetPath}/${deployed.name}/${deployed.name}.ear
if [[ $? -ne 0 ]]; then
	echo "ERROR: ${deployed.name}.ear did not unzip properly."
	echo "		Exiting... "
	exit 5
else
	echo "Info: ${deployed.name}.ear unzipped successfully."
fi
# Remove ear file
rm ${targetPath}/${deployed.name}/${deployed.name}.ear
