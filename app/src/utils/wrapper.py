import pickle

def wrapper_factory(object_param):
    class Wrapper:
        """
            Scikit Learn Wrapper, to separate from luigi workflow
        """        

        def __init__(self, **params):
            """
                constructor, passing params to real object class

                :parameter kwargs:
                :return: None
            """
            self.__object = object_param(**params)

        @property
        def instance(self):
            """
                return object instance
            """
            return self.__object
        
        def to_file(self, file_io):
            """
                dump object to binary file
            """
            pickle.dump(self.__object, file_io)

    return Wrapper()