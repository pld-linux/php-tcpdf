# NOTE:
# - *.z are just gzcompress-ed .ttf files
%define		pkgname	tcpdf
%define		php_min_version 5.2.7
Summary:	TCPDF - PHP class for PDF
Name:		php-%{pkgname}
Version:	6.6.5
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	https://github.com/tecnickcom/TCPDF/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	6dba74875045bf54f0099515c8d7213e
Patch0:		shebang.patch
URL:		http://www.tcpdf.org/
BuildRequires:	%{php_name}-cli
BuildRequires:	%{php_name}-devel
BuildRequires:	%{php_name}-pcre
BuildRequires:	%{php_name}-zlib
BuildRequires:	fonts-TTF-DejaVu
BuildRequires:	fonts-TTF-freefont
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	php(bcmath)
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(gd)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(openssl)
Requires:	php(pcre)
Requires:	php(xml)
Suggests:	php-tcpdf-fonts-dejavu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/%{pkgname}
%define		_sysconfdir	/etc/%{pkgname}

%description
Generic TCPDF screenshot TCPDF is a PHP class for generating PDF
documents without requiring external extensions. TCPDF Supports UTF-8,
Unicode, RTL languages and HTML.

%package fonts-dejavu
Summary:	DejaVu fonts for TCPDF
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description fonts-dejavu
This package allow to use system DejaVu font faces in TCPDF.

%package fonts-freefont
Summary:	GNU FreeFonts for TCPDF
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description fonts-freefont
This package allow to use system GNU FreeFont font faces in TCPDF.

%package examples
Summary:	TCPDF example programs
Summary(pl.UTF-8):	TCPDF programy przykładowe
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description examples
TCPDF example programs.

%description examples -l pl.UTF-8
TCPDF - przykładowe programy.

%prep
%setup -q -n TCPDF-%{version}
%undos *.TXT
%patch -P0 -p1

# remove bundled fonts
rm -r fonts/dejavu-fonts-ttf-* fonts/freefont-* fonts/ae_fonts_*

%build
pkgs="fonts-TTF-DejaVu fonts-TTF-freefont"
install -d build/fonts
for pkg in $pkgs; do
	fonts=$(rpm -ql $pkg | grep %{_fontsdir}/TTF | xargs | tr ' ' ',')
	%{__php} tools/tcpdf_addfont.php -t TrueTypeUnicode -i $fonts -o build/fonts
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir},%{_bindir},%{_examplesdir}/%{name}-%{version}}
cp -a *.php fonts include $RPM_BUILD_ROOT%{_appdir}
cp -p config/*.php $RPM_BUILD_ROOT%{_sysconfdir}
cp -a build/fonts/* $RPM_BUILD_ROOT%{_appdir}/fonts
install -p tools/tcpdf_addfont.php $RPM_BUILD_ROOT%{_bindir}/tcpdf_addfont
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT README.md
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tcpdf_config.php
%attr(755,root,root) %{_bindir}/tcpdf_addfont
%dir %{_appdir}
%{_appdir}/include
%{_appdir}/tcpdf*.php

%dir %{_appdir}/fonts
%{_appdir}/fonts/aealarabiya*
%{_appdir}/fonts/aefurat*
%{_appdir}/fonts/cid0*
%{_appdir}/fonts/courier*
%{_appdir}/fonts/dejavumathtexgyre*
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

%files fonts-freefont
%defattr(644,root,root,755)
%{_appdir}/fonts/freemono*
%{_appdir}/fonts/freesans*
%{_appdir}/fonts/freeserif*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
