%define _topdir %(cd ..; pwd)/
%define name python-setuptools
%define packagename setuptools
%define version 1.1.6
%define unmangled_version 1.1.6
%define release 1

Summary: Easily download, build, install, upgrade, and uninstall Python packages
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{packagename}-%{unmangled_version}.tar.gz
License: PSF or ZPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Python Packaging Authority <distutils-sig@python.org>
Url: https://pypi.python.org/pypi/setuptools

%description

%prep
%setup -n %{packagename}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/easy_install
/usr/bin/easy_install-2.6
/usr/lib/python2.6/site-packages/_markerlib/__init__.py
/usr/lib/python2.6/site-packages/_markerlib/__init__.pyc
/usr/lib/python2.6/site-packages/_markerlib/__init__.pyo
/usr/lib/python2.6/site-packages/_markerlib/markers.py
/usr/lib/python2.6/site-packages/_markerlib/markers.pyc
/usr/lib/python2.6/site-packages/_markerlib/markers.pyo
/usr/lib/python2.6/site-packages/easy_install.py
/usr/lib/python2.6/site-packages/easy_install.pyc
/usr/lib/python2.6/site-packages/easy_install.pyo
/usr/lib/python2.6/site-packages/pkg_resources.py
/usr/lib/python2.6/site-packages/pkg_resources.pyc
/usr/lib/python2.6/site-packages/pkg_resources.pyo
/usr/lib/python2.6/site-packages/setuptools-1.1.6-py2.6.egg-info
/usr/lib/python2.6/site-packages/setuptools

%defattr(-,root,root)

%changelog
* Sat Oct 26 2013 Jukka Ojaniemi <jukka.ojaniemi@gmail.com> - 3.0-1
- Initial RPM release
