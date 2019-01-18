#!/usr/bin/python3
import gi
import sys
gi.require_version('MatePanelApplet', '4.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from gi.repository import MatePanelApplet
import subprocess

def applet_fill(applet):    
    btn = Gtk.Button.new_with_label("GTranslate")
    btn.connect("clicked", on_btn_clicked)
    applet.add(btn)
    applet.show_all()

def applet_factory(applet,iid,data):
    if iid != "GTranslate":
        return False
    applet_fill(applet)
    return True

def on_btn_clicked(button):                
    win = Gtk.Window()
    win.set_border_width(10)    
    mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)    
    label = Gtk.Label("Input a text that you want to translate")
    sterm = Gtk.Entry()    
    mainBox.pack_start(label, True, True, 0)    
    sterm.set_activates_default(True)
    mainBox.pack_start(sterm, True, True, 0)
    btn1 = Gtk.Button.new_with_label("Translate it!")            
    btn1.connect("clicked", on_click,sterm,label)        
    btn1.set_can_default(True)
    mainBox.pack_start(btn1, True,True, 0)
    win.add(mainBox)      
    win.set_position(Gtk.WindowPosition.CENTER)
    win.connect("destroy", finish)        
    win.set_default(btn1)    
    win.show_all()    
        
def finish(window):    
    window.close()

def on_click(button,sterm,label):
    term = sterm.get_text()    
    translate_request(term,label)

def translate_request(term,label):    
    cmd = "/usr/bin/trans -brief -sl en -tl ru \"%s\"" % term.replace('"',"'")        
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)    
    (output, err) = p.communicate()
    p_status = p.wait()
    translation = output.decode('utf-8')    
    label.set_text(translation)

MatePanelApplet.Applet.factory_main("GTranslateAppletFactory", True, MatePanelApplet.Applet.__gtype__, applet_factory, None)
