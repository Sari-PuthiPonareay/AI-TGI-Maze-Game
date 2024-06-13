from BFS import bfs
from a_star import aStarcl
from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit

mMaze = maze()
mMaze.CreateMaze(loadMaze='maze--2022-07-15--10-53-19.csv',theme= 'light')
fwdbfsPath, bfssearch, bfsPath = bfs(mMaze)
asearchPath,aPath,fwdaPath = aStar(mMaze)

t1 = textLabel (mMaze, 'a* Path Length',len(fwdaPath)+1)
t2 = textLabel (mMaze, 'BFS Path Lenght', len (fwdbfsPath)+1)
t3 = textLabel (mMaze, 'a* Search', len(asearchPath)+1)
t4 = textLabel (mMaze, 'BFS Search',len(bfssearch)+1)

a = agent (mMaze, footprints=True, color=COLOR.cyan, filled = True)
b = agent (mMaze, footprints=True, color=COLOR.yellow)
mMaze.tracePath({a:fwdbfsPath},delay = 10)
mMaze.tracePath({b:fwdaPath},delay = 10)

time1 = timeit(stmt='aStar (mMaze)', number=1000,globals=globals())
time2 = timeit(stmt='bfs (mMaze)', number=1000,globals=globals())

textLabel(mMaze,' A- Star Time',time1)
textLabel(mMaze,'bfs Time', time2)


mMaze.run()
