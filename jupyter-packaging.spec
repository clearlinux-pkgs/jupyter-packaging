#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter-packaging
Version  : 0.11.0
Release  : 26
URL      : https://files.pythonhosted.org/packages/04/ed/a61feec48ace4acd2a9083232a4fde042c44529dcd5a11d0e3816bd3629d/jupyter_packaging-0.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/04/ed/a61feec48ace4acd2a9083232a4fde042c44529dcd5a11d0e3816bd3629d/jupyter_packaging-0.11.0.tar.gz
Summary  : Jupyter Packaging Utilities.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyter-packaging-license = %{version}-%{release}
Requires: jupyter-packaging-python = %{version}-%{release}
Requires: jupyter-packaging-python3 = %{version}-%{release}
Requires: deprecation
Requires: packaging
Requires: setuptools
Requires: tomlkit
Requires: wheel
BuildRequires : buildreq-distutils3
BuildRequires : deprecation
BuildRequires : packaging
BuildRequires : setuptools
BuildRequires : tomlkit
BuildRequires : wheel

%description
# Jupyter Packaging
Tools to help build and install Jupyter Python packages that require a pre-build step that may include JavaScript build steps.

%package license
Summary: license components for the jupyter-packaging package.
Group: Default

%description license
license components for the jupyter-packaging package.


%package python
Summary: python components for the jupyter-packaging package.
Group: Default
Requires: jupyter-packaging-python3 = %{version}-%{release}

%description python
python components for the jupyter-packaging package.


%package python3
Summary: python3 components for the jupyter-packaging package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_packaging)
Requires: pypi(deprecation)
Requires: pypi(packaging)
Requires: pypi(setuptools)
Requires: pypi(tomlkit)
Requires: pypi(wheel)

%description python3
python3 components for the jupyter-packaging package.


%prep
%setup -q -n jupyter_packaging-0.11.0
cd %{_builddir}/jupyter_packaging-0.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635745966
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter-packaging
cp %{_builddir}/jupyter_packaging-0.11.0/LICENSE %{buildroot}/usr/share/package-licenses/jupyter-packaging/7a88a926691422ae250d28e9a8214e9e40469383
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyter-packaging/7a88a926691422ae250d28e9a8214e9e40469383

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
