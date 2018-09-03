%define major 5
%define libname %mklibname KF5JobWidgets %{major}
%define devname %mklibname KF5JobWidgets -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kjobwidgets
Version:	5.50.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Widgets for tracking KJob instances
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WidgetsAddons)
Requires: %{libname} = %{EVRD}

%description
Widgets for tracking KJob instances.

%package -n %{libname}
Summary: Widgets for tracking KJob instances
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Widgets for tracking KJob instances.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_datadir}/dbus-1/interfaces/*
%{_sysconfdir}/xdg/kjobwidgets.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5JobWidgets
%{_libdir}/qt5/mkspecs/modules/*
