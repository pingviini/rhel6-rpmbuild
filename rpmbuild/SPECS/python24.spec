%define _topdir %(ehco `cd ..; pwd`)/
%define binsuffix 24
%define pybasever 2.4
%define version 2.4.6
%define name python
%define release 1
%define _prefix /usr/local/python24

Name: %{name}%{binsuffix}
Version: %{version}
Release: %{release}
Summary: An interpreted, interactive, object-oriented programming language.
Group: Development/Languages
Source0: http://www.python.org/ftp/python/2.4.6/Python-%{version}.tar.bz2

License: PSF
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

AutoReq: no
Provides: python(abi) = %{pybasever}

BuildRequires: autoconf
BuildRequires: bzip2
BuildRequires: bzip2-devel
BuildRequires: db4-devel
BuildRequires: expat-devel
BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: glibc-devel
# BuildRequires: gmp-devel
# BuildRequires: libffi-devel
# BuildRequires: libGL-devel
# BuildRequires: libX11-devel
BuildRequires: make
# BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: sqlite-devel
BuildRequires: tar
# BuildRequires: tcl-devel
# BuildRequires: tix-devel
# BuildRequires: tk-devel
BuildRequires: zlib-devel

%description
Python is an interpreted, interactive, object-oriented programming
language.  It incorporates modules, exceptions, dynamic typing, very high
level dynamic data types, and classes. Python combines remarkable power
with very clear syntax. It has interfaces to many system calls and
libraries, as well as to various window systems, and is extensible in C or
C++. It is also usable as an extension language for applications that need
a programmable interface.  Finally, Python is portable: it runs on many
brands of UNIX, on PCs under Windows, MS-DOS, and OS/2, and on the
Mac.

%package devel
Summary: The libraries and header files needed for Python extension development.
Requires: %{name} = %{version}-%{release}
Group: Development/Libraries

%description devel
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.
This package contains the header files and libraries needed to do
these types of tasks.

Install python-devel if you want to develop Python extensions.  The
python package will also need to be installed.  You'll probably also
want to install the python-docs package, which contains Python
documentation.

%prep
%setup -n Python-%{version}


%build
%configure \
	--enable-ipv6 \
	--enable-unicode=ucs4 \
	--enable-shared \
	--with-system-ffi \
	--with-system-expat \
	--prefix=%{_prefix}
%{__make} %{?_smp_mflags}


%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT

%{__make} altinstall DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/python{,2}
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/python{,2}-config
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/2to3
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/idle
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/pydoc
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/smtpd.py
%{__rm} -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/

%{__ln_s} %{_exec_prefix}/lib/python2.4/config $RPM_BUILD_ROOT%{_prefix}/lib/python2.4/config
%{__ln_s} %{_exec_prefix}/lib/python2.4/lib-dynload $RPM_BUILD_ROOT%{_prefix}/lib/python2.4/lib-dynload
%{__ln_s} %{_exec_prefix}/lib/ $RPM_BUILD_ROOT%{_prefix}/lib64

mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
touch $RPM_BUILD_ROOT/etc/ld.so.conf.d/python24.conf
echo "/usr/local/python24/lib64" > $RPM_BUILD_ROOT/etc/ld.so.conf.d/python24.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_prefix}/lib/python2.4/*
%{_prefix}/lib64
%{_bindir}/python2.4*
/usr/local/python24/lib/libpython2.4.so
/usr/local/python24/lib/libpython2.4.so.1.0
%config(noreplace) /etc/ld.so.conf.d/python24.conf

%doc

%files devel
%defattr(-,root,root,-)
%{_prefix}/include/python2.4/*
%{_prefix}/lib64

%changelog
* Sat Oct 26 2013 Jukka Ojaniemi <jukka.ojaniemi@gmail.com> - 2.4.6-1
- Initial RPM release
