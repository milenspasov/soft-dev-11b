class Triangle:
    layer_count = 0
    layers = []
    def __init__(self, argument):
        if isinstance(argument, int):
            layer_count = argument
            self.layer_count = layer_count
            for i in range(0, layer_count):
                self.layers.append([])
                print("Layer {0} [{0}]:".format(i+1, i+1, end=""))
                for j in range(0, i+1):
                    self.layers[i].append(int(input(" ")))
        elif isinstance(argument, str):
            filename = argument
            with open(filename, 'r') as file:
                for line in file:
                    self.layer_count += 1
                    self.layers.append(list(map(int, line.split(" "))))



    def printt(self):
        for i in range(0, self.layer_count):
            print(self.layers[i])

    def highest_sum_r(self, vindex, hindex):
        if(vindex == self.layer_count-1):
            return self.layers[vindex][hindex]
        left_sum=0
        right_sum=0
        left_sum += self.layers[vindex][hindex]
        right_sum += self.layers[vindex][hindex]
        left_sum += self.highest_sum_r(vindex+1, hindex)
        right_sum += self.highest_sum_r(vindex+1, hindex+1)
        return max(left_sum, right_sum)

    def highest_sum(self):
        if(self.layer_count == 0):
            return 0;
        max_sum = 0
        left_sum = 0
        right_sum = 0
        left_sum = self.highest_sum_r(1, 0)
        right_sum = self.highest_sum_r(1, 1)
        max_sum += self.layers[0][0]
        max_sum += max(left_sum, right_sum)
        return max_sum
        
numbers = Triangle("highsum.txt")
numbers.printt()
print(numbers.highest_sum())


