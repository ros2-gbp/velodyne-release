Name:           ros-indigo-velodyne-msgs
Version:        1.5.2
Release:        0%{?dist}
Summary:        ROS velodyne_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/velodyne_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
ROS message definitions for Velodyne 3D LIDARs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jan 28 2019 Josh Whitley <jwhitley@autonomoustuff.com> - 1.5.2-0
- Autogenerated by Bloom

* Mon Dec 10 2018 Josh Whitley <jwhitley@autonomoustuff.com> - 1.5.1-0
- Autogenerated by Bloom

* Fri Oct 19 2018 Josh Whitley <jwhitley@autonomoustuff.com> - 1.5.0-0
- Autogenerated by Bloom

* Wed Sep 19 2018 Josh Whitley <jwhitley@autonomoustuff.com> - 1.4.0-0
- Autogenerated by Bloom

* Fri Nov 10 2017 Josh Whitley <jwhitley@autonomoustuff.com> - 1.3.0-0
- Autogenerated by Bloom

* Wed Aug 06 2014 Jack O'Quin <jack.oquin@gmail.com> - 1.2.0-0
- Autogenerated by Bloom

