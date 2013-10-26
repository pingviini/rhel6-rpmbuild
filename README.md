# Introduction

This repository contains spec-files for building following rpm-packages
for RHEL/CentOS 6.x:

* Python 2.4.6
* Python 2.7.5
* Mercurial 2.7.2
* Git 1.8.4.1
* python-setuptools 1.1.6
* supervisor 3.0
* plone43-virtualenv
  * Uses Python 2.7.5
  * lxml 2.7.2
  * Pillow 2.2.1
  * python-ldap x.x
* plone42-virtualenv
  * System Python (2.6.x)
  * lxml 2.7.2
  * Pillow 2.2.1
  * python-ldap x.x
* plone41-virtualenv
  * System Python (2.6.x)
  * lxml 2.7.2
  * Pillow 2.2.1
  * python-ldap x.x
* plone40-virtualenv
  * System Python (2.6.x)
  * lxml 2.7.2
  * Pillow 1.7.8
  * python-ldap x.x
* plone3-virtualenv
  * Python 2.4.6
  * lxml 2.7.2
  * Pillow 1.7.8
  * python-ldap x.x

I included an vagrant setup for building CentOS 6.4 box for testing & creating
RPMS.

## Setup your build environment

You will need following:

1. CentOS/RHEL 6.x box or [Vagrant](http://www.vagrantup.com) (there is an vagrant setup included).
2. RPM build tools:

    $ sudo yum groupinstall "Development Tools"
    $ sudo yum install kernel-devel rpmdevtools rpmlint rpm-build
3. BuildRequirements for each package. Commands to install package-specific
   requirements are listed below.
4. Clone this repo.
5. rpmbuild -bb <specfile.spec>

## Package requirements

### Python 2.4.6 & 2.7.5:

    $ sudo yum install autoconf bzip2 bzip2-devel db4-devel expat-devel findutils gcc-c++ glibc-devel make openssl-devel pkgconfig readline-devel sqlite-devel tar zlib-devel

### Git 1.8.4.1:

    $ sudo yum install zlib-devel openssl-devel curl-devel expat-devel gettext xmlto asciidoc perl-Error perl-ExtUtils-MakeMaker

### Mercurial 2.7.2:

    $ sudo yum install python python-devel

### Supervisor 3.0:

    $ sudo yum install python python-devel python-meld3 python-setuptools

### Setuptools 1.1.6:

    $ sudo yum install python python-devel

### plone-virtualenvs:

    $ sudo yum install python27 python27-devel libxslt-devel libxml2-devel openldap-devel libpng-devel libjpeg-turbo-devel zlib-devel freetype-devel openssl-devel

