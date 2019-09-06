#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : glslang
Version  : 7.12.3352
Release  : 17
URL      : https://github.com/KhronosGroup/glslang/archive/7.12.3352/glslang-7.12.3352.tar.gz
Source0  : https://github.com/KhronosGroup/glslang/archive/7.12.3352/glslang-7.12.3352.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AML BSD-3-Clause BSD-3-Clause-Clear
Requires: glslang-bin = %{version}-%{release}
Requires: glslang-lib = %{version}-%{release}
Requires: glslang-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : flex
BuildRequires : glibc-dev
BuildRequires : python3

%description
Also see the Khronos landing page for glslang as a reference front end:
https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/

%package bin
Summary: bin components for the glslang package.
Group: Binaries
Requires: glslang-license = %{version}-%{release}

%description bin
bin components for the glslang package.


%package dev
Summary: dev components for the glslang package.
Group: Development
Requires: glslang-lib = %{version}-%{release}
Requires: glslang-bin = %{version}-%{release}
Provides: glslang-devel = %{version}-%{release}
Requires: glslang = %{version}-%{release}

%description dev
dev components for the glslang package.


%package lib
Summary: lib components for the glslang package.
Group: Libraries
Requires: glslang-license = %{version}-%{release}

%description lib
lib components for the glslang package.


%package license
Summary: license components for the glslang package.
Group: Default

%description license
license components for the glslang package.


%package staticdev
Summary: staticdev components for the glslang package.
Group: Default
Requires: glslang-dev = %{version}-%{release}

%description staticdev
staticdev components for the glslang package.


%prep
%setup -q -n glslang-7.12.3352

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567782660
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DCMAKE_INSTALL_LIBDIR=lib64 \
-DENABLE_GLSLANG_INSTALL=True
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567782660
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glslang
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/glslang/LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glslangValidator
/usr/bin/spirv-remap

%files dev
%defattr(-,root,root,-)
/usr/include/SPIRV/GLSL.ext.AMD.h
/usr/include/SPIRV/GLSL.ext.EXT.h
/usr/include/SPIRV/GLSL.ext.KHR.h
/usr/include/SPIRV/GLSL.ext.NV.h
/usr/include/SPIRV/GLSL.std.450.h
/usr/include/SPIRV/GlslangToSpv.h
/usr/include/SPIRV/Logger.h
/usr/include/SPIRV/SPVRemapper.h
/usr/include/SPIRV/SpvBuilder.h
/usr/include/SPIRV/SpvTools.h
/usr/include/SPIRV/bitutils.h
/usr/include/SPIRV/disassemble.h
/usr/include/SPIRV/doc.h
/usr/include/SPIRV/hex_float.h
/usr/include/SPIRV/spirv.hpp
/usr/include/SPIRV/spvIR.h
/usr/include/glslang/Include/BaseTypes.h
/usr/include/glslang/Include/Common.h
/usr/include/glslang/Include/ConstantUnion.h
/usr/include/glslang/Include/InfoSink.h
/usr/include/glslang/Include/InitializeGlobals.h
/usr/include/glslang/Include/PoolAlloc.h
/usr/include/glslang/Include/ResourceLimits.h
/usr/include/glslang/Include/ShHandle.h
/usr/include/glslang/Include/Types.h
/usr/include/glslang/Include/arrays.h
/usr/include/glslang/Include/intermediate.h
/usr/include/glslang/Include/revision.h
/usr/include/glslang/MachineIndependent/Initialize.h
/usr/include/glslang/MachineIndependent/LiveTraverser.h
/usr/include/glslang/MachineIndependent/ParseHelper.h
/usr/include/glslang/MachineIndependent/RemoveTree.h
/usr/include/glslang/MachineIndependent/Scan.h
/usr/include/glslang/MachineIndependent/ScanContext.h
/usr/include/glslang/MachineIndependent/SymbolTable.h
/usr/include/glslang/MachineIndependent/Versions.h
/usr/include/glslang/MachineIndependent/attribute.h
/usr/include/glslang/MachineIndependent/gl_types.h
/usr/include/glslang/MachineIndependent/glslang_tab.cpp.h
/usr/include/glslang/MachineIndependent/iomapper.h
/usr/include/glslang/MachineIndependent/localintermediate.h
/usr/include/glslang/MachineIndependent/parseVersions.h
/usr/include/glslang/MachineIndependent/preprocessor/PpContext.h
/usr/include/glslang/MachineIndependent/preprocessor/PpTokens.h
/usr/include/glslang/MachineIndependent/propagateNoContraction.h
/usr/include/glslang/MachineIndependent/reflection.h
/usr/include/glslang/Public/ShaderLang.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/libHLSL.so
/usr/lib64/libSPIRV.so
/usr/lib64/libSPVRemapper.so
/usr/lib64/libglslang-default-resource-limits.so
/usr/lib64/libglslang.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glslang/LICENSE.txt

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libOGLCompiler.a
/usr/lib64/libOSDependent.a
