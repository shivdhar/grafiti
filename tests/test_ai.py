from grafiti import Graph
from octupy import call_service_anywhere, clause_detection

ip = '172.31.0.111'
port = 12002

g = Graph()

mknode = lambda name, needs: g(make_request, args=[name], needs=needs)

cd = mknode('clause_detection', [])

cc = g(make_request, args=[clause_classification], needs=[cd])

N(clause_detection) << [n(clause_classification)]



cd = lambda contract: call_service_anywhere(ip, port, clause_detection, )
