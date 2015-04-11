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

data.Update()

data.Update()
data.GetOutput().GetPointData().SetScalars(data.GetOutput().GetPointData().GetArray("G"))

[low,high] = data.GetOutput().GetPointData().GetArray("H2").GetRange()

#print ar.GetName()

## Get Outline
outline = vtk.vtkOutlineFilter()
outline.SetInputConnection(data.GetOutputPort())

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
iso.SetInputConnection(data.GetOutputPort())
iso.ComputeNormalsOn()
iso.SetNumberOfContours(1)
iso.SetValue(0, 2500) #Chnge here to change the isovalue

ass = vtk.vtkAssignAttribute()
ass.SetInputConnection(iso.GetOutputPort())
ass.Assign("H2", "SCALARS", "POINT_DATA")

### Creating Color mapping:
#colorT = vtk.vtkLookupTable()
#colorT.SetNumberOfTableValues(100)
#colorT.SetTableRange (low, high)
#colorT.Build()
#for i in range(100):
#    colorT.SetTableValue(i, 0.0, 0.0, 0.0, 0.5)
#colorT.SetTableValue(5, 1.0, 0.0, 0.0, 1.0)
#colorT.SetTableValue(10, 0.0, 1.0, 0.0, 1.0)
#colorT.SetTableValue(100, 0.0, 0.0, 1.0, 1.0)
colorT = vtk.vtkDiscretizableColorTransferFunction()
print colorT.AddHSVPoint(low,0.5,0.5,1.0)
print colorT.AddHSVPoint(high*0.5,0.5,0.3,1.0)
print colorT.AddHSVPoint(high,0.5,0.3,0.1)

colorT.SetScaleToLinear()
colorT.Build()

scalarBar = vtk.vtkScalarBarActor()
scalarBar.SetLookupTable(colorT)
scalarBar.SetOrientationToVertical()
scalarBar.SetPosition( 0.85, 0.7 );
scalarBar.SetPosition2( 0.1, 0.3 );
## Create a mapper to traverse the polydata and
## generate graphics commands for drawing the
## polygons onto the output device.

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(ass.GetOutputPort())
mapper.SetLookupTable(colorT)
mapper.SetScalarRange(low,high)
mapper.SetColorModeToMapScalars()
mapper.ScalarVisibilityOff()


actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren1 = vtk.vtkRenderer()
ren1.AddActor(actor)
ren1.AddActor(outlineActor)
ren1.AddActor(scalarBar)
ren1.SetBackground(1, 1, 1)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(500, 500)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Initialize()
iren.Start()

