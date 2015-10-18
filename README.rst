	
Install
'''''''

github.com_: :code:`pip install git+git://github.com/russianidiot/gitconfig.py.git`

pypi.python.org_: :code:`pip install gitconfig`

download_: :code:`python setup.py install` or :code:`setup.py/.setup.py develop.command`

.. _github.com: http://github.com/russianidiot/gitconfig.py
.. _pypi.python.org: https://pypi.python.org/pypi/gitconfig
.. _download: https://github.com/russianidiot/gitconfig.py/archive/master.zip

	

	

	

Usage 
'''''
.. code-block::

	from gitconfig import *

	gitconfig.sections
	>>> [...]

	gitconfig.user.password
	>>> 'secret'

	gitconfig.not_existing
	>>> None

------------

**Tested**: python 2.6, 2.7, 3+

**Bug Tracker**: `github.com/russianidiot/gitconfig.py/issues`__

__ https://github.com/russianidiot/gitconfig.py/issues