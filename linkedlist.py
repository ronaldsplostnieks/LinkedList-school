class Node:
    def __init__(self, saturs, pirms=None, pec=None):
        self.info = saturs
        self.prev = pirms
        self.next = pec

    def read(self):
        print(self.info)

class List:
    def __init__(self, pirmais_info):
        self.pirmais = Node(pirmais_info)
    
    def add(self, jaunais_info, index = -1):
        if index == -1:
            pedejais = self.pirmais
            while pedejais.next:
                pedejais = pedejais.next
            # pedejais.next = Node(jaunais_info, pirms = pedejais)
            pedejais.next = Node(jaunais_info)
            pedejais.next.prev = pedejais
            return pedejais.next
        
        if index == 0:
            self.pirmais = Node(jaunais_info, pec=self.pirmais)
            return self.pirmais
        
        ieprieksejais = self.pirmais
        for i in range(index-1):
            if ieprieksejais.next == None:
                return self.add(jaunais_info)
            ieprieksejais = ieprieksejais.next
           
        ieprieksejais.next = Node(jaunais_info, pec = ieprieksejais.next, pirms=ieprieksejais)
    
    def remove(self, index):
        if index < 0:
            return
        
        if index == 0:
            if self.pirmais is None:
                print("Nav pirmā elementa")
                return
            else:
                self.pirmais = self.pirmais.next
                if self.pirmais is not None:
                    self.pirmais.prev = None
                return
        
        tagadejais = self.pirmais
        for i in range(index - 1):
            if tagadejais is None:
                raise IndexError("Index out of range")
            tagadejais = tagadejais.next
        
        if tagadejais is None or tagadejais.next is None:
            raise IndexError("Index out of range")
        
        tagadejais.next = tagadejais.next.next
        if tagadejais.next is not None:
            tagadejais.next.prev = tagadejais
    
    def read(self):
        esosais = self.pirmais
        while esosais:
            esosais.read()
            esosais = esosais.next

saraksts = List("suns")
saraksts.add(24)
saraksts.add("hei, visi!")
saraksts.add("pirmais", 0)
saraksts.add("ceturtais", 3)
saraksts.add("beigas",33)
saraksts.read()
print("Noņem \n")
saraksts.remove(2)
saraksts.read()



# Izveidot saistītajam sarakstam metodes:
# 1. kura dzēš konkrētā indeksa elementu,
# 2. kura nolasa tikai vienu konkrēta indeksa elementu.

