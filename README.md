# Astar Path Planning Algorithm for 3D point cloud
Here A* algorithm of path planning is used for generating optimum path for a given 3d Point cloud. 

Here pyvista is used for 3d point cloud visualization. 

So, install the required python modules:
* Numpy
* pyvista
## Files and its functions:
* odm_georeferenced_model.csv contains point cloud information - X,Y,Z values of about 22 lakhs points
* astar_algo_lib.py contains the A* algorithm code
* 3d_with_sphere_widget.py is the main file that combines all other files.

## Run the file.
First clone the repository:
```
git clone https://github.com/pongthang/astar_path_planning_3d_pc.git
```
Then run it.
```
cd astar_path_planning_3d_pc
python3 3d_with_sphere_widget.py
```

## Result:
The output of the above should be something like this.

<img src="https://github.com/pongthang/astar_path_planning_3d_pc/assets/57061570/4f8e484a-5e20-4fc9-b06b-4055ebb6ec5d" alt="My Image" width="750" height="400">

* There will two shperes - green one is for starting point and blue one is the endpoint.
* Move the two shperes apart such that they both touch the points in the point cloud.
* Click the checkbox and it will start the path finding.
* Wait for sometimes and you will get the generated path.
Then you will see the generated path.
<img src="https://github.com/pongthang/astar_path_planning_3d_pc/assets/57061570/f0794cf2-143c-401b-aa7b-a1ba622e0897" alt="My Image" width="750" height="400">

## Theory

![Astar_progress_animation](https://github.com/pongthang/astar_path_planning_3d_pc/assets/57061570/abe20f70-6042-49ee-9bf2-ef0e1235e8ac)

Astar is an algorithm that finds points when connected gives the minimum distance from the source and the destination. It works well for 2d map where there is binary map. Binary map means obstacle and free path can be represented as 0 and 1. So astar alogrithm will apply only in free path. 

<img src="https://github.com/pongthang/astar_path_planning_3d_pc/assets/57061570/93105832-ac41-488c-a10f-6fd5fdafbf93" alt="My Image" width="750" height="400">

## Need Extra effort for 3d:
** Point cloud data is not in matrix form so to apply astar algorithm we need to convert the point cloud data to matrix form first. So the pre-processing of point cloud data is done by "pc_accessories.py".

The above astart algorithm will not work with 3d data points as you can decide a point is obstacle or not according to its height. It should depends on slope. If the slope of a path is steady - not steep then it should be considered as free path. So A new definitions of obstacle and cost are implemented.

<img src="https://github.com/pongthang/astar_path_planning_3d_pc/assets/57061570/0677abc2-401a-4023-9c86-56c53a31ffce" alt="My Image" width="750" height="400">

In the above diagram , Node means a point in 3d point cloud. So, Node has three properties - position coordinates x,y and height. 





