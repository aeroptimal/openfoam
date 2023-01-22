# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
import sys

loadPath = sys.argv[1] 

# create a new 'OpenFOAMReader'
casefoam = OpenFOAMReader(FileName=loadPath + '/case.foam')
casefoam.MeshRegions = ['internalMesh']
casefoam.CellArrays = ['U', 'ddt0(k)', 'ddt0(omega)', 'k', 'k_0', 'nut', 'omega', 'omega_0', 'p']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on casefoam
casefoam.MeshRegions = ['frontAndBack']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [902, 674]

# show data in view
casefoamDisplay = Show(casefoam, renderView1)

# trace defaults for the display properties.
casefoamDisplay.Representation = 'Surface'
casefoamDisplay.AmbientColor = [0.0, 0.0, 0.0]
casefoamDisplay.ColorArrayName = [None, '']
casefoamDisplay.DiffuseColor = [0.0, 0.0, 0.0]
casefoamDisplay.EdgeColor = [0.0, 0.0, 0.0]
casefoamDisplay.BackfaceDiffuseColor = [0.0, 0.0, 0.0]
casefoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
casefoamDisplay.SelectOrientationVectors = 'None'
casefoamDisplay.ScaleFactor = 3.35
casefoamDisplay.SelectScaleArray = 'None'
casefoamDisplay.GlyphType = 'Arrow'
casefoamDisplay.GlyphTableIndexArray = 'None'
casefoamDisplay.GaussianRadius = 0.1675
casefoamDisplay.SetScaleArray = [None, '']
casefoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
casefoamDisplay.OpacityArray = [None, '']
casefoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
casefoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
casefoamDisplay.SelectionCellLabelFontFile = ''
casefoamDisplay.SelectionPointLabelFontFile = ''
casefoamDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
casefoamDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
casefoamDisplay.DataAxesGrid.XTitleFontFile = ''
casefoamDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
casefoamDisplay.DataAxesGrid.YTitleFontFile = ''
casefoamDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
casefoamDisplay.DataAxesGrid.ZTitleFontFile = ''
casefoamDisplay.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
casefoamDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
casefoamDisplay.DataAxesGrid.XLabelFontFile = ''
casefoamDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
casefoamDisplay.DataAxesGrid.YLabelFontFile = ''
casefoamDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
casefoamDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
casefoamDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
casefoamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
casefoamDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
casefoamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
casefoamDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
casefoamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
casefoamDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
casefoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4.25, 0.0, 10000.0]
renderView1.CameraFocalPoint = [4.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# change representation type
casefoamDisplay.SetRepresentationType('Wireframe')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4.25, 0.0, 10000.0]
renderView1.CameraFocalPoint = [4.25, 0.0, 0.0]
renderView1.CameraParallelScale = 14.275022067158565

# save screenshot
SaveScreenshot(loadPath + '/lejana.png', renderView1, ImageResolution=[640, 480])

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.43540159792227895, 0.003525441532139198, 80.75163016016904]
renderView1.CameraFocalPoint = [0.43540159792227895, 0.003525441532139198, 0.0]
renderView1.CameraParallelScale = 0.6785925569193711

# save screenshot
SaveScreenshot(loadPath+'/cercana.png', renderView1, ImageResolution=[640, 480])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.43540159792227895, 0.003525441532139198, 80.75163016016904]
renderView1.CameraFocalPoint = [0.43540159792227895, 0.003525441532139198, 0.0]
renderView1.CameraParallelScale = 0.6785925569193711

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).