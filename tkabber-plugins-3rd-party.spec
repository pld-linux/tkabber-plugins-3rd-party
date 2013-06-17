%define	snap 20130617
Summary:	Tk Jabber client 3rd party plugins
Summary(pl.UTF-8):	Wtyczki do klienta Jabbera opartego o Tk
Name:		tkabber-plugins-3rd-party
Version:	0.1
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
# svn export http://svn.xmpp.ru/repos/tkabber-3rd-party/trunk tkabber-3rd-party-plugins
Source0:	tkabber-3rd-party-plugins-%{snap}.tar.bz2
# Source0-md5:	1f61e8b13a5294a2fbfc0f6eda22210f
URL:		http://tkabber.jabber.ru/
Requires:	tkabber >= %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tkabber (Tk Jabber client) plugins.

%description -l pl.UTF-8
Wtyczki dla Tkabbera - klienta Jabbera opartego o Tk.

%prep
%setup -q -n tkabber-3rd-party-plugins

# now in tkabber-plugins.spec
rm -rf plugins/unixkeys

sed -i -e 's|#!/usr/bin/tclsh.*|%{_bindir}/tclsh|g' plugins/bldjid2/log2base.tcl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/tkabber/plugins

cd plugins
for d in *; do
	[ -d "$d" ] && cp -a "$d" $RPM_BUILD_ROOT%{_datadir}/tkabber/plugins
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/tkabber/plugins/*
