name: rundeck-repo
version: 2
release: 0
summary: RunDeck Repository Bootstrap
group: Applications/System
license: APL
packager: noahcampbell AT gmail DOT com
requires: yum
conflicts: rundeck-repo-bleeding

%description
The RunDeck project consists of numerous RPMs ready for install on a users machine.  This package contains the necessary yum .repo files that can be used to bootstrap the repository configuration.

%files
/etc/yum.repos.d/rundeck.repo

%package bleeding
version: 2
release: 0
summary: Rundeck Repository Bootstrap - Bleeding Edge Releases
group: Application/System
license: APL
packager: noahcampbell AT gmail DOT com
requires: yum
conflicts: rundeck-repo

%description bleeding
The RunDeck project consists of numerous RPMs ready for install on a users machine.  This package contains the necessary yum .repo files that can be used to bootstrap the repository configuration.

%files bleeding
/etc/yum.repos.d/rundeck-bleedingedge.repo
