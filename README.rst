.. image:: https://img.shields.io/pypi/v/gitconfig.svg
   :target: https://pypi.python.org/pypi/gitconfig

.. image:: https://img.shields.io/pypi/pyversions/gitconfig.svg
   :target: https://pypi.python.org/pypi/gitconfig

.. image:: https://img.shields.io/pypi/dm/gitconfig.svg
   :target: https://pypi.python.org/pypi/gitconfig

	

Install
~~~~~~~

github.com_: :code:`pip install git+git://github.com/russianidiot/gitconfig.py.git`

pypi.python.org_: :code:`pip install gitconfig`

download_: :code:`[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

.. _github.com: http://github.com/russianidiot/gitconfig.py
.. _pypi.python.org: https://pypi.python.org/pypi/gitconfig.py
.. _download: https://github.com/russianidiot/gitconfig.py/archive/master.zip

	

	

	

Usage
~~~~~

.. code-block::

	from gitconfig import *

	gitconfig.sections
	>>> [...]

	gitconfig.user.password
	>>> 'secret'

	gitconfig.not_existing
	>>> None

----

Feedback
~~~~~~~~

|github_issues| - Github Issues

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/gitconfig.py.svg
	:target: https://github.com/russianidiot/gitconfig.py/issues

|gitter| - **Chat** with me (english/russian) 

.. |gitter| image:: https://badges.gitter.im/russianidiot/gitconfig.py.svg
	:target: https://gitter.im/russianidiot/gitconfig.py

`russianidiot.github.io/python/`_  - my Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/