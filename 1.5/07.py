class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[:4]

    def get_config(self):
        return [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
            f"Память: " + "; ".join([f"{mem.name} - {mem.volume}" for mem in self.mem_slots])
        ]


cpu = CPU("cpu_1", 3000)
memory_1 = Memory("mem_1", 2)
memory_2 = Memory("mem_2", 4)
mb = MotherBoard("motherboard", cpu, memory_1, memory_2)

# test
lst = mb.get_config()
for i in lst:
    print(i)
