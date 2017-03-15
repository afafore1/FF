class Solution:

    def convert(self, input):
        #use exception handling to return correct type
        try:
            int(input)
        except:
            try:
                float(input)
            except:
                return type('') # type is string
            else:
                return type(0.0) # type is float
        else:
            return type(0) # type is int

    def apply_operation(self, left_operand, right_operand, operator):
        #not sure if I will call this elegant :(
        result = {'+': left_operand+right_operand, '-': left_operand - right_operand, '*': left_operand*right_operand, '/': left_operand/right_operand}
        return result[operator]

    def animalDetails(self, animalDetailsDict):
        '''
        we should have a dictionary with details such as
        animaldetailsDict = {'animalType': 'someAnimal', 'animalName' : 'someName', 'animalAge': 'someAge'}
        from this we can get
        '''
        animal = animalDetailsDict['animalType']
        name = animalDetailsDict['animalName']
        age = animalDetailsDict['animalAge']
        output = ('{name} the {animal} is {age} years old'.format(animal=animal, name=name, age=age))
        print output

    def getMin(self, num1, num2, num3):
        min = num1
        if min > num2:
            min = num2
        if min > num3:
            min = num3
        return min


#Test cases
s = Solution()
print s.convert('7 is a number')
print s.convert('4')
print s.convert('1.0')
print s.getMin(4,1,0)
print s.apply_operation(5,6,'+')
print s.apply_operation(10,2,'/')
animalDetailsDict = {'animalType': 'dog', 'animalName' : 'Fido', 'animalAge' : '10'}
s.animalDetails(animalDetailsDict)
