%global fontname lohit-telugu
%global fontconf 65-0-%{fontname}.conf
%global metainfo io.pagure.lohit.telugu.font.metainfo

Name:           %{fontname}-fonts
Version:        2.5.5
Release:        3%{?dist}
Summary:        Free Telugu font

Group:          User Interface/X
License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires:  ttfautohint
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}


%description
This package provides a free Telugu truetype/opentype font.

%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-telugu.conf


%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml

%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README
%{_datadir}/metainfo/%{metainfo}.xml


%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.5.5-1
- Upstream new release 2.5.5
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 03 2015 Pravin Satpute <psatpute@redhat.com> - 2.5.4-1
- Upstream release 2.5.4
- Added support for Unicode 8.0 characters U0C00, U0C34 and U0C5A
- Added support for Latin characters
- Using TTFAUTOHINT now while building ttf file.
- Resolves #985343, #1229213 and #1258123.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.3-6
- Added metainfo for gnome-software

* Mon Jul 28 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.3-5
- Resolved #1105878 - Rendering problem of స్త్ర

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Resolved #950525

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Fri Nov 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-2
- Upstream release 2.5.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug 803563

* Wed Mar 28 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Wed Feb 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.0-3
- Resolved bug 640607

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Jul 27 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-14
- fixes bug 714557

* Fri Jul 15 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-13
- fixes bug 714560

* Fri Jul 15 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-12
- fixes bug 714563

* Thu Jun 30 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-11
- fixes bug 714561

* Wed Jun 22 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-10
- fixes bug 714562

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-9
- fixes bug 692368

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-7
- fixes bug 673420

* Tue Aug 10 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-6
- fixes bug 622682

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- fixes bug 578040

* Wed Dec 30 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- fixes bug 551317

* Mon Dec 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- corrected patch 

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- fixed bug 548686, license field

* Wed Nov 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release
- bug fix 531201

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
