#!/bin/bash

cd ${targetPath}/${deployed.name}
# For each .war file, make a dir and unzip each within
WAR_COUNT=0
for WAR in `ls *.war`; do
  cd ${targetPath}/${deployed.name}
  # Trim off .war
  WAR_NAME=`echo $WAR | awk -F"." '{print $1}'`
  echo "Info: Unpacking $WAR into ${targetPath}/${deployed.name}/$WAR_NAME."
  mkdir $WAR_NAME
  mv $WAR $WAR_NAME
  cd $WAR_NAME

  unzip -q $WAR
	if [[ $? -ne 0 ]]; then
		echo "ERROR: $WAR did not unpack successfully."
		echo "		Exiting... "
		exit 5
	else
		echo "Info: $WAR unzipped successfully."
	fi
	WAR_COUNT=$((WAR_COUNT+1))

done

echo "Info: $WAR_COUNT were unzipped."

exit 0
