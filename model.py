
class Plank:
    """Object met een bepaalde lengte.

    Plank is een object dat initieerd met een bepaalde lengte (lengte zoals in de winkel op voorraad)
    daarna kan dit object opgedeeld worden in bepaalde gezaagde lengtes.
    """

    def __init__(self, lengte):
        self.Lengte = lengte
        self.LengteOver= lengte
        self.Soort = 'Meubelplaat'
        self.ZaagBreedte = 1# 0.3
        self.GezaagdeLengtes=[]

    def Halveer(self):
        "Test definitie: niet gebruiken. Halveerd de lengte door 2."
        self.Lengte = self.Lengte/2

    def AddZaagLengte(self, Zaaglengte, Lengtes_list):
        """voeg een gezaagde lengte toe aan het plank object.

        De lijst in .GezaagdeLengtes wordt hiermee aangevuld.
        Tevens verminderd de .LengteOver met de Zaaglengte
        """
        if Zaaglengte <= self.LengteOver:
            if Zaaglengte in Lengtes_list: 
                self.GezaagdeLengtes.append(Zaaglengte)
                self.LengteOver= self.LengteOver-(Zaaglengte+self.ZaagBreedte)
                Lengtes_list.remove(Zaaglengte)     # remove de lengte uit de Lengtes_list
            else:
                print ('error 2343, kan ({}) niet verwijderen/bestaat niet in lijst'.format(Zaaglengte))
        else:
            print ('error 234235, te lang ({} cm) om (nog) uit deze plank te halen (over:{} cm)'.format(Zaaglengte,self.LengteOver))
            #print ('zaaglengte: {}, lengteover {}'.format(Zaaglengte, self.LengteOver))

    def PrintGezaagdeLijst(self):
        print ('planklengtes: ',)
        if len(self.GezaagdeLengtes)==0:
            print ('none')
        else:
            for i in self.GezaagdeLengtes:
                print (i,' mm')
        print ('\n')

    def IsNestDone(self, Lengtes_list):
        if self.LengteOver>min(Lengtes_list):
            return False # minimaal de kleinste plank lengtes kunnen nog uit het restand van de plank gehaald worden.
        else:
            return True # zelfs de kleinste plank kan niet meer uit het restand van de plank gehaald worden.

    def NestWithLessWaste(self, Lengtes_list):
        """Lengtes_list is de lijst met nog te zagen lengtes"""

        #print ('Is nesting done? : {}'.format(self.IsNestDone(Lengtes_list)))
        count=0

        while len(Lengtes_list) and self.LengteOver>min(Lengtes_list) and count<len(Lengtes_list) :
            count=count+1
            print ('loop: {}'.format(count))
            if self.Lengte==self.LengteOver:
                #is dus een nieuwe plank. Dan standaard de max lengte toevoegen (die moet hoe dan ook een keer gezaagd worden)
                print ('pak eerst de langste =({})'.format(max(Lengtes_list)))
                self.AddZaagLengte(max(Lengtes_list),Lengtes_list)

            elif self.IsNestDone(Lengtes_list) == False:
                if min(Lengtes_list)< self.LengteOver: 
                    print('ga bruteforce nesten. nog {} cm lengte over'.format(self.LengteOver))
                    print('over van lijst: {}'.format(Lengtes_list))
                    #roep functie om brute force te nesten
                    #die functie returned een list met lengtes
                    #loop door die list om de lengte toe te voegen aan .AddZaagLengte
                    for Lengte in BFnest(self,Lengtes_list):
                        print ('Lengte ({} cm) wordt door Bruteforce nesting toegevoegd aan de plank.'.format(Lengte))
                        self.AddZaagLengte(Lengte,Lengtes_list)
                else:
                    print('kan niet nesten')
                    break
            else:
                print ('nesten niet meer mogelijk. Grotere plank nodig.')
                break



class Zaagplan:
    "Zaagplan omvat alle plank objecten"

    def __init__(self, name): 
        self.Name = name
        self.PlankLst = [] #list of objects of class Plank

    def AddWholePlank(self, PlankObject):
        "Voeg een Plank object toe aan de lijst .PlankLst"
        self.PlankLst.append(PlankObject)
        
    def PrintInhoud(self):
        "Print de inhoud van het zaagplan"
        print ('Inhoud Zaagplan:')
        for i in self.PlankLst:
            print ('lengte: ', i.Lengte, ' soort: ', i.Soort, ' LengteOver: ', round(i.LengteOver,1))
            i.PrintGezaagdeLijst()
            


def BFnest(plank_object,Lengtes_list):
    
    Min_Waste_List=[]  
    RecurringLoopNest(plank_object, len(Lengtes_list), 0, Lengtes_list, 0, Min_Waste_List, 0)
    best_nest_tot = Calc_Lengte_Tot(plank_object.ZaagBreedte, Min_Waste_List)
    #print ('beste nesting met {} cm over is: {}'.format(plank_object.LengteOver-Best_Nest_Value,Min_Waste_List))
    print ('beste nesting met {} cm over is: {}'.format(plank_object.LengteOver - best_nest_tot, Min_Waste_List))
    #nog brute forcen :-). dit is een voorbeeld return
    return Min_Waste_List #[20,43,29]
 
def MakeList(input_list, first_part_list, second_part_list, output_list, depth):
    depth=depth+1
    
    Length_of_input = len(input_list)
    
    for i in range(Length_of_input):
        print (depth*'.','depth:{}'.format(depth))
        print (depth*'.','loop:{}'.format(i))
        
        first_part_list.append(input_list[i])
        second_part_list=list(input_list)
        for j in first_part_list:
            second_part_list.remove(j)
        second_part_list.append(0)
        print (depth*'.','1st part list:')
        print (depth*'.',first_part_list)
        print (depth*'.','2nd part list:')
        print (depth*'.',second_part_list)
        #MakeList(second_part_list,[],[],output_list,depth)

        output_list.append([]) #voeg lijst toe
        #output_list[i].append(input_list[i])
        output_list[i].append(first_part_list)
        if second_part_list:
            MakeList(second_part_list, first_part_list, [], output_list, depth)
        first_part_list=[] # make empty
        second_part_list=[] # make empty
    #2do; remove 0's from output
    print ('output', output_list)


def RecurringLoopNest(plank_object, max_loops, loop_i, l_list, best_nest_tot, best_nest_list, rec_level):
    rec_level_1=rec_level+1
    best_nest_tot=0
    try_nest_tot=0
    print ('Recurring level/depth: {}'.format(rec_level_1))

    if loop_i<=max_loops:
        l_list_1=list(l_list)
        #l_list_1.append(0)

        for lengte_1 in l_list_1:
            count=loop_i+1
            l_list_2=list(l_list_1)
            l_list_2.remove(lengte_1)
            
            lengte_2=RecurringLoopNest(plank_object, len(l_list_2), count, l_list_2, best_nest_tot, best_nest_list, rec_level_1)
            if lengte_2 is None: lengte_2=0
            print (rec_level_1*'.', 'lengte_1:{}, lengte_2:{}'.format(lengte_1,lengte_2))
            try_nest_tot = lengte_1 + lengte_2 + plank_object.ZaagBreedte
            
            best_nest_tot=Calc_Lengte_Tot(plank_object.ZaagBreedte, best_nest_list)

            if try_nest_tot>best_nest_tot and try_nest_tot<=plank_object.LengteOver:
                if lengte_1!=0:
                    best_nest_list.append(lengte_1)
                if lengte_2!=0:
                    best_nest_list.append(lengte_2)
                
                #best_nest_tot=try_nest_tot
                #if len(best_nest_list)>1:
                #    zaagafval=(len(best_nest_list)-1) * plank_object.ZaagBreedte
                #else:
                #    zaagafval=0
                ##########nog toevoegen: Calc_Lengte_Tot
                #best_nest_tot=sum(best_nest_list) + zaagafval
                
                best_nest_tot=Calc_Lengte_Tot(plank_object.ZaagBreedte, best_nest_list)
                print (rec_level_1*'.', 'best_nest_list:{}'.format(best_nest_list))
                print (rec_level_1*'.', 'best_nest_tot:{}'.format(best_nest_tot))
        return best_nest_tot
    

def Calc_Lengte_Tot(zaag_breedte, list_1):
    if list_1: #inhoud list is > 0
        if len(list_1)>1:
            zaagafval=(len(list_1)-1) * zaag_breedte
        else:
            zaagafval=0

        return sum(list_1) + zaagafval    
    else:
        return 0


class Nest:
    def __init__(self, Plank_object, Lengtes_list): 
        self.list = Lengtes_list
        self.Lengte = Plank_object.Lengte
        self.Lengte_over=Plank_object.LengteOver
    
