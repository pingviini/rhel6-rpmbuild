%define _topdir %(cd ..; pwd)
%define name supervisor
%define version 3.0
%define unmangled_version 3.0
%define release 1

Summary: A system for controlling process state under UNIX
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://pypi.python.org/packages/source/s/supervisor/%{name}-%{unmangled_version}.tar.gz
License: BSD-derived (http://www.repoze.org/LICENSE.txt)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mike Naberezny <mike@naberezny.com>
Requires:  python-meld3, python-setuptools
Url: http://supervisord.org/

%description
Supervisor is a client/server system that allows its users to
control a number of processes on UNIX-like operating systems.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/echo_supervisord_conf
/usr/bin/pidproxy
/usr/bin/supervisorctl
/usr/bin/supervisord
/usr/lib/python2.6/site-packages/supervisor-3.0-py2.6-nspkg.pth
/usr/lib/python2.6/site-packages/supervisor-3.0-py2.6.egg-info
/usr/lib/python2.6/site-packages/supervisor


%changelog
* Sat Oct 26 2013 Jukka Ojaniemi <jukka.ojaniemi@gmail.com> - 3.0-1
- Initial RPM release
