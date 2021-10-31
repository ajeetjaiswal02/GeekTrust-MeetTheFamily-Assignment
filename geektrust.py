import sys
from person import *
from familytree import *
from familyaddition import *


def initiateRoot(root,husbandName,wifeName):
    """
    Make Queen Anga and King Shan as root of all the Family

    """
    husband=Male(husbandName)
    wife=Female(wifeName)
    husband.husbandOf = wife
    wife.wifeOf = husband
    return wife


def printList(lst):
    """
    when a list is passed , it will print the list if not empty, otherwise NONE will be printed
    """
    if len(lst) == 0:
        print("NONE",end=" ")
    else:
        for items in lst:
            print(items,end=" ")

def getMother(target):
    if target.gender == "Male":
        mother = target.sonOf
    else:
        mother = target.daughterOf
    return mother

def getPaternalUncle(root,target):
    paternalUncleList=list()
    mother=getMother(target)
    if mother != None:
        father=mother.wifeOf
        grandmom=father.sonOf
        if grandmom != None and len(grandmom.children) > 1:
            for x in grandmom.children:
                if x.gender == "Male" and x.name != father.name:  
                    paternalUncleList.append(x.name)
    printList(paternalUncleList)
    
def getMaternalUncle(root,target):
    maternalUncleList=list()
    mother=getMother(target)
    if mother != None:
        grandmom=mother.daughterOf
        if grandmom != None and len(grandmom.children) > 1:
            for x in grandmom.children:
                if x.gender == "Male":
                    maternalUncleList.append(x.name)
    printList(maternalUncleList)
    
def getPaternalAunt(root,target):
    paternalAuntList=list()
    mother=getMother(target)
    if mother != None and mother.wifeOf != None:
        father = mother.wifeOf
        grandmom=father.sonOf
        if grandmom != None and len(grandmom.children) > 1:
            for childs in grandmom.children:
                if childs.gender == "Female":
                    paternalAuntList.append(childs.name)
    printList(paternalAuntList)
    
def getMaternalAunt(root,target):
    maternalAuntList=list()
    mother=getMother(target)
    if mother != None:
        grandmom=mother.daughterOf
        if grandmom != None and len(grandmom.children) > 1:
            for childs in grandmom.children:
                if childs.gender == "Female" and childs.name != mother.name:
                    maternalAuntList.append(childs.name)
    printList(maternalAuntList)
    
def getSisterInLaw(root,target):
    sisterInLawList=list()
    mother=getMother(target)
    if mother != None and len(mother.children) > 1:
        for child in mother.children:
            if child.name != target.name and child.gender == "Male" and child.husbandOf != None:
                sisterInLawList.append(child.husbandOf.name)
    if target.gender == "Male":
        spouse = target.husbandOf
        if spouse != None:
            spouseMother = spouse.daughterOf
            if spouseMother != None and len(spouseMother.children > 1):
                for child in spouseMother.children:
                    if child.name != spouse.name and child.gender == "Female":
                        sisterInLawList.append(child.name)
    else:
        spouse = target.wifeOf
        if spouse != None:
            spouseMother = spouse.sonOf
            if spouseMother != None and len(spouseMother.children) > 1:
                for child in spouseMother.children:
                    if child.gender == "Female":
                        sisterInLawList.append(child.name)
    printList(sisterInLawList)
    
def getBrotherInLaw(root,target):
    brotherInLawList=list()
    mother=getMother(target)
    if mother != None and len(mother.children) > 1:
        for child in mother.children:
            if child.name != target.name and child.gender == "Female" and child.wifeOf != None:            
                brotherInLawList.append(child.wifeOf.name)
    if target.gender == "Male":
        spouse=target.husbandOf
        if spouse != None:
            spouseMother = spouse.daughterOf
            if spouseMother != None and len(spouseMother.children) > 1:
                for child in spouseMother.children:
                    if child.gender == "Male":
                        brotherInLawList.append(child.name)
    else:
        spouse = target.wifeOf
        if spouse != None:
            spouseMother = spouse.sonOf
            if spouseMother != None and len(spouseMother.children) > 1:
                for child in spouseMother.children:
                    if child.name != spouse.name and child.gender == "Male":
                        brotherInLawList.append(child.name)
    printList(brotherInLawList)
    
def getSon(root,target):
    sonList=list()
    if target.gender == "Male":
        wife = target.husbandOf
        if wife != None and len(wife.children) > 0:
            for x in wife.children:
                if x.gender == "Male":
                    sonList.append(x.name)
    else:
        if len(target.children) > 0:
            for x in target.children:
                if x.gender == "Male":
                    sonList.append(x.name)
    printList(sonList)
    
def getDaughter(root,target):
    daughterList=list()
    if target.gender == "Male":
        wife = target.wifeOf
        if wife != None and len(wife.children) > 0:
            for x in wife.children:
                if x.gender == "Female":
                    daughterList.append(x.name)
    else:
        if len(target.children) > 0:
            for x in target.children:
                if x.gender == "Female":
                    daughterList.append(x.name)
    printList(daughterList)
    
def getSiblings(root,target):
    siblingsList=list()
    mother=getMother(target)
    if mother != None and len(mother.children) > 1: 
        for x in mother.children:
            if x.name != target.name:
                siblingsList.append(x.name)
    printList(siblingsList)
    
def getRelationShip(root,name,relationName):
    target=findPerson(root,name)
    if target == None:
        print("PERSON_NOT_FOUND",end=" ")
    else:
        #create Dictionary to get the data in right Place
        methodDict={"Paternal-Uncle":"getPaternalUncle(root,target)",
                    "Maternal-Uncle":"getMaternalUncle(root,target)",
                    "Paternal-Aunt":"getPaternalAunt(root,target)",
                    "Maternal-Aunt":"getMaternalAunt(root,target)",
                    "Sister-In-Law":"getSisterInLaw(root,target)",
                    "Brother-In-Law":"getBrotherInLaw(root,target)",
                    "Son":"getSon(root,target)",
                    "Daughter":"getDaughter(root,target)",
                    "Siblings":"getSiblings(root,target)"}
        eval(methodDict[relationName])
        

# Build Tree Gathering all the requirments

if __name__=="__main__":
    root=None
    root=initiateRoot(root,"King Shan","Queen Anga")
    root=buildtree(root)
    input_file = sys.argv[1]
    file=open(input_file)
    for x in file:
        gaps=0
        lst=x.strip().split(' ')
        for i in lst:
            if i == '':
                gaps=gaps + 1
        for y in range(1,gaps + 1):
            lst.remove('')
        if lst[0] == "ADD_CHILD":
            root=addChild(root,lst[1],lst[2],lst[3],False)
        elif lst[0] == "GET_RELATIONSHIP":
            getRelationShip(root,lst[1],lst[2])
            print("")
    
    