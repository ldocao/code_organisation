#!/bin/bash

#PURPOSE: Will sync all directories hierarchy from app/ inside tests, so as you can arrange your tests. You should run this script each time you want to write some tests so as you are sure the tests folder is always in-sync with app/ . By default, only ["analytics", "cleaning", "data", "setup"] is synchronized, but you can add other folders by modifying dir_to_sync variable.
#USAGE:
# $ cd app/tests
# $ source sync_app_dir.sh


basedir="../"
dir_to_sync="domain infrastructure application interface"

for d in $dir_to_sync
do
    src=$basedir/$d
    echo $src
    rsync -av -f"+ */" -f"- *" $src ./
done

