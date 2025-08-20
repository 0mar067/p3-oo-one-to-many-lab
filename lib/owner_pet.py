class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        """Returns a full list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Checks that the pet is of type Pet and adds the owner to the pet."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be of type Pet")
        pet.owner = self
    
    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Validate pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception("pet_type must be one of the approved types")
        
        # Add instance to all
        Pet.all.append(self)
