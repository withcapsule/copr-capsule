Name:           capsule
Version:        0.1.11
Release:        1%{?dist}
Summary:        CLI for the Capsule server
License:        MIT
URL:            https://github.com/withcapsule/CLI

BuildRequires:  curl

%description
A simple CLI file transfer tool.

%prep
%ifarch x86_64
curl -fsSL "https://github.com/withcapsule/CLI/releases/download/v%{version}/capsule-x86_64-linux.tar.gz" | tar -xz -C %{_builddir}
%endif
%ifarch aarch64
curl -fsSL "https://github.com/withcapsule/CLI/releases/download/v%{version}/capsule-aarch64-linux.tar.gz" | tar -xz -C %{_builddir}
%endif

%build

%install
install -Dm755 %{_builddir}/capsule %{buildroot}%{_bindir}/capsule

%files
%{_bindir}/capsule

%changelog
* Sun Jun 22 2026 Sean Singh <sean.9s9s0@gmail.com> - 0.1.11-1
- Initial package
