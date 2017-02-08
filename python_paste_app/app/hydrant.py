class Hydrant(object):
    '''
    classdocs
    '''
    def __init__(self, in_arg):
        '''
        Constructor
        '''
        print 'Hydrant init'
        self.in_arg = in_arg
    
    def __call__(self,environ,start_response):
        print 'Hydrant callable object'
        
        start_response('200 OK',[('Content-Type','text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'Hydrant')]
        
def app_factory(global_config,in_arg):
    return Hydrant(in_arg)