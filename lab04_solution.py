'''
Created on Jun 22, 2012

@author: Annor Theophilus
'''
# Q1 
groceries =['bananas','strawberries','apples','bread']

groceries.append('champagne')
print 'Q1 part a results is'
for item in groceries:
    print item
print # print a line

groceries.remove('bread')

print 'part b result  is'
print #printing a line
for item in groceries:
    print item
    
print
print 'part c results'
print
groceries.sort()
for item in groceries:
    print item
  
print 'Question 2'
print 'results  of a : Dictionary'

print 'results of b '  
#items=

itemsAndprice = {'Apple':'SPIC_APPLES','Bananas':'SPIC_BANANAS','Bread':'SPIC_BREAD','Carrots':'SPIC_CARROTS','Champagne':'SPIC_CAMPAGNE','Strawberries':'SPIC_STRAWBERRIES'}
# printing the items
for key,value in itemsAndprice.iteritems():
    print key,'   ',value

print
print 'results of Ques. 2c'
itemsAndprice['strawberries']='WPIC_STRAWBERRIES'
for key,value in itemsAndprice.iteritems():
    print key,'    ',value

print 
print 'results of d is'
itemsAndprice['chicken']='SPIC_CHICKEN'
for key ,value in itemsAndprice.iteritems():
    print key,'   ',value
print
print
print'------------------'
print 'LISTS'
print
print 'Resultd of'
list_items=['Apple','Bananas','Bread','Carrot','Champagne','Strawberries']
in_stock={'Apple':7.3,'Carrot':10.0,'Bananas':5.5,'Bread':1.0,'Champagne':20.90,'Strawberries':32.6}
print 'items to be Advertised'
print 'items','            ','Prices'
for items in list_items:
    if items in in_stock:
        print items,in_stock[items]
    else:
        print items,' out of stock'    
print
print ' Tuples'
print

always_in_stock = in_stock.items()
for items in always_in_stock:
    print items


    
