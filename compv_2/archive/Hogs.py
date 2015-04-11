#!/usr/bin/env vtkpython

import vtk

pl3d = vtk.vtkPLOT3DReader()
pl3d.SetXYZFileName("combxyz.bin")
pl3d.SetQFileName("combq.bin")
pl3d.SetScalarFunctionNumber(100)
pl3d.SetVectorFunctionNumber(202)
pl3d.Update()
(lo, hi) = pl3d.GetOutput().GetPointData().GetScalars().GetRange()

# PLOT3D functions:
# scalar: 100 - density 
#         110 - pressure 
#         120 - temperature 
#         130 - enthalpy 
#         140 - internal energy 
#         144 - kinetic energy 
#         153 - velocity magnitude 
#         163 - stagnation energy 
#         170 - entropy 
#         184 - swirl
# vector: 
#         200 - velocity 
#         201 - vorticity 
#         202 - momentum 
#         210 - pressure gradient

hogs = vtk.vtkHedgeHog()
hogs.SetInputConnection(pl3d.GetOutputPort())
hogs.SetVectorModeToUseVector()
hogs.SetScaleFactor(0.001)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(64)
lut.SetHueRange(0.66,0)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

map = vtk.vtkPolyDataMapper()
map.SetInputConnection(hogs.GetOutputPort())
map.SetScalarRange(lo, hi)
map.SetLookupTable(lut)
map.SetColorModeToMapScalars()


actor = vtk.vtkActor()
actor.SetMapper(map)
actor.GetProperty().SetColor(1,0,0)


outline = vtk.vtkStructuredGridOutlineFilter()
outline.SetInputConnection(pl3d.GetOutputPort())

outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())

outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)
outlineActor.GetProperty().SetColor(0, 0, 0)


ren1 = vtk.vtkRenderer()
ren1.AddActor(actor)
ren1.AddActor(outlineActor)
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


