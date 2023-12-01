from multiprocessing import Process, Manager
from math import ceil


class ProcessingController:
    def __init__(self, functions, max_cpus):
        """
        Controla a execução paralela de várias funções

        :param functions: lista das funções a serem executadas
        :param max_cpus: número máximo de threads simultâneas
        """
        self._functions = functions
        self._max_cpus = max_cpus

    @staticmethod
    def _runner_auxiliar(func, arg, output, i):
        """
        Salva o retorno da função em uma lista

        :return: Este método não possui retorno
        """
        if arg is None:
            output[i] = func()
        else:
            output[i] = func(arg)

    def run(self, args=None):
        """
        Executa várias funções em paralelo com diferentes parâmetros criando novos processos.

        :param args: parâmetros das funções
        :return: lista com os resultados
        """
        if isinstance(self._functions, list):
            num = len(self._functions)
        else:
            num = 1
        if args is None:
            args = [None for i in range(num)]

        if callable(self._functions):
            return self._run_functions([self._functions for i in range(len(args))], args, self._max_cpus)
        else:
            assert len(self._functions) == len(args), "Number of args must be the same of functions"
            return self._run_functions(self._functions, args, self._max_cpus)

    @staticmethod
    def _run_functions(funcs, args, cpus):
        """
        Executa todas as funções com um dado parâmetro

        :param arg: parâmetro a ser passado
        :return: lista com o resultado de cada função
        """
        output = Manager().dict()
        parameters = [(f, a) for f, a in zip(funcs, args)]
        for i in range(ceil(len(args) / cpus)):
            temp_process = []
            for j, (f, e) in enumerate(parameters[i * cpus:(i + 1) * cpus]):
                temp_process.append(Process(target=ProcessingController._runner_auxiliar,
                                            args=(f, e, output, i * cpus + j)))
            for p in temp_process:
                p.start()
            for p in temp_process:
                p.join()
        return list(output.values())
