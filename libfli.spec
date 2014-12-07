%define major	1
%define libname %mklibname fli %{major}
%define devname %mklibname fli -d

Summary:	Finger Lakes Instrument Library
Name:		libfli
Version:	1.7
Release:	13
License:	GPLv2+
Group:		Development/Other
Url:		http://indi.sourceforge.net/index.php/Main_Page
Source0:	http://downloads.sourceforge.net/indi/libfli1_%{version}.tar.gz
Patch0:		libfli-1.7.190-fix-link.patch
Patch1:		libfli-1.7.190-fix-lib.patch
BuildRequires:	cmake

%description
Finger Lakes Instrument Library

%package -n %{libname}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libname}
%{name} library

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	libfli-devel 1.7-6

%description  -n %{devname}
Files needed to build applications based on %{name}.

%prep
%setup -qn libfli1-%{version}
%apply_patches

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libfli.so.%{major}*

%files -n %{devname}
%{_includedir}/libfli.h
%{_libdir}/libfli.so

