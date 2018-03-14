Name:           rpmfusion-nonfree-obsolete-packages
Version:        28
Release:        1%{?dist}
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
* Tue Mar 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 28-1
- Initial spec file
