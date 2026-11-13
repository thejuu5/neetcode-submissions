class TimeMap:

    def __init__(self):
        self.time_dict = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = []
        self.time_dict[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.time_dict:
            return result
        else:
            time_list = self.time_dict[key]
            low = 0 
            high = len(time_list) - 1 
            while low <= high:
                mid = (low + high) // 2
                if (time_list[mid])[1] <= timestamp:
                    result = (time_list[mid])[0]
                    low = mid + 1
                else:
                    high = mid - 1
        return result
                



        
