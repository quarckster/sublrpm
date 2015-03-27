%define build_number 3083

Name: sublime_text
Version: 3
Release: 0
Group: Applications/Editors
%ifarch x86_64
Source: %{name}_%{version}_build_%{build_number}_x64.tar.bz2
%else
Source: %{name}_%{version}_build_%{build_number}_x32.tar.bz2
%endif
Summary: Sublime Text %{version}
URL: http://www.sublimetext.com/%{version}
License: SUSE-NonFree
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Sublime Text Authors
Requires: libgobject-2.0.so.0
Requires: librt.so.1
Requires: libglib-2.0.so.0
Requires: libpthread.so.0
Requires: libdl.so.2
Requires: libX11.so.6
Requires: libm.so.6
Requires: libc.so.6
Requires: libxcb.so.1
Requires: libXau.so.6

%description
Sublime Text 3 for GNU/Linux is a sophisticated text editor for code, markup and prose.

%prep
%setup -q -c -n %{name}

%build
# Do nothing...

%install
# Unpacking...
rm -rf %{buildroot}

# Creating general directories...
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/opt/%{name}/
mkdir -p %{buildroot}/usr/bin/

# Installing to working directory from official package...
mv "%_builddir/%{name}/%{name}_%{version}" %_builddir/%{name}/%{name}
cp -fpr %_builddir/%{name}/%{name}/* %{buildroot}/opt/%{name}/
rm -f %{buildroot}/opt/%{name}/%{name}.desktop
chmod +x %{buildroot}/opt/%{name}/%{name}
ln -sf /opt/%{name}/%{name} %{buildroot}/usr/bin/sublime%{version}

# Creating desktop icon...
echo "[Desktop Entry]" > %{buildroot}/usr/share/applications/%{name}.desktop
echo "GenericName=Text Editor" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "GenericName[ru]=Текстовый редактор" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Name=Sublime Text %{version}" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Name[ru]=Sublime Text %{version}" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Comment=Edit text files" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Exec=/opt/%{name}/sublime_text" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Icon=/opt/%{name}/Icon/256x256/sublime-text.png" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Terminal=false" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Type=Application" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Encoding=UTF-8" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Categories=Utility;TextEditor;" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "MimeType=text/plain;text/x-c++src;text/x-c++hdr;text/x-xsrc;text/html;text/javascript;text/php;text/xml;" >> %{buildroot}/usr/share/applications/%{name}.desktop

# Generating list of files...
find %{buildroot} -not -type d -printf "\"/%%P\"\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest
%defattr(-,root,root)
%dir /opt/%{name}
%dir /opt/%{name}/Icon/
%dir /opt/%{name}/Icon/*
%dir /opt/%{name}/Packages

%changelog