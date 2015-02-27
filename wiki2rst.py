#!/usr/bin/python
import sys
import re



class wiki2rst(object):
   """ My Wiki to rst conversion class """

   codere=re.compile(r'^[ ][ ]')
   langrestart=re.compile('<syntaxhighlight lang=\"')
   langreend=re.compile('</syntaxhighlight> ')

   def __init__(self,htmlfile):
       self.htmlfile=htmlfile
       self.indent=0
       self.incode=0
       self.level1=re.compile('^(=)')
       self.level2=re.compile('^(==)')
       self.level3=re.compile('^(===)')
       self.langstart=re.compile(r"<syntaxhighlight lang=\"([a-zA-Z]+)\">")
       self.langend=re.compile(r'</syntaxhighlight>')
       self.convert()

   def setindent(self,i):
       self.indent=i
  
   def lineout(self,line):
       i=0
       s=''
       if self.incode==0:
          while (i<self.indent):
            s=''+s+' '
            i=i+1
       print ("%s%s")%(s,line)

   def convert(self):
       htmf=open(self.htmlfile,'r')
       for line in htmf:
           line=line.replace('\n','')
           if self.level3.match(line):
              self.indent=9
              line=line.replace('=','').strip()
              line=str.format('\n%s\n%s\n%s'%('='*len(line),line,'='*len(line)))
           elif self.level2.match(line):
              self.indent=6
              line=line.replace('=','').strip()
              line=str.format('\n%s\n%s\n%s'%('-'*len(line),line,'-'*len(line)))
           elif self.level1.match(line):
              self.indent=0 
              line=line.replace('=','').strip()
              line=str.format('\n%s\n%s\n%s'%('~'*len(line),line,'~'*len(line)))
           elif self.langstart.match(line):
              p=self.langstart.match(line)
              self.incode=1
              line='.. code:: '+ p.group(1).strip()+'\n'
           elif self.langend.match(line):
              self.incode=0
              line=' '
           self.lineout(line)
          


if __name__=="__main__":
   wk=wiki2rst(sys.argv[1])
    
