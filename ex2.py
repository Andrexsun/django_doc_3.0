##############insertion_sort###########
# def insertion_sort(arr):
#     for i in range(len(arr)):
#         cursor = arr[i]
#         pos = i
#         while pos > 0 and arr[pos - 1] > cursor:
#             # Меняем местами число, продвигая по списку
#             arr[pos] = arr[pos - 1]
#             pos = pos - 1
#         # Остановимся и сделаем последний обмен
#         arr[pos] = cursor
#
#     return arr
#
#
# a = [22,11,55,33,44,22]
# print(insertion_sort(a))


############Graph algorithm###########
a, b, c, d, e, f, g, h = range(8)
N = [
   {b, c, d, e, f}, # a
   {c, e}, # b
   {d}, # c
   {e}, # d
   {f}, # e
   {c, g, h}, # f
   {f, h}, # g
   {f, g} # h
]


from queue import Queue

letters="abcdefgh"
visited_nodes={}

queue=Queue()
beg_node=a
target_node=h

# 1.
queue.put(beg_node)
visited_nodes={beg_node}

while True:
   # 2.

   u=queue.get()
   print("Let'us round the node:", letters[u])
   print(u, "u")

   #
   if u==target_node:
      print("Search is successfully finished.")
      break
   else:
      #
      for node in N[u]:
         print(node, "node here")
         #print(N[u], "{} is here".format(N[u]))
         #print(" -- Look at the edge.", letters[node])
         if not(node in visited_nodes):
            visited_nodes.add(node)
            print("   ---- Node", letters[node], "is added in queue")
            queue.put(node)



   # 3.
   if queue.empty():
      print("Top node",letters[u]," not found!(")

   # 4. 2.