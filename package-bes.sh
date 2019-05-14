#!/bin/bash

set -o errexit

appName='bes'
distributeDir='dist'

. venv/bin/activate

pyinstaller -y ${appName}.spec

cd ${distributeDir}

packageDir='..'
packageName="${appName}_$(date '+%Y%m%d-%H%M%S').tgz"
packageFile="${packageDir}/${packageName}"

tar czvf ${packageFile} ${appName}

cd - > /dev/null

echo -e "package file: ${packageName}"

deactivate
