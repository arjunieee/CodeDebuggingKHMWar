from math import gcd
t=int(input())
for _ in range(t):
	n=int(input())#no has been changed to n
	factors=list([0]*n)
	leaves=[]
	parent=list([1]*n)
	queue=[0]
	adj=[]								#Variable has been chaged to adj
	for x in range(n):
		adj.append(input())					#[] has been changed and datatype has been updated variable has been chaged to adj
	for i in range(n-1):
		u,v=map(int ,input().strip().split())			#Indendation corrected
	adj[u-1].append(adj[v-1])					#Indendation corrected and adj has been added
	adj[v-1].append(adj[u-1])					#Indendation corrected and adj has been added
	v=list(map(str,input().strip().split()))
	m=list(map(str,input().strip().split()))
	for i in queue:
		children=set(adj[i])-set([parent[i]])
		if(parent[i]==-1):
			factors[i]=v[i]
		else:
			factors[i]=gcd(factors[parent[i]],v[i])
		if(len(children)<=0):
			leavs.append(i)
		for q in children:
			parent[q]=i
			queue.append(q)					#Indendation Corrected
	sorted(leaves)
	re=[m[i]-gcd(m[i],factors[i]) for i in leaves]
	print(re)							#* has been removed
