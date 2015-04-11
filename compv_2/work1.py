#!/usr/bin/env vtkpython

# Import the VTK library bindings for Python

import vtk

# Create a reader to provide a source for data.
# This filter reads image datasets using VTK's
# XML-based file format.  The file contains
# information about the data format, data
# arrays and extent, so the only parameter that
# the filter needs is the file name.

data = vtk.vtkXMLImageDataReader()
data.SetFileName("/Users/y1275963/Documents/homework/multifield.0060.vti")

data_g = vtk.vtkAssignAttribute()
data_g.SetInputConnection(data.GetOutputPort())
data_g.Assign('G','SCALARS','POINT_DATA')


outline = vtk.vtkOutlineFilter()
outline.SetInputConnection(data_g.GetOutputPort())

outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())

outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)
outlineActor.GetProperty().SetColor(0,0,0)


# Create a filter to extract an isosurface from
# the dataset.  Connect the input of this
# filter to the output of the reader.  Set the
# value for the (one) isosurface that we want
# to extract, and tell the filter to compute
# normal vectors for each triangle on the
# output isosurface.

iso = vtk.vtkContourFilter()
iso.SetInputConnection(data_g.GetOutputPort())
iso.ComputeNormalsOn()
iso.SetNumberOfContours(1)
iso.SetValue(0, 20000) #Chnge here to change the isovalue

iso.Update()
outp = iso.GetOutput()
print outp

# Create a mapper to traverse the polydata and
# generate graphics commands for drawing the
# polygons onto the output device.

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(iso.GetOutputPort())
mapper.ScalarVisibilityOff()

# Output primitives (i.e. the triangles making
# up the isosurface) are managed as an actor;
# we specify that all outputs are coloured
# red.

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1, 0, 0)
actor.GetProperty().SetOpacity(0.5)
# Create a renderer which will output the
# graphics commands onto a drawing surface within
# a window.  By default the renderer will fill
# all of the window.  We set the background
# colour of the window to white.

ren1 = vtk.vtkRenderer()
ren1.AddActor(actor)
ren1.AddActor(outlineActor)
ren1.SetBackground(1, 1, 1)#white

# Create the window for output, setting its
# initial size.


renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(500, 500)

# Create an interactor to allow mouse and keyboard
# control of the render window content.  VTK supports
# a number of different interaction styles, here we
# choose a "trackball" style where object motion in
# the window starts and stops with input into the
# interaction device.

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

# Initialise the system; this will force the window
# content to be redrawn, triggering execution of the
# visualization pipeline.

iren.Initialize()
iren.Start()

