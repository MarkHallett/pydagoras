# dag.py

class DAG: # implementation
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

        if hasattr(self,'values'):
            return

        self.values = {}

    def __str__(self):
        return f'DAG(values={self.values})'

    def pp_json(self):
        return self.values
    
#    def __repr__(self):
#        return self.__str__()


    def set_value(self, key, value):
        self.values[key] = value
        
    def get_value(self, key):
        return self.values.get(key, None)

if __name__ == '__main__':
    print('dag.py main')
    my_dag = DAG()
    my_dag.set_value('a', 1)
    my_dag.set_value('b', 2)
     
    #my_dag.values['c'] = 3  # Directly setting a value
    #print(DAG().values)  # Output: {'a': 1, 'b': 2}

    #my_dag.test = 'test_value'  # Adding a new attribute dynamically
    #print(my_dag.test)  # Output: test_value
    #print(DAG().test)  # Output: test_value
    print('prints --------------')
    print (f'{my_dag=}')
    import json
    print(json.dumps(my_dag.pp_json(), sort_keys=True, indent=2))
    print(repr(my_dag))