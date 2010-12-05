%define module testpack

Name: haskell-%{module}
Version: 1.0.2
Release: %mkrel 2
Summary: Test Utililty Pack for HUnit and QuickCheck
Group: Development/Other
License: LGPL
Url: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{module}
Source: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{module}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: haskell-macros
BuildRequires: ghc

%description
Haskell Test Utility Pack for HUnit and QuickCheck testpack provides
utilities for both HUnit and QuickCheck. These include tools for running
QuickCheck properties as HUnit test cases, allowing you to combine both
approaches in a single program. It also includes tools for more helpful
displays of running progress in both HUnit and QuickCheck, additional
generators for other types for QuickCheck, and shortcuts for quickly
defining new test cases.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%{_docdir}/%{module}-%{version}/*
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot
