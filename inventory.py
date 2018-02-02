class item:
    def __init__(self,name,costPrice,sellingPrice):
        self.Id=1
        self.name=name
        self.costPrice=costPrice
        self.sellingPrice=sellingPrice
        self.quantity=0
    

class inventory:
    def __init__(self):
        #dict key,value-->name,item
        self.Id=1
        self.itemDB={}
        self.old_profit=0
        self.profit=0
    
    def Create(self,itemName,costPrice,sellingPrice):
        costPrice=round(costPrice,2)
        sellingPrice=round(sellingPrice,2)
        #create item
        t=item(itemName,costPrice,sellingPrice)
        t.Id=self.Id
        self.autoIncrementID()
        #put item in inventory
        self.itemDB[itemName]=t
    
    def autoIncrementID(self):
        self.Id+=1
        
    def delete(self,itemName):
        self.profit-=self.itemDB[itemName].quantity*self.itemDB[itemName].costPrice
        self.itemDB.pop(itemName)
        
    def updateBuy(self,itemName,quantity):
        self.itemDB[itemName].quantity+=quantity
        
    def updateSell(self,itemName,quantity):
        self.itemDB[itemName].quantity-=quantity
        self.profit+=quantity*(self.itemDB[itemName].sellingPrice-self.itemDB[itemName].costPrice)
        
    def report(self):
        print(*['item Name','Bought At','Sold At','Available Qty','Value'],sep="  ")
        total_value=0
        for name,obj in self.itemDB.items():
            value=obj.costPrice*obj.quantity
            print(*[name,obj.costPrice,obj.sellingPrice,obj.quantity,value],sep="   ")
            total_value+=value
        print("\nTotal Value %.2f \nProfit since last report %.2f\n"%(total_value,self.profit-self.old_profit))
        self.old_profit=self.profit
    
    def updateSellPrice(itemName,newSellprice):
        self.itemDB[itemName].sellingPrice=newSellPrice
        
def main():
        Inv=inventory()
        Inv.Create('Book01',10.50,13.79)
        Inv.Create('Food01',1.47,3.98)
        Inv.Create('Med01',30.63,34.29)
        Inv.Create('Tab01',57.00,84.98)
        Inv.updateBuy('Tab01',100)
        Inv.updateSell('Tab01',2)
        Inv.updateBuy('Food01',500)
        Inv.updateBuy('Book01',100)
        Inv.updateBuy('Med01',100)
        Inv.updateSell('Food01',1)
        Inv.updateSell('Food01',1)
        Inv.updateSell('Tab01',2)
        Inv.report()
        Inv.delete('Book01')
        Inv.updateSell('Tab01',5)
        Inv.Create('Mobile01',10.51,44.56)
        Inv.updateBuy('Mobile01',250)
        Inv.updateSell('Food01',5)
        Inv.updateSell('Mobile01',4)
        Inv.updateSell('Med01',10)
        Inv.report()

if __name__ == "__main__":
    main()