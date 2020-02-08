import random
import pandas as pd
import csv

def infect_day(courier_n,resident_n,parcel_n):
    #courier_n=10 #服务于该小区的快递员数量
    #resident_n=1000 #服务于该小区的居民数
    #parcel_n=30 #快递员每人每天投递的包裹数

    #python列表第一个序号为0，简单起见，这里感染的快递员和居民均设为0号
    #简单模型：因居民都在小区隔离，快递员接触人较多，设最开始一个快递员（0号）感染，快递员之间不接触因而不互相传染
    courier=[0 for _ in range(courier_n)]
    courier[0]=1
    #print(courier)

    #目前居民均为健康状态，当居民0号被感染，则程序停止
    resident=[0 for _ in range(resident_n)]

    day=0 #初始状态为0天

    while True:
        day+=1

        #每个快递员每天的投递居民号，单户居民可单个快递员投递多个快递，也可有多个快递员分别投递，也可无快递
        parcel=[[random.randint(0, resident_n-1) for j in range(parcel_n)] for i in range(courier_n)]
        #print(courier)
        #print(courier[1][3])

        for i in range(courier_n):
            if courier[i] == 1:
                for j in range(parcel_n):
                    resident[parcel[i][j]-1]=1 #被传染快递员投递过的居民也会被传染

                    for m in range(courier_n):
                        for n in range(parcel_n):
                            if parcel[m][n]==resident[parcel[i][j]-1]:
                                courier[m]=1 #接触过该居民的快递员也都会被传染

        if resident[0]==1: #当居民0号被感染，则程序停止
            break

    return day

sim_n=10 #模拟次数1000

days_d2d=[] #送货上门0号居民传染天数

courier_n=10 #服务于该小区的快递员数量
resident_n=1000 #服务于该小区的居民数
parcel_n=100 #快递员每人每天投递的包裹数

for i in range(sim_n):
    days_d2d.append(infect_day(courier_n,resident_n,parcel_n))

days_no2d=[] #送货到小区门卫0号居民传染天数

courier_n=1 #服务于该小区的快递员数量，这里功能相当于缩到门卫一人
resident_n=1000 #服务于该小区的居民数
parcel_n=1000 #快递员每人每天投递的包裹数

for i in range(sim_n):
    days_no2d.append(infect_day(courier_n,resident_n,parcel_n))

days=pd.DataFrame(data={
    '送货上门0号居民传染天数':days_d2d,
    '送货到小区门卫0号居民传染天数':days_no2d
})
print(days.describe())
days.to_csv("./infect_days.csv", encoding="utf-8", header=False, index=False)