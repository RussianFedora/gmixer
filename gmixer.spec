%{!?python_sitelib:  %global python_sitelib  %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           gmixer
Version:        1.3
Release:        4%{?dist}
Summary:        Just a simple audio mixer

Group:          Applications/Multimedia
License:        GPLv3+
URL:            https://launchpad.net/gmixer
Source0:        http://launchpad.net/gmixer/1.x/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        gmixer.desktop
Patch0:         version_fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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


%build



%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %SOURCE1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-) 
%{_bindir}/gmixer
%{python_sitelib}/gtktrayicon.py*
%{python_sitelib}/volkeys.so
%{python_sitelib}/gmixer-1.0-py?.?.egg-info
%{_datadir}/gmixer/
%{_datadir}/applications/gmixer.desktop
%lang(fr) %doc %{_datadir}/locale/fr/LC_MESSAGES/gmixer.mo



%changelog
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
