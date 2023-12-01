from time import sleep
from processing_controller import ProcessingController


def run_for_client(branche):
    sleep(5)
    print(branche)

if __name__ == "__main__":
    branches = ['filial_01','filial_02','filial_03',
                'filial_04','filial_05','filial_06',
                'filial_07','filial_08','filial_09',
                'filial_10','filial_11','filial_12']
    pc = ProcessingController(functions=lambda x: run_for_client(x), max_cpus=5)
    pc.run(branches)


