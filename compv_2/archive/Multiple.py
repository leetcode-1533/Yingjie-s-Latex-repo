#!/usr/bin/env vtkpython

import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("fuel.vti")

surf = vtk.vtkMarchingCubes()
surf.SetInputConnection(data.GetOutputPort())
surf.ComputeNormalsOn()
surf.SetNumberOfContours(4)
surf.SetValue(0,  50)
surf.SetValue(1, 100)
surf.SetValue(2, 150)
surf.SetValue(3, 200)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(4)
lut.SetTableValue(0, 1, 0, 0)
lut.SetTableValue(1, 0, 1, 0)
lut.SetTableValue(2, 0, 0, 1)
lut.SetTableValue(3, 1, 0, 1)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(surf.GetOutputPort())
mapper.SetLookupTable(lut)
mapper.SetScalarRange(50, 200)
mapper.SetColorModeToMapScalars()

actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren1 = vtk.vtkRenderer()
ren1.AddActor(actor)
ren1.SetBackground(0.1, 0.2, 0.4)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Initialize()
iren.Start()
