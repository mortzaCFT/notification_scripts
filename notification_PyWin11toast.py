import argparse
from win11toast import toast

from rtl import rtl
#  from bidi.algorithm import get_display
#  from persian_converter import fprint
import persianutils as pu

import sys

# For right aligment language..
def text_orientation(text):
  if rtl(text):
   # reshaped_text = reshape(text)
   # num_spaces = max(80 - len(text), 0)
   # aligned_text = ' ' * num_spaces + text
   return pu.standardize(text)
    #return fprint(text)
    #return reshaped_text
    #return text.rjust(50)
  else:
    return text


def main():
  parser = argparse.ArgumentParser(description='notification')
  parser.add_argument('--title', type=str, required=True )
  parser.add_argument('--body', type=str, required=True)
  parser.add_argument('--image', type=str, )
  parser.add_argument('--appname', type=str, default=' ')
  parser.add_argument('--issilent', action='store_true')
  args = parser.parse_args()

  if args.image:
    image = {
      'src': args.image,
      'placement': 'appLogoOverride',
      'hint-crop': 'circle'
    }
  orientation_title = text_orientation(args.title)
  orientation_body = text_orientation(args.body)

  toast(
    orientation_title,
    orientation_body,
    icon=image,
    app_id=args.appname,
    audio={'sillent': args.issilent},
    on_dismissed=lambda *args: None,
  )

if __name__ == "__main__":
  sys.stdout.reconfigure(encoding='utf-8') 
  main()
