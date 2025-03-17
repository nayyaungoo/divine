__all__ = ['paradise', 'Heaven']

def paradise(func):
    """
    Registers a function for future execution by Heaven.
    
    This decorator appends the provided function to Heaven.paradises and returns it unmodified.
    """
    Heaven.paradises.append(func)
    return func


class Heaven(object):
    paradises = []

    def run(self, *args, returnable=False):
        # the list 'received' is always parallel to the list 'paradises'
        """
        Executes stored functions and collects their outputs.
        
        If no indices are specified, all functions in the paradises list are executed
        with the current instance as an argument. If indices are provided, only the functions
        at those positions are executed. The results are stored in the instance's 'received'
        list in the same order as execution and are returned if 'returnable' is True.
        
        Args:
            *args: Indices of the functions in the paradises list to execute. If empty,
                all functions are run.
            returnable (bool): If True, returns the list of collected results; otherwise,
                the results must be accessed via the 'received' attribute.
        
        Returns:
            list: The list of results from the executed functions when 'returnable' is True.
        """
        self.received = []

        if len(args) == 0:
            for paradise in self.paradises:
                # Run the all the paradise and store the return value in 'received'
                self.received.append(paradise(self))

        else:
            for index in args:
                # Run the specified Paradises and store the return value in 'received'
                self.received.append(self.paradises[index](self))

        # Strongly recommend to directly use from the list 'received' than returning
        if returnable:
            return self.received
