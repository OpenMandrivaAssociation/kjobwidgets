%define major 5
%define libname %mklibname KF5JobWidgets %{major}
%define devname %mklibname KF5JobWidgets -d
%define debug_package %{nil}

Name: kjobwidgets
Version: 4.98.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Widgets for tracking KJob instances
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
Requires: %{libname} = %{EVRD}

%description
Widgets for tracking KJob instances

%package -n %{libname}
Summary: Widgets for tracking KJob instances
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Widgets for tracking KJob instances

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

%files
%{_datadir}/dbus-1/interfaces/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5JobWidgets
%{_libdir}/qt5/mkspecs/modules/*
