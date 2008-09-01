%define gimpplugindir %(gimptool-2.0 --gimpplugindir)/plug-ins
%define gimpscriptdir %(gimptool-2.0 --gimpdatadir)/scripts

Summary: Gimp plug-in for texture synthesis
Name: gimp-resynthesizer
Version: 0.15
Release: %mkrel 1
Group: Graphics
License: GPLv2+
Requires: gimp
BuildRequires: gimp, gimp-devel
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
URL: http://logarithmic.net/pfh/resynthesizer
Source: http://logarithmic.net/pfh-files/resynthesizer/resynthesizer-%{version}.tar.gz

%description
Resynthesizer is a Gimp plug-in for texture synthesis. Given a sample of a 
texture, it can create more of that texture. This has uses including: 
- Creating more of a texture (including creation of tileable textures)
- Removing objects from images (great for touching up photos)
- Creating themed images (by transfering a texture from one image to another)

%prep
%setup -q -n resynthesizer-%{version}

%build
%make CFLAGS="%{optflags}" GIMPTOOL=gimptool-2.0

%install
%__rm -rf %{buildroot}
%__install -p -d %{buildroot}/%{gimpplugindir}
%__install -p -d %{buildroot}/%{gimpscriptdir}
%__install -p resynth %{buildroot}/%{gimpplugindir}/
%__install -p -m 644 smart-remove.scm %{buildroot}/%{gimpscriptdir}
%__install -p -m 644 smart-enlarge.scm %{buildroot}/%{gimpscriptdir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING
%{gimpplugindir}/resynth
%{gimpscriptdir}/smart-remove.scm
%{gimpscriptdir}/smart-enlarge.scm
