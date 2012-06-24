Summary:	Matt's Traceroute - network diagnostic tool
Summary(es):	Herramienta para diagn�stico de red, combinando ping/traceroute
Summary(pl):	Matt's Traceroute - narz�dzie do diagnostyki sieci
Summary(pt_BR):	Ferramenta para diagn�stico da rede, combinando ping/traceroute
Summary(ru):	Matt's Traceroute - ������� ��� ����������� ����
Summary(uk):	Matt's Traceroute - ���̦�� ��� Ħ��������� ����֦
Name:		mtr
Version:	0.50
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
URL:		http://www.bitwizard.nl/mtr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mtr-ncurses

%description
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description -l es
mtr es una herramienta para diagn�stico de la red que combina ping y
traceroute en un programa. Tiene dos interfaces, una ncurses, �til
para uso en sesiones telnet/ssh y una gtk para uso en el X Window.

%description -l pl
mtr jest narz�dziem do diagnostyki sieci, ��cz�cym funkcje
traceroute'a oraz pinga. Program ten �ledzi tras� po��cznia mi�dzy
punktem z kt�rego zosta� uruchomiony, a punktem docelowym. Po
skompletowaniu listy punkt�w po�rednich przez kt�re pzrechodz� pakiety
mi�dzy tymi punktami do ka�dego z nich wysy�ane s� pakiety ICMP ECHO i
czasy odpowiedzi s� nast�pnie prezentowane na bie��co.

%description -l pt_BR
O mtr � uma ferramenta para diagn�stico da rede que combina ping e
traceroute em um programa. Tem duas interfaces, uma ncurses, �til para
uso em sess�es telnet/ssh e uma gtk para uso no X Window.

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

%package X11
Summary:	Matt's Traceroute - network diagnostic tool, X11 version
Summary(es):	Interface GTK para mtr
Summary(pl):	Matt's Traceroute - narz�dzie do diagnostyki sieci, wersja X11
Summary(pt_BR):	Interface GTK para o mtr
Summary(ru):	Matt's Traceroute - ������� ��� ����������� ����
Summary(uk):	Matt's Traceroute - ���̦�� ��� Ħ��������� ����֦
Group:		Networking/Utilities
Obsoletes:	mtr-gtk

%description X11
mtr combines the functionaly of the traceroute and ping programs in a
single network diagnostic tool. As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the
machines, it sends a sequence ICMP ECHO requests to each one to
determine the quality of the link to each machine. As it does this, it
prints running statistics about each machine.

%description X11 -l es
mtr es una herramienta para diagn�stico de la red que combina ping y
traceroute en un programa. Tiene dos interfaces, una ncurses, �til
para uso en sesiones telnet/ssh y una gtk para uso en el X Window.

%description X11 -l pl
mtr jest narz�dziem do diagnostyki sieci, ��cz�cym funkcje
traceroute'a oraz pinga. Program ten �ledzi tras� po��cznia mi�dzy
punktem z kt�rego zosta� uruchomiony, a punktem docelowym. Po
skompletowaniu listy punkt�w po�rednich przez kt�re pzrechodz� pakiety
mi�dzy tymi punktami do ka�dego z nich wysy�ane s� pakiety ICMP ECHO i
czasy odpowiedzi s� nast�pnie prezentowane na bie��co.

%description X11 -l pt_BR
O mtr � uma ferramenta para diagn�stico da rede que combina ping e
traceroute em um programa. Tem duas interfaces, uma ncurses, �til para
uso em sess�es telnet/ssh e uma gtk para uso no X Window.

%description X11 -l ru
mtr - ��� traceroute � ping � ����� �������. ��� ������ mtr ���������
������� ���������� ����� �������, �� ������� �� �������, � �������,
�������� �������������. ����� ����, ��� �� ��������� ������ �������
���� ����� ����� ����� ��������, mtr �������� ������������������ ICMP
ECHO �������� �� ������ �� ����� ��� ����������� �������� ����� �
������ �� �����. �� ���� ����, ��� �� ��� ������, mtr ������� �������
���������� �� ������ ������.

%description X11 -l uk
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
	--with-gtk \
	--enable-ipv6

%{__make}
mv -f mtr mtr-x11
%{__make} clean

%configure \
	--without-gtk \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir},%{_prefix}/X11R6/sbin/}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install mtr-x11 $RPM_BUILD_ROOT%{_prefix}/X11R6/sbin/mtr

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

%files X11
%defattr(644,root,root,755)
%attr(4754,root,adm) /usr/X11R6/sbin/mtr
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
