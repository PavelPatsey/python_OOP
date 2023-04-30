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
            f"Память: "
            + "; ".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots)),
        ]


cpu = CPU("Intel", 3000)
memory_1 = Memory("Kingston", 32)
memory_2 = Memory("Kingston", 16)
mb = MotherBoard("motherboard", cpu, memory_1, memory_2)

# test
lst = mb.get_config()
for i in lst:
    print(i)
