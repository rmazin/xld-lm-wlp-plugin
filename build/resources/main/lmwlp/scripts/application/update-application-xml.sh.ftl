#!/bin/bash

echo "Info: Updating the <web-uri> values in ${targetPath}/${deployed.name}/META-INF/application.xml."

cp ${targetPath}/${deployed.name}/META-INF/application.xml ${targetPath}/${deployed.name}/META-INF/application.xml.backup
sed 's/.war//g' ${targetPath}/${deployed.name}/META-INF/application.xml > ${targetPath}/${deployed.name}/META-INF/application.xml.tmp
cp ${targetPath}/${deployed.name}/META-INF/application.xml.tmp ${targetPath}/${deployed.name}/META-INF/application.xml
rm ${targetPath}/${deployed.name}/META-INF/application.xml.tmp

echo "Info: All the <web_uri> values have been updated."
rm ${targetPath}/${deployed.name}/META-INF/application.xml.backup
echo "Info: Unpacking complete."
