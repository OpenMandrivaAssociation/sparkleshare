%define oname SparkleShare

Summary:	Easy file sharing based on git repositories
Name:		sparkleshare
Version:	3.28
Release:	1
License:	GPLv3+
Group:		Networking/File transfer
Url:		http://www.sparkleshare.org/
Source0:	https://github.com/hbons/%{oname}/archive/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	nant
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(notify-sharp)
BuildRequires:	pkgconfig(webkit-sharp-1.0)
BuildRequires:  meson
Requires:	git
Requires:	desktop-file-utils
Requires:	yelp

%description
Easy file sharing based on git repositories. A special folder is setup,
and directories/files placed within are placed in a git-based version
control system and synchronized elsewhere.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_iconsdir}/gnome/scalable/apps/%{name}-symbolic.svg
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/status/*
%{_iconsdir}/ubuntu-mono-*/status/24/process-syncing*.png

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

