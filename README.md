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
  * Python 2.7.5
  * lxml, Pillow, python-ldap & pip
* plone42-virtualenv
  * System Python (2.6.x)
  * lxml, Pillow, python-ldap & pip
* plone41-virtualenv
  * System Python (2.6.x)
  * lxml, Pillow, python-ldap & pip
* plone40-virtualenv
  * System Python (2.6.x)
  * lxml, Pillow, python-ldap & pip
* plone3-virtualenv
  * Python 2.4.6
  * lxml, Pillow (1.7.8), python-ldap & pip

I included an vagrant setup for building CentOS 6.4 box for testing & creating
RPMS.

## Setup your build environment

You will need following:

1. CentOS/RHEL 6.x box or [Vagrant](http://www.vagrantup.com) (there is an vagrant setup included).
2. RPM build tools:

        $ sudo yum groupinstall "Development Tools"
        $ sudo yum install kernel-devel rpmdevtools rpmlint rpm-build
3. BuildRequirements for each package. Commands to install package-specific
   requirements are listed below in the package specific instructions.
4. Clone this repo.
5. Build rpms:

        $ rpmbuild -bb <specfile>.spec

## Package build requirements

### Python 2.4.6 & 2.7.5:

Below command will install required packages for building python 2.4/2.7 rpms:

    $ sudo yum install autoconf bzip2 bzip2-devel db4-devel expat-devel
    findutils gcc-c++ glibc-devel make openssl-devel pkgconfig readline-devel
    sqlite-devel tar zlib-devel

Resulting rpm is tailored serving web apps and won't include support for
ncurses, tk and few more libs. If you need support for eg. ncurses you can
modify the 'configure' commands parameters and install required development
packages. RPMs will install python under /usr/local/python<24/27>. If you want
to use different prefix, just modify spec-files configure-command.

To build python rpms go under SPECS-folder and run:

    $ rpmbuild -bb python24.spec python27.spec


### Git 1.8.4.1:

    $ sudo yum install zlib-devel openssl-devel curl-devel expat-devel gettext
    xmlto asciidoc perl-Error perl-ExtUtils-MakeMaker
    $ rpmbuild -bb git.spec

If you don't need git docs you can run:

    $ rpmbuild -bb git.spec --without docs


### Mercurial 2.7.2:

    $ sudo yum install python python-devel
    $ rpmbuild -bb mercurial.spec

### Supervisor 3.0:

    $ sudo yum install python python-devel python-meld3 python-setuptools
    $ rpmbuild -bb supervisor.spec

### Setuptools 1.1.6:

    $ sudo yum install python python-devel
    $ rpmbuild -bb setuptools.spec

### plone-virtualenvs:

Building plone43-virtualenv assumes you have already built and installed
python2.7. Same goes to plone3-virtualenv - you should have built and installed
python24. Virtualenvs will be installed under /usr/local/virtualenvs/plone<xx>.
If you want to use another location, feel free to modify spec-file.

    $ sudo yum install python27 python27-devel python24 python24-devel
    libxslt-devel libxml2-devel openldap-devel libpng-devel libjpeg-turbo-devel
    zlib-devel freetype-devel openssl-devel python-virtualenv $ rpmbuild -bb
    plone3-virtualenv plone40-virtualenv plone41-virtualenv plone42-virtualenv
    plone43-virtualenv
    $ rpmbuild -bb plone43-virtualenv plone42-virtualenv plone41-virtualenv
    plone40-virtualenv plone3-virtualenv
