class Graph:
    def __init__(self, num_of_nodes):
        self.m_v = num_of_nodes
        self.m_edges = []
        self.m_component = {}
    def add_edge(self, u, v, weight):
        self.m_edges.append([u, v, weight])
    def find_component(self, u):
        if self.m_component[u] == u:
            return u
        return self.find_component(self.m_component[u])

    def set_component(self, u):
        if self.m_component[u] == u:
            return
        else:
            for k in self.m_component.keys():
                self.m_component[k] = self.find_component(k)
    def union(self, component_size, u, v):
        if component_size[u] <= component_size[v]:
            self.m_component[u] = v
            component_size[v] += component_size[u]
            self.set_component(u)

        elif component_size[u] >= component_size[v]:
            self.m_component[v] = self.find_component(u)
            component_size[u] += component_size[v]
            self.set_component(v)

    def boruvka(self):
        component_size = []
        mst_weight = 0

        minimum_weight_edge = [-1] * self.m_v

        for node in range(self.m_v):
            self.m_component.update({node: node})
            component_size.append(1)

        num_of_components = self.m_v

        print("MST: ")
        while num_of_components > 1:
            for i in range(len(self.m_edges)):

                u = self.m_edges[i][0]
                v = self.m_edges[i][1]
                w = self.m_edges[i][2]

                u_component = self.m_component[u]
                v_component = self.m_component[v]

                if u_component != v_component:
                    if minimum_weight_edge[u_component] == -1 or minimum_weight_edge[u_component][2] > w:
                        minimum_weight_edge[u_component] = [u, v, w]
                    if minimum_weight_edge[v_component] == -1 or minimum_weight_edge[v_component][2] > w:
                        minimum_weight_edge[v_component] = [u, v, w]

            for node in range(self.m_v):
                if minimum_weight_edge[node] != -1:
                    u = minimum_weight_edge[node][0]
                    v = minimum_weight_edge[node][1]
                    w = minimum_weight_edge[node][2]

                    u_component = self.m_component[u]
                    v_component = self.m_component[v]

                    if u_component != v_component:
                        mst_weight += w
                        self.union(component_size, u_component, v_component)
                        print("Added edge [" + str(u) + " - "
                              + str(v) + "]\n"
                              + "Added weight: " + str(w) + "\n")
                        num_of_components -= 1

            minimum_weight_edge = [-1] * self.m_v
        print("The total weight of the MST is: " + str(mst_weight))

print("Number of nodes = ")
n = int(input())
g = Graph(n)

f = open('inp3.txt','r')
for row in f:
    row = row.split(' ')
    n1,n2,w = int(row[0]), int(row[1]), int(row[2])
    g.add_edge(n1,n2,w)

g.boruvka()
print("Memory: ",tracemalloc.get_traced_memory())
print("time taken: ",(time.time()-start_time))