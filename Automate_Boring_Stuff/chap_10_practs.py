#write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10

spam = 10

try:
    assert spam < 10, 'Spam is not less than 10. Is currently has the value {}'.format(spam)
except:
    print('This AssertionError has been caught and dealt with!')
#write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different

eggs = 'BACON'
bacon = 'bacon'

try:
    assert eggs.lower() != bacon.lower(), 'vars eggs and bacon are same when in lowercase!'
except:
    print('This AssertionError has been caught and dealt with!')
    
#write an assert statement that always triggers an AssertionError

try:
    assert 1 == 0, '1 is not equal to 0!'
except:
    print('This AssertionError has been caught and dealt with!')
