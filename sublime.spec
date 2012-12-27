Name: sublimetext
Version: 2.0.1
Release: 1
Group: Applications/Develop
Source: Sublime Text %{version} x64.tar.bz2
Summary: Sublime Text 2
URL: http://www.sublimetext.com/2
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Sublime Text Authors
Requires: python >= 2.6

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