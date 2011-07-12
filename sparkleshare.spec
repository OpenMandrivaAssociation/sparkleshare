Name:           sparkleshare
Version:        0.2.4
Release:        %mkrel 1
Summary:        Easy file sharing based on git repositories
Group:          Networking/File transfer 
License:        GPLv3
URL:            http://www.sparkleshare.org/
Source0:        https://github.com/downloads/hbons/SparkleShare/sparkleshare-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  mono-devel ndesk-dbus-devel ndesk-dbus-glib-devel notify-sharp-devel
BuildRequires:  desktop-file-utils intltool 
BuildRequires:  gnome-doc-utils nant
BuildRequires:  webkit-sharp-devel
# BuildRequires:  smartirc4net-devel
Requires:       git desktop-file-utils yelp

%description
Easy file sharing based on git repositories. A special folder is setup,
and directories/files placed within are placed in a git-based version
control system and synchronized elsewhere.


%prep
%setup -q

%build
%configure
# no parallel make on SMP because it's racy for this build :(
GMCS_FLAGS=-codepage:utf8 make

%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_libdir}/mono/gac/
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/sparkleshare.desktop

# find translations
%find_lang %{name}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
/usr/bin/sparkleshare
%{_libdir}/sparkleshare/
/usr/share/sparkleshare/
/usr/share/applications/sparkleshare.desktop
# /usr/share/gnome/help/sparkleshare/
/usr/share/icons/hicolor/16x16/apps/folder-sparkleshare.png
/usr/share/icons/hicolor/22x22/apps/folder-sparkleshare.png
/usr/share/icons/hicolor/24x24/apps/folder-sparkleshare.png
/usr/share/icons/hicolor/256x256/apps/folder-sparkleshare.png
/usr/share/icons/hicolor/32x32/apps/folder-sparkleshare.png
/usr/share/icons/hicolor/48x48/apps/folder-sparkleshare.png
/usr/share/icons/hicolor/24x24/status/process-syncing-sparkleshare-i*.png

%doc README
%doc %{_mandir}/man1/sparkleshare.1.*
