%define _topdir %(echo `cd ..; pwd`)
%define name mercurial
%define version 2.7.2
%define unmangled_version 2.7.2
%define release 1

Summary: Fast scalable distributed SCM (revision control, version control) system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://pypi.python.org/packages/source/M/Mercurial/%{name}-%{unmangled_version}.tar.gz
License: GNU GPLv2 or any later version
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildRequires: python
Requires: python
Vendor: Matt Mackall and many others <mercurial@selenic.com>
Url: http://mercurial.selenic.com/

%description
Mercurial is a distributed SCM tool written in Python. It is used by a number of large projects that require fast, reliable distributed revision control, such as Mozilla.

%prep
%setup -n %{name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Sat Oct 26 2013 Jukka Ojaniemi <jukka.ojaniemi@gmail.com> - 2.7.2-1
- Initial RPM release
