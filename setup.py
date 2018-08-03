from Cython.Build import cythonize
from distutils.core import setup

ext_options = {"compiler_directives": {"profile": True}, "annotate": True}
setup(
    ext_modules = cythonize("email_validation_cy.pyx", **ext_options)
)