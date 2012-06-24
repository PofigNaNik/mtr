# Conditional build:
# --with X11 - build wihtt X11/gtk+ interface
#
Summary:	Matt's Traceroute - network diagnostic tool
Summary(pl):	Matt's Traceroute - narz�dzie do diagnostyki sieci
Summary(ru):	Matt's Traceroute - ������� ��� ����������� ����
Summary(uk):	Matt's Traceroute - ���̦�� ��� Ħ��������� ����֦
Name:		mtr
Version:	0.49
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-resolv.patch
Patch1:		%{name}-makefile.patch
#Patch2:	ftp://ftp.kame.net/pub/kame/misc/mtr-045-v6-20020207.diff.gz
Patch2:		%{name}-0.48-v6-20020306.patch.gz
Patch3:		%{name}-nogtk.patch
Icon:		mtr.xpm
BuildRequires:	autoconf
BuildRequires:	automake
%{?_with_X11:BuildRequires:	gtk+-devel}
BuildRequires:	ncurses-devel >= 5.2
URL:		http://www.bitwizard.nl/mtr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mtr-gtk
Obsoletes:	mtr-ncurses

%description
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description -l pl
mtr jest narz�dziem do diagnostyki sieci, ��cz�cym funkcje
traceroute'a oraz ping'a. Program ten �ledzi tras� po��cznia mi�dzy
punktem z kt�rego zosta� uruchomiony, a punktem docelowym. Po
skompletowaniu listy punkt�w po�rednich przez kt�re pzrechodz� pakiety
mi�dzy tymi punktami do ka�dego z nich wysy�ane s� pakiety ICMP ECHO i
czasy odpowiedzi s� nast�pnie prezentowane na bie��co.

%description -l ru
mtr - ��� traceroute � ping � ����� �������. ��� ������ mtr ���������
������� ���������� ����� �������, �� ������� �� �������, � �������,
�������� �������������. ����� ����, ��� �� ��������� ������ �������
���� ����� ����� ����� ��������, mtr �������� ������������������ ICMP
ECHO �������� �� ������ �� ����� ��� ����������� �������� ����� �
������ �� �����. �� ���� ����, ��� �� ��� ������, mtr ������� �������
���������� �� ������ ������.

%description -l uk
mtr - �� traceroute �� ping � ������ �����Φ. ��� ������� mtr
���̦��դ �������� �'������� ͦ� �������, �� �˦� צ� ��������� ��
������� ������������. ���� ���������� ����� ������� ���� ͦ� ����
����� ��������, mtr ������� ���̦���Φ��� ICMP ECHO ����Ԧ� �� ������
� ��Ц� ��� ���������� ����Ԧ ̦��� �� ����ϧ � �����. � ��Ħ �����
������� mtr �������� ������� ���������� �� ���Φ� ����Φ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoheader
aclocal
autoconf
rm -f missing
automake -a -c -f
%configure \
	--with%{!?_with_X11:out}-gtk \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf mtr $RPM_BUILD_ROOT%{_sbindir}/mtr6

gzip -9nf AUTHORS NEWS README SECURITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(4754,root,adm) %{_sbindir}/mtr
%attr(4754,root,adm) %{_sbindir}/mtr6
%{_mandir}/man8/*
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
