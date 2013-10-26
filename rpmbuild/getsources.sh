#!/bin/bash

if [ ! -f "./SOURCES/Python-2.7.5.tar.bz2" ]; then
    wget http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2 --no-check-certificate
fi

if [ ! -f "./SOURCES/mercurial-2.7.2.tar.gz" ]; then
    wget https://pypi.python.org/packages/source/M/Mercurial/mercurial-2.7.2.tar.gz --no-check-certificate
fi

if [ ! -f "./SOURCES/Python-2.4.6.tar.bz2" ]; then
    wget http://www.python.org/ftp/python/2.4.6/Python-2.4.6.tar.bz2 --no-check-certificate
fi

if [ ! -f "./SOURCES/supervisor-3.0.tar.gz" ]; then
    wget https://pypi.python.org/packages/source/s/supervisor/supervisor-3.0.tar.gz --no-check-certificate
fi

if [ ! -f "./SOURCES/git-1.8.4.1.tar.gz" ]; then
    wget http://git-core.googlecode.com/files/git-1.8.4.1.tar.gz --no-check-certificate
fi
