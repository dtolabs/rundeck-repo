
.PHONY: rundeck-repo.spec

rundeck-repo.spec:
	mkdir -p dist/RPMS/noarch
	rpmbuild -bb --target noarch-linux --define "_topdir ${PWD}/dist" --buildroot ${PWD}/target $@

clean:
	rm -rf dist
