import re, queue

class Node :
  def __init__(self) :
    self.neigh

class Graph :
  def __init__(self) :
    self.nr_nodes = 0
    self.nodes = {}
  
  def add_node(self, node) :
    if (node in self.nodes) :
      return False
    else :
      self.nodes[node] = []
      return True
  
  def add_edge(self, u, v) :
    if (v in self.nodes and u in self.nodes) :
      self.nodes[u].append(v)
    else :
      return False

  def bfs(self, target):
    count = 0
    visited = {}

    # set visited for all nodes to false
    for node in self.nodes :
      visited[node] = False

    q = queue.Queue()
    q.put(target)
    
    # do BFS without iterating over already visited nodes
    while not q.empty() :
      curr_node = q.get()

      for neighbour in self.nodes[curr_node] :
        if (not visited[neighbour]) :
          visited[neighbour] = True
          count += 1
          q.put(neighbour)
      
    return count

  # lets hope it is not cyclic... 
  def weighted_dfs(self, target, dependencies):
    count = 0
    if self.nodes[target] == [] :
      return 0
    else :
      for neighbour in self.nodes[target] :
        weight = dependencies[target][neighbour]
        count = count + (weight + weight * self.weighted_dfs(neighbour, dependencies))
      return count

  def print_graph(self) :
    for v in self.nodes :
      print(f"node: {v} edges: {self.nodes[v]}")

def init_graph_task_1(dependencies) :
  g = Graph()
  for i in dependencies :
    g.add_node(i)
    for n in dependencies[i] :
      g.add_node(n)
      g.add_edge(n, i)

  return g

def init_graph_task_2(dependencies) :
  g = Graph()
  for i in dependencies :
    g.add_node(i)
    for n in dependencies[i] :
      g.add_node(n)
      g.add_edge(i, n)

  return g

def task_1(dependencies) :
  target = "shiny gold bag"
  g = init_graph_task_1(dependencies)
  # g.print_graph()
  return g.bfs(target)

def task_2(dependencies) :
  target = "shiny gold bag"
  g = init_graph_task_2(dependencies)
  # g.print_graph()
  return g.weighted_dfs(target, dependencies)

def read_input() :
  dependencies = {}
  with open("input_day_7.txt", 'r') as input_file :
    head_pattern = "[a-z][a-z\s]+bag"
    tail_pattern = "[0-9]+[a-z\s]+bag"
    for line in input_file :
      head = (re.findall(head_pattern, line)[0])
      tail = re.findall(tail_pattern, line)
      curr_dependencies = {}
      for c in tail :
        identifier = (c[2:])
        nr = int(c[0])

        curr_dependencies[identifier] = nr
      dependencies[head] = curr_dependencies
  
  return dependencies

def main() :
  dependencies = read_input()

  print(f"Task 1: {task_1(dependencies)}")
  print(f"Task 2: {task_2(dependencies)}")
  
  return

if __name__ == "__main__":
  main()