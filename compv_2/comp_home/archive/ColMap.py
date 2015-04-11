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
lut.SetHueRange(0.6,0)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

cmap = vtk.vtkPolyDataMapper()
cmap.SetInputConnection(cut.GetOutputPort())
cmap.SetLookupTable(lut)
cmap.SetScalarRange(0,255)
cmap.SetColorModeToMapScalars()

cact = vtk.vtkActor()
cact.SetMapper(cmap)

ren1 = vtk.vtkRenderer()
ren1.SetBackground(0.1, 0.2, 0.4)
ren1.AddActor(cact)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(500, 500)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Initialize()
iren.Start()
