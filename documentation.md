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
# inarytools
```
def executable_insinto(destinationDirectory, *sourceFiles):
    """insert a executable file into destinationDirectory"""
def readable_insinto(destinationDirectory, *sourceFiles):
    """inserts file list into destinationDirectory"""
def lib_insinto(sourceFile, destinationDirectory, permission=644):
    """inserts a library fileinto destinationDirectory with given permission"""
def dobin(sourceFile, destinationDirectory='/usr/bin'):
    """insert a executable file into /bin or /usr/bin"""
def dopixmaps(sourceFile, destinationDirectory='/usr/share/pixmaps'):
    """insert a data file into /usr/share/pixmaps"""
def dodir(destinationDirectory):
    """creates a directory tree"""
def dodoc(*sourceFiles, **kw):
    """inserts the files in the list of files into /usr/share/doc/PACKAGE"""
def dohtml(*sourceFiles, **kw):
    """inserts the files in the list of files into /usr/share/doc/PACKAGE/html"""
def doinfo(*sourceFiles):
    """inserts the into files in the list of files into /usr/share/info"""
def dolib(sourceFile, destinationDirectory='/usr/lib', mode=755):
    """insert the library into /usr/lib"""
def doman(*sourceFiles, pageDirectory=None):
    """inserts the man pages in the list of files into /usr/share/man/"""
def domo(sourceFile, locale, destinationFile, localeDirPrefix='/usr/share/locale'):
    """inserts the mo files in the list of files into /usr/share/locale/LOCALE/LC_MESSAGES"""
def domove(sourceFile, destination, destinationFile=''):
    """moves sourceFile/Directory into destinationFile/Directory"""
def rename(sourceFile, destinationFile):
    """ renames sourceFile as destinationFile"""
def dosed(sources, findPattern, replacePattern='', filePattern='', deleteLine=False, level=-1):
    """replaces patterns in sources"""
def dosbin(sourceFile, destinationDirectory='/usr/sbin'):
    """insert a executable file into /sbin or /usr/sbin"""
def dosym(sourceFile, destinationFile):
    """creates soft link between sourceFile and destinationFile"""
def insinto(destinationDirectory, sourceFile, destinationFile='', sym=True):
    """insert a sourceFile into destinationDirectory as a destinationFile with same uid/guid/permissions"""
def newdoc(sourceFile, destinationFile):
    """inserts a sourceFile into /usr/share/doc/PACKAGE/ directory as a destinationFile"""
def newman(sourceFile, destinationFile):
    """inserts a sourceFile into /usr/share/man/manPREFIX/ directory as a destinationFile"""
def remove(sourceFile):
    """removes sourceFile"""
def removeDir(destinationDirectory):
    """removes destinationDirectory and its subtrees"""
```
# javamodules
```
def compile(argument='', parameters='', build_tool='ant'):
    """compile source with given build tool and related parameters"""
def installExe(exe='', java_args='', exe_args='', dest_dir=''):
    """install executable jar to specified location and get jar prepared to
    execute with given arguments.

    exe:        Path in work dir to executable jar
    java_args:  Arguments passed to jvm
    exe_args:   Arguments passed to executable jar
    dest_dir:   Installation dir of executable jar"""
def installLib(src='*.jar', dest='/usr/share/java'):
    """install compilation output that is mix of the utility classes as
    in jars or meta/data files to specified locations.

    src:    Source file pattern to be installed
    dest:   Destination dir where the source files to be installed
    """
def dojavadoc(*source_files, **kw):
    """generate & copy javadoc files to /usr/share/doc/src_name recursively"""
def run(argument='', parameters='', build_tool='ant'):
    """run build tool with given parameters"""
```
# kde
```
def configure(parameters='', installPrefix=prefix, sourceDir='..'):
    """ parameters -DLIB_INSTALL_DIR="hede" -DSOMETHING_USEFUL=1"""
def make(parameters=''):
def install(parameters='', argument='install'):
```
# kerneltools
```
def getKernelVersion(flavour=None):
def configure():
def dumpVersion():
    """ Writes the specific kernel version into /etc/kernel"""
def build(debugSymbols=False):
def install():
def installHeaders(extraHeaders=None):
def installLibcHeaders(excludes=None):
```
# libtool
```
def preplib(sourceDirectory='/usr/lib'):
def gnuconfig_update():
    """ copy newest config.* onto source\'s """
def libtoolize(parameters=''):
def gen_usr_ldscript(dynamicLib):
```
# mesontools
```
def fixpc():
    """ fix .pc files in installDIR()/usr/lib32/pkgconfig"""
def meson_configure(parameters=""):
def cmake_configure(parameters=""):
def ninja_build(parameters=""):
def ninja_install(parameters=""):
def ninja_check():
```
# perlmodules
```
def configure(parameters=''):
    """configure source with given parameters."""
def make(parameters=''):
    """make source with given parameters."""
def install(parameters='install'):
    """install source with given parameters."""
def removePacklist(path='usr/lib/perl5/'):
    """ cleans .packlist file from perl packages """
def removePodfiles(path='usr/lib/perl5/'):
    """ cleans *.pod files from perl packages """
def removeEmptydirs(d):
    """ remove empty dirs from perl package if exists after deletion .pod and .packlist files """
```
# pkgconfig
```
def getVariableForLibrary(library, variable):
    """Returns a specific variable provided in the library .pc file"""
def getLibraryVersion(library):
    """Returns the module version provided in the library .pc file."""
def getLibraryCFLAGS(library):
    """Returns compiler flags for compiling with this library.
    Ex: -I/usr/include/nss"""
def getLibraryLIBADD(library):
    """Returns linker flags for linking with this library.
    Ex: -lpng14"""
def runManualCommand(*args):
    """Runs the given command and returns the output."""
def libraryExists(library):
    """Returns True if the library provides a .pc file."""
```
#pythonmodules
```
def configure(parameters='', pyVer=''):
    """does python setup.py configure"""
def compile(parameters='', pyVer=''):
    """compile source with given parameters."""
def install(parameters='', pyVer=''):
    """does python setup.py install"""
def run(parameters='', pyVer=''):
    """executes parameters with python"""
def fixCompiledPy(lookInto='/usr/lib/{}/'.format(get.curPYTHON())):
    """ cleans *.py[co] from packages """
```
# qt
```
def configure(projectfile='', parameters='', installPrefix=prefix):
def make(parameters=''):
def install(parameters='', argument='install'):
```
# rubymodules
```
def get_config(config):
def get_ruby_version():
def get_rubylibdir():
def get_sitedir():
def get_gemdir():
def get_ruby_install_name():
def get_gemhome():
def get_sitelibdir():
def generate_gemname():
def auto_dodoc():
def install(parameters=''):
    """does ruby setup.rb install"""
def rake_install(parameters=''):
def gem_build(parameters=''):
def gem_install(parameters=''):
    """Make installation from GemFile"""
def run(parameters=''):
    """executes parameters with ruby"""
```
# scons
```
def make(parameters=''):
def install(parameters='install', prefix=get.installDIR(), argument='prefix'):
```
# shelltools
```
def can_access_file(filePath):
    """test the existence of file"""
def can_access_directory(destinationDirectory):
    """test readability, writability and executablility of directory"""
def makedirs(destinationDirectory):
    """recursive directory creation function"""
def echo(destionationFile, content):
def chmod(filePath, mode=0o755):
    """change the mode of filePath to the mode"""
def chown(filePath, uid='root', gid='root'):
    """change the owner and group id of filePath to uid and gid"""
def sym(source, destination):
    """creates symbolic link"""
def unlink(pattern):
    """remove the file path"""
def unlinkDir(sourceDirectory):
    """delete an entire directory tree"""
def move(source, destination):
    """recursively move a "source" file or directory to "destination\""""
def copy(source, destination, sym=True):
    """recursively copy a "source" file or directory to "destination\" """
def copytree(source, destination, sym=True):
    """recursively copy an entire directory tree rooted at source"""
def touch(filePath):
    """changes the access time of the 'filePath', or creates it if it does not exist"""
def cd(directoryName=''):
    """change directory"""
def ls(source):
    """listdir"""
def export(key, value):
    """export environ variable"""
def isLink(filePath):
    """return True if filePath refers to a symbolic link"""
def isFile(filePath):
    """return True if filePath is an existing regular file"""
def isDirectory(filePath):
    """Return True if filePath is an existing directory"""
def isEmpty(filePath):
    """Return True if filePath is an empty file"""
def realPath(filePath):
    """return the canonical path of the specified filename, eliminating any symbolic links encountered in the path"""
def baseName(filePath):
    """return the base name of pathname filePath"""
def dirName(filePath):
    """return the directory name of pathname path"""
def system(command):
    """command an list but should be an str"""
```
# textlivemodules
```
def compile(parameters=''):
    """compiling texlive packages"""
def install(parameters=''):
    """Installing texlive packages"""
def createSymlinksFormat2Engines():
    """Create symlinks from format to engines"""
def installDocFiles():
    """Installing docs"""
def installTexmfFiles():
    """Installing texmf, texmf-dist, tlpkg, texmf-var"""
def installConfigFiles():
    """Installing config files"""
def handleConfigFiles():
    """Handling config files"""
def addFormat(parameters):
    """Add format files"""
def moveSources():
def buildFormatFiles():
    """Build format files"""
def addLanguageDat(parameter):
    """Create language.*.dat files"""
def addLanguageDef(parameter):
    """Create language.*.def files"""
def generateConfigFiles():
    """Generate config files"""
```
