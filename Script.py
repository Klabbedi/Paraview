import vtk

f = open('c:/tmp/Example-2.csv')

pd = vtk.vtkPolyData()
points = vtk.vtkPoints()
cells = vtk.vtkCellArray()
connectivity = vtk.vtkIntArray()
connectivity.SetName('Connectivity')
stress = vtk.vtkFloatArray()
stress.SetName('Stress')

line = f.readline()
for line in iter(lambda: f.readline(), ""):
    if 'Faces' in line:
        break
    v = line.split(',')
    points.InsertNextPoint(float(v[1]),
                           float(v[2]),
                           float(v[3]))
    stress.InsertNextTuple1(float(v[5]))
    connectivity.InsertNextTuple1(float(v[4]))

for line in iter(lambda: f.readline(), ""):
    v = line.split(',')
    cell = vtk.vtkTriangle()
    Ids = cell.GetPointIds()
    for kId in range(len(v)):
        Ids.SetId(kId,int(v[kId]))
    cells.InsertNextCell(cell)
f.close()

pd.SetPoints(points)
pd.SetPolys(cells)
pd.GetPointData().AddArray(stress)
pd.GetPointData().AddArray(connectivity)

writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName('c:/tmp/Example-2.vtp')
writer.SetInputData(pd)

writer.Write()
