class Purifier(object):
    '''
    classdocs
    '''
    def __init__(self,app,in_arg):
        '''
        Constructor
        '''
        print 'Purifier init'
        self.app = app
        self.in_arg = in_arg
    
    def __call__(self,environ,start_response):
        print 'Purifier callable object'
        
        return self.app(environ, start_response)
        
def filter_app_factory(app,global_config,in_arg):
    return Purifier(app,in_arg)
