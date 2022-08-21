class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: 'List[int]', experience: 'List[int]') -> int: # O( N | 1 )
        hours = 0  # initialize the training hours 
        en = initialEnergy
        ex = initialExperience
        
        for i, e in enumerate(energy):
            if (en-e) <= 0: # check if current energy can defeat the enermy
                hours += abs(en-e)+1
                en = 1  # reset the energy
            else:
                en -= e # loss the experience
            
            if ex-experience[i] <= 0:  # check if current experience can defeat the enermy
                hours += abs(ex-experience[i])+1 
                ex += abs(ex-experience[i])+1 # add the learned exp to current, and fight the enemy
            ex += experience[i] # gain the experience
            
        return hours
    


