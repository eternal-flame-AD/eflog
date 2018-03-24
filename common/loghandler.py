import time
import colorama

colorama.init(autoreset=True)

def _add_zero(s,rlen):
    return "0"*(rlen-len(s))+s

def formattime(s):
    yr=str(s.tm_year)
    mon=_add_zero(str(s.tm_mon),2)
    day=_add_zero(str(s.tm_mday),2)
    hr=_add_zero(str(s.tm_hour),2)
    minute=_add_zero(str(s.tm_min),2)
    sec=_add_zero(str(s.tm_sec),2)
    date="/".join((yr,mon,day))
    time=":".join((hr,minute,sec))
    return date,time

def __severity_to_color(a):
    if a=="FATAL":
        return colorama.Fore.RED
    elif a=="SEVERE":
        return colorama.Fore.YELLOW
    elif a=="WARNING":
        return colorama.Fore.MAGENTA
    elif a=="INFO":
        return colorama.Fore.WHITE

def __severity_to_int(a):
    if a=="FATAL":
        return 3
    elif a=="SEVERE":
        return 2
    elif a=="WARNING":
        return 1
    elif a=="INFO":
        return 0

def __severity_ge(a,b):
    '''
    true if a>b
    fatal
    severe
    warning
    info
    '''
    return __severity_to_int(a)>=__severity_to_int(b)


def printlog(string,severity):
    print(__severity_to_color(severity)+string)

def writelog(f,string):
    f.write(string)
    f.write("\n")

class logitem():
    '''
    time
    source
    severity
    desc
    '''
    def __init__(self,source,severity,desc):
        self.time=formattime(time.localtime())
        self.source=source
        self.severity=severity
        self.desc=desc
    def get(self,showdate=False):
        result={}
        result['time']=" ".join(self.time) if showdate else self.time[1]
        result['source']=self.source
        result['severity']=self.severity
        result['desc']=self.desc
        return result
    def tostring(self,showdate=False):
        item=self.get(showdate)
        result=" ".join((item['time'],'{0:<15}'.format(item['source']),'{0:<8}'.format(item['severity']),item['desc']))
        return result
    def Printlogitem(self,showdate=False):
        result=self.tostring(showdate)
        printlog(result,self.severity)
    def Writelogitem(self,f,showdate=False):
        result=self.tostring(showdate)
        writelog(f,result)