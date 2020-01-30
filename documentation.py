# Autotools
```
def configure(parameters=''):
    """configure source with given parameters = "--with-nls --with-libusb --with-something-usefull"""
def rawConfigure(parameters=''):
    """configure source with given parameters = --prefix=/usr --libdir=/usr/lib --with-nls """
def compile(parameters=''):
def make(parameters=''):
def fixInfoDir():
def fixpc():
    """ fix .pc files in installDIR()/usr/lib32/pkgconfig"""
def install(parameters='', argument='install'):
    """install source into install directory with given parameters"""
def rawInstall(parameters='', argument='install'):
    """install source into install directory with given parameters = PREFIX=get.installDIR()"""
def aclocal(parameters=''):
    """generates an aclocal.m4 based on the contents of configure.in."""
def autogen():
    """generates configure script from autogen"""
def autoconf(parameters=''):
    """generates a configure script"""
def autoreconf(parameters=''):
    """re-generates a configure script"""
def automake(parameters=''):
    """generates a makefile"""

def autoheader(parameters=''):
    """generates templates for configure"""
```
