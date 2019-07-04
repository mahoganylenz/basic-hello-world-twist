#Michelle Mason
#Week9- First Django Application
#Written June 22, 2019

class Dog():
    """Represent a simple dog profile."""

    def__init__(self,dogID,dogName, dogBreed,dogAge, ownerID):
        """Initalize the dog."""
        self.dogID = dogID
        self.dogName = dogName.title()
        self.dogBreed = dogBreed.title()
        self.dogAge = dogAge
        self.ownerID = ownerID
    def describe_dog(self):
        """Display a summary of the dog's information.""" 
        print("\n" + str(self.dogID) + ": " + self.dogName)
        print(" Breed:" + self.dogBreed)
        print(" Age:" + str(self.dogAge))
        print(" OwnerID:" + str(self.ownerID))

class Owner():
    """Represent a simple owner profile."""

    def__init__(self, ownerID, ownerFName,ownerLName):
        """Initialize the owner"""
        self.ownerID = ownerID
        self.ownerFName = ownerFName.title()
        self.ownerLName = ownerLName.title()

    def describe_owner(self):
        """Display a summary of the owner's information."""
        print("\n" + str(self.ownerID) + ": " + self.ownerFName + " " + self.ownerLName)



