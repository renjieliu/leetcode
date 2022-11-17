class Solution:
    def convertTemperature(self, celsius: float) -> 'List[float]': # O( 1 | 1 )
        return [celsius + 273.15, celsius*1.8+32]
    
