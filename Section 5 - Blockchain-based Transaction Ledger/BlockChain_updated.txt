# Blockchain.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class someClass:
    string = None
    num = 328965
    def __init__(self, mystring):
        self.string = mystring
    def __repr__(self):      # representation of the fn is something that is going to be called when you either call the string or print on it  
        return self.string + "^^^" + str(self.num)

# can compute its own hash and store all kinds of data 
class CBlock:
    data = None
    previousHash = None
    previousBlock = None
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock != None: 
            self.previousHash = previousBlock.computeHash()
    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend)
        digest.update(bytes(str(self.data), 'utf8'))           # what makes the blockchain secure is is that we 
        digest.update(bytes(str(self.previousHash), 'utf8'))   # has not only the data but the hash of the previousBlock
        return digest.finalize()
    def is_valid(self):
        if self.previousBlock == None:
            return True
        return self.previousBlock.computeHash() == self.previousHash
        
    
# chain of blocks that to pass all kinds of data
if __name__== '__main__':
    root = CBlock('I am a root', None)
    B1 = CBlock(b'I am a child.', root)
    B2 = CBlock('I am B1s Brother', root)
    B3 = CBlock(12354, B1)
    B4 = CBlock(someClass('Hi there!'), B3)
    B5 = CBlock("Top block", B4)
           

    for b in [B1, B2, B3, B4, B5]:    
        if b.is_valid():
            print ("Success! Hash is good.")
        else:
            print ("ERROR! Hash is no good.")

    B3.data=12345
    if B4.is_valid():
        print ("ERROR! Couldn't detect tampering.")
    else:
        print ("Success! Tampering detected.")
        
    print(B4.data)
    B4.data.num = 99999
    print(B4.data)
    if B5.is_valid():
        print ("ERROR! Couldn't detect tampering.")
    else:
        print ("Success! Tampering detected.")



