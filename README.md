# astar_path_planning_3d_pc
Here A* algorithm of path planning is used for generating optimum path for a given 3d Point cloud. 

Here pyvista is used for 3d point cloud visualization. 

So, install the required modules:
* Numpy
* pyvista

* odm_georeferenced_model.csv contains point cloud information - X,Y,Z values of about 22 lakhs points
* astar_algo_lib.py contains the A* algorithm code
* 3d_with_sphere_widget.py is the main file that combines all other files.

# Run the file.
python3 3d_with_sphere_widget.py

* There will two shperes - green one is for starting point and blue one is the endpoint.
* Click the checkbox and it will start the path finding.
* Wait for sometimes and you will get the generated path.
