# TODO
# - config to /etc
%define		pkgname	tcpdf
%define		ver	%(echo %{version} | tr . _)
Summary:	TCPDF - PHP class for PDF
Name:		php-%{pkgname}
Version:	6.2.6
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/tcpdf/tcpdf_%{ver}.zip
# Source0-md5:	9185f0ca4ecc65fb8a1dc115ab96b52b
URL:		http://www.tcpdf.org/
BuildRequires:	%{php_name}-cli
BuildRequires:	%{php_name}-pcre
BuildRequires:	%{php_name}-zlib
BuildRequires:	fonts-TTF-DejaVu
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	php(core) >= 5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/%{pkgname}

%description
Generic TCPDF screenshot TCPDF is a PHP class for generating PDF
documents without requiring external extensions. TCPDF Supports UTF-8,
Unicode, RTL languages and HTML.

%package fonts-dejavu
Summary:	DejaVu fonts for TCPDF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description fonts-dejavu
This package allow to use system DejaVu font faces in TCPDF.

%package examples
Summary:	TCPDF example programs
Summary(pl.UTF-8):	TCPDF programy przykładowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
TCPDF example programs.

%description examples -l pl.UTF-8
TCPDF - przykładowe programy.

%prep
%setup -qc
mv tcpdf/* .
%undos *.TXT

# remove bundled fonts
rm -r fonts/dejavu-fonts-ttf-* fonts/freefont-* fonts/ae_fonts_*

%build
for a in %{_fontsdir}/TTF/DejaVuS*; do
	%{__php} tools/tcpdf_addfont.php -t TrueTypeUnicode -i $a
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir},%{_examplesdir}/%{name}-%{version}}

cp -a *.php config fonts include $RPM_BUILD_ROOT%{_appdir}
install -p tools/tcpdf_addfont.php $RPM_BUILD_ROOT%{_bindir}/tcpdf_addfont
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT README.TXT
%attr(755,root,root) %{_bindir}/tcpdf_addfont
%dir %{_appdir}
%{_appdir}/config
%{_appdir}/include
%{_appdir}/tcpdf*.php

%dir %{_appdir}/fonts
%{_appdir}/fonts/aealarabiya*
%{_appdir}/fonts/aefurat*
%{_appdir}/fonts/cid0*
%{_appdir}/fonts/courier*
%{_appdir}/fonts/freemono*
%{_appdir}/fonts/freesans*
%{_appdir}/fonts/freeserif*
%{_appdir}/fonts/helvetica*
%{_appdir}/fonts/hysmyeongjostdmedium*
%{_appdir}/fonts/kozgopromedium*
%{_appdir}/fonts/kozminproregular*
%{_appdir}/fonts/msungstdlight*
%{_appdir}/fonts/pdfacourier*
%{_appdir}/fonts/pdfahelvetica*
%{_appdir}/fonts/pdfasymbol*
%{_appdir}/fonts/pdfatimes*
%{_appdir}/fonts/pdfazapfdingbats*
%{_appdir}/fonts/stsongstdlight*
%{_appdir}/fonts/symbol*
%{_appdir}/fonts/times*
%{_appdir}/fonts/uni2cid_*
%{_appdir}/fonts/zapfdingbats*

%files fonts-dejavu
%defattr(644,root,root,755)
%{_appdir}/fonts/dejavusans*
%{_appdir}/fonts/dejavuserif*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
