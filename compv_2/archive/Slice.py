#!/usr/bin/env vtkpython

import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("fuel.vti")

plane = vtk.vtkPlane()
plane.SetOrigin(32, 32, 32)
plane.SetNormal(0, 0, 1)

cut = vtk.vtkCutter()
cut.SetInputConnection(data.GetOutputPort())
cut.SetCutFunction(plane)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(64)
lut.SetHueRange(0.66,0)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cut.GetOutputPort())
mapper.SetScalarRange(0,255)
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
