# Polyline drawing in codeskulptor

import simplegui

# Define canvas size
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300

# Create a polyline with three points
polyline = simplegui.PolyLine([(10, 10), (50, 50), (90, 10)], 3)

# Draw the polyline on the canvas
def draw(canvas):
  canvas.draw_polyline(polyline, "Red")

# Create a frame and register the draw handler
frame = simplegui.create_frame("Polyline", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)

# Start the frame
frame.start()

#You can adjust the points of the polyline by modifying the PolyLine constructor,
#and you can change the color of the line by modifying the second argument to the canvas.draw_polyline method.
