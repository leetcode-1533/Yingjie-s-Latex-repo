#!/usr/bin/env vtkpython

import vtk

pl3d = vtk.vtkPLOT3DReader()
pl3d.SetXYZFileName("combxyz.bin")
pl3d.SetQFileName("combq.bin")
pl3d.SetScalarFunctionNumber(110)
pl3d.SetVectorFunctionNumber(200)
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

plane = vtk.vtkStructuredGridGeometryFilter()
plane.SetInputConnection(pl3d.GetOutputPort())
plane.SetExtent(10, 10, 1, 100, 1, 100)
plane2 = vtk.vtkStructuredGridGeometryFilter()
plane2.SetInputConnection(pl3d.GetOutputPort())
plane2.SetExtent(30, 30, 1, 100, 1, 100)
plane3 = vtk.vtkStructuredGridGeometryFilter()
plane3.SetInputConnection(pl3d.GetOutputPort())
plane3.SetExtent(45, 45, 1, 100, 1, 100)

appendF = vtk.vtkAppendPolyData()
appendF.AddInput(plane.GetOutput())
appendF.AddInput(plane2.GetOutput())
appendF.AddInput(plane3.GetOutput())

warp = vtk.vtkWarpVector()
warp.SetInputConnection(appendF.GetOutputPort())
warp.SetScaleFactor(.001)

normals = vtk.vtkPolyDataNormals()
normals.SetInput(warp.GetPolyDataOutput())
normals.SetFeatureAngle(60)

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(64)
lut.SetHueRange(0.66,0)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

map = vtk.vtkPolyDataMapper()
map.SetInputConnection(normals.GetOutputPort())
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


