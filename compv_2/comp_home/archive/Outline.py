#!/usr/bin/env vtkpython

import vtk

pl3d = vtk.vtkPLOT3DReader()
pl3d.SetXYZFileName("combxyz.bin")
pl3d.SetQFileName("combq.bin")
pl3d.SetScalarFunctionNumber(100)
pl3d.SetVectorFunctionNumber(202)
pl3d.Update()

outline = vtk.vtkStructuredGridOutlineFilter()
outline.SetInputConnection(pl3d.GetOutputPort())

outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())

outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)
outlineActor.GetProperty().SetColor(0, 0, 0)


ren1 = vtk.vtkRenderer()
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


