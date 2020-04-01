class Pilha:
    def __init__(self):
        self._vet = []

    def peek(self):
        return self._vet[-1]
       
    def push(self, item):
        self._vet.append(item)
        
    def pop(self):
        if not self.is_empty():
          return self._vet.pop()
        else:
          print("Pilha vazia!")
        
    def is_empty(self):
        if len(self._vet) == 0:
          return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self):
        return str(self._vet)