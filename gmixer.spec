%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           gmixer
Version:        1.3
Release:        17%{?dist}.1
Summary:        Just a simple audio mixer

Group:          Applications/Multimedia
License:        GPLv3+
URL:            https://launchpad.net/gmixer
Source0:        http://launchpad.net/gmixer/1.x/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        gmixer.desktop
Source2:        gmixer-trayicon.desktop
Patch0:         version_fix.patch
Patch1:         gmixer-1.3-setup-py.patch
Patch2:         icons.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=537803
Patch3:         gmixer-1.3-local-variable-not-assigned.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=638277
Patch4:         gmixer-1.3-no-title.patch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  pkgconfig
BuildRequires:  python-devel, pygtk2-codegen, pygtk2-devel, gtk2-devel
BuildRequires:  desktop-file-utils
Requires:       python-xlib, pygtk2, gstreamer-python
       

%description
A simple gtk/gstreamer audio mixer, aimed to work with light desktop managers.

Features:
 - support all mixer plugins of gstreamer (alsa/oss/pulseaudio/...)
 - tray icon support
 - support special keys of multimedia keyboard. 


%prep
%setup -q
%patch0 -p1 -b .version_fix
%patch1 -p1 -b .gmixer-1.3-setup-py
%patch2 -p1 -b .icons
%patch3 -p0 -b .local-variable-assignment
%patch4 -p0 -b .no-title


%build
python setup.py build



%install
rm -rf $RPM_BUILD_ROOT
# fix permissions
python setup.py install \
  --prefix=%{_prefix} \
  --root=$RPM_BUILD_ROOT \
  --skip-build

# fix permissions
chmod 755 $RPM_BUILD_ROOT%{python_sitearch}/volkeys.so

# icon
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 644 data/mixer.png \
        $RPM_BUILD_ROOT%{_datadir}/pixmaps/gmixer.png

# menu-entry
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %SOURCE1

# autostart launcher
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart \
  %SOURCE2



%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc gpl.txt 
%{_bindir}/gmixer
%{_sysconfdir}/xdg/autostart/gmixer-trayicon.desktop
%{python_sitearch}/gtktrayicon.py*
%{python_sitearch}/volkeys.so
%{python_sitearch}/gmixer-1.0-py?.?.egg-info
%{_datadir}/gmixer/
%{_datadir}/applications/gmixer.desktop
%{_datadir}/pixmaps/gmixer.png



%changelog
* Sat Oct  9 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.3-17.1
- apply patches from upstream

* Thu Oct  6 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.3-15.4
- rebuilt against gcc bug

* Wed Sep 29 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.3-15.3
- also not show in XFCE too

* Fri Sep 24 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.3-15.2
- autostart again but not in GNOME and KDE

* Mon Aug 30 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.3-15.1
- do not start gmixer at startup

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Mar 16 2010 leigh scott <leigh123linux@googlemail.com> - 1.3-14
- complete the icon patch so it works

* Tue Mar 16 2010 leigh scott <leigh123linux@googlemail.com> - 1.3-13
- Fix icon naming

* Wed Jan 13 2010 leigh scott <leigh123linux@googlemail.com> - 1.3-12
- fix python macros
- fix permissions on volkeys.so
- update spec to new packaging guidelines

* Mon Sep 21 2009 leigh scott <leigh123linux@googlemail.com> - 1.3-11
- remove X-Fedora from desktop file

* Mon Sep 21 2009 leigh scott <leigh123linux@googlemail.com> - 1.3-10
- remove

* Mon Sep 21 2009 leigh scott <leigh123linux@googlemail.com> - 1.3-9
- added German translations for desktop files
- revert last desktop file edit and add a autostart launcher

* Fri Sep 18 2009 leigh scott <leigh123linux@googlemail.com> - 1.3-8
- edit desktop file so gmixer launches with trayicon

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 7 2009  Leigh Scott   <leigh123linux@googlemail.com> - 1.3-6
- bump version as I couldn't remove CVS tag

* Sun Jun 7 2009  Leigh Scott   <leigh123linux@googlemail.com> - 1.3-5
- re-add doc 
- add icon
- add setup-py.patch to remove cleanup
- add Br pkgconfig
- use find_lang to install language files 
 
* Thu May 21 2009  Leigh Scott   <leigh123linux@googlemail.com> - 1.3-4
- change egg-info so it builds with any python version
- remove doc

* Thu May 21 2009  Leigh Scott   <leigh123linux@googlemail.com> - 1.3-3
- remove --vendor from desktop file validate
- change {python_sitearch} tag to {python_sitelib}

* Thu May 21 2009  Leigh Scott   <leigh123linux@googlemail.com> - 1.3-2
- change licence tag to GPLv3+
- fix version in about
- add gstreamer-python to requires

* Thu May 21 2009  Leigh Scott   <leigh123linux@googlemail.com> - 1.3-1
- Update to 1.3 

* Sat Apr 25 2009  Leigh Scott   <leigh123linux@googlemail.com> - 0.3.5-1
- First build
