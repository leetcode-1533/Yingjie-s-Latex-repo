# -*- coding: utf-8 -*-
"""
    Created on Fri Mar  6 10:26:23 2015
    
    @author: y1275963
    """
#!/usr/bin/env vtkpython

import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("/Users/y1275963/Documents/homework/multifield.0045.vti")


data_g = vtk.vtkAssignAttribute()
data_g.SetInputConnection(data.GetOutputPort())
data_g.Assign('G','SCALARS','POINT_DATA')

plane = vtk.vtkPlane()
plane.SetOrigin(320, 124, 124)
plane.SetNormal(0, 1, 0)

cut = vtk.vtkCutter()
cut.SetInputConnection(data_g.GetOutputPort())
cut.SetCutFunction(plane)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(128)
lut.SetHueRange(0.66,0)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cut.GetOutputPort())
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
