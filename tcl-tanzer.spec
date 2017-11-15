#
# spec file for package tcl-tanzer
#

%define tarname tanzer

Name:           tcl-tanzer
BuildRequires:  tcl
Version:        0.1
Release:        0
Summary:        The Web Framework for Tcl
Url:            http://tanzer.io/
License:        MIT
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       tcl >= 8.6
BuildRoot:      %{_tmppath}/%{tarname}-%{version}-build
Source0:        %{tarname}%{version}.tar.gz

%description
tanzer is a minimalistic web server framework for Tcl which provides a
very straightforward environment for writing HTTP/1.1 web applications.

%prep
%setup -q -n %{tarname}%{version}

%build

%install
dir=%buildroot%tcl_noarchdir/%tarname%version
mkdir -m755 -p $dir
cp -a -R lib/* $dir

%files
%defattr(-,root,root)
%doc examples LICENSE README.md
%tcl_noarchdir/%tarname%version

%changelog

