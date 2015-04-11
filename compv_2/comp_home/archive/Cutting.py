#!/usr/bin/env vtkpython

import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("fuel.vti")

surf = vtk.vtkMarchingCubes()
surf.SetInputConnection(data.GetOutputPort())
surf.ComputeNormalsOn()
surf.SetNumberOfContours(2)
surf.SetValue(0, 100)
surf.SetValue(1, 200)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(surf.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1, 0, 0)
actor.GetProperty().SetOpacity(0.35)

plane = vtk.vtkPlane()
plane.SetOrigin(32, 32, 32)
plane.SetNormal(0, 1, 0)

cut = vtk.vtkCutter()
cut.SetInputConnection(data.GetOutputPort())
cut.SetCutFunction(plane)

cont = vtk.vtkContourFilter()
cont.SetInputConnection(cut.GetOutputPort())
cont.SetNumberOfContours(8)
cont.GenerateValues(16, 0, 255)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(4)
lut.SetTableValue(0, 1, 0, 0)
lut.SetTableValue(1, 0, 1, 0)
lut.SetTableValue(2, 0, 0, 1)
lut.SetTableValue(3, 1, 0, 1)


cmap = vtk.vtkPolyDataMapper()
cmap.SetInputConnection(cont.GetOutputPort())
cmap.SetScalarRange(0,255)
cmap.SetLookupTable(lut)

cact = vtk.vtkActor()
cact.SetMapper(cmap)


ren1 = vtk.vtkRenderer()
ren1.SetBackground(0.1, 0.2, 0.4)
ren1.AddActor(actor)
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
