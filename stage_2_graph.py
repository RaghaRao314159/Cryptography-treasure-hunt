import random


#example of an edge: [node1,node2,weight,colour]


def get_connection(x,e_G):
    """
    x: name of node (string)
    
    e_G: set of edges
    function returns all connections of x

    connection: [neighbour, weight, colour=optional]
    
    """
    
    return [[j for j in i if j!= x] for i in e_G if x in i]

    
"""
copleted_pile, concerned_node, progress_list
completed_pile: all nodes that have been analysed   [name of node(str), path to node(str), weight to reach node(number)]
concerned_node: the node previously on top of progress_list
progress_list: [node, route to get to node(string), sum of weights, colour_state] sorted on increasing weights 


individual iteration of djakstra:
1. pick my concerned_node
2. remove concerned_node from progress_list
3. add in all neighbours into progress_list
4. sort all based on increasing weights
5. put concerned_node into completed_pile
"""


def del_rep_progress(progress):
    "deletes already visited nodes to make checking quicker"
    temp_list = []
    for i in progress:
        temp_node = i[0]
        if temp_node not in temp_list:
            temp_list.append(temp_node)
        else:
            progress.remove(i)
    return progress
        

"""
IF NO COLOURS ARE INVOLVED

def one_iteration_nocolour(concerned_node,completed_pile, progress, e_G):
    concerned_node = progress[0]
    progress.remove(concerned_node)
    connections = get_connection(concerned_node[0], e_G)
    for i in connections:
        if i[0] not in completed_pile:
            progress.append([i[0],concerned_node[1]+concerned_node[0]+" , ",concerned_node[2]+i[1]])
    progress.sort(key=lambda x:x[2])
    completed_pile.append(concerned_node[0])
    return (concerned_node,completed_pile,del_rep_progress(progress))

def dijkstra_nocolour(initial,final,e_G):
    concerned_node = []
    completed_pile, progress = [],[[initial,'',0,'']]
    while progress[0][0] != final:
        concerned_node,completed_pile, progress = one_iteration_nocolour(concerned_node,completed_pile, progress, e_G)

    best_route = progress[0][1] + progress[0][0]
    total_weight = progress[0][2]
    return "best route: {}.  Total weigth: {}".format(best_route, total_weight)
"""

def one_iteration(concerned_node,completed_pile, progress, e_G):
    concerned_node = progress[0]
    progress.remove(concerned_node)
    connections = get_connection(concerned_node[0], e_G)
    for i in connections:
        if i[0] not in completed_pile:
            progress.append([i[0],concerned_node[1]+ concerned_node[0]+" , ",concerned_node[2]+i[1]+(lambda x: 2 if x != '' and x!=i[2] else 0)(concerned_node[3]),i[2]])
    progress.sort(key=lambda x:x[2])
    completed_pile.append(concerned_node[0])
    return (concerned_node,completed_pile,del_rep_progress(progress))


def dijkstra(initial,final,e_G):
    concerned_node = []
    completed_pile, progress = [],[[initial,'',0,'']]
    while progress[0][0] != final:
        concerned_node,completed_pile, progress = one_iteration(concerned_node,completed_pile, progress, e_G)

    best_route = progress[0][1] + progress[0][0]
    total_weight = progress[0][2]
    return "best route: {}.  Total weigth: {}".format(best_route, total_weight)
        

#TEST CASE

#edges = [["a","b",5,"blue"],["c","a",3,"green"],["e","d",1,"yellow"],["b","d",2,"blue"],["b","c",4,"yellow"],["c","e",8,"green"]]

    
"""
IF NO COLOURS ARE INVOLVED

e_1 =[["a_1","a_2",10.8],
["a_2","a_3",12.2],
["a_2","a_27",5.6],
["a_3","a_4",10.2],
["a_3","a_28",12.8],
["a_4","a_5",9.9],
["a_5","a_6",14],
["a_5","a_29",8.6],
["a_6","a_7",8.8],
["a_7","a_8",11.8],
["a_7","a_31",8.2],
["a_7","a_29",16.4],
["a_7","a_30",15.8],
["a_30","a_31",8.2],
["a_8","a_9",6.6],
["a_9","a_10",10.8],
["a_9","a_32",9.8],
["a_10","a_32",10.1],
["a_10","a_11",10],
["a_11","a_33",9.1],
["a_11","a_34",7.9],
["a_11","a_12",8.8],
["a_12","a_13",18.8],
["a_12","a_34",13.2],
["a_13","a_14",7.9],
["a_13","a_35",7.2],
["a_14","a_15",8.4],
["a_14","a_36",12.1],
["a_15","a_37",7.9],
["a_15","a_16",7.7],
["a_16","a_17",10.3],
["a_17","a_38",8.1],
["a_17","a_39",13.5],
["a_17","a_18",14.9],
["a_18","a_19",9.2],
["a_18","a_39",0.3],
["a_39","a_40",7.4],
["a_19","a_20",17.8],
["a_19","a_40",11.5],
["a_20","a_40",12.2],
["a_20","a_41",5.9],
["a_20","a_21",11],
["a_21","a_41",11.2],
["a_21","a_42",11.5],
["a_22","a_43",4.8],
["a_22","a_23",8.2],
["a_23","a_51",11.3],
["a_23","a_44",15.1],
["a_23","a_24",12.7],
["a_24","a_25",20.4],
["a_25","a_26",8],
["a_26","a_44",7.2],
["a_26","a_45",14.2],
["a_26","a_27",7.8],
["a_45","a_28",6.8],
["a_45","a_30",13.2],
["a_28","a_29",8.6],
["a_29","a_30",9.8],
["a_30","a_46",8.1],
["a_31","a_32",9.2],
["a_32","a_33",4.1],
["a_33","a_47",7.9],
["a_33","a_48",7.8],
["a_34","a_48",10.8],
["a_34","a_50",4.2],
["a_34","a_35",10.5],
["a_35","a_36",10.5],
["a_36","a_37",15.2],
["a_36","a_42",10.1],
["a_37","a_49",7.9],
["a_38","a_49",9.2],
["a_38","a_39",7.3],
["a_40","a_41",9.3],
["a_40","a_49",8.8],
["a_41","a_42",6],
["a_42","a_49",12.9],
["a_42","a_50",19.8],
["a_42","a_43",9.2],
["a_43","a_51",8.3],
["a_51","a_52",9.7],
["a_44","a_52",7.3],
["a_44","a_53",14.5],
["a_46","a_53",7.2],
["a_46","a_47",9.3],
["a_47","a_53",5.5],
["a_47","a_48",6.5],
["a_48","a_50",12],
["a_50","a_51",11.4],
["a_50","a_52",9.5],
["a_52","a_53",11.8]]

"""

edges = [
['a_1', 'a_2', 10.8, 'blue'],
['a_2', 'a_3', 12.2, 'blue'],
['a_2', 'a_27', 5.6, 'blue'],
['a_3', 'a_4', 10.2, 'red'],
['a_3', 'a_28', 12.8, 'green'],
['a_4', 'a_5', 9.9, 'red'],
['a_5', 'a_6', 14, 'red'],
['a_5', 'a_29', 8.6, 'green'],
['a_6', 'a_7', 8.8, 'blue'],
['a_7', 'a_8', 11.8, 'green'],
['a_7', 'a_31', 8.2, 'yellow'],
['a_7', 'a_29', 16.4, 'yellow'],
['a_7', 'a_30', 15.8, 'red'],
['a_30', 'a_31', 8.2, 'yellow'],
['a_8', 'a_9', 6.6, 'red'],
['a_9', 'a_10', 10.8, 'blue'],
['a_9', 'a_32', 9.8, 'blue'],
['a_10', 'a_32', 10.1, 'red'],
['a_10', 'a_11', 10, 'yellow'],
['a_11', 'a_33', 9.1, 'red'],
['a_11', 'a_34', 7.9, 'yellow'],
['a_11', 'a_12', 8.8, 'yellow'],
['a_12', 'a_13', 18.8, 'green'],
['a_12', 'a_34', 13.2, 'green'],
['a_13', 'a_14', 7.9, 'green'],
['a_13', 'a_35', 7.2, 'green'],
['a_14', 'a_15', 8.4, 'blue'],
['a_14', 'a_36', 12.1, 'green'],
['a_15', 'a_37', 7.9, 'red'],
['a_15', 'a_16', 7.7, 'green'],
['a_16', 'a_17', 10.3, 'green'],
['a_17', 'a_38', 8.1, 'red'],
['a_17', 'a_39', 13.5, 'green'],
['a_17', 'a_18', 14.9, 'yellow'],
['a_18', 'a_19', 9.2, 'yellow'],
['a_18', 'a_39', 0.3, 'red'],
['a_39', 'a_40', 7.4, 'red'],
['a_19', 'a_20', 17.8, 'red'],
['a_19', 'a_40', 11.5, 'yellow'],
['a_20', 'a_40', 12.2, 'green'],
['a_20', 'a_41', 5.9, 'yellow'],
['a_20', 'a_21', 11, 'yellow'],
['a_21', 'a_41', 11.2, 'green'],
['a_21', 'a_42', 11.5, 'yellow'],
['a_22', 'a_43', 4.8, 'red'],
['a_22', 'a_23', 8.2, 'yellow'],
['a_23', 'a_51', 11.3, 'red'],
['a_23', 'a_44', 15.1, 'yellow'],
['a_23', 'a_24', 12.7, 'yellow'],
['a_24', 'a_25', 20.4, 'red'],
['a_25', 'a_26', 8, 'yellow'],
['a_26', 'a_44', 7.2, 'yellow'],
['a_26', 'a_45', 14.2, 'green'],
['a_26', 'a_27', 7.8, 'red'],
['a_45', 'a_28', 6.8, 'green'],
['a_45', 'a_30', 13.2, 'red'],
['a_28', 'a_29', 8.6, 'yellow'],
['a_29', 'a_30', 9.8, 'red'],
['a_30', 'a_46', 8.1, 'red'],
['a_31', 'a_32', 9.2, 'yellow'],
['a_32', 'a_33', 4.1, 'red'],
['a_33', 'a_47', 7.9, 'green'],
['a_33', 'a_48', 7.8, 'yellow'],
['a_34', 'a_48', 10.8, 'red'],
['a_34', 'a_50', 4.2, 'blue'],
['a_34', 'a_35', 10.5, 'red'],
['a_35', 'a_36', 10.5, 'blue'],
['a_36', 'a_37', 15.2, 'green'],
['a_36', 'a_42', 10.1, 'blue'],
['a_37', 'a_49', 7.9, 'blue'],
['a_38', 'a_49', 9.2, 'blue'],
['a_38', 'a_39', 7.3, 'red'],
['a_40', 'a_41', 9.3, 'green'],
['a_40', 'a_49', 8.8, 'blue'],
['a_41', 'a_42', 6, 'green'],
['a_42', 'a_49', 12.9, 'red'],
['a_42', 'a_50', 19.8, 'green'],
['a_42', 'a_43', 9.2, 'green'],
['a_43', 'a_51', 8.3, 'blue'],
['a_51', 'a_52', 9.7, 'yellow'],
['a_44', 'a_52', 7.3, 'blue'],
['a_44', 'a_53', 14.5, 'blue'],
['a_46', 'a_53', 7.2, 'red'],
['a_46', 'a_47', 9.3, 'red'],
['a_47', 'a_53', 5.5, 'green'],
['a_47', 'a_48', 6.5, 'green'],
['a_48', 'a_50', 12, 'blue'],
['a_50', 'a_51', 11.4, 'blue'],
['a_50', 'a_52', 9.5, 'blue'],
['a_52', 'a_53', 11.8, 'blue']]



"""
Gives all the INITIAL-FINAL pairs where colour MAKES A DIFFERENCE

lissy = []
for i in range(1,52):
    for j in range(1,52):
        if j>i:
            aa = dijkstra_nocolour('a_{}'.format(i),'a_{}'.format(j),e_1)
            bb = dijkstra('a_{}'.format(i),'a_{}'.format(j),e_2)
            if aa != bb:
               lissy.append([i,j,len(bb.split(" , "))])

lissy.sort(reverse = True, key = lambda x: x[-1])

print(lissy)
"""


print(dijkstra('a_4','a_18',edges))


# ANSWER: best route: a_4 , a_3 , a_2 , a_27 , a_26 , a_44 , a_52 , a_50 , a_42 , a_41 , a_40 , a_39 , a_18.  Total weigth: 114.6



#[4,3,2,2,1,4,2,0,2,1,0,4,3]













