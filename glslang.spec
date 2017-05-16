#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glslang
Version  : SPIRV99
Release  : 3
URL      : https://github.com/KhronosGroup/glslang/archive/SPIRV99.tar.gz
Source0  : https://github.com/KhronosGroup/glslang/archive/SPIRV99.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: glslang-bin
BuildRequires : bison
BuildRequires : cmake
BuildRequires : flex

%description
This directory contains data needed by Bison.
* Skeletons
Bison skeletons: the general shapes of the different parser kinds,
that are specialized for specific grammars by the bison program.

%package bin
Summary: bin components for the glslang package.
Group: Binaries

%description bin
bin components for the glslang package.


%prep
%setup -q -n glslang-SPIRV99

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484492848
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1484492848
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glslangValidator
/usr/bin/spirv-remap
