#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Generation of bin_prot readers and writers from types
Summary(pl.UTF-8):	Generowanie funkcji odczytujących i zapisujących bin_prot z typów
Name:		ocaml-ppx_bin_prot
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_bin_prot/tags
Source0:	https://github.com/janestreet/ppx_bin_prot/archive/v%{version}/ppx_bin_prot-%{version}.tar.gz
# Source0-md5:	de707369a339cd359897a161b70485b5
URL:		https://github.com/janestreet/ppx_bin_prot
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-bin_prot-devel >= 0.14
BuildRequires:	ocaml-bin_prot-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_here-devel >= 0.14
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Generation of binary serialization and deserialization functions from
type definitions.

This package contains files needed to run bytecode executables using
ppx_bin_prot library.

%description -l pl.UTF-8
Generowanie funkcji binarnej serializacji i deserializacji z definicji
typów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_bin_prot.

%package devel
Summary:	Generation of bin_prot readers and writers from types - development part
Summary(pl.UTF-8):	Generowanie funkcji odczytujących i zapisujących bin_prot z typów - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-bin_prot-devel >= 0.14
Requires:	ocaml-ppx_here-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_bin_prot library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_bin_prot.

%prep
%setup -q -n ppx_bin_prot-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_bin_prot/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_bin_prot/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_bin_prot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_bin_prot
%{_libdir}/ocaml/ppx_bin_prot/META
%{_libdir}/ocaml/ppx_bin_prot/*.cma
%dir %{_libdir}/ocaml/ppx_bin_prot/shape-expander
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_bin_prot/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_bin_prot/*.cmi
%{_libdir}/ocaml/ppx_bin_prot/*.cmt
%{_libdir}/ocaml/ppx_bin_prot/*.cmti
%{_libdir}/ocaml/ppx_bin_prot/*.mli
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.cmi
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.cmt
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.cmti
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_bin_prot/ppx_bin_prot.a
%{_libdir}/ocaml/ppx_bin_prot/*.cmx
%{_libdir}/ocaml/ppx_bin_prot/*.cmxa
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/bin_shape_expand.a
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.cmx
%{_libdir}/ocaml/ppx_bin_prot/shape-expander/*.cmxa
%endif
%{_libdir}/ocaml/ppx_bin_prot/dune-package
%{_libdir}/ocaml/ppx_bin_prot/opam
