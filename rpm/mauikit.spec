%global qt5_min_version 5.15.8
%global kf5_min_version 5.90.0

Name:       opt-maui-mauikit
Version:    2.2.1
Release:    1
Summary:    Kit for developing MAUI Apps
License:    LGPL-3.0
URL:        https://mauikit.org/
Source:     mauikit-%{version}.tar.xz
Patch0:     0001-Remove-uses-of-X11-libraries.patch
Requires:   opt-kf5-kconfig >= %{kf5_min_version}
Requires:   opt-kf5-kcoreaddons >= %{kf5_min_version}
Requires:   opt-kf5-ki18n >= %{kf5_min_version}
Requires:   opt-kf5-knotifications >= %{kf5_min_version}
Requires:   opt-kf5-kwindowsystem >= %{kf5_min_version}
Requires:   opt-maui-mauiman
Requires:   opt-qt5-qtbase >= %{qt5_min_version}
Requires:   opt-qt5-qtbase-gui >= %{qt5_min_version}
Requires:   opt-qt5-qtdeclarative >= %{qt5_min_version}
Requires:   opt-qt5-qtgraphicaleffects >= %{qt5_min_version}
Requires:   opt-qt5-qtquickcontrols2 >= %{qt5_min_version}
Requires:   opt-qt5-qtsvg >= %{qt5_min_version}
BuildRequires:  cmake >= 3.16
BuildRequires:  opt-extra-cmake-modules >= %{kf5_min_version}
BuildRequires:  opt-kf5-kconfig-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-kcoreaddons-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-ki18n-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-knotifications-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-kwindowsystem-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-maui-mauiman-devel
BuildRequires:  opt-qt5-qtbase-devel >= %{qt5_min_version}
BuildRequires:  opt-qt5-qtdeclarative-devel >= %{qt5_min_version}
BuildRequires:  opt-qt5-qtquickcontrols2-devel >= %{qt5_min_version}
BuildRequires:  opt-qt5-qtsvg-devel >= %{qt5_min_version}
%{?opt_kf5_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^libMauiMan.*$

%description
MauiKit is a set of utilities and "templated" controls based on
Kirigami and QCC2 that follow the ongoing work on the Maui HIG.
It let you quickly create a Maui application and access utilities
and widgets shared among the other Maui apps.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}

mkdir -p build
pushd build

%_opt_cmake_kf5 .. \
    -DKDE_INSTALL_BINDIR:PATH=/usr/bin \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DQUICK_COMPILER=OFF
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%files
%license LICENSES/*.txt
%{_opt_kf5_libdir}/libMauiKit.so
%{_opt_kf5_qmldir}/QtQuick/Controls.2/maui-style
%{_opt_kf5_qmldir}/org/mauikit/controls
%{_datadir}/org.mauikit.controls
%{_datadir}/locale/*/*/mauikit.mo

%files devel
%{_opt_kf5_includedir}/MauiKit
%{_opt_kf5_libdir}/cmake/MauiKit
