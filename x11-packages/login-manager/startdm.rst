.. -*- coding: utf-8 -*-

%%%%%%%
StartDM
%%%%%%%

The common login manager service for sulinos. You can change default login manager or enable autologin
StartDM written in python3. If login manager die or killed StartDM respawn again it.

**Installation**
----------------
StartDM can be installed via master repositories of SulinOS

.. code-block:: shell

          sh ~# inary it dm-service
          
**OpenRC**
----------

For enable StartDM on boot

.. code-block:: shell

          sh ~# rc-update add dm default

**Invoking**
------------
For starting dm-service

.. code-block:: shell

          sh ~# rc-service dm start
          
For stop dm-sercive

.. code-block:: shell

          sh ~# rc-service dm stop

Note: if dm-service stoped current login manager not killed. you must kill manually


**Configuration**
^^^^^^^^^^^^^^^^^
StartDM config file is **/etc/start-dm/default.conf**

.. code-block:: shell

          default=lightdm            # default login manager command
          dm-user=root               # login manager username
          isole-env=True             # Environment isolation value (True or False)
          autologin=False            # Autologin value (True or False)
          autologin-user=root        # Autologin user name
          autologin-session=xterm    # Autologin session command

**Bugs**
-------------------
visit https://gitlab.com/sulinos/devel/start-dm/-/issues 
