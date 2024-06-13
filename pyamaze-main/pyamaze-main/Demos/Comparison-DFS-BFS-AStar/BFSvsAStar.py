from BFSDemo import BFS
from aStarDemo import aStar
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

###########################
## Comparison One by One ##

#First Run this for BFS:
m=maze()
m.CreateMaze(loadMaze='maze--2022-07-15--10-26-53.csv')
bsearch,bfspath,fwdpath= BFS(m)


l=textlabel(m,'bfs path length',len(fwdpath)+1)
l=textlabel(m,'bfs search length',len(bsearch)+1)


a=agent(m,footprints=true,color=color.blue,filled=true)
b=agent(m,1,1,footprints=true,color=color.yellow,filled=true,goal=(m.rows,m.cols))
c=agent(m,footprints=true,color=color.red)
m.tracepath({a:bsearch},delay=50)
m.tracepath({b:bfspath},delay=100)
m.tracepath({c:fwdpath},delay=100)

m.run()


# Then run this for A-Star
# m=maze(20,30)
# m.CreateMaze(loadMaze='mazeComparison1.csv')
# aSearch,aPath,fwdPath=aStar(m)

# l=textLabel(m,'A-Star Path Length',len(fwdPath)+1)
# l=textLabel(m,'A-Star Search Length',len(aSearch)+1)

# a=agent(m,footprints=True,color=COLOR.blue,filled=True)
# b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
# c=agent(m,footprints=True,color=COLOR.red)
# m.tracePath({a:aSearch},delay=50)
# m.tracePath({b:aPath},delay=100)

# m.tracePath({c:fwdPath},delay=100)


# m.run()




###########################
## Combined Comparison ##

# myMaze=maze(50,70)
# myMaze.CreateMaze(loadMaze='maze--2022-07-15--10-26-53.csv')
# # myMaze.CreateMaze()
# searchPath,aPath,fwdPath=aStar(myMaze)
# bSearch,bfsPath,fwdBFSPath=BFS(myMaze)

# l=textLabel(myMaze,'A-Star Path Length',len(fwdPath)+1)
# l=textLabel(myMaze,'BFS Path Length',len(fwdBFSPath)+1)
# l=textLabel(myMaze,'A-Star Search Length',len(searchPath)+1)
# l=textLabel(myMaze,'BFS Search Length',len(bSearch)+1)

# a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
# b=agent(myMaze,footprints=True,color=COLOR.yellow)
# myMaze.tracePath({a:fwdBFSPath},delay=50)
# myMaze.tracePath({b:fwdPath},delay=50)

# t1=timeit(stmt='aStar(myMaze)',number=100,globals=globals())
# t2=timeit(stmt='BFS(myMaze)',number=100,globals=globals())

# textLabel(myMaze,'A-Star Time',t1)
# textLabel(myMaze,'BFS Time',t2)


# myMaze.run()