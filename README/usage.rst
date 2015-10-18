.. code-block::

	from gitconfig import *

	gitconfig.sections
	>>> [...]

	gitconfig.user.password
	>>> 'secret'

	gitconfig.not_existing
	>>> None
