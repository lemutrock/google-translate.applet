#!/bin/bash

idir=`pwd`

ln -s $idir/gtranslate.py /usr/bin/gtranslate

cp org.mate.panel.applet.GTranslateAppletFactory.service /usr/share/dbus-1/services/
cp org.mate.panel.GTranslate.mate-panel-applet /usr/share/mate-panel/applets/

echo "done"
