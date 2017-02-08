class Shower(object):
    '''
    classdocs
    '''
    def __init__(self, in_arg):
        '''
        Constructor
        '''
        print 'Shower init'
        self.in_arg = in_arg
    
    def __call__(self,environ,start_response):
        print 'Shower callable object'
        
        start_response('200 OK',[('Content-Type','text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'Shower')]
        
def app_factory(global_config,in_arg):
    return Shower(in_arg)