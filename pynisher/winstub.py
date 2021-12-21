import signal
from collections import namedtuple

class resource:
    RUSAGE_CHILDREN=None
    RUSAGE_SELF=None
    RLIMIT_AS=None
    
    struct_rusage_fields=['ru_utime', 'ru_stime', 'ru_maxrss', 'ru_ixrss', 'ru_idrss', 'ru_isrss', 'ru_minflt', 'ru_majflt', 'ru_nswap', 'ru_inblock', 'ru_oublock', 'ru_msgsnd', 'ru_msgrcv', 'ru_nsignals', 'ru_nvcsw', 'ru_nivcsw']
    struct_rusage = namedtuple('struct_rusage', struct_rusage_fields, defaults=(None,) * len(struct_rusage_fields))
    
    def getrusage(who):
        return resource.struct_rusage()
    
    def setrlimit(resource, limits):
        pass
    

class signalstub():
    SIGALRM=None
    SIGXCPU=None
    SIGQUIT=None
    def signal(signalnum, handler):
        if signalnum is not None:
            signal.signal(signalnum, handler)
    
    def alarm(time):
        pass
