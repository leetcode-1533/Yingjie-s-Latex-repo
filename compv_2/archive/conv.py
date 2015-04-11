
import vtk
import vtkLocalPython

rd = vtkLocalPython.vtkRAWReader()
rd.SetRAWFile("fuel.raw", 64, 64, 64)
rd.Update()

wr = vtk.vtkXMLImageDataWriter()
wr.SetFileName("fuel.xim")
wr.SetDataModeToAscii()
wr.SetInputConnection(rd.GetOutputPort())
wr.Write()

