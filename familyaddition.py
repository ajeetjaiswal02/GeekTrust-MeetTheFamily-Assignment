from geektrust import *
from person import *
from familytree import *


def findPerson(root,PersonName):
    """
    Returns pointer of the node corresponding to person Name
    """
    if root == None:
        return None
    else:
        if root.name == PersonName:
            return root
        else:
            if root.gender == "Female":
                if root.wifeOf != None:
                    if root.wifeOf.name==PersonName:
                        return root.wifeOf
            else:
                if root.husbandOf == None:
                    return None
                else:
                    root = root.husbandOf
                    if root.name == PersonName:
                        return root
            
            if len(root.children)==0:
                    return None
            else:
                for x in root.children:
                    resultPerson=findPerson(x,PersonName)
                    if resultPerson != None:
                        return resultPerson
                """
                if not found just return a None 
                """
                return None
            


def addHusband(root,brideName,groomName):
    """
    new wedding in family, groom is new person in family
    :param groom: member of the family, who is going to get married
    :param bridename: new person who is going to get married to family member and going to added in family
    """
    target=findPerson(root,brideName)
    if target==None:
        return root
    else:
        groom=Male(groomName)
        groom.husbandOf=target
        target.wifeOf=groom
    
    return root



def addWife(root,groomName,brideName):
    """
    new wedding in family, spouse is new person in family
        :param spouse: new person who is going to get married to family member and going to added in family
    """
    target=findPerson(root,groomName)
    if target == None:
        return root
    else:
        bride=Female(brideName)
        bride.wifeOf=target
        target.husbandOf=bride
    return root

def printer(str,noPrint):
    """
    To check if print is False required for the buldtree to properly message Declaration
    """
    if noPrint == False:
        print(str)

def addChild(root,motherName,childName,gender,noPrint):
    if gender != "Male" and gender != "Female":
        printer("CHILD_ADDITION_FAILED",noPrint)
    else:
        target=findPerson(root,motherName)
        if target==None:
            printer("PERSON_NOT_FOUND",noPrint)
        else:
            if target.gender == "Male":
                printer("CHILD_ADDITION_FAILED",noPrint)
            elif target.wifeOf==None:
                printer("CHILD_ADDITION_FAILED",noPrint)
            else:
                if gender == "Male":
                    son=Male(childName)
                    son.sonOf=target
                    target.children.append(son)
                else:
                    daughter=Female(childName)
                    daughter.daughterOf=target
                    target.children.append(daughter)
                printer("CHILD_ADDITION_SUCCEEDED",noPrint)
    return root

def addChildBulk(root,motherName,childDict):
    kidsKeys=childDict.keys()
    for x in kidsKeys:
        root=addChild(root,motherName,x.strip(),childDict[x],True)
    return root

def addWifeBulk(root,CoupleDict):
    wifeKeys=CoupleDict.keys()
    for x in wifeKeys:
        root=addWife(root,x,CoupleDict[x])
    return root
