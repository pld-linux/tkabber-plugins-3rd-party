%define	snap 20080212
Summary:	Tk Jabber client 3rd party plugins
Summary(pl.UTF-8):	Wtyczki do klienta Jabbera opartego o Tk
Name:		tkabber-plugins-3rd-party
Version:	0.1
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
# svn export http://svn.xmpp.ru/repos/tkabber-3rd-party/trunk tkabber-3rd-party-plugins
Source0:	tkabber-3rd-party-plugins-%{snap}.tar.bz2
# Source0-md5:	d4ac7da3c0aea6574e4c407a3559ba4b
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
