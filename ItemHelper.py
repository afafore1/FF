class Someitem(object):
    frequency = 0

    def __init__(self, frequency):
        self.frequency = frequency

class ItemHelper:
    itemList = []

    def storeList(self, itemList):
        self.itemList = itemList

    def getUniqueItemsFromList(self):
        global itemList
        uniqueItems = []
        listMap = {}
        for item in itemList:
            if item in listMap:
                listMap[item] += 1
            else:
                listMap[item] = 1
        for item in listMap:
            if listMap[item] == 1:
                uniqueItems.append(item)
        return uniqueItems

    def getItemsAndFrequency(self):
        global itemList
        itemFrequencyDict = {}
        for item in itemList:
            itemFrequencyDict[item] = item.frequency
        return itemFrequencyDict

    def updateItemList(self, someItem):
        global itemList
        itemList.append(someItem)

# Test
item1 = Someitem(5)
item2 = Someitem(10)
item3 = Someitem(89)
itemList = [item1, item2, item1]
helper = ItemHelper()
helper.storeList(itemList)
uniqueItems = helper.getUniqueItemsFromList()
for item in uniqueItems:
    print item.frequency

itemDict = helper.getItemsAndFrequency()
for item, value in itemDict.iteritems():
    print item
    print value

helper.updateItemList(item3)
print helper.getItemsAndFrequency()



