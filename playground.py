import pyvista as pv


p = pv.Plotter()

sphere = pv.Sphere(radius=1)
p.add_mesh(sphere,color="yellow")    
p.show()