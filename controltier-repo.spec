name: controltier-repo
version: 3.5
release: 1
summary: ControlTier repository bootstrap
group: Applications/System
license: APL
packager: noahcampbell AT gmail DOT com
requires: yum

%description
The controltier project consists of numerous RPMs ready for install on a users machine.  This package contains the necessary yum .repo files that can be used to bootstrap the repository configuration.

%files
/etc/yum.repos.d/controltier.repo
