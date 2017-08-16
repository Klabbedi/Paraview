import vtk

f = open('C:/tmp/Example-2.csv')

pd = vtk.vtkPolyData()
points = vtk.vtkPoints()
cells = vtk.vtkCellArray()
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

for line in iter(lambda: f.readline(), ""):
    v = line.split(',')
    cell = vtk.vtkTriangle()
    Ids = cell.GetPointIds()
    for kId in range(len(v)-1):
        Ids.InsertNextId(int(v[kId+1])-1)
    cells.InsertNextCell(cell)
f.close()

pd.SetPoints(points)
pd.SetPolys(cells)
pd.GetPointData().AddArray(stress)

writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName('C:/tmp/example.vtp')
writer.SetInputData(pd)

writer.Write()