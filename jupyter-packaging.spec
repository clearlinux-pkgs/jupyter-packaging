#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter-packaging
Version  : 0.8.3
Release  : 9
URL      : https://files.pythonhosted.org/packages/38/58/3eb9edf1bd2f773077594b6c83b375d949c11287fb2fc1b2e6b69ad3112d/jupyter_packaging-0.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/38/58/3eb9edf1bd2f773077594b6c83b375d949c11287fb2fc1b2e6b69ad3112d/jupyter_packaging-0.8.3.tar.gz
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
Tools to help build and install Jupyter Python packages that require a pre-build step that may include JavaScript build steps.
        
        ## Install
        
        `pip install jupyter-packaging`
        
        ## Usage
        
        There are three ways to use `jupyter-packaging` in another package.
        
        ### As a Build Requirement

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
%setup -q -n jupyter_packaging-0.8.3
cd %{_builddir}/jupyter_packaging-0.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618243354
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter-packaging
cp %{_builddir}/jupyter_packaging-0.8.3/LICENSE %{buildroot}/usr/share/package-licenses/jupyter-packaging/7a88a926691422ae250d28e9a8214e9e40469383
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
