class Boiler(object):
    '''
    classdocs
    '''
    def __init__(self,app,in_arg):
        '''
        Constructor
        '''
        print 'Boiler init'
        self.app = app
        self.in_arg = in_arg
    
    def __call__(self,environ,start_response):
        print 'Boiler callable object'
        
        return self.app(environ, start_response)
        
def filter_app_factory(app,global_config,in_arg):
    return Boiler(app,in_arg)
