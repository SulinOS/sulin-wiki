.. -*- coding: utf-8 -*-

%%%%%%%
LightDM
%%%%%%%

LightDM is a free and open source X imaging manager that aims to be light, fast,
 extensible and multi-desktop. It can use various front ends to draw the User Interface,
 also called Greeters. It also supports Wayland.

**Installation**
----------------

LightDM can be installed via master repositories of SulinOS


.. code-block:: shell

          sh ~# inary it lightdm


Vanilla installation can come with some errors:

.. code-block:: shell

          DEBUG: Failed to load session file /usr/share/xsessions/ubuntu.desktop
          DEBUG: Session 1800: Sending SIGTERM
          Started seesion 2020 with service 'lightdm', username 'lightdm'
          DEBUG: Session 2020 authentication complete with return value 0: Success
          DEBUG: Greeter authorized
          DEBUG: Logging to /var/log/lightdm/x-0-greeter.log
          DEUBG: Failed to load session file /usr/share/xgreeters/default.desktop: No such file or directory
          DEBUG: Greeter failed to start
          DEBUG: Stopping display


This causes due to that. LightDM package have some greeters. Qt and GTK greaters
has included in our repositories. It is possible to use LightDM without a greeter
with changing config file, but only if an automatic login is configured

```/etc/lightdm/lightdm.conf```

.. code-block::

          [Seat:*]
          ...
          # greeter-session=lightdm-gtk-greeter
          ...

you need to disable greeter with using `#` ;
otherwise you will need to install xorg-server and one of the greeter packages below.

* lightdm-gtk-greeter
* lightdm-qt-greeter

With chaning option on `/etc/lightdm/lightdm.conf` file, option named
`greeter-session` used to change greeters.

**OpenRC**
----------
For staring lightdm as a display manager you need to use startdm server :doc:`StartDM <./startdm>`

**Invoking**
------------


**Debugging**
-------------


**TroubleShooting**
-------------------
