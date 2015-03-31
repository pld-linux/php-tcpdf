# TODO
# - config to /etc
%define		ver	%(echo %{version} | tr . _)
Summary:	TCPDF - PHP class for PDF
Name:		php-tcpdf
Version:	6.2.6
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/tcpdf/tcpdf_%{ver}.zip
# Source0-md5:	9185f0ca4ecc65fb8a1dc115ab96b52b
URL:		http://www.tcpdf.org/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	php(core) >= 5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/tcpdf

%description
Generic TCPDF screenshot TCPDF is a PHP class for generating PDF
documents without requiring external extensions. TCPDF Supports UTF-8,
Unicode, RTL languages and HTML.

%prep
%setup -q -n tcpdf
%undos *.TXT

%build
for a in %{_datadir}/fonts/TTF/DejaVuS*; do
	php tools/tcpdf_addfont.php -t TrueTypeUnicode -i $a
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -a *.php config fonts include $RPM_BUILD_ROOT%{_appdir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -r $RPM_BUILD_ROOT%{_appdir}/fonts/*-*
rm -rf $RPM_BUILD_ROOT%{_appdir}/fonts/utils

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT README.TXT
%{_appdir}
%{_examplesdir}/%{name}-%{version}
