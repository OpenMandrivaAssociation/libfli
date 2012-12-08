Name:          libfli
Summary:       Finger Lakes Instrument Library
Version:       1.7
Release:       %mkrel 5
Url:           http://indi.sourceforge.net/index.php/Main_Page
License:       GPLv2+
Group:         Development/Other
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       http://downloads.sourceforge.net/indi/libfli1_%version.tar.gz
Patch0:        libfli-1.7.190-fix-link.patch
Patch1:        libfli-1.7.190-fix-lib.patch
BuildRequires: cmake

%description
Finger Lakes Instrument Library

#---------------------------------------------

%define fli_major 1
%define libfli %mklibname fli %{fli_major}

%package -n %libfli
Summary: %name library
Group: System/Libraries

%description -n %libfli
%name library

%files -n %libfli
%defattr(-,root,root)
%_libdir/libfli.so.%{fli_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/Other
Requires: %libfli = %version

%description  devel
Files needed to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_includedir/libfli.h
%_libdir/libfli.so

#---------------------------------------------

%prep
%setup -q -n libfli1-%version
%patch0 -p0
%patch1 -p0

%build
%cmake
%make

%install
rm -rf "%{buildroot}"
%makeinstall_std -C build

%clean
rm -rf "%{buildroot}"


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7-5mdv2011.0
+ Revision: 660248
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-4mdv2011.0
+ Revision: 602542
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-3mdv2010.1
+ Revision: 520769
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.7-2mdv2010.0
+ Revision: 425542
- rebuild

* Tue Nov 25 2008 Funda Wang <fwang@mandriva.org> 1.7-1mdv2009.1
+ Revision: 306529
- 1.7 final

* Wed Oct 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.7-0.190.5mdv2009.1
+ Revision: 298470
- Use default include dir,  kdeedu was wrong
  TODO: fix kdeedu

* Wed Oct 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.7-0.190.4mdv2009.1
+ Revision: 298263
- Bump release*
- Fix include path

* Wed Oct 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.7-0.190.2mdv2009.1
+ Revision: 298202
- Bump release
- Fix lib install on x86_64
- import libfli


