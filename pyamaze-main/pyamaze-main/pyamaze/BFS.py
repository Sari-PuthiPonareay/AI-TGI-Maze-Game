from pyamaze import maze, agent, textLabel, COLOR
from collections import deque


def bfs(m,start = None):
    if start is None:
        start = (m.rows, m.cols)
    first = deque()
    first.append(start)
    bfsPath = {}
    visit = [start]
    bfssearch = []
    
    while len(first)>0:
        currCell = first.popleft()
        if currCell == m._goal:
            break
        for des in 'ESNW':
            if m.maze_map[currCell][des] == True:
                if des == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif des == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif des == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                elif des == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                if childCell in visit:
                    continue
                first.append(childCell)
                visit.append(childCell)
                bfsPath[childCell] = currCell
                bfssearch.append(childCell)
                
    fwdPath = {}
    cell = m._goal
    while cell != (m.rows, m.cols):
        fwdPath [bfsPath[cell]] = cell
        cell = bfsPath [cell]
    return fwdPath, bfssearch, bfsPath

if __name__ == '__main__':
    
    m = maze()
    m.CreateMaze(loadMaze='maze--2022-07-15--10-53-19.csv',theme= 'light')
    fwdbfsPath, bfssearch, bfsPath = bfs(m)
    a = agent (m, footprints= True,color=COLOR.yellow,shape='square',filled= True)
    b = agent (m,footprints=True, color=COLOR.red,shape='square', filled=False)
    c = agent (m,1,1, footprints= True, color=COLOR.cyan,shape = 'square', filled= True, goal=(m.rows, m.cols))
    m.tracePath({a: bfssearch}, delay = 10)
    m.tracePath({b:fwdbfsPath}, delay = 10)
    m.tracePath({c:bfsPath}, delay = 1000)
    t1 = textLabel(m,'bfsPath',len(bfsPath)+1)
    t2 = textLabel(m,'bfsSearch',len(bfssearch)+1)
    t3 = textLabel(m,'fwdbfsPath',len(fwdbfsPath)+1)
    m.run()