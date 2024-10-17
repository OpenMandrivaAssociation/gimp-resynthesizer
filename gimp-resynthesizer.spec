%define git e637010

Summary: Gimp plug-in for texture synthesis
Name: gimp-resynthesizer
Version: 2.0
Release: 0.2
Group: Graphics
License: GPLv2+
Requires: gimp
Obsoletes: gimp2-resynthesizer
Provides: gimp2-resynthesizer
BuildRequires: gimp, gimp-devel
BuildRequires: intltool
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
URL: https://logarithmic.net/pfh/resynthesizer
Source: bootchk-resynthesizer-v%{version}-1-g%git.zip
Patch0: resynthesizer-2.0-fix-linking.patch

%description
Resynthesizer is a Gimp plug-in for texture synthesis. Given a sample of a 
texture, it can create more of that texture. This has uses including: 
- Creating more of a texture (including creation of tileable textures)
- Removing objects from images (great for touching up photos)
- Creating themed images (by transfering a texture from one image to another)

%prep
%setup -q -n bootchk-resynthesizer-%git/
%autopatch -p1
./autogen.sh

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%find_lang resynthesizer

%clean
%__rm -rf %{buildroot}

%files -f resynthesizer.lang
%defattr(-,root,root,-)
%doc README COPYING
%_libdir/gimp/*/plug-ins/*
%_datadir/resynthesizer



%changelog
* Fri Mar 30 2012 Götz Waschk <waschk@mandriva.org> 2.0-0.1mdv2012.0
+ Revision: 788329
- fix linking
- new version
- fix build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.16-3
+ Revision: 610855
- rebuild

* Sun Mar 28 2010 Götz Waschk <waschk@mandriva.org> 0.16-2mdv2010.1
+ Revision: 528585
- obsolete old gimp2-resynthesizer package (Anssi)

* Tue Sep 02 2008 Götz Waschk <waschk@mandriva.org> 0.16-1mdv2009.0
+ Revision: 278860
- new version
- fix build

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 0.15-1mdv2009.0
+ Revision: 278112
- import gimp-resynthesizer


* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.15-3
- Autorebuild for GCC 4.3

*Sun Aug 19 2007 Ewan Mac Mahon <ewan@macmahon.me.uk> - 0.15-2
Fixed review problems: Spurious comment, License tag, variable style 
build root, ignoring opt flags.
* Mon Jul 30 2007 Ewan Mac Mahon <ewan@macmahon.me.uk> - 0.15-1
Initial Fedora package
