import numpy as np
import pyvista as pv
from time import sleep
from astar_algo_lib import search
from pc_accessories import path_tiles,from_point_indexes,from_index_point

# NumPy array with shape (n_points, 3)
# points = np.genfromtxt('odm_georeferenced_model.csv', delimiter=",", dtype=np.float32)

points_old = np.loadtxt("odm_georeferenced_model.csv",
                 delimiter=",", dtype=str)


######

# Here is the data processing starts
# First the data points
points_old=points_old[1:]

def data_name(n):
    return n[:-2]+"50"

func_data = np.vectorize(data_name)

points = func_data(points_old)

points[:,2] = points_old[:,2] 

points = points.astype('float32')

points = points[np.lexsort((points[:,1],points[:,0]))]

## The points are sorted and converted into float 
#############

indexes_mat = [] # 2d list containing the indices of the points
for i,data in enumerate(points):
    if len(indexes_mat) == 0:
        indexes_mat.append([i])
    else:
#         print(data[0])
        if data[0] == points[indexes_mat[-1][0]][0]:
            indexes_mat[-1].append(i)
        else:
            indexes_mat.append([i])

max_=0
for row in indexes_mat:
    if max_<len(row):
        max_=len(row)
    else:
        max_=max_ # maximum number of element in a row

algo_mat = np.empty(shape=(len(indexes_mat),max_))

#algo_mat.fill(1)
algo_mat.fill(-100)

point_cloud = pv.PolyData(points)
p = pv.Plotter()

start_corr=[0,0,0]
end_corr = [0,0,0]

#This is the callback function that will be called when the spheres are moved
def callback(point,i):

    global start_corr
    global end_corr
    print(point)
    print(i)
    if i==0:
        start_corr = point
    elif i==1:
        end_corr = point




def toggle(flag):

    global algo_mat
    global indexes_mat
    global start_corr
    global end_corr
    global points

    
    if flag:
        algo_mat = path_tiles(indexes_mat,points,algo_mat)
    
        start = from_point_indexes(points,start_corr,indexes_mat)
        end =  from_point_indexes(points,end_corr,indexes_mat)
        cost=1 # cost per movement
        result,path = search(algo_mat,cost, start, end)
        path_index_list = [i for i in range(len(path))]
        
        # selected_points = np.random.choice(path_index_list,int(len(path)/3))
        
        for i,point in enumerate(path_index_list):
            if i%10==0:
                point_= from_index_point(points,path[point],indexes_mat)
                sphere = pv.Sphere(center=point_,radius=1)
                p.add_mesh(sphere,color="yellow")
            else:
                continue
                    
        # print(path)



start_end = [points[1],points[1000]]

colors = ["#0bf707","#f71707"]


p.add_sphere_widget(callback, center=start_end,color=colors,radius=2)
p.add_checkbox_button_widget(toggle,value=False)

p.add_mesh(point_cloud, opacity=0.1, name='data',scalars=points[:,2],
    lighting=False,)


p.show()