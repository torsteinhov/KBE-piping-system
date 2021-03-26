import math
import random
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

from drawGivenInfo import drawGivenInfo
num_eq = 3
eq_size_list = [[70,70,70],[150,150,150],[1000,1000,1000]]
eq_pos = [[50,50,50],[150,150,150], [1000,1000,1000]]
env_size = [3000,3000,3000]
eq_in_out = [[0,35,35], [70,35,35],[0,75,75],[150,75,75],[0,500,500],[1000,500,500]]
startPoint = [0,1500,1500]
endPoint = [3000, 1500,1500]
pipeDia =  50.8
# def __init__(self, num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: int, startPoint, endPoint, pipeDia: float):
#custommer = drawGivenInfo([num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, pipeDia])
#custommer.run_model()

theSession  = NXOpen.Session.GetSession()
workPart = theSession.Parts.Work
theSession.ExecutingJournal(drawGivenInfo, drawGivenInfo, run_model(), [num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, pipeDia])


