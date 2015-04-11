#!/usr/bin/env vtkpython

import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("fuel.vti")

plane = vtk.vtkPlane()
plane.SetOrigin(32, 32, 32)
plane.SetNormal(0, 0, -1)

clip = vtk.vtkClipVolume()
clip.SetClipFunction(plane)
clip.SetInputConnection(data.GetOutputPort())

cut = vtk.vtkCutter()
cut.SetInputConnection(data.GetOutputPort())
cut.SetCutFunction(plane)

iso = vtk.vtkContourFilter()
iso.SetInputConnection(cut.GetOutputPort())
iso.SetNumberOfContours(8)
iso.GenerateValues(8, 10, 255)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(64)
lut.SetHueRange(0.66,0)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(iso.GetOutputPort())
mapper.SetScalarRange(0,255)
mapper.SetLookupTable(lut)
mapper.SetColorModeToMapScalars()

actor = vtk.vtkActor()
actor.SetMapper(mapper)

iso2 = vtk.vtkContourFilter()
iso2.SetInputConnection(clip.GetOutputPort())
iso2.ComputeNormalsOn()
iso2.SetNumberOfContours(1)
iso2.SetValue(0, 10)

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(iso2.GetOutputPort())
mapper2.ScalarVisibilityOff()

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(0, 0, 1)

ren1 = vtk.vtkRenderer()
ren1.SetBackground(1, 1, 1)
ren1.AddActor(actor)
ren1.AddActor(actor2)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(500, 500)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Initialize()
iren.Start()
