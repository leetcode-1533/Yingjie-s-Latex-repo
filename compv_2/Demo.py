
import vtk

data = vtk.vtkXMLImageDataReader()
data.SetFileName("/Users/y1275963/Documents/homework/multifield.0060.vti")
data.Update()
data.GetOutput().GetPointData().SetScalars(data.GetOutput().GetPointData().GetArray("G"))
print data.GetOutput().GetPointData().GetArray("H2").GetRange()

iso = vtk.vtkContourFilter()
iso.SetInputConnection(data.GetOutputPort())
iso.ComputeNormalsOn()
iso.SetNumberOfContours(1)
iso.SetValue(0, 2500)

ass = vtk.vtkAssignAttribute()
ass.SetInputConnection(iso.GetOutputPort())
ass.Assign("H2", "SCALARS", "POINT_DATA")

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(512)
lut.SetHueRange(0.66,1)
lut.SetValueRange(1,1)
lut.SetSaturationRange(1,1)
lut.Build()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(ass.GetOutputPort())
mapper.SetLookupTable(lut)
mapper.SetScalarRange(1.5680000158523055e-13, 4.954000178258866e-05)
mapper.SetColorModeToMapScalars()

actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren1 = vtk.vtkRenderer()
ren1.AddActor(actor)
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


