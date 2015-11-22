%global modname keypy
%global commit 820be04a3d4fbbc80326267dac245e7b9bf4a35d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# https://github.com/keyinst/keypy/pull/1
%global with_python3 0

Name:           python-%{modname}
Version:        1.0
Release:        1.git%{shortcommit}%{?dist}
Summary:        EEG preprocessing, analysis (microstates, spectra) and statistics 

License:        GPLv3+
URL:            https://github.com/keyinst/keypy
Source0:        https://github.com/keyinst/keypy/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
This package contains functionality for EEG preprocessing, microstate analysis,
spectral analysis, and statistics.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-numpy
# Test deps
BuildRequires:  python2-nose
BuildRequires:  python2-scipy
BuildRequires:  h5py

Requires:       python2-numpy
Requires:       python2-scipy
Requires:       h5py

%description -n python2-%{modname}
This package contains functionality for EEG preprocessing, microstate analysis,
spectral analysis, and statistics.

Python 2 version.

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  /usr/bin/2to3
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-scipy
BuildRequires:  python3-h5py

Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-h5py

%description -n python3-%{modname}
This package contains functionality for EEG preprocessing, microstate analysis,
spectral analysis, and statistics.

Python 3 version.
%endif

%prep
%autosetup -n %{modname}-%{commit}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
pushd tests/
  PYTHONPATH=%{buildroot}%{python2_sitelib} nosetests-%{python2_version} -v */scripts/*.py
  %if 0%{?with_python3}
  PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version} -v */scripts/*.py
  %endif
popd

%files -n python2-%{modname}
%license LICENSE
%doc example/ README.md
%{python2_sitelib}/%{modname}*

%if 0%{?with_python3}
%files -n python3-%{modname}
%license LICENSE
%doc example/ README.md
%{python2_sitelib}/%{modname}*
%endif

%changelog
* Sun Nov 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-1.git820be04
- Initial package
