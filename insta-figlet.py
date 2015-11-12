import sys
import subprocess
import time

args = sys.argv

FONTS = [
'banner',
'big',
'block',
'bubble',
'digital',
'ivrit',
'lean',
'mini',
'mnemonic',
'script',
'shadow',
'slant',
'small',
'smscript',
'smshadow',
'smslant',
'standard',
'term',
]

TIMEOUT = 1 #timeout between banners, set as desired.

def bonus():
  print "\n                      /--/)"
  print "                    ,/   /"
  print "                   /    /"
  print "             /'  /'   '/'  '."
  print "          /'/   /    /      /\" \\"
  print "        ('(    '    '     /'   ')"
  print "         \                 '     /"
  print "          ''   \           _  '"
  print "            \              ("
  print "              \             \\"
  print "                 BONUS FVCK\n"
  sys.exit(0)

if __name__ == "__main__":

  if len(args) == 3:
    font_list = [args[1]]
    keyword = args[2] 
  elif len(args) == 2:
    if args[1] == "--bonus":
      bonus()
    else:
      keyword = args[1]
      font_list = FONTS
  else:
    print 'Usage: python [fontname] keyword'
    print 'If you don\'t specify the fontname all fonts will be shown'
    sys.exit(1)

  for font in font_list:
    print font
    subprocess.call(['figlet', '-f', '{0}'.format(font), keyword])
    time.sleep(timeout)
    print
    print '#'*30
    print '#'*30
    print '#'*30
    print
