import sys
from math import log
from cStringIO import StringIO # for stdout capturing
# TODO http://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call





def color(string,**kwargs):
    """Color"""
    # http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    text_color_dict = { "black"     : "0;30;",  "red"       : "1;31;",
                        "green"     : "0;32;",  "yellow"    : "1;33;", "orange"    : "1;33;",
                        "blue"      : "1;34;",  "purple"    : "0;35;",
                        "magenta"   : "1;36;",  "grey"      : "0;37;",  }
    background_color_dict = {   "black"     : "40", "red"       : "41",
                                "green"     : "42", "yellow"    : "43", "orange"    : "43",
                                "blue"      : "44", "purple"    : "45",
                                "magenta"   : "46", "grey"      : "47", }                  
    color_code = text_color_dict[kwargs.get('color',"red")] + background_color_dict[kwargs.get('background',"black")]
    return kwargs.get('prepend',"") + "\x1b[%sm%s\033[0m" % ( color_code, string )

def warning(string,**kwargs):
    return color("Warning! "+string, color="yellow", prepend=">>> "+kwargs.get('prepend',""))
    
def error(string,**kwargs):
    return color("ERROR! "+string, color="red", prepend=">>> "+kwargs.get('prepend',""))
    




def printVerbose(string,verbosity,**kwargs):
    """Print string if verbosity is true or verbosity int is lager than given level."""
    level = kwargs.get('level',False)
    if level:
        if verbosity>=level: print string
    elif verbosity: print string
    




def printSameLine(string):
    """Print string without making new line. (Write to stdout and flush.)"""
    #http://stackoverflow.com/questions/3249524/print-in-one-line-dynamically
    if string: string = string+" "
    sys.stdout.write(string)
    sys.stdout.flush()





def header(header):
    """Returns formatted header"""
    
    return ( ">>>\n>>>\n" +
             ">>>   ###%s\n"    % ('#'*(len(header)+3)) +
             ">>>   #  %s  #\n" % (header) +
             ">>>   ###%s\n"    % ('#'*(len(header)+3)) +
             ">>>" )
    




class capturing(object):
    """Capture standard output"""

    def __init__(self,**kwargs):
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        self.captured0 = StringIO()
        sys.stdout = self.captured0
        sys.stderr = self.captured0

    def stop(self):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        self.captured0.close()

    def captured(self):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        out = self.captured0.getvalue()
        if '\n' in out[-2:]: out = out[:-1]
        self.captured0.close()
        return out
    




class LoadingBar(object):
    """Class to make a simple, custom loading bar."""
    # from math import log, import sys

    def __init__(self, *args, **kwargs):
        '''Constructor for LoadingBar object.'''
        self.steps = 10
        if len(args)>0 and isinstance(args[0],int) and args[0]>0: self.steps = args[0]
        self.tally   = 0
        self.position = 0
        self.steps   = max(kwargs.get('steps',self.steps),1)
        self.width   = max(kwargs.get('width',self.steps),1)
        self.counter = kwargs.get('counter',False)
        self.counterformat = "%%%ii" % (log(self.steps,10)+1)
        self.remove  = kwargs.get('remove',False)
        self.symbol  = kwargs.get('symbol',"=")
        self.prepend = kwargs.get('prepend',">>> ")
        self.append  = kwargs.get('append',"")
        self.message_ = kwargs.get('message',"")
        self.done    = False
        if self.counter: self.counter = " %s/%i" % (self.counterformat%self.tally,self.steps)
        else:            self.counter = ""
        sys.stdout.write("%s[%s]" % (self.prepend," "*self.width))
        sys.stdout.flush()
        sys.stdout.write("\b"*(self.width+1)) # return to start of line, after '['
        if self.counter: self.updateCounter()
        if self.message_: self.message(self.message_)

    def count(self,*args,**kwargs):
        """Count one step."""
        if self.done: return
        i = 1.0
        message = ""
        if len(args)>0 and isinstance(args[0],int) and args[0]>0:
            i = args[0]
            args.remove(i)
        if len(args)>0 and isinstance(args[0],str):
            message = args[0]
        i = max(min(i,self.steps-self.tally),0)
        newposition = int(round(float(self.tally+i)*self.width/self.steps))
        step = newposition-self.position
        self.position = newposition
        sys.stdout.write(self.symbol*step)
        sys.stdout.flush()
        self.tally += i
        if self.counter: self.updateCounter()
        if message: self.message(message)
        if self.tally >= self.steps:
            if self.append: self.message(self.append,moveback=self.remove)
            if self.remove:
                sys.stdout.write("\b"*(self.width+1+len(self.prepend)))
                sys.stdout.write(' '*(len(self.prepend)+self.width+len(self.counter)+len(self.message_)+4))
                sys.stdout.write("\b"*(len(self.prepend)+self.width+len(self.counter)+len(self.message_)+4))
            elif not self.append: self.message("\n")
            self.done = True

    def updateCounter(self,**kwargs):
        """Update the counter."""
        self.counter = " %s/%i" % (self.counterformat%self.tally,self.steps)
        sys.stdout.write("%s]%s" % (' '*(self.width-self.position), self.counter))
        sys.stdout.flush()
        sys.stdout.write("\b"*(self.width+1-self.position+len(self.counter)))

    def message(self,newmessage,moveback=True):
        """Append the counter with some progress message."""
        end_ = ""
        if "\n" in newmessage:
            end_ = newmessage[newmessage.index("\n"):]
            newmessage = newmessage[:newmessage.index("\n")]
        self.message_ = newmessage.ljust(len(self.message_))+end_
        sys.stdout.write("%s]%s %s" % (' '*(self.width-self.position), self.counter, self.message_))
        sys.stdout.flush()
        if moveback: sys.stdout.write("\b"*(self.width+2-self.position+len(self.counter)+len(self.message_)))
    



