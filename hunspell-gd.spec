Name: hunspell-gd
Summary: Scots Gaelic hunspell dictionaries
Version: 2.6
Release: 2%{?dist}
Source: http://downloads.sourceforge.net/project/aoo-extensions/4587/8/hunspell-gd-2.6.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/en/project/faclair-afb
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ and GPLv3+
BuildArch: noarch

Requires: hunspell

%description
Scots Gaelic hunspell dictionaries.

%prep
%setup -q -c hunspell-gd-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/gd_GB.dic dictionaries/gd_GB.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc dictionaries/README_gd_GB.txt LICENSES-en.txt
%{_datadir}/myspell/*

%changelog
* Tue Jun 04 2013 Caolán McNamara <caolanm@redhat.com> - 2.6-2
- clarify license. The .aff still says GPLv2+ while the LICENSES-en.txt etc say
  GPLv3+

* Mon May 20 2013 Caolán McNamara <caolanm@redhat.com> - 2.6-1
- latest version

* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 2.5-1
- latest version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 2.3-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Caolán McNamara <caolanm@redhat.com> - 2.1-1
- latest version

* Wed Nov 16 2011 Caolán McNamara <caolanm@redhat.com> - 2.0-1
- latest version

* Wed Jun 29 2011 Caolán McNamara <caolanm@redhat.com> - 1.3-1
- latest version

* Sat Apr 02 2011 Caolán McNamara <caolanm@redhat.com> - 1.2-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.rc.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.rc.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 1.0.0-0.2.rc.1
- tidy spec

* Mon Jun 15 2009 Caolán McNamara <caolanm@redhat.com> - 1.0.0-0.1.rc.1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 27 2008 Caolán McNamara <caolanm@redhat.com> - 0.1.1-1
- initial version
