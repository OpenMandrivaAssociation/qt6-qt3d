%define beta rc

Name:		qt6-qt3d
Version:	6.9.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qt3d-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qt3d-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
#Patch0:		qt3d-6.5.0-compile.patch
Group:		System/Libraries
Summary:	Qt %{qtmajor} 3D Library
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	qt6-cmake
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(OpenGL)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
License:	LGPLv3/GPLv3/GPLv2

%description
Qt %{qtmajor} 3D library

%global extra_files_3DCore \
%dir %{_qtdir}/qml/Qt3D \
%{_qtdir}/qml/Qt3D/Core \
%dir %{_qtdir}/plugins/geometryloaders \
%{_qtdir}/plugins/geometryloaders/libdefaultgeometryloader.so \
%{_qtdir}/plugins/geometryloaders/libgltfgeometryloader.so \
%dir %{_qtdir}/plugins/renderers \
%{_qtdir}/plugins/renderers/libopenglrenderer.so \
%{_qtdir}/plugins/renderers/librhirenderer.so \
%dir %{_qtdir}/plugins/sceneparsers \
%{_qtdir}/plugins/sceneparsers/libassimpsceneimport.so \
%{_qtdir}/plugins/sceneparsers/libgltfsceneexport.so \
%{_qtdir}/plugins/sceneparsers/libgltfsceneimport.so

%global extra_devel_files_3DCore \
%{_qtdir}/lib/cmake/Qt6/FindWrapQt3DAssimp.cmake \
%{_qtdir}/lib/cmake/Qt6BuildInternals/StandaloneTests/Qt3DTestsConfig.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6quick3dcoreplugin*.cmake

%global extra_files_3DAnimation \
%{_qtdir}/qml/Qt3D/Animation

%global extra_devel_files_3DAnimation \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6quick3danimationplugin*.cmake

%global extra_files_3DExtras \
%{_qtdir}/qml/Qt3D/Extras

%global extra_devel_files_3DExtras \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6quick3dextrasplugin*.cmake

%global extra_files_3DInput \
%{_qtdir}/qml/Qt3D/Input

%global extra_devel_files_3DInput \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6quick3dinputplugin*.cmake

%global extra_files_3DLogic \
%{_qtdir}/qml/Qt3D/Logic

%global extra_devel_files_3DLogic \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6quick3dlogicplugin*.cmake

%global extra_files_3DQuick \
%{_qtdir}/qml/QtQuick/Scene3D

%global extra_devel_files_3DQuick \
%{_qtdir}/sbom/*

%global extra_files_3DQuickScene2D \
%{_qtdir}/qml/QtQuick/Scene2D \
%dir %{_qtdir}/plugins/renderplugins \
%{_qtdir}/plugins/renderplugins/libscene2d.so \

%global extra_devel_files_3DQuickScene2D \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquickscene2dplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquickscene3dplugin*.cmake

%global extra_files_3DQuickRender \
%{_qtdir}/qml/Qt3D/Render

%global extra_devel_files_3DRender \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6quick3drenderplugin*.cmake

%qt6libs 3DCore 3DAnimation 3DExtras 3DInput 3DLogic 3DQuickAnimation 3DQuickExtras 3DQuickInput 3DQuick 3DQuickRender 3DQuickScene2D 3DQuickScene3D 3DRender

%package examples
Summary:	Example code for the Qt 6 3D module
Group:		Documentation

%description examples
Example code for the Qt 6 3D module

%prep
%autosetup -p1 -n qt3d%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON \
	-DBUILD_WITH_PCH:BOOL=OFF

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall

%files examples
%{_qtdir}/examples
