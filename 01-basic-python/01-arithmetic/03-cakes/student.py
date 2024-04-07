# Write your code here
def cakes(eggs, butter, flour):
    cakes_eggs = eggs // 5
    cakes_butter = butter // 250
    cakes_flour = flour // 250
    return min(cakes_butter, cakes_eggs, cakes_flour)