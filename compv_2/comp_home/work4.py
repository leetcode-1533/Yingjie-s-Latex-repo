#!/usr/bin/env vtkpython

import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("/Users/y1275963/Documents/homework/multifield.0135.vti")

data_g = vtk.vtkAssignAttribute()
data_g.SetInputConnection(data.GetOutputPort())
data_g.Assign('G','SCALARS','POINT_DATA')

plane = vtk.vtkPlane()
plane.SetOrigin(320, 124, 124)
plane.SetNormal(0, 1, 0)


cut = vtk.vtkCutter()
cut.SetInputConnection(data_g.GetOutputPort())
cut.SetCutFunction(plane)

iso = vtk.vtkContourFilter()
iso.SetInputConnection(cut.GetOutputPort())
#iso.SetNumberOfContours(8)
iso.GenerateValues(16, 72, 26000)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(64)
lut.SetHueRange(1,1)
lut.SetValueRange(0.5,1)
lut.SetSaturationRange(1,1)
lut.Build()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(iso.GetOutputPort())
mapper.SetScalarRange(72,26000)
mapper.SetLookupTable(lut)
mapper.SetColorModeToMapScalars()

actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren1 = vtk.vtkRenderer()
ren1.SetBackground(1, 1, 1)
ren1.AddActor(actor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(500, 500)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Initialize()
iren.Start()