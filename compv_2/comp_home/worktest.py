# -*- coding: utf-8 -*-
"""
    Created on Fri Mar  6 10:26:23 2015
    
    @author: y1275963
    """
#!/usr/bin/env vtkpython

import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("/Users/y1275963/Documents/homework/multifield.0135.vti")


data_g = vtk.vtkAssignAttribute()
data_g.SetInputConnection(data.GetOutputPort())
data_g.Assign('G','SCALARS','POINT_DATA')

opacityTransferFunction = vtk.vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(10.0, 0.001)
opacityTransferFunction.AddPoint(1900.0,0.001 )
opacityTransferFunction.AddPoint(2000.0, 1.0)
opacityTransferFunction.AddPoint(2500.0, 1.0)
opacityTransferFunction.AddPoint(2600.0, 0.001)
opacityTransferFunction.AddPoint(22000.0, 0.001)
opacityTransferFunction.AddPoint(23000.0, 1.0)
opacityTransferFunction.AddPoint(27000.0, 1.0)

colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddHSVPoint(10.0, 0.1, 0.0, 0.0)
colorTransferFunction.AddHSVPoint(1900.0, 0.1, 0.0, 0.0)
colorTransferFunction.AddHSVPoint(2000.0, 0.9, 1.0, 1.0)
colorTransferFunction.AddHSVPoint(2500.0, 0.9, 1.0, 1.0)
colorTransferFunction.AddHSVPoint(2600.0, 0.6, 0.0, 0.0)
colorTransferFunction.AddHSVPoint(22000.0, 0.6, 0.0, 0.0)
colorTransferFunction.AddHSVPoint(23000.0, 0.5, 1.0, 1.0)
colorTransferFunction.AddHSVPoint(27000.0, 0.5, 1.0, 1.0)

volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(1,colorTransferFunction)
volumeProperty.SetScalarOpacity(1,opacityTransferFunction)
volumeProperty.SetInterpolationTypeToLinear()
volumeProperty.ShadeOff()

#compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()
volumeMapper = vtk.vtkFixedPointVolumeRayCastMapper()
#volumeMapper.SetFixedPointVolumeRayCastFunction(compositeFunction)
volumeMapper.SetInputConnection(data.GetScalars().GetOutputPort())
volumeMapper.SetBlendModeToComposite()



## Adding ScalarBar:
scalarBar = vtk.vtkScalarBarActor()
scalarBar.SetLookupTable(colorTransferFunction)
scalarBar.SetOrientationToVertical()
scalarBar.SetPosition( 0.85, 0.7 );
scalarBar.SetPosition2( 0.1, 0.3 );

volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

ren1 = vtk.vtkRenderer()
ren1.SetBackground(1, 1, 1)
ren1.AddVolume(volume)
ren1.AddActor(scalarBar)


renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(500, 500)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Initialize()
iren.Start()


