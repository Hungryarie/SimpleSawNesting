from model import Zaagplan, Plank, MakeList#, BFnest 

print ('\n\nstart')

#plank_lengtes= [244.0, 242.0, 242.0, 242.0, 181.0, 129.0, 115.0, 97.4, 97.4, 97.4, 97.4, 97.4, 97.4, 85.0, 85.0, 80.5, 80.5, 80.5, 80.5, 80.5, 80.5, 43.0, 43.0, 43.0]
plank_lengtes= [1,2,3]
plank_lengte= 250 #cm
zaag_dikte=0.3 #cm

output_list=[]
MakeList(plank_lengtes, [], [], output_list,0)
print (output_list)

#print ('plank lengte = ', plank_lengte, " cm")
print ('zaag dikte = ', (zaag_dikte*10), " mm")

Plan = Zaagplan('zaagplannaam')

newPlank = Plank(13)
newPlank.NestWithLessWaste(plank_lengtes)

newPlank2 = Plank(250)
newPlank2.NestWithLessWaste(plank_lengtes)

newPlank3 = Plank(250)
newPlank3.NestWithLessWaste(plank_lengtes)

newPlank4 = Plank(250)
newPlank4.NestWithLessWaste(plank_lengtes)

newPlank5 = Plank(250)
newPlank5.NestWithLessWaste(plank_lengtes)

newPlank6 = Plank(250)
newPlank6.NestWithLessWaste(plank_lengtes)

newPlank7 = Plank(250)
newPlank7.NestWithLessWaste(plank_lengtes)

#newPlank2.AddZaagLengte(102)
#newPlank2.AddZaagLengte(55)

Plan.AddWholePlank(newPlank)
Plan.AddWholePlank(newPlank2)
Plan.AddWholePlank(newPlank3)
Plan.AddWholePlank(newPlank4)
Plan.AddWholePlank(newPlank5)
Plan.AddWholePlank(newPlank6)
Plan.AddWholePlank(newPlank7)

print ("\n\n")
print ('Aantal planken in Plan: ', len(Plan.PlankLst))
#newPlank2.PrintGezaagdeLijst()
Plan.PrintInhoud()

print ('end\n\n\n')