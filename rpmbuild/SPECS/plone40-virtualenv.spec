%define _topdir %(echo `cd ..; pwd`)/
%define python_minver 2.6.6
%define shortname plone40
%define name %{shortname}-virtualenv
%define libname %{name}
%define version 1.0

Summary: Virtualenv for Plone 4.0 instances.
Name: %{name}
Version: %{version}
Release: 1
License: GPLv2
Group: System Environment/Daemons

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: python-devel >= %{python_minver}
BuildRequires: python >= %{python_minver}
BuildRequires: python-virtualenv
BuildRequires: libxslt-devel, libxml2-devel, openldap-devel, libpng-devel, libjpeg-turbo-devel
BuildRequires: zlib-devel, freetype-devel, openssl-devel
BuildRequires: prelink
Requires:      python >= %{python_minver}
Requires:      libxslt, libxml2, openldap, libpng, libjpeg-turbo, zlib, freetype, openssl
AutoReqProv:   no

%description
This packages provides %{shortname} virtualenv for Plone 4.0.

%prep

%build
if [ -d %{_builddir}/usr/local/virtualenvs/%{shortname} ]; then
    echo "Cleaning out stale build directory" 1>&2
    rm -rf %{_builddir}/usr/local/virtualenvs/%{shortname}
fi

mkdir -p %{_builddir}/usr/local/virtualenvs/%{shortname}
/usr/bin/virtualenv --no-site-packages -p /usr/bin/python %{_builddir}/usr/local/virtualenvs/%{shortname}
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U setuptools
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U pip
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U Pillow==1.7.8
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U lxml
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U python-ldap

echo "FIXING virtualenv PATHS"
find -H %{_builddir}/usr/local/virtualenvs/%{shortname} -type f | while read filename; 
do 
     perl -p -i.bak -e "s|%{_builddir}||g" ${filename} 
     if [ -f ${filename}.bak ]; then 
        rm -f ${filename}.bak 
        echo "FIXED ${filename}" 
     fi 
done

%install

mkdir -p %{buildroot}/usr/local/virtualenvs
cp -R %{_builddir}/usr/local/virtualenvs/%{shortname} %{buildroot}/usr/local/virtualenvs

# This avoids prelink & RPM helpfully breaking the package signatures:
/usr/sbin/prelink -u $RPM_BUILD_ROOT/usr/local/virtualenvs/%{shortname}/bin/python

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root,-)
/usr/local/virtualenvs/%{shortname}/

%changelog
* Sat Oct 26 2013 Ojaniemi Jukka <jukka.ojaniemi@gmail.com> 1.0-1
- First version
