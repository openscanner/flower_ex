#!/usr/bin/env bash

# find project root
cd "$(dirname "$0")" ; cd ..

find . -name "*.pyc" | xargs rm -f
find . -name ".coverage" | xargs rm -f
find . -name "coverage.xml" | xargs rm -f
find . -name "pylint.out" | xargs rm -f

if ! which pylint; then
    pip install pylint
fi

pylint --jobs=4  --rcfile=etc/pylint.cfg flower_ex  | tee  pylint.out


# check and install nose
if ! which nosetests; then
    pip install nose
fi

if ! which coverage; then
    pip install coverage
fi



nosetests ./tests --exe  --with-coverage --cover-package=flower_ex --with-xunit --process-timeout=600
coverage xml
