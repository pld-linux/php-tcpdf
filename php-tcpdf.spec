# TODO
# - config to /etc
%define		ver	%(echo %{version} | tr . _)
Summary:	TCPDF - PHP class for PDF
Name:		php-tcpdf
Version:	4.8.013
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/tcpdf/tcpdf_%{ver}.zip
# Source0-md5:	4a8b478f9d078e176824ef6a1b220be8
URL:		http://www.tecnick.com/public/code/cp_dpage.php?aiocp_dp=tcpdf
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(triggerpostun):	sed >= 4.0
Requires:	php-common >= 4:5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/tcpdf
%define		_phpdocdir		%{_docdir}/phpdoc

%description
Generic TCPDF screenshot TCPDF is a PHP class for generating PDF
documents without requiring external extensions. TCPDF Supports UTF-8,
Unicode, RTL languages and HTML.

%package phpdoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for %{name}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q -n tcpdf

%{__sed} -i -e 's,\r$,,' *.TXT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -a *.php config fonts images $RPM_BUILD_ROOT%{_appdir}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{name}
cp -a doc/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}

rm -rf $RPM_BUILD_ROOT%{_appdir}/fonts/*-*
rm -rf $RPM_BUILD_ROOT%{_appdir}/fonts/utils

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT README.TXT
%{_appdir}

%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}
