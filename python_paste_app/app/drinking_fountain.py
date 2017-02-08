class DrinkingFountain(object):
    '''
    classdocs
    '''
    def __init__(self, in_arg):
        '''
        Constructor
        '''
        print 'DrinkingFountain init'
        self.in_arg = in_arg
    
    def __call__(self,environ,start_response):
        print 'DrinkingFountain callable object'
        
        start_response('200 OK',[('Content-Type','text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'DrinkingFountain')]
        
def app_factory(global_config,in_arg):
    return DrinkingFountain(in_arg)