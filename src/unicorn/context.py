from math import *
import sys

class GCodeContext:
    def __init__(self, xy_feedrate, z_feedrate, start_delay, stop_delay, pen_up_angle, pen_down_angle, z_height, finished_height, file):
      self.xy_feedrate = xy_feedrate
      self.z_feedrate = z_feedrate
      self.start_delay = start_delay
      self.stop_delay = stop_delay
      self.pen_up_angle = pen_up_angle
      self.pen_down_angle = pen_down_angle
      self.z_height = z_height
      self.finished_height = finished_height
      self.file = file
      
      self.drawing = False
      self.last = None

      self.preamble = [
        "(Scribbled version of %s @ %.2f)" % (self.file, self.xy_feedrate),
        "( %s )" % " ".join(sys.argv),
        "G21 (metric ftw)",
        "G90 (absolute mode)",
        "G92 X0 Y0 Z0 (zero all axes)",
        "G92 Z%0.2F F%0.2F (go to printing level)" % (self.z_height, self.z_feedrate),
        ""
      ]

      self.postscript = [
        "",
				"(end of print job)",
				"M300 S%0.2F (pen up)" % self.pen_up_angle,
				"G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay),
				"M300 S255 (turn off servo)",
				"G1 X0 Y0 F%0.2F" % self.xy_feedrate,
        # FIXME - parameterize z finished height
				"G1 Z%0.2F F%0.2F (go up to finished level)" % (self.finished_height, self.z_feedrate),
				"G1 X0 Y0 F%0.2F (go back to center)" % self.z_feedrate,
				"M18 (drives off)",
      ]

      self.codes = []

    def generate(self):
      for codeset in [self.preamble, self.codes, self.postscript]:
        for line in codeset:
          print line

    def start(self):
      self.codes.append("M300 S%0.2F (pen down)" % self.pen_down_angle)
      self.codes.append("G4 P%d (wait %dms)" % (self.start_delay, self.start_delay))
      self.drawing = True

    def stop(self):
      self.codes.append("M300 S%0.2F (pen up)" % self.pen_up_angle)
      self.codes.append("G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay))
      self.drawing = False

    def go_to_point(self, x, y, stop=False):
      if self.last == (x,y):
        return
      if stop:
        return
      else:
        if self.drawing: 
            self.codes.append("M300 S%0.2F (pen up)" % self.pen_up_angle) 
            self.codes.append("G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay))
            self.drawing = False
        self.codes.append("G1 X%.2f Y%.2f F%.2f" % (x,y, self.xy_feedrate))
      self.last = (x,y)
	
    def draw_to_point(self, x, y, stop=False):
      if self.last == (x,y):
          return
      if stop:
        return
      else:
        if self.drawing == False:
            self.codes.append("M300 S%0.2F (pen down)" % self.pen_up_angle)
            self.codes.append("G4 P%d (wait %dms)" % (self.start_delay, self.start_delay))
            self.drawing = True
        self.codes.append("G1 X%0.2f Y%0.2f F%0.2f" % (x,y, self.xy_feedrate))
      self.last = (x,y)
