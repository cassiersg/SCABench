import lascar


class MyNPYContainer(lascar.Container):
    def __init__(self, traces, data_dic, **kwargs):
        self.leakages = traces
        self.values = data_dic
        lascar.Container.__init__(self, **kwargs)

    def __getitem__(self, key):
        return lascar.TraceBatchContainer.__getitem__(self, key)

    def __setitem__(self, key, value):
        lascar.TraceBatchContainer.__setitem__(self, key, value)


def get_partition_function(byte):
    def partition_function(value):
        return value[byte]

    return partition_function
