#!/usr/bin/env python3
"""
based on http://pygobject.readthedocs.io/en/latest/guide/cairo_integration.html
"""

import cairo
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
try:
    gi.require_foreign("cairo")
except ImportError:
    print("No pycairo integration :(")


def draw(da, ctx):
    """
    print("type draw     : " + str(type(draw)))     type draw     : < class 'function'>
    print("type draw:da  : " + str(type(da)))       type draw: da : < class 'gi.repository.Gtk.DrawingArea'>
    print("type draw:ctx : " + str(type(ctx)))      type draw: ctx: < class 'cairo.Context'>
    """

    # Sets the source pattern within the Context to an opaque color.
    # This opaque color will then be used for any subsequent drawing operation until a new source pattern is set.
    # The color components are floating point numbers in the range 0 to 1. If the values passed in are outside that range, they will be clamped.
    # Parameters:
    #   red 	red component of color
    #   green 	green component of color
    #   blue 	blue component of color

    # clear background (?)
    # ctx.set_source_rgb(1,1,1)

    ctx.set_source_rgb()



def main():
    win = Gtk.Window()
    win.connect('destroy', lambda w: Gtk.main_quit())
    win.set_default_size(800, 600)

    drawingarea = Gtk.DrawingArea()
    win.add(drawingarea)
    drawingarea.connect('draw', draw)

    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()


