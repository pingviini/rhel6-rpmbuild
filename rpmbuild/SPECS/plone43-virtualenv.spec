%define python_minver 	2.7.5

%define shortname	plone43
%define name		%{shortname}-virtualenv
%define libname     	%{name}
%define version		1.0


Summary: Virtualenv for Plone 4.3 instances.
Name: %{name}
Version: %{version}
Release: 1
License: GPLv2
Group: System Environment/Daemons

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: python27-devel >= %{python_minver}
BuildRequires: python27 >= %{python_minver}
BuildRequires: python-virtualenv
BuildRequires: libxslt-devel, libxml2-devel, openldap-devel, libpng-devel, libjpeg-turbo-devel
BuildRequires: zlib-devel, freetype-devel, openssl-devel
# BuildRequires: prelink
Requires:      python27 >= %{python_minver}
Requires:      libxslt, libxml2, openldap, libpng, libjpeg-turbo, zlib, freetype, openssl
AutoReqProv:   no

%description
This packages provides %{shortname} virtualenv for Plone 4.3.

%prep

%build
if [ -d %{_builddir}/usr/local/virtualenvs/%{shortname} ]; then
    echo "Cleaning out stale build directory" 1>&2
    rm -rf %{_builddir}/usr/local/virtualenvs/%{shortname}
fi

mkdir -p %{_builddir}/usr/local/virtualenvs/%{shortname}
/usr/bin/virtualenv --no-site-packages -p /usr/local/python27/bin/python2.7 %{_builddir}/usr/local/virtualenvs/%{shortname}
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U setuptools
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U pip
%{_builddir}/usr/local/virtualenvs/%{shortname}/bin/pip install -U Pillow
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

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root,-)
/usr/local/virtualenvs/%{shortname}/

%changelog
* Sat Oct 26 2013 Ojaniemi Jukka 1.0-1
- First version

