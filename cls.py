class Mobile:

    type = "android"

    def __init__(self):
        self.brand="oneplus"
        self.os="Pie"

jn = Mobile()
jnn = Mobile()
jn.type = "ios"
jn.os = 'AN 10'
print('OS:',jn.os,"brand",jn.brand, jn.type)
print(jnn.type)
