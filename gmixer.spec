%{!?python_sitelib:  %global python_sitelib  %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           gmixer
Version:        1.3
Release:        7%{?dist}
Summary:        Just a simple audio mixer

Group:          Applications/Multimedia
License:        GPLv3+
URL:            https://launchpad.net/gmixer
Source0:        http://launchpad.net/gmixer/1.x/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        gmixer.desktop
Patch0:         version_fix.patch
Patch1:         gmixer-1.3-setup-py.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	pkgconfig
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


%build
python setup.py build



%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
  --prefix=%{_prefix} \
  --root=$RPM_BUILD_ROOT \
  --skip-build

# icon
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 644 data/mixer.png \
	$RPM_BUILD_ROOT%{_datadir}/pixmaps/gmixer.png

# menu-entry
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %SOURCE1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc gpl.txt 
%{_bindir}/gmixer
%{python_sitelib}/gtktrayicon.py*
%{python_sitelib}/volkeys.so
%{python_sitelib}/gmixer-1.0-py?.?.egg-info
%{_datadir}/gmixer/
%{_datadir}/applications/gmixer.desktop
%{_datadir}/pixmaps/gmixer.png



%changelog
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
