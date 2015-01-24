# Let's disable compilation of Python scripts and modules and debug packages.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%define debug_package %{nil}

%define archive_name sublime_text_3_build_3065

Name: sublimetext
Version: 3.0.3065
Release: 1
Group: Applications/Editors
%ifarch x86_64
Source: %{archive_name}_x64.tar.bz2
%else
Source: %{archive_name}_x32.tar.bz2
%endif
Summary: Sublime Text 3
URL: http://www.sublimetext.com/3
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

# Installing to working directory from official package...
mv "%_builddir/%{name}/sublime_text_3" %_builddir/%{name}/%{name}
cp -fpr %_builddir/%{name}/%{name}/* %{buildroot}/opt/%{name}/
rm -f %{buildroot}/opt/%{name}/sublime_text.desktop
chmod +x %{buildroot}/opt/%{name}/sublime_text

# Creating desktop icon...
echo "[Desktop Entry]" > %{buildroot}/usr/share/applications/%{name}.desktop
echo "GenericName=Text Editor" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "GenericName[ru]=Текстовый редактор" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Name=Sublime Text 2" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Name[ru]=Sublime Text 2" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Comment=Edit text files" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Exec=/opt/sublimetext/sublime_text" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Icon=/opt/sublimetext/Icon/128x128/sublime_text.png" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Terminal=false" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Type=Application" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Encoding=UTF-8" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Categories=Utility;TextEditor;" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "MimeType=text/plain;text/x-c++src;text/x-c++hdr;text/x-xsrc;text/html;text/javascript;text/php;text/xml;" >> %{buildroot}/usr/share/applications/%{name}.desktop

# Generating list of files...
find %{buildroot} -not -type d -printf "\"/%%P\"\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest

%changelog
* Sat Jan 24 2015 V1TSK <vitaly@easycoding.org>
- Updated SPEC for Sublime Text 3 support.

* Sun Dec 21 2014 V1TSK <vitaly@easycoding.org>
- Updated SPEC and desktop files for openSUSE 13.2 and Fedora 21+ support.