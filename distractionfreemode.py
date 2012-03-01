from gi.repository import GObject, Gedit, Gtk
'''
class ExampleAppActivatable(GObject.Object, Gedit.AppActivatable):
    __gtype_name__ = "ExampleAppActivatable"
    app = GObject.property(type=Gedit.App)
    
    def __init__(self):
        GObject.Object.__init__(self)
    
    def do_activate(self):
        pass
        #print "Application %s activated." % self.app

    def do_deactivate(self):
        pass
        #print "Application %s deactivated." % self.app
'''  

_width = 600

UI_XML = """<ui>
<toolbar name="ToolBar">
    <separator/>
    <toolitem action="DFModeAction"/>
</toolbar>
</ui>"""
   
class DistractionFreeWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "DistractionFreeMode"
    window = GObject.property(type=Gedit.Window)
    
    def __init__(self):
        GObject.Object.__init__(self)
        self._active = True
    
    def _add_ui(self):
        manager = self.window.get_ui_manager()
        self._actions = Gtk.ActionGroup("DF Mode")
        self._actions.add_actions([
            ('DFModeAction', Gtk.STOCK_INFO, "Toggle DF", 
                None, "Toggle distraction free mode", 
                self.on_DF_action_activate),
        ])
        manager.insert_action_group(self._actions)
        self._ui_merge_id = manager.add_ui_from_string(UI_XML)
        manager.ensure_update()

    def do_activate(self):
        self._add_ui()
        #print "Window %s activated." % self.window
        self.window.connect("check-resize", self.resize_check, self)
        '''w, h = self.window.get_size()
        views = self.window.get_views()
        margin = (w-_width)/2
        for view in views:
            view.set_left_margin(margin)
            view.set_right_margin(margin)'''


    def resize_check(self, container, widget):
        view = self.window.get_active_view()
        if(self._active):
            w, h = self.window.get_size()
            margin = (w-_width)/2
            view.set_left_margin(margin)
            view.set_right_margin(margin)
        else:
            view.set_left_margin(0)
            view.set_right_margin(0)


    def do_deactivate(self):
        self.window.disconnect("check-resize")
        self._remove_ui()
        #print "Window %s deactivated." % self.window

    def do_update_state(self):
        '''w, h = self.window.get_size()
        views = self.window.get_views()
        margin = (w-_width)/2
        for view in views:
            view.set_left_margin(margin)
            view.set_right_margin(margin)'''

    def on_DF_action_activate(self, action, data=None):
        self._active = not self._active
        
    def _remove_ui(self):
        manager = self.window.get_ui_manager()
        manager.remove_ui(self._ui_merge_id)
        manager.remove_action_group(self._actions)
        manager.ensure_update()
            
'''  
class ExampleViewActivatable(GObject.Object, Gedit.ViewActivatable):
    __gtype_name__ = "ExampleViewActivatable"
    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)
    
    def do_activate(self):
        self.view.set_wrap_mode(gtk.WRAP_WORD_CHAR)

    def do_deactivate(self):
        pass
        #print "View %s deactivated." % self.view

    def do_update_state(self):
        pass
        #print "View %s state updated." % self.view
        #global _width
        #self.view.set_left_margin((_width-500)/2)
    
'''
