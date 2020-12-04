from grafiti import Graph

g = Graph()

cd = g(make_request, args=[clause_detection], needs=[])
cc = g(make_request, args=[clause_classification], needs=[cd])


