
.PHONY: controltier-repo.spec

controltier-repo.spec:
	mkdir -p dist/RPMS/noarch
	rpmbuild -bb --target noarch --define "_topdir ${PWD}/dist" --buildroot ${PWD}/target $@

clean:
	rm -rf dist
