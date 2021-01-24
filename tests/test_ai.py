from grafiti import Graph

g = Graph()

mknode = lambda name, needs: g(make_request, args=[name], needs=needs)

cd = mknode('clause_detection', [])

cc = g(make_request, args=[clause_classification], needs=[cd])

N(clause_detection) << [n(clause_classification)]
