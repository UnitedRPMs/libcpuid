%global gitdate 20190601
%global commit0 179fbcb713566c2084a1903729b6eebba68a4424
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libcpuid
Version:        0.5.1
Release: 	1%{?gver}%{dist}
Summary:        Provides CPU identification for x86
License:        BSD-2-Clause
Group:		Development/Libraries
Url:            https://github.com/anrieff/libcpuid
Source0: 	https://github.com/anrieff/libcpuid/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  make git autoconf libtool automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libcpuid provides CPU identification for the x86 (and x86_64).

%package devel
Summary:	Development files for libcpuid
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package provides the development files required to build
applications.

%prep
%autosetup -n %{name}-%{commit0}


%build
libtoolize
autoreconf --install
%configure


make V=1 %{?_smp_mflags}


%install
make V=1 DESTDIR=%{buildroot} install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%{_bindir}/cpuid_tool
%{_libdir}/libcpuid.so.15
%{_libdir}/libcpuid.so.15.0.1


%files devel
%{_libdir}/pkgconfig/libcpuid.pc
%{_includedir}/libcpuid/libcpuid.h
%{_includedir}/libcpuid/libcpuid_constants.h
%{_includedir}/libcpuid/libcpuid_types.h
%{_libdir}/libcpuid.a
%{_libdir}/libcpuid.so

%changelog

* Sat Apr 17 2021 David Va <davidva at tuta dot io> 0.5.1-1.git179fbcb
- Updated to 0.5.1-1.git179fbcb

* Wed May 27 2020 David Vasquez <davidjeremias82 at gmail dot com> 0.5.0-1.git5da90c9
- Updated to 0.5.0-1.git5da90c9

* Sat Jun 01 2019 David Vasquez <davidjeremias82 at gmail dot com> 0.4.1-2.git7a0701d
- Updated to 0.4.1-2.git7a0701d

* Mon Jul 03 2017 David Vasquez <davidjeremias82 at gmail dot com> 0.4.0-2.gitb5bd535
- Updated to 0.4.0-2.gitb5bd535

* Thu Jan 12 2017 David Vasquez <davidjeremias82 at gmail dot com> - 0.4.0-1-20170112gitfa87a5e
- Updated to 0.4.0-20170112gitfa87a5e

* Thu Apr 28 2016 David Vasquez <davidjeremias82 at gmail dot com> - 0.2.1-3-20151001git4e3b633
- Rebuilt 

* Thu Oct 01 2015 David Vasquez <davidjeremias82 at gmail dot com> - 0.2.1-2-20151001git4e3b633
- Updated to 0.2.1-20151001-4e3b633

*Tue Apr 14 2015 David Vasquez <davidjeremias82 at gmail dot com> - 0.2.1-1-20150414git325904f
- Updated to 0.2.1-20150414-325904f

* Sun Feb  2 2014 dap.darkness@gmail.com
- Initial build.
