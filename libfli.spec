Name:          libfli
Summary:       Finger Lakes Instrument Library
Version:       1.7
Release:       %mkrel 3
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
