#!/bin/bash

# repack ear
cd ${targetPath}
touch ${previousDeployed.name}.ear
rm -rf ${targetPath}/${previousDeployed.name}
