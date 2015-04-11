# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:15:51 2015

@author: y1275963
"""

#!/usr/bin/env vtkpython

# Import the VTK library bindings for Python

import vtk
def contour_G(filename):
    # Creating contour for G fileld
    
    data = vtk.vtkXMLImageDataReader()
    data.SetFileName(filename)#"/Users/y1275963/Documents/homework/multifield.0060.vti")
    

    data_g = vtk.vtkAssignAttribute()
    data_g.SetInputConnection(data.GetOutputPort())
    data_g.Assign('G','SCALARS','POINT_DATA')
    

    outline = vtk.vtkOutlineFilter()
    outline.SetInputConnection(data_g.GetOutputPort())
    
    outlineMapper = vtk.vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outline.GetOutputPort())
    
    outlineActor = vtk.vtkActor()
    outlineActor.SetMapper(outlineMapper)
    outlineActor.GetProperty().SetColor(0,0,1)
    
    
    # Create a filter to extract an isosurface from
    # the dataset.  Connect the input of this
    # filter to the output of the reader.  Set the
    # value for the (one) isosurface that we want
    # to extract, and tell the filter to compute
    # normal vectors for each triangle on the
    # output isosurface.
    
    iso = vtk.vtkContourFilter()
    iso.SetInputConnection(data_g.GetOutputPort())
    iso.ComputeNormalsOn()
    iso.SetNumberOfContours(1)
    iso.SetValue(0, 2500) #Chnge here to change the isovalue
    
    
    # Create a mapper to traverse the polydata and
    # generate graphics commands for drawing the
    # polygons onto the output device.
    
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(iso.GetOutputPort())
    mapper.ScalarVisibilityOff()
    
    # Output primitives (i.e. the triangles making
    # up the isosurface) are managed as an actor;
    # we specify that all outputs are coloured
    # red.
    
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 0, 0)
    actor.GetProperty().SetOpacity(0.5)
    
    # Create a renderer which will output the
    # graphics commands onto a drawing surface within
    # a window.  By default the renderer will fill
    # all of the window.  We set the background
    # colour of the window to white.
    return (outlineActor,actor)
def multi_con_h2(filename):
    # Creating contour for h2 fileld
    
    data = vtk.vtkXMLImageDataReader()
    data.SetFileName(filename)#"/Users/y1275963/Documents/homework/multifield.0060.vti")
    data.Update()
    #Getting highest value
    [low,high] = data.GetOutput().GetPointData().GetArray("H2").GetRange()

    data_h2 = vtk.vtkAssignAttribute()
    data_h2.SetInputConnection(data.GetOutputPort())
    data_h2.Assign('H2','SCALARS','POINT_DATA')
    
    
    
    # Create a filter to extract an isosurface from
    # the dataset.  Connect the input of this
    # filter to the output of the reader.  Set the
    # value for the (one) isosurface that we want
    # to extract, and tell the filter to compute
    # normal vectors for each triangle on the
    # output isosurface.
    
    iso = vtk.vtkContourFilter()
    iso.SetInputConnection(data_h2.GetOutputPort())
    iso.ComputeNormalsOn()
    iso.SetNumberOfContours(10)
    for i in range(10):
        iso.SetValue(i, (1.0-0.1*i)*high) #Chnge here to change the isovalue
    
    
    # Create a mapper to traverse the polydata and
    # generate graphics commands for drawing the
    # polygons onto the output device.
    
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(iso.GetOutputPort())
    mapper.ScalarVisibilityOff()
    
    # Output primitives (i.e. the triangles making
    # up the isosurface) are managed as an actor;
    # we specify that all outputs are coloured
    # red.
    
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0, 0, 1)
    actor.GetProperty().SetOpacity(0.3)
    
    # Create a renderer which will output the
    # graphics commands onto a drawing surface within
    # a window.  By default the renderer will fill
    # all of the window.  We set the background
    # colour of the window to white.
    return actor

# Create the window for output, setting its
# initial size.
def single_graph(filename):
    outlineActor_G,actor_G = contour_G(filename)
    actor_h2 = multi_con_h2(filename)
    ren1 = vtk.vtkRenderer()
    ren1.AddActor(actor_G)
    ren1.AddActor(actor_h2)
    ren1.AddActor(outlineActor_G)
    ren1.SetBackground(1, 1, 1)#white
    
    # Setting perspective:
#    camera = vtk.vtkCamera()
#    camera.SetPosition(1000,400,1500)
#    camera.SetFocalPoint(0,0,0)
#    
#    ren1.SetActiveCamera(camera)
    return ren1
def create_img(path,filename):
    ren1 = single_graph(path+filename+".vti")
    renWin = vtk.vtkRenderWindow()
  #  renWin.SetSize(500, 500)
    
    renWin.SetOffScreenRendering(1)
    renWin.AddRenderer(ren1)

    renWin.Render()
    
    windowToImageFilter = vtk.vtkWindowToImageFilter()
    windowToImageFilter.SetInput(renWin)
    windowToImageFilter.SetMagnification(3)
    windowToImageFilter.SetInputBufferTypeToRGBA()
    windowToImageFilter.ReadFrontBufferOff()
    windowToImageFilter.Update()
    
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(filename+".png")
    writer.SetInputConnection(windowToImageFilter.GetOutputPort())
    writer.Write()
if __name__ == "__main__":
    create_img("/Users/y1275963/Documents/homework/","multifield.0045")
    create_img("/Users/y1275963/Documents/homework/","multifield.0060")
    create_img("/Users/y1275963/Documents/homework/","multifield.0075")
    create_img("/Users/y1275963/Documents/homework/","multifield.0090")
    create_img("/Users/y1275963/Documents/homework/","multifield.0105")
    create_img("/Users/y1275963/Documents/homework/","multifield.0120")
    create_img("/Users/y1275963/Documents/homework/","multifield.0135")

    

    
    

