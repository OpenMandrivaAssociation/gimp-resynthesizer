%define git e637010

Summary: Gimp plug-in for texture synthesis
Name: gimp-resynthesizer
Version: 2.0
Release: %mkrel 0.1
Group: Graphics
License: GPLv2+
Requires: gimp
Obsoletes: gimp2-resynthesizer
Provides: gimp2-resynthesizer
BuildRequires: gimp, gimp-devel
BuildRequires: intltool
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
URL: http://logarithmic.net/pfh/resynthesizer
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
%apply_patches
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

