#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.12.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		poxml
Summary:	poxml
Name:		ka6-%{kaname}
Version:	24.12.3
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4418bd63344a51090a3171da30e6c450
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	shared-mime-info
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Translates DocBook XML files using gettext po files.

%description -l pl.UTF-8
poxml tłumaczy pliki DocBook XML korzystając z plików .po gettexta.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/xml2pot
%{_mandir}/ca/man1/po2xml.1*
%{_mandir}/ca/man1/split2po.1.*
%{_mandir}/ca/man1/swappo.1.*
%{_mandir}/ca/man1/xml2pot.1.*
%{_mandir}/da/man1/po2xml.1.*
%{_mandir}/da/man1/split2po.1.*
%{_mandir}/da/man1/swappo.1.*
%{_mandir}/da/man1/xml2pot.1.*
%{_mandir}/de/man1/po2xml.1.*
%{_mandir}/de/man1/split2po.1.*
%{_mandir}/de/man1/swappo.1.*
%{_mandir}/de/man1/xml2pot.1.*
%{_mandir}/es/man1/po2xml.1.*
%{_mandir}/es/man1/split2po.1.*
%{_mandir}/es/man1/swappo.1.*
%{_mandir}/es/man1/xml2pot.1.*
%{_mandir}/et/man1/split2po.1.*
%{_mandir}/fr/man1/po2xml.1.*
%{_mandir}/fr/man1/split2po.1.*
%{_mandir}/fr/man1/swappo.1.*
%{_mandir}/fr/man1/xml2pot.1.*
%{_mandir}/gl/man1/po2xml.1.*
%{_mandir}/gl/man1/split2po.1.*
%{_mandir}/gl/man1/swappo.1.*
%{_mandir}/gl/man1/xml2pot.1.*
%{_mandir}/it/man1/po2xml.1.*
%{_mandir}/it/man1/split2po.1.*
%{_mandir}/it/man1/swappo.1.*
%{_mandir}/it/man1/xml2pot.1.*
%{_mandir}/man1/po2xml.1.*
%{_mandir}/man1/split2po.1.*
%{_mandir}/man1/swappo.1.*
%{_mandir}/man1/xml2pot.1.*
%{_mandir}/nl/man1/po2xml.1.*
%{_mandir}/nl/man1/split2po.1.*
%{_mandir}/nl/man1/swappo.1.*
%{_mandir}/nl/man1/xml2pot.1.*
%{_mandir}/pt/man1/po2xml.1.*
%{_mandir}/pt/man1/split2po.1.*
%{_mandir}/pt/man1/swappo.1.*
%{_mandir}/pt/man1/xml2pot.1.*
%{_mandir}/pt_BR/man1/po2xml.1.*
%{_mandir}/pt_BR/man1/split2po.1.*
%{_mandir}/pt_BR/man1/swappo.1.*
%{_mandir}/pt_BR/man1/xml2pot.1.*
%{_mandir}/ru/man1/po2xml.1.*
%{_mandir}/ru/man1/split2po.1.*
%{_mandir}/ru/man1/swappo.1.*
%{_mandir}/ru/man1/xml2pot.1.*
%{_mandir}/sl/man1/po2xml.1*
%{_mandir}/sl/man1/split2po.1*
%{_mandir}/sl/man1/swappo.1*
%{_mandir}/sl/man1/xml2pot.1*
%{_mandir}/sv/man1/po2xml.1.*
%{_mandir}/sv/man1/split2po.1.*
%{_mandir}/sv/man1/swappo.1.*
%{_mandir}/sv/man1/xml2pot.1.*
%{_mandir}/uk/man1/po2xml.1.*
%{_mandir}/uk/man1/split2po.1.*
%{_mandir}/uk/man1/swappo.1.*
%{_mandir}/uk/man1/xml2pot.1.*
