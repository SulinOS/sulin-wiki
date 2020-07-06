.. -*- coding: utf-8 -*-

%%%%
SDDM
%%%%

Simple Desktop Display Manager is the display manager for X11 and Wayland window
systems. SDDM was written when kde version 5 published from scratch  in C ++ 11 and supports theme via QML.
SDDM is free and open source software that is subject to the GNU General Public License version two or later.

**Installation**
----------------

SDDM can be installed via master repositories of SulinOS


.. code-block:: shell

          sh ~# inary it sddm

This installation adds system sddm user as mentioned on `SDDM Documentation`_.

**OpenRC**
----------
For staring lightdm as a display manager you need to use startdm server :doc:`StartDM <./startdm>`

**Invoking**
------------

**Configuration**
^^^^^^^^^^^^^^^^^

This part a copy of Gentoo wiki pages.
As mentioned Gentoo Wiki:
SDDM has two configuration files: the package installed /usr/share/sddm/sddm.conf.d/00default.conf
and /etc/sddm.conf which is used to override specific options. The second is not created by the package.
KDE Plasma writes user changed options to /etc/sddm.conf. Both files have the same format. See comments in the file and man 5 sddm.conf for details on available options.

Keymap
""""""

To select the correct keymap on the login screen, add following lines to the /etc/sddm.conf file:

```/etc/sddm.conf```
.. code-block:: shell

        [X11]
        DisplayCommand=/etc/sddm/scripts/Xsetup

This file is not created automatically when the package is installed so you'll need to create it if you haven't done so already.

Next create the directory `/etc/sddm/scripts`

.. code-block:: shell

        root #mkdir -p /etc/sddm/scripts

and the file `/etc/sddm/scripts/Xsetup`

```/etc/sddm/scripts/Xsetup```
.. code-block:: shell

        setxkbmap gb,us

the first country code is the default. Finally set execute permissions on the file /etc/sddm/scripts/Xsetup.

.. code-block:: shell

        root #chmod a+x /etc/sddm/scripts/Xsetup


**Debugging**
-------------


**TroubleShooting**
-------------------


Get the latest news at `SDDM`_.

.. _SDDM Documentation: https://github.com/sddm/sddm/wiki
