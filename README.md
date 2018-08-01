# 基于paste实现python app应用管理
paste对wsgi的app管理 通过对paste.ini进行配置，可加载新的应用，或者对应用增加过滤器，每个app_factory返回一个实现__call__的对象，并且实现wsgi规范，接受的参数(environ,start_response) filter_app_factory返回一个wsgi app

composite：master_valve filter：purifier，boiler app：hydrant，tap，shower，drinking_fountain

global_conf是在ini文件中default section中定义的一系列key-value对，而**kwargs，即一些本地配置，是在其他section中定义的key-value
