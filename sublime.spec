Name: sublimetext
Version: 2.0.1
Release: 1
Group: Applications/Editors
%ifarch x86_64
Source: Sublime Text %{version} x64.tar.bz2
%else
Source: Sublime Text %{version}.tar.bz2
%endif
Summary: Sublime Text 2
URL: http://www.sublimetext.com/2
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Sublime Text Authors
Requires: python >= 2.6
Requires: libgobject-2.0.so.0
Requires: librt.so.1
Requires: libglib-2.0.so.0
Requires: libpthread.so.0
Requires: libdl.so.2
Requires: libutil.so.1
Requires: libX11.so.6
Requires: libstdc++.so.6
Requires: libm.so.6
Requires: libgcc_s.so.1
Requires: libc.so.6
Requires: libgthread-2.0.so.0
Requires: libffi.so.5
Requires: libxcb.so.1
Requires: libXau.so.6

%description
Sublime Text 2 for GNU/Linux

%prep
%setup -q -c -n %{name}

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/opt/%{name}/
wget https://github.com/xvitaly/sublrpm/raw/master/%{name}.desktop -O %{buildroot}/usr/share/applications/%{name}.desktop
mv "%_builddir/%{name}/Sublime Text 2" %_builddir/%{name}/%{name}
cp -fpr %_builddir/%{name}/%{name}/* %{buildroot}/opt/%{name}/
chmod +x %{buildroot}/opt/%{name}/sublime_text

%install
find %{buildroot} -not -type d -printf "\"/%%P\"\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest