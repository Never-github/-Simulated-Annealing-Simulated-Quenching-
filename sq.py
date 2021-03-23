import numpy as np
'''
question:
One of the traps we will encounter in the Pyramid is located in the Large Room. 
A lot of small holes are drilled into the floor. They look completely harmless at the first sight. 
But when activated, they start to throw out very hot java, uh ... pardon, lava. Unfortunately, all known paths to the Center Room (where the Sarcophagus is) contain a trigger that activates the trap.
 The ACM were not able to avoid that. But they have carefully monitored the positions of all the holes. 
 So it is important to find the place in the Large Room that has the maximal distance from all the holes. This place is the safest in the entire room and the archaeologist has to hide there.

input:The input consists of T test cases. The number of them (T) is given on the first line of the input file. 
Each test case begins with a line containing three integers X, Y, M separated by space. 
The numbers satisfy conditions: 1 <= X,Y <=10000, 1 <= M <= 1000. The numbers X and Yindicate the dimensions of the Large Room which has a rectangular shape. 
The number M stands for the number of holes. Then exactly M lines follow, each containing two integer numbers Ui and Vi (0 <= Ui <= X, 0 <= Vi <= Y) indicating the coordinates of one hole. There may be several holes at the same position.

output:Print exactly one line for each test case. The line should contain the sentence "The safest point is (P, Q)." 
where P and Qare the coordinates of the point in the room that has the maximum distance from the nearest hole, rounded to the nearest number with exactly one digit after the decimal point (0.05 rounds up to 0.1).

solution: Simulated quenching algorithm
'''

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_mindis( x, y):
    mindis = np.inf
    for i in range(n):
        temp = np.sqrt((x-n_points[i].x)*(x-n_points[i].x)+(y-n_points[i].y)*(y-n_points[i].y))
        if temp < mindis:
            mindis = temp
    return mindis

def get_best_dis():
    temp = -np.inf
    for i in range(m):
        if temp < mindis_m[i]:
            temp = mindis_m[i]
            index = i
    return index,temp

h = 100
w = 100
n = 30
n_points = [] # n个点
for i in range(n):
    x = np.random.rand()*w
    y = np.random.rand()*h
    n_points.append(Point(x,y))

m = 30
m_origin_points = [] # m个初始解
mindis_m = []
for i in range(m):
    x = np.random.rand()*w
    y = np.random.rand()*h
    m_origin_points.append(Point(x,y))

for i in range(m):
    mindis_m.append(get_mindis(m_origin_points[i].x,m_origin_points[i].y))

T = (w)/np.sqrt(1.0*n) if w > h else (h)/np.sqrt(1.0*n)

min_T = 1e-8
k = 100 # 内循环次数
time = 0
while(T>min_T):
    for i in range(m):
        for j in range(k):
            theta = np.random.rand()*np.pi*2
            temp_x = m_origin_points[i].x + T*np.cos(theta)
            temp_y = m_origin_points[i].y + T*np.sin(theta)
            if (temp_x < 0 or temp_x > w or temp_y < 0 or temp_y > h):
                continue
            temp = get_mindis(temp_x,temp_y)
            if(temp > mindis_m[i]):
                m_origin_points[i].x = temp_x
                m_origin_points[i].y = temp_y
                mindis_m[i] = temp
            else:
                p = np.exp((temp - mindis_m[i])/T)
                r = np.random.rand()
                if (r < p):
                    m_origin_points[i].x = temp_x
                    m_origin_points[i].y = temp_y
                    mindis_m[i] = temp
    time = time + 1
    print(time,T,get_best_dis())
    T = 0.8 * T
i,dis = get_best_dis()
print("最佳点为第",i,"个点","位置在","(",m_origin_points[i].x,m_origin_points[i].y,")")
print("距离为",dis)