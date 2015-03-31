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
%setup -q -n tcpdf
%undos *.TXT

# remove bundled fonts
rm -r fonts/dejavu-fonts-ttf-* fonts/freefont-*

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
%{_appdir}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
