from person import *
from geektrust import *
from familyaddition import *


def buildtree(root):
    kids={"Chit":"Male","Ish":"Male","Vich":"Male","Aras":"Male","Satya":"Female"}
    root=addChildBulk(root,"Queen Anga",kids)
    Couples={"Chit":"Amba","Vich":"Lika","Aras":"Chitra"}
    root=addWifeBulk(root,Couples)
    root=addHusband(root,"Satya","Vyan")
    kids={}
    kids={"Dritha":"Female","Tritha":"Female","Vritha":"Male"}
    root=addChildBulk(root,"Amba",kids)
    root=addHusband(root,"Dritha","Jaya")
    kids={}
    kids={"Vila":"Female","Chika":"Female"}
    root=addChildBulk(root,"Lika",kids)
    kids={}
    kids={"Jnki":"Female","Ahit":"Male"}
    root=addChildBulk(root,"Chitra",kids)
    root=addHusband(root,"Jnki","Arit")
    kids={}
    kids={"Asva":"Male","Vyas":"Male","Atya":"Female"}
    root=addChildBulk(root,"Satya",kids)
    Couples={}
    Couples={"Asva":"Satvy","Vyas":"Krpi"}
    root=addWifeBulk(root,Couples)
    root=addChild(root,"Dritha","Yodhan","Male",True)
    kids={}
    kids={"Laki":"Male","Lavnya":"Female"}
    root=addChildBulk(root,"Jnki",kids)
    root=addChild(root,"Satvy","Vasa","Male",True)
    kids={}
    kids={"Kriya":"Male","Krithi":"Female"}
    root=addChildBulk(root,"Krpi",kids)
    return root
