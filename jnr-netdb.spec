%{?scl:%scl_package jnr-netdb}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

Name:    %{?scl_prefix}jnr-netdb
Version: 1.1.5
Release: 1.%{baserelease}%{?dist}
Summary: Network services database access for java

Group:   System Environment/Libraries
License: ASL 2.0
URL:     http://github.com/jnr/%{pkg_name}/
Source0: https://github.com/jnr/%{pkg_name}/archive/%{version}.tar.gz
BuildArch: noarch


BuildRequires: %{?scl_prefix_java_common}jpackage-utils
BuildRequires: %{?scl_prefix}jnr-ffi
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix}jffi

BuildRequires:  %{?scl_prefix_maven}maven-local

Requires: %{?scl_prefix_java_common}jpackage-utils
Requires: %{?scl_prefix}jnr-ffi

%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3)

%package        javadoc
Summary:        Javadoc for %{pkg_name}
Group:          Documentation

%description    javadoc
Javadoc for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -n %{pkg_name}-%{version} -q

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files  -f .mfiles
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jul 22 2016 Mat Booth <mat.booth@redhat.com> - 1.1.5-1.1
- Auto SCL-ise package for rh-eclipse46 collection

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 1.1.5-1
- Update to upstream 1.1.5 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 1.1.4-1
- Update to upstream 1.1.4 release.

* Sat Aug 02 2014 Mo Morsi <mmorsi@redhat.com> - 1.1.1-5
- Fix rawhide build
- Update to latest java packaging guidelines

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.1.1-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.1-1
- Updated to version 1.1.1.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-5
- Fix FTBFS.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010  <mmorsi@redhat.com> - 1.0.1-3
- updates to conform to pkging guidelines

* Mon Oct 25 2010  <mmorsi@redhat.com> - 1.0.1-2
- include javadocs

* Mon Oct 25 2010  <mmorsi@redhat.com> - 1.0.1-1
- initial package