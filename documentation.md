# autotools
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
# cmaketools
```
def configure(parameters='', installPrefix='/{}'.format(get.defaultprefixDIR()), sourceDir='.'):
    """configure source with given cmake parameters = "-DCMAKE_BUILD_TYPE -DCMAKE_CXX_FLAGS ... " """
def make(parameters=''):
    """build source with given parameters"""
def fixInfoDir():
def install(parameters='', argument='install'):
    """install source into install directory with given parameters"""
def rawInstall(parameters='', argument='install'):
    """install source into install directory with given parameters = PREFIX=get.installDIR()"""
```
# get
```
def curDIR():
    """returns current work directory's path"""
def curKERNEL():
    """returns currently running kernel's version"""
def curPYTHON():
    """ returns currently used python's version"""
def curPERL():
    """ returns currently used perl's version"""
def ENV(environ):
    """returns any given environ variable"""
def pkgDIR():
    """returns the path of binary packages"""
def workDIR():
def installDIR():
    """returns the path of binary packages"""
def lsbINFO():
    """Returns a dictionary filled through /etc/lsb-release."""
def kernelVERSION():
def srcNAME():
def srcVERSION():
def srcRELEASE():
def srcTAG():
def srcDIR():
def ARCH():
def HOST():
def CHOST():
def CFLAGS():
def CXXFLAGS():
def LDFLAGS():
def makeJOBS():
def buildTYPE():
    """returns the current build type"""
def docDIR():
def sbinDIR():
def infoDIR():
def manDIR():
def dataDIR():
def confDIR():
def localstateDIR():
def libexecDIR():
def defaultprefixDIR():
def emul32prefixDIR():
def kdeDIR():
def qtDIR():
def existBinary(bin):
def getBinutilsInfo(util):
def AR():
def AS():
def CC():
def CXX():
def LD():
def NM():
def RANLIB():
def F77():
def GCJ():
```
