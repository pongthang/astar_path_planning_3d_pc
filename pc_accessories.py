def path_tiles(index_mat,ref_list,algo_mat):
    for i in range(len(index_mat)):
        for j in range(len(index_mat[i])):
            
            # if abs(thr_height-ref_list[index_mat[i][j]][2])<=varr_height:
            #     algo_mat[i,j] = 0
            # else:
            #     continue
            algo_mat[i,j] = ref_list[index_mat[i][j]][2]
    return algo_mat


def from_point_indexes(ref_mat,point,index_mat):
    req_index = 0
    for i, p in enumerate(ref_mat):
        if abs(p[0]-point[0])+abs(p[1]-point[1]) < 5:
            req_index=i
            break
    for r,_ in enumerate(index_mat):
        for c,value in enumerate(_):
            if value==req_index:
                return [r,c]
            else:
                continue
        
def from_index_point(ref_mat,index,index_mat):
    value = index_mat[index[0]][index[1]]
    return ref_mat[value]

def calcu_cost(point1,point2,fixed_cost,algo_matrix):

    return fixed_cost+((algo_matrix[point1[0],point1[1]] - algo_matrix[point2[0],point2[1]]))**2

