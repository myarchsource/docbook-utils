%define Name docbook-utils
%define Version 0.6.14

Name        	: %{Name}
Version     	: %{Version}
Release     	: 1
Group       	: Textprocessing/Tools

Summary     	: Shell scripts to manage DocBook documents.

Copyright   	: Eric Bischoff, Mark Galassi, Jochem Huhmann, Steve Cheng, and Frederik Fouvry; GPL 2.0
Packager    	: Eric Bischoff <eric@caldera.de>, Mark Galassi <rosalia@galassi.org>

Requires	: docbook-style-dsssl >= 1.49
Requires	: jadetex >= 2.5
Requires	: perl-SGMLSpm >= 1.03ii

BuildRoot   	: /tmp/%{Name}-%{Version}

BuildArch	: noarch
Source0		: %{Name}-%{Version}.tar.gz


%Description
These little scripts allow to convert easily DocBook files to other formats
(HTML, RTF, PostScript...), and to compare SGML files.


%Prep
%setup -q


%Build
./configure --prefix=/usr --mandir=/usr/share/man/en
make


%Install
DESTDIR=$RPM_BUILD_ROOT
make install prefix=$DESTDIR/usr mandir=$DESTDIR/usr/share/man/en docdir=$DESTDIR/usr/share/doc


%Clean
DESTDIR=$RPM_BUILD_ROOT
rm -rf $DESTDIR


%Files
%defattr (-,root,root)
%doc README COPYING TODO
%doc /usr/share/doc/html/
/usr/bin/jw
/usr/bin/docbook2*
/usr/bin/sgmldiff
/usr/share/sgml/docbook/utils-%{Version}/docbook-utils.dsl
/usr/share/sgml/docbook/utils-%{Version}/backends/*
/usr/share/sgml/docbook/utils-%{Version}/frontends/*
/usr/share/sgml/docbook/utils-%{Version}/helpers/*
/usr/share/man/en/man1/*
/usr/share/man/en/man7/*
