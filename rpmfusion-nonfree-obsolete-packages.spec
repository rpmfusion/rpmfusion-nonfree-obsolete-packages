Name:           rpmfusion-nonfree-obsolete-packages
Version:        37
Release:        3%{?dist}
Summary:        A package to obsolete retired packages from rpmfusion-nonfree

License:        MIT
URL:            http://rpmfusion.org
Source0:        README
BuildArch:      noarch

# Last build nvidia-304xx-kmod-304.137-5.fc28
Provides: akmod-nvidia-304xx = 304.137-100
Obsoletes: akmod-nvidia-304xx < 304.137-100
Provides: kmod-nvidia-304xx = 304.137-100
Obsoletes: kmod-nvidia-304xx < 304.137-100
# Last build xorg-x11-drv-nvidia-304xx-304.137-2.fc28
Provides: xorg-x11-drv-nvidia-304xx = 304.137-100
Obsoletes: xorg-x11-drv-nvidia-304xx < 304.137-100
# Last build comical-0.8-19.fc29
Provides: comical = 0.8-20
Obsoletes: comical < 0.8-20
# Last build gens-gs-2.16.7-11.fc29
Provides: gens-gs = 2.16.7-12
Obsoletes: gens-gs < 2.16.7-12
# Last build Mosaic-2.7-0.12.b5.fc29
Provides: Mosaic = 2.7-0.13
Obsoletes: Mosaic < 2.7-0.13
# Last build gstreamer-plugins-bad-nonfree-0.10.23-10.fc31
Provides: gstreamer-plugins-bad-nonfree = 0.10.23-11
Obsoletes: gstreamer-plugins-bad-nonfree < 0.10.23-11
# Last build nautilus-dropbox-2020.03.04-3.fc35
Provides: nautilus-dropbox = 2020.03.04-4
Obsoletes: nautilus-dropbox < 2020.03.04-4
Provides: dropbox = 2020.03.04-4
Obsoletes: dropbox < 2020.03.04-4
# Last build caja-dropbox-1.26.0-2.fc37
Provides: caja-dropbox = 1.26.0-3
Obsoletes: caja-dropbox < 1.26.0-3
# Last build libspotify-12.1.51-11.fc36
Provides: libspotify = 12.1.51-12
Obsoletes: libspotify < 12.1.51-12
# Last build python-pyspotify-2.1.3-2.fc35
Provides: python-pyspotify = 2.1.3-3
Obsoletes: python-pyspotify < 2.1.3-3
# Last build mopidy-spotify-4.1.1-1.fc35
Provides: mopidy-spotify = 4.1.1-2
Obsoletes: mopidy-spotify < 4.1.1-2


%description
This package exists only to obsolete other packages which need to be removed
from the RPM Fusion nonfree for some reason.

%prep
cp -p %{SOURCE0} .


%build
# Nothing to build


%install
# Nothing to install

%files
%doc README



%changelog
* Fri Sep 23 2022 Leigh Scott <leigh123linux@gmail.com> - 37-3
- Add libspotify, mopidy-spotify and python-pyspotify

* Tue Sep 13 2022 Leigh Scott <leigh123linux@gmail.com> - 37-2
- Add caja-dropbox
- Remove pcsx2

* Mon Sep 12 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 37-1
- Add nautilus-dropbox and it's sub-package
- Bump version to 37

* Fri Aug 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 31-1
- Bump version to 31
- Add gstreamer-plugins-bad-nonfree

* Mon Apr 08 2019 Leigh Scott <leigh123linux@googlemail.com> - 30-1
- Bump version to 30

* Mon Apr 08 2019 Leigh Scott <leigh123linux@googlemail.com> - 28-2
- Add comical, gens-gs, Mosaic and pcsx2

* Tue Mar 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 28-1
- Initial spec file
