#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : glslang
Version  : 11.3.0
Release  : 25
URL      : https://github.com/KhronosGroup/glslang/archive/11.3.0/glslang-11.3.0.tar.gz
Source0  : https://github.com/KhronosGroup/glslang/archive/11.3.0/glslang-11.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AML Apache-2.0 BSD-3-Clause
Requires: glslang-bin = %{version}-%{release}
Requires: glslang-lib = %{version}-%{release}
Requires: glslang-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : flex
BuildRequires : glibc-dev

%description
# News
1. Visual Studio 2013 is no longer supported
Microsoft Visual Studio 2013 is no longer officially supported. \
Please upgrade to at least Visual Studio 2015.

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
%setup -q -n glslang-11.3.0
cd %{_builddir}/glslang-11.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619142927
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DCMAKE_INSTALL_LIBDIR=lib64 \
-DENABLE_GLSLANG_INSTALL=True
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1619142927
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glslang
cp %{_builddir}/glslang-11.3.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/glslang/ec42d6637226afc8675c101f4eaa6b19ca32f202
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
/usr/include/glslang/HLSL/hlslAttributes.h
/usr/include/glslang/HLSL/hlslGrammar.h
/usr/include/glslang/HLSL/hlslOpMap.h
/usr/include/glslang/HLSL/hlslParseHelper.h
/usr/include/glslang/HLSL/hlslParseables.h
/usr/include/glslang/HLSL/hlslScanContext.h
/usr/include/glslang/HLSL/hlslTokenStream.h
/usr/include/glslang/HLSL/hlslTokens.h
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
/usr/include/glslang/Include/glslang_c_interface.h
/usr/include/glslang/Include/glslang_c_shader_types.h
/usr/include/glslang/Include/intermediate.h
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
/usr/include/glslang/SPIRV/GLSL.ext.AMD.h
/usr/include/glslang/SPIRV/GLSL.ext.EXT.h
/usr/include/glslang/SPIRV/GLSL.ext.KHR.h
/usr/include/glslang/SPIRV/GLSL.ext.NV.h
/usr/include/glslang/SPIRV/GLSL.std.450.h
/usr/include/glslang/SPIRV/GlslangToSpv.h
/usr/include/glslang/SPIRV/Logger.h
/usr/include/glslang/SPIRV/NonSemanticDebugPrintf.h
/usr/include/glslang/SPIRV/SPVRemapper.h
/usr/include/glslang/SPIRV/SpvBuilder.h
/usr/include/glslang/SPIRV/SpvTools.h
/usr/include/glslang/SPIRV/bitutils.h
/usr/include/glslang/SPIRV/disassemble.h
/usr/include/glslang/SPIRV/doc.h
/usr/include/glslang/SPIRV/hex_float.h
/usr/include/glslang/SPIRV/spirv.hpp
/usr/include/glslang/SPIRV/spvIR.h
/usr/include/glslang/build_info.h
/usr/lib64/cmake/HLSLTargets-relwithdebinfo.cmake
/usr/lib64/cmake/HLSLTargets.cmake
/usr/lib64/cmake/OGLCompilerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/OGLCompilerTargets.cmake
/usr/lib64/cmake/OSDependentTargets-relwithdebinfo.cmake
/usr/lib64/cmake/OSDependentTargets.cmake
/usr/lib64/cmake/SPIRVTargets-relwithdebinfo.cmake
/usr/lib64/cmake/SPIRVTargets.cmake
/usr/lib64/cmake/SPVRemapperTargets-relwithdebinfo.cmake
/usr/lib64/cmake/SPVRemapperTargets.cmake
/usr/lib64/cmake/glslang-default-resource-limitsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/glslang-default-resource-limitsTargets.cmake
/usr/lib64/cmake/glslangTargets-relwithdebinfo.cmake
/usr/lib64/cmake/glslangTargets.cmake
/usr/lib64/cmake/glslangValidatorTargets-relwithdebinfo.cmake
/usr/lib64/cmake/glslangValidatorTargets.cmake
/usr/lib64/cmake/spirv-remapTargets-relwithdebinfo.cmake
/usr/lib64/cmake/spirv-remapTargets.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/libHLSL.so
/usr/lib64/libSPIRV.so
/usr/lib64/libSPVRemapper.so
/usr/lib64/libglslang-default-resource-limits.so
/usr/lib64/libglslang.so
/usr/lib64/libglslang.so.11
/usr/lib64/libglslang.so.11.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glslang/ec42d6637226afc8675c101f4eaa6b19ca32f202

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libOGLCompiler.a
/usr/lib64/libOSDependent.a
