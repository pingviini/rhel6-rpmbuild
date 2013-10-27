#!/bin/bash

paths="http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2
http://www.python.org/ftp/python/2.4.6/Python-2.4.6.tar.bz2
https://pypi.python.org/packages/source/M/Mercurial/mercurial-2.7.2.tar.gz
https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz
https://pypi.python.org/packages/source/s/supervisor/supervisor-3.0.tar.gz
http://git-core.googlecode.com/files/git-1.8.4.1.tar.gz"

if [ ! -d "SOURCES" ]; then
    mkdir SOURCES
fi

for path in $paths
do
    filename=${path##*/}
    if [ ! -f "./SOURCES/$filename" ]; then
        echo "Downloading $filename"
        wget -q $path --no-check-certificate -P SOURCES
    fi
done

