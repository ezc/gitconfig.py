.. image:: https://img.shields.io/badge/language-python-blue.svg

.. image:: https://img.shields.io/pypi/pyversions/gitconfig.svg
   :target: https://pypi.python.org/pypi/gitconfig

.. image:: https://img.shields.io/codacy/None.svg
   :target: https://www.codacy.com/app/russianidiot-github/gitconfig-py/dashboard

.. image:: https://landscape.io/github/russianidiot/gitconfig.py/master/landscape.svg?style=flat
   :target: https://landscape.io/github/russianidiot/gitconfig.py/master
   :alt: landscape.io

.. image:: https://img.shields.io/codeship/None.svg
   :target: https://codeship.com/projects/None

Install
```````

pip: `[sudo] pip install gitconfig`

Usage
`````

.. code-block::

	from gitconfig import *

	gitconfig.sections
	>>> [...]

	gitconfig.user.password
	>>> 'secret'

	gitconfig.not_existing
	>>> None

Examples
~~~~~~~~

`Examples/`_ folder, 1 file = 1 example

.. _Examples/: https://github.com/russianidiot/gitconfig.py/tree/master/Examples

source code `https://github.com/russianidiot/gitconfig.py/blob/master/py_modules/gitconfig.py`_

.. _https://github.com/russianidiot/gitconfig.py/blob/master/py_modules/gitconfig.py/: https://github.com/russianidiot/gitconfig.py/blob/master/py_modules/gitconfig.py

Feedback

|github_issues|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/gitconfig.py.svg
	:target: https://github.com/russianidiot/gitconfig.py/issues

|gitter|

.. |gitter| image:: https://badges.gitter.im/russianidiot/gitconfig.py.svg
	:target: https://gitter.im/russianidiot/gitconfig.py

|github_follow|

.. |github_follow| https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

----

`russianidiot.github.io/python/`_  - Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/

`russianidiot.github.io/cli/`_  - command line scripts

.. _russianidiot.github.io/cli/: http://russianidiot.github.io/cli/

`README.rst`_  - generated with `readmemako.py`_ (python+ `mako`_ templates) and `.README`_ dotfiles

.. _README.rst: https://github.com/russianidiot/gitconfig.py/blob/master/README.rst
.. _readmemako.py: http://github.com/russianidiot/readmemako.py/
.. _mako: http://www.makotemplates.org/
.. _.README: https://github.com/russianidiot-dotfiles/.README
