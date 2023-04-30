class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(
        self,
        name,
        cpu,
        memory_1=None,
        memory_2=None,
        memory_3=None,
        memory_4=None,
    ):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.memory_1 = memory_1
        self.memory_2 = memory_2
        self.memory_3 = memory_3
        self.memory_4 = memory_4
        self.mem_slots = [
            x for x in [self.memory_1, self.memory_2, self.memory_3, self.memory_4] if x
        ]

    def get_config(self):
        lst = [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
        ]
        memory_lst = []
        for mem in self.mem_slots:
            memory_lst.append(f"{mem.name} - {mem.volume}")
        memory_str = "Память: " + "; ".join(memory_lst)

        lst.append(memory_str)
        return lst


cpu = CPU("cpu_1", 3000)
memory_1 = Memory("mem_1", 2)
memory_2 = Memory("mem_2", 4)
mb = MotherBoard("motherboard", cpu, memory_1, memory_2)

# test
lst = mb.get_config()
for i in lst:
    print(i)
