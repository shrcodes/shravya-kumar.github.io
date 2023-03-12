class Solution(object):
   def canFinish(self, numCourses, prerequisites):
      if len(prerequisites) == 0:
         return True
      visited = [0 for i in range(numCourses)]
      adj_list = self.make_graph(prerequisites)
      for i in range(numCourses):
         if not visited[i]:
            if not self.cycle(adj_list,visited,i):
               return False
      return True
   def cycle(self,adj_list,visited,current_node = 0):
      if visited[current_node] ==-1:
         return False
      if visited[current_node] == 1:
         return True
      visited[current_node] = -1
      if(current_node in adj_list):
         for i in adj_list[current_node]:
            if not self.cycle(adj_list,visited,i):
               return False
      visited[current_node] = 1
      return True
   def make_graph(self,array):
      adj_list = {}
      for i in array:
         if i[1] in adj_list:
            adj_list[i[1]].append(i[0])
         else:
            adj_list[i[1]] = [i[0]]
      return adj_list
ob = Solution()
print(ob.canFinish(2, [[1,0]]))