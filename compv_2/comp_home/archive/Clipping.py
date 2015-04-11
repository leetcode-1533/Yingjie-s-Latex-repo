#!/usr/bin/env vtkpython

import vtk

plane = vtk.vtkPlane()
plane.SetOrigin(32, 32, 32)
plane.SetNormal(0, 1, 0)

data = vtk.vtkXMLImageDataReader()
data.SetFileName("fuel.vti")

clip = vtk.vtkClipVolume()
clip.SetClipFunction(plane)
clip.SetInputConnection(data.GetOutputPort())


surf = vtk.vtkContourFilter()
surf.SetInputConnection(clip.GetOutputPort())
surf.ComputeNormalsOn()
surf.GenerateValues(8, 0, 250)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(64)
lut.SetHueRange(0.66,0)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

cmap = vtk.vtkPolyDataMapper()
cmap.SetInputConnection(surf.GetOutputPort())
cmap.SetScalarRange(0,255)
cmap.SetLookupTable(lut)
cmap.SetColorModeToMapScalars()

actor = vtk.vtkActor()
actor.SetMapper(cmap)

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
