#Part 1 Open Traverse Computation
print("This program calculates the coordinates in open traverse serie")
print("----------------------------------------------------------------------------")
import math
a_523 = input("Enter the point ID of first known point                   : ")
y1_523 = float(input("Enter the Y coordinates of first known point (m)   : "))
x1_523 = float(input("Enter the X coordinates of first known point (m)   : "))
b_523 = input("Enter the point ID of second known point                  : ")
y2_523 = float(input("Enter the Y coordinates of second known point (m)  : "))
x2_523 = float(input("Enter the X coordinates of second known point (m)  : "))
point3_523 = input("Enter the number of unknown traverse points          : ")
p1_523 = float(input("Enter the point ID of unknown point 1              : "))
p2_523 = float(input("Enter the point ID of unknown point 2              : "))
p3_523 = float(input("Enter the point ID of unknown point 3              : "))
gradb_523 = float(input("Enter the traverse angle of B (grad)            : "))
grad1_523 = float(input("Enter the traverse angle of 1 (grad)            : "))
grad2_523 = float(input("Enter the traverse angle of 2 (grad)            : "))
radb_523 = float(gradb_523*((math.pi)/200))
rad1_523 = float(grad1_523*((math.pi)/200))
rad2_523 = float(grad2_523*((math.pi)/200))
distb1_523 = float(input("Enter a horizontal distance between B and 1 (m): "))
dist12_523 = float(input("Enter a horizontal distance between 1 and 2 (m): "))
dist23_523 = float(input("Enter a horizontal distance between 2 and 3 (m): "))

if x1_523 == x2_523 and y1_523>y2_523:
    azimuthab_523 = 300
elif x1_523==x2_523 and y1_523<y2_523:
    azimuthab_523 = 100
elif y1_523==y2_523 and x1_523>x2_523:
    azimuthab_523 = 200
elif y1_523==y2_523 and x1_523<x2_523:
    azimuthab_523=0
else:
    azimuthab_523=(math.atan(abs(y2_523 - y1_523)/abs(x2_523 - x1_523))*200/math.pi)
if (y2_523 - y1_523)>0 and (x2_523-x1_523)>0:
    azimuthab_523 = azimuthab_523
elif (y2_523 - y1_523 )>0 and (x2_523 - x1_523)<0:
    azimuthab_523 = 200 - azimuthab_523
elif (y2_523 - y1_523)<0 and (x2_523 - x1_523)<0:
    azimuthab_523 = 200 + azimuthab_523
elif (y2_523 - y1_523)<0 and (x2_523 - x1_523)>0:
    azimuthab_523 = 400 - azimuthab_523


azimuthb1_523 = azimuthab_523 + gradb_523
if azimuthb1_523 > 200:
    azimuthb1_523 = azimuthb1_523 - 200
elif azimuthb1_523 < 200:
    azimuthb1_523 = azimuthb1_523 + 200
elif azimuthb1_523 > 600:
    azimuthb1_523 = azimuthb1_523 - 400

    
azimuth12_523 = azimuthb1_523 + grad1_523
if azimuth12_523 > 200:
    azimuth12_523 = azimuth12_523 - 200
elif azimuth12_523 < 200:
    azimuth12_523 = azimuth12_523 + 200
elif azimuth12_523 > 600:
    azimuth12_523 = azimuth12_523 - 400


azimuth23_523 = azimuth12_523 + grad2_523
if azimuth23_523 > 200:
    azimuth23_523 = azimuth23_523 - 200
elif azimuth23_523 < 200:
    azimuth23_523 = azimuth23_523 + 200
elif azimuth23_523 > 600:
    azimuth23_523 = azimuth23_523 - 400


deltayb1_523 = math.sin((azimuthb1_523*(math.pi)/200))*distb1_523
deltay12_523 = math.sin((azimuth12_523*(math.pi)/200))*dist12_523
deltay23_523 = math.sin((azimuth23_523*(math.pi)/200))*dist23_523

deltaxb1_523 = math.cos((azimuthb1_523*(math.pi)/200))*distb1_523
deltax12_523 = math.cos((azimuth12_523*(math.pi)/200))*dist12_523
deltax23_523 = math.cos((azimuth23_523*(math.pi)/200))*dist23_523

print("Point ID  \tPoint ID \tAzimuth \tDelta Y  \tDelta X")
print("-------------------------------------------------------------------------------")
print(a_523, b_523 , format(azimuthab_523, ".4f") , sep="               ")
print(b_523, p1_523, format(azimuthb1_523,".4f"),  format(deltayb1_523, ".2f"), format(deltaxb1_523,".2f"),sep="              ")
print(p1_523, p2_523, format(azimuth12_523, ".4f"), format(deltay12_523, ".2f"), format(deltax12_523, ".2f"),sep="             ")
print(p2_523, p3_523, format(azimuth23_523, ".4f"), format(deltay23_523, ".2f"), format(deltax23_523, ".2f"),sep="             ")

p1y_523 = y2_523 + deltayb1_523
p2y_523 = p1y_523 + deltay12_523
p3y_523 = p2y_523 + deltay23_523

p1x_523 = x2_523 + deltaxb1_523
p2x_523 = p1x_523 + deltax12_523
p3x_523 = p2x_523 + deltax23_523

print("-------------------------------------------------------------------------------")

print("Point ID  \tCoordinate(Y)    \tCoordinate(X)")
print("-------------------------------------------------------------------------------")
print(p1_523, format(p1y_523,".2f"), format(p1x_523,".2f"),sep="                ")
print(p2_523, format(p2y_523,".2f"), format(p2x_523,".2f"),sep="                ")
print(p3_523, format(p3y_523,".2f"), format(p3x_523,".2f"),sep="                ")



#Part 2 Open Levelling Net Computation
print("This program calculates the elevations in open levelling net")
pa_523 = input("Enter the point ID of known point                   : ")
eleva_523 = float(input("Enter the elevation of point %s (m)        : " %pa_523))
unk_523 = int(input("Enter the number of unknown points             : " ))

list_523 = []

for i in range(1, unk_523+1):
    unkn_523 = input("Enter the point ID of unknown point {}: ".format(i))
    list_523.append(unkn_523)


bsa_523 = float(input("Enter the BS reading of point %s (m)        : " %pa_523))
fsb_523 = float(input("Enter the FS reading of point {} (m)        : ".format(list_523[0])))
bsb_523 = float(input("Enter the BS reading of point {} (m)        : ".format(list_523[0])))
fs1_523 = float(input("Enter the FS reading of point {} (m)        : ".format(list_523[1])))
bs1_523 = float(input("Enter the BS reading of point {} (m)        : ".format(list_523[1])))
fs2_523 = float(input("Enter the FS reading of point {} (m)        : ".format(list_523[2])))
bs2_523 = float(input("Enter the BS reading of point {} (m)        : ".format(list_523[2])))
fs3_523 = float(input("Enter the FS reading of point {} (m)        : ".format(list_523[3])))

deltahab_523 = bsa_523 - fsb_523
deltahb1_523 = bsb_523 - fs1_523
deltah12_523 = bs1_523 - fs2_523
deltah23_523 = bs2_523 - fs3_523

hb_523 = eleva_523 + deltahab_523
h1_523 = hb_523 + deltahb1_523
h2_523 = h1_523 + deltah12_523
h3_523 = h2_523 + deltah23_523

print("Point ID  \tPoint ID    \tDelta H")
print("--------------------------------------------------------------------------------")
print(pa_523, list_523[0], format(deltahab_523,".3f"),sep="                ")
print(list_523[0], list_523[1], format(deltahb1_523,".3f"),sep="                ")
print(list_523[1], list_523[2], format(deltah12_523,".3f"),sep="                ")
print(list_523[2], list_523[3], format(deltah23_523,".3f"),sep="                ")
print("--------------------------------------------------------------------------------")
print("Point ID \tElevation")
print("-------------------------------------")
print(list_523[0], format(hb_523,".3f"),sep="                ")
print(list_523[1], format(h1_523,".3f"),sep="                ")
print(list_523[2], format(h2_523,".3f"),sep="                ")
print(list_523[3], format(h3_523,".3f"),sep="                ")
print("-------------------------------------")

#Part 3 Electrometric Tacheometry Computation
import math
print("Program for Electrometric Tacheometry Computation")
print("---------------------------------------------------------------------------")
p102_523 = input("Enter the stationary traverse ID                              : ")
p101_523 = input("Enter the referenced traverse ID                              : ")
p101y_523 = float(input("Enter the Y coordinates of {} (m)                      :".format(p101_523)))
p101x_523 = float(input("Enter the X coordinates of {} (m)                      : ".format(p101_523)))
p101h_523 = float(input("Enter the height of {} (m)                             : ".format(p101_523)))
p102y_523 = float(input("Enter the Y coordinates of {} (m)                      : ".format(p102_523)))
p102x_523 = float(input("Enter the X coordinates of {} (m)                      : ".format(p102_523)))
p102h_523 = float(input("Enter the height of {} (m)                             : ".format(p102_523)))
detailp1_523 = input("Enter the point ID of detail point                        : ")
hdetailp_523 = float(input("Enter the horizantol direction of point {} (grad)   : ".format(detailp1_523)))
detailpangle_523 = float(input("Enter the verticle angle of point {} (grad)     : ".format(detailp1_523)))
slopedist_523 = float(input("Enter the slope distance between %s and %s (m)     : "%(p102_523, detailp1_523)))
ih_523 = float(input("Enter the height of instrument(m)                         : "))
rh_523 = float(input("Enter the height of reflector(m)                          : "))



deltah1_523 = math.cos((detailpangle_523*math.pi)/200)*slopedist_523
deltah2_523 = deltah1_523 - ih_523
deltah_523 = deltah2_523 + rh_523

h1_523 = p102h_523 + deltah_523
#Aciklik Acisi

if p101x_523 == p102x_523 and p101y_523 > p102y_523:
    azimuth_523 = 300
elif p101x_523==p102x_523 and p101y_523<p102y_523:
    azimuth_523 = 100
elif p101y_523==p102y_523 and p101x_523>p102x_523:
    azimuth_523 = 200
elif p101y_523==p102y_523 and p101x_523<p102x_523:
    azimuth_523=0
else:
    azimuth_523=(math.atan(abs(p102y_523 - p101y_523)/abs(p102x_523 - p101x_523))*200/math.pi)

if (p102y_523 - p101y_523)>0 and (p102x_523-p101x_523)>0:
    azimuth_523 = azimuth_523

elif (p102y_523 - p101y_523 )>0 and (p102x_523 - p101x_523)<0:
    azimuth_523 = 200 - azimuth_523

elif (p102y_523 - p101y_523)<0 and (p102x_523 - p101x_523)<0:
    azimuth_523 = 200 + azimuth_523

elif (p102y_523 - p101y_523)<0 and (p102x_523 - p101x_523)>0:
    azimuth_523 = 400 - azimuth_523
#2.Aciklik Acisi

azimuth_523 = azimuth_523 + hdetailp_523
if azimuth_523 < 200:
    azimuth_523 = azimuth_523 + 200
elif 200 < azimuth_523 < 600:
    azimuth_523 = azimuth_523 -200
elif azimuth_523 > 600:
    azimuth1021 = azimuth_523 - 400
deltax_523  =(slopedist_523*math.cos((azimuth_523*math.pi)/200))
deltay_523 =(slopedist_523*math.sin((azimuth_523*math.pi)/200))
p1x_523 = p102x_523 + deltax_523
p1y_523 = p102y_523 + deltay_523
print("Point ID \t Point ID \tHor.Dist \tDelta H  \tElevation   \tCoord.(Y)    \tCoord.(X)")
print("------------------------------------------------------------------------------------------------------------------")
print(p102_523, detailp1_523, slopedist_523, format(deltah_523, ".3f"), format(h1_523,".3f"), format(p1y_523,".3f") ,format(p1x_523, ".3f"), sep="             ")
print("------------------------------------------------------------------------------------------------------------------")



